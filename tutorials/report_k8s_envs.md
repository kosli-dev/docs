---
title: "Report Kubernetes environments to Kosli"
description: "Learn how to report running artifacts from a Kubernetes cluster to Kosli — using a Helm chart for production, the CLI for a quick test, or an externally scheduled cron job."
---

By the end of this tutorial, you will have reported a snapshot of your Kubernetes cluster to Kosli, making its running artifacts visible and trackable.

## Prerequisites

* Have access to a Kubernetes cluster.
* [Create a Kubernetes Kosli environment](/getting_started/environments#create-an-environment) named `k8s-tutorial`.
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).

## Report a snapshot

<Tabs>
<Tab title="Helm chart (recommended)">

The [Kosli K8S reporter Helm chart](/helm) deploys a <Tooltip tip="A Kubernetes resource that runs a container on a defined schedule, similar to a Unix cron job.">CronJob</Tooltip> inside your cluster that automatically reports running artifacts to Kosli on a schedule. This is the recommended approach for production use.

[Install Helm](https://helm.sh/docs/intro/install/) if you have not done so.

1. Create a Kubernetes secret containing your Kosli API token:

```shell
kubectl create secret generic kosli-api-token --from-literal=apikey=<your-kosli-api-token>
```

<Warning>
Make sure the secret value does not contain trailing whitespace.
</Warning>

2. Create a `tutorial-values.yaml` file to configure the chart:

```yaml
# the cron schedule at which the reporter is triggered
cronSchedule: "*/5 * * * *"

kosliApiToken:
  # the name of the secret containing the Kosli API token
  secretName: "kosli-api-token"
  # the key in the secret data that contains the token
  secretKey: "apikey"

reporterConfig:
  # the name of the Kosli org
  kosliOrg: "<your-kosli-org-name>"
  # the Kosli environment(s) to report to
  environments:
    # omit the namespace fields to report the entire cluster
    - name: "k8s-tutorial"
      # optionally restrict to specific namespaces:
      # namespaces: [namespace1, namespace2]
```

3. Install the chart:

```shell
helm repo add kosli https://charts.kosli.com/
helm repo update
helm install kosli-reporter kosli/k8s-reporter -f tutorial-values.yaml
```

4. Confirm the CronJob was created:

```shell
kubectl get cronjobs
```

The CronJob will now run every 5 minutes and report what is running in the cluster to Kosli.

<Note>
Running on EKS with Karpenter, or another node autoscaler? A reporter pod arriving every 5 minutes can stop nodes being consolidated. Pin the reporter to a stable node group, widen `cronSchedule`, or run it out of cluster. See [Running on EKS with Karpenter](/helm/k8s_reporter/karpenter).
</Note>

</Tab>
<Tab title="Externally scheduled cron">

If you cannot run the reporter inside the cluster, you can run `kosli snapshot k8s` from outside on a regular schedule. This requires network access to the cluster from wherever the CLI runs.

The example below uses a GitHub Actions scheduled workflow:

<Info>
The workflow requires the following GitHub Actions secrets: `MY_KOSLI_API_TOKEN`, `GKE_SA_KEY`, `GKE_PROJECT`.
</Info>

```yaml
name: Regular Kubernetes reports to Kosli

on:
  workflow_dispatch:
  schedule:
    - cron: '0 * * * *' # every hour

jobs:
  k8s-report:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: write
    env:
      KOSLI_API_TOKEN: ${{ secrets.MY_KOSLI_API_TOKEN }}

    steps:
      - name: Install Kosli CLI
        uses: kosli-dev/setup-cli-action@v5

      # Replace this step with one that connects to your cluster if not using GKE
      - name: Connect to GKE
        uses: 'Swibi/connect-to-gke'
        with:
          GCP_SA_KEY: ${{ secrets.GKE_SA_KEY }}
          GCP_PROJECT_ID: ${{ secrets.GKE_PROJECT }}
          GKE_CLUSTER: <your-cluster-name>
          GKE_ZONE: <your-cluster-zone>

      - name: Report K8S snapshot to Kosli
        run: kosli snapshot k8s k8s-tutorial --org <your-kosli-org-name>

      - name: Notify Slack on failure
        if: ${{ failure() }}
        uses: rtCamp/action-slack-notify@v2
        env:
          SLACK_CHANNEL: kosli-reports-failure
          SLACK_COLOR: ${{ job.status }}
          SLACK_TITLE: Reporting K8S artifacts to Kosli has failed
          SLACK_USERNAME: GithubActions
          SLACK_WEBHOOK: ${{ secrets.SLACK_CI_FAILURES_WEBHOOK }}
          SLACK_MESSAGE: "Reporting K8S artifacts to Kosli has failed. Please check the logs for more details."
```

</Tab>
<Tab title="Kosli CLI (testing only)">

<Warning>
This approach is intended for ad-hoc and local testing only. Do not use it in production — use the Helm chart instead.
</Warning>

[Install Kosli CLI](/getting_started/install) if you have not done so.

<Info>
All commands below use the default <Tooltip tip="The active cluster, user, and namespace settings stored in $HOME/.kube/config. You can override it by passing --kubeconfig to any kosli snapshot k8s command.">kubeconfig context</Tooltip>. Pass `--kubeconfig` to use a different one.
</Info>

To report all artifacts running in the entire cluster:

```shell
kosli snapshot k8s k8s-tutorial \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

To report only artifacts running in specific namespaces:

```shell
kosli snapshot k8s k8s-tutorial \
    --namespaces namespace1,namespace2 \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

To report the entire cluster except for certain namespaces:

```shell
kosli snapshot k8s k8s-tutorial \
    --exclude-namespaces namespace1,namespace2 \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

</Tab>
</Tabs>

## What gets reported

The reporter collects **pods**, and is blind to workload kind: it has no awareness of `Deployment`, `StatefulSet`, `Job`, or `CronJob` objects, so a Job pod is reported exactly like a Deployment pod. For each pod it records the pod name, its namespace, its container image digests, its creation timestamp, and its owner references.

In the snapshot those pods are grouped under the artifact whose image they run — a snapshot is a list of artifacts, each carrying the pods running it. That is why the churn rules below turn on image digests rather than on individual pods.

Only pods in certain phases are reported:

| Pod phase | Reported | Notes |
| :--- | :---: | :--- |
| `Running` | Yes | |
| `Failed` | Yes* | *Skipped, with a warning, if any of its containers has no image ID. |
| `Succeeded` | No | Where a completed Job pod ends up. |
| `Pending` | No | No image digests exist yet. |
| `Unknown` | No | |

Owner references are stored on the snapshot, so the `Job` or `CronJob` that owns a pod does reach Kosli. They are not in the table output of [`kosli get snapshot`](/client_reference/kosli_get_snapshot) — read them from the JSON:

```shell
kosli get snapshot k8s-tutorial \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name> \
    --output json | jq '.artifacts[].pods'
```

### Jobs and CronJobs

Because reporting is driven by pod phase, a `Job` or `CronJob` pod is captured only while it is running — or, if it fails, until the failed pod is cleaned up:

* A job that starts and finishes between two snapshots never appears at all. As a rough guide, a run is captured about as often as its runtime divides into the snapshot interval — so on the Helm chart's default `*/5 * * * *` schedule a job that runs for a few seconds is almost always missed, while one that runs for most of the interval is almost always caught. That guide assumes the job starts at an arbitrary point in the interval. A `CronJob` whose schedule shares a period with the reporter's does not sample randomly at all: it is caught on nearly every run or on nearly none, depending on which of the two fires first.
* A job that happens to be running when a snapshot is taken appears in that snapshot and is gone from the next one.
* A job that **fails** is the exception. `Failed` is a terminal phase, so the pod stays in it — and keeps being reported — until Kubernetes garbage-collects it: the Job's `ttlSecondsAfterFinished`, or for a `CronJob` the failed Job retained by `failedJobsHistoryLimit` (default `1`). Until then a failed run is not a flicker; it parks a stopped artifact in the environment.
* A job that succeeds leaves no trace. `Succeeded` pods are never reported, so nothing in the environment records that the run happened.

Whether a captured run shows up as environment churn depends on the image:

* If the job runs an image that nothing else in the environment runs, each captured run produces one snapshot where the artifact started and a later one where it exited.
* If the job runs the same image as a long-running workload, only the instance count changes. Instance-count-only differences do not create a snapshot, so the run is invisible — and because the report is discarded, the pod's owner references are not stored either. Owner references only reach Kosli for runs that produce a snapshot.

<Warning>
If the job's image was never attested to a Kosli flow, it is reported as an artifact with no provenance. Under an [environment policy](/policy-reference/environment_policy) that requires provenance, snapshots taken while a job was running are non-compliant and snapshots taken between runs are compliant — so compliance appears to flicker. A failed run is worse than a flicker: the `Failed` pod is reported in every snapshot until it is garbage-collected, holding the environment non-compliant for as long as it survives.
</Warning>

<Note>
The reporter deployed by the Helm chart is itself a `CronJob`, and at the default whole-cluster scope it is running whenever it takes a snapshot — so it appears in its own snapshots. Kosli ignores the reporter's image (`ghcr.io/kosli-dev/cli`) when deciding whether a snapshot is worth saving, so the reporter's own pods never create snapshots or start and exit events. The reporter is *not* exempt from compliance evaluation, though: under a policy that requires provenance it counts as an artifact without provenance — persistently, not intermittently. Either waive provenance for its image, or install the reporter into a namespace of its own and exclude that namespace:

```shell
helm install kosli-reporter kosli/k8s-reporter -n kosli --create-namespace -f tutorial-values.yaml
```

The install command earlier on this page has no `-n`, so the reporter shares whichever namespace you are currently in — excluding *that* would drop your own workloads from the environment along with it.
</Note>

### Handling job workloads

The reporter filters by namespace only; there is no way to exclude pods by owner kind. Three options:

* **Run jobs in their own namespace,** then either leave that namespace out of reporting or give it its own Kosli environment, so job churn does not affect the compliance of your long-running workloads. With the Helm chart, both are per-entry namespace selectors under `reporterConfig.environments`: `excludeNamespaces` on your main entry, plus a second entry whose `namespaces` is the job namespace if you want it reported separately. If your main entry already lists `namespaces` or `namespacesRegex`, drop the job namespace from that list instead — the include and exclude selectors are mutually exclusive within one entry. A second entry is not a second reporter, so the caveats in [Running multiple reporters](#running-multiple-reporters) do not apply. See the [chart configuration reference](/helm/k8s_reporter/configuration). With the CLI, use `--exclude-namespaces` when reporting the whole cluster, or simply omit the job namespace from `--namespaces`.
* **Waive provenance for the job's image** if you want the job pods in the environment but not the compliance flicker. An environment policy's `artifacts.provenance.exceptions` drops the provenance requirement for artifacts matching a policy expression:

    ```yaml
    _schema: https://docs.kosli.com/schemas/policy/v1

    artifacts:
      provenance:
        required: true
        exceptions:
          - if: ${{ matches(artifact.name, "^my-job:.*") }}
    ```

    See [environment policy](/policy-reference/environment_policy).
* **Attest the job to a flow instead.** Environment snapshots answer "what is running right now"; they are the wrong tool for "what ran, when, and did it succeed". Create a [flow](/getting_started/flows) for the job, [begin a trail](/getting_started/trails) for each run, and attest its outcome. Unlike snapshots, this captures every run no matter how briefly it ran.

## Running multiple reporters

If you are considering running more than one reporter against the same cluster, the table below summarizes which setups produce meaningful snapshots and which don't.

| Scenario | Supported | Explanation |
| :--- | :---: | :--- |
| Two orgs, separate environments, overlapping namespaces | Yes | Different environments → independent snapshots. |
| One org, two environments, overlapping namespaces | Yes | Same as above. |
| One org, **same environment**, two reporters with overlapping namespaces | No | Snapshots toggle between each reporter's view. No data is deleted, but diffs between consecutive snapshots become meaningless. |
| One org, same environment, two reporters with **disjoint** namespaces | No | Each snapshot only reflects one reporter's namespaces, so diffs compare unrelated scopes. |

<Warning>
A single Kosli environment must have exactly one reporter feeding it. Snapshots are never overwritten or deleted, but if two reporters take turns updating the same environment:

* Diffs between consecutive snapshots compare unrelated views of the cluster.
* The environment history shows artifacts continuously stopping and starting as each report toggles which namespaces are visible.
</Warning>

## What you've accomplished

You have reported a snapshot of your Kubernetes cluster to Kosli. Kosli now tracks the running artifacts in that environment and will record changes as they happen.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
