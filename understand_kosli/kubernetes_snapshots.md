---
title: 'Kubernetes environment snapshots'
description: 'What the Kosli Kubernetes reporter captures, which pod phases it reports, and what that means for Job and CronJob workloads.'
---

A Kubernetes environment snapshot records what was running in your cluster at a moment in time. This page explains what the reporter actually collects, which pods it skips, and why short-lived workloads such as `Job` and `CronJob` behave differently from long-running ones. To set reporting up in the first place, see [Report Kubernetes environments to Kosli](/tutorials/report_k8s_envs).

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
kosli get snapshot <your-environment> \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name> \
    --output json | jq '.artifacts[].pods'
```

## Jobs and CronJobs

Because reporting is driven by pod phase, a `Job` or `CronJob` pod is captured only while it is running — or, if it fails, until the failed pod is cleaned up:

* A job that starts and finishes between two snapshots never appears at all. As a rough guide, a run is captured about as often as its runtime divides into the snapshot interval — so on the Helm chart's default `*/5 * * * *` schedule a job that runs for a few seconds is almost always missed, while one that runs for most of the interval is almost always caught. That guide assumes the job starts at an arbitrary point in the interval. A `CronJob` whose schedule shares a period with the reporter's does not sample randomly at all: it is caught on nearly every run or on nearly none, depending on which of the two fires first.
* A job that happens to be running when a snapshot is taken appears in that snapshot and is gone from the next one.
* A job that **fails** is the exception. `Failed` is a terminal phase, so the pod stays in it — and keeps being reported — for as long as it exists, and nothing removes it by default. `ttlSecondsAfterFinished` is unset unless you set it, so a standalone Job's failed pods survive until the Job is deleted; a `CronJob` always retains its most recent failed Job (`failedJobsHistoryLimit`, default `1`). A Job with `restartPolicy: Never` that keeps failing leaves one `Failed` pod per attempt, up to `backoffLimit` (default `6`), and each is reported. Until they are gone, a failed run is not a flicker: Kosli keeps showing the dead pods' artifact as running in the environment.
* A job that succeeds leaves no trace. `Succeeded` pods are never reported, so nothing in the environment records that the run happened.

Whether a captured run shows up as environment churn depends on the image:

* If the job runs an image that nothing else in the environment runs, each captured run produces one snapshot where the artifact started and a later one where it exited.
* If the job runs the same image as a long-running workload, only the instance count changes. Instance-count-only differences do not create a snapshot, so the run is invisible — and because the report is discarded, the pod's owner references are not stored either. Owner references only reach Kosli for runs that produce a snapshot.

<Warning>
If the job's image was never attested to a Kosli flow, it is reported as an artifact with no provenance. Under an [environment policy](/policy-reference/environment_policy) that requires provenance, snapshots taken while a job was running are non-compliant and snapshots taken between runs are compliant — so compliance appears to flicker. A failed run is worse than a flicker: the `Failed` pod is reported in every snapshot until it is garbage-collected, holding the environment non-compliant for as long as it survives.
</Warning>

<Note>
The reporter deployed by the Helm chart is itself a `CronJob`, and at the default whole-cluster scope it is running whenever it takes a snapshot — so it appears in its own snapshots. Kosli ignores the reporter's image (`ghcr.io/kosli-dev/cli`) when deciding whether a snapshot is worth saving, so the reporter's own pods never create snapshots or start and exit events. The match is on the image name, so if you override `image.repository` to mirror the reporter image into your own registry, its pods stop being ignored and each run shows up as an artifact starting and exiting.

The reporter is *not* exempt from compliance evaluation, though: under a policy that requires provenance it counts as an artifact without provenance — persistently, not intermittently. Either waive provenance for its image, or install the reporter into a namespace of its own and exclude that namespace — subject to the same include/exclude constraint as the [first option below](#handling-job-workloads).

The API token secret is namespace-scoped, so a dedicated namespace needs its own copy of it. Create both before installing:

```shell
kubectl create namespace kosli
kubectl create secret generic kosli-api-token -n kosli --from-literal=apikey=<your-kosli-api-token>
helm install kosli-reporter kosli/k8s-reporter -n kosli -f values.yaml
```

The install steps in the [tutorial](/tutorials/report_k8s_envs) pass no `-n`, so they put the secret and the reporter in whichever namespace you are currently in — usually alongside the workloads you came there to report. Excluding *that* namespace would drop those workloads from the environment too.
</Note>

## Handling job workloads

The reporter filters by namespace only; there is no way to exclude pods by owner kind. Three options:

* **Run jobs in their own namespace,** then either leave that namespace out of reporting or give it its own Kosli environment, so job churn does not affect the compliance of your long-running workloads. With the Helm chart, both are per-entry namespace selectors under `reporterConfig.environments`: `excludeNamespaces` on your main entry, plus a second entry whose `namespaces` is the job namespace if you want it reported separately. If your main entry already lists `namespaces` or `namespacesRegex`, drop the job namespace from that list instead — the include and exclude selectors are mutually exclusive within one entry. A second entry is not a second reporter, so the caveats in [Running multiple reporters](/tutorials/report_k8s_envs#running-multiple-reporters) do not apply. See the [chart configuration reference](/helm/k8s_reporter/configuration). With the CLI, use `--exclude-namespaces` when reporting the whole cluster, or simply omit the job namespace from `--namespaces`.
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
