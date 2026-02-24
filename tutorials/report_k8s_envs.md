---
title: "Report Kubernetes environments to Kosli"
description: "Learn how to report running artifacts from a Kubernetes cluster to Kosli — using a Helm chart for production, the CLI for a quick test, or an externally scheduled cron job."
---

By the end of this tutorial, you will have reported a snapshot of your Kubernetes cluster to Kosli, making its running artifacts visible and trackable.

## Prerequisites

* Have access to a Kubernetes cluster.
* [Create a Kosli account](https://app.kosli.com/sign-up) if you do not have one.
* [Create a Kubernetes Kosli environment](/getting_started/environments#create-an-environment) named `k8s-tutorial`.
* [Get a Kosli API token](/getting_started/service-accounts).

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
  # the name of the Kosli environment to report to
  kosliEnvironmentName: "k8s-tutorial"
  # comma-separated list of namespace name regex patterns to report
  # leave empty to report the entire cluster
  namespaces: ""
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
        uses: kosli-dev/setup-cli-action@v2

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

## What you've accomplished

You have reported a snapshot of your Kubernetes cluster to Kosli. Kosli now tracks the running artifacts in that environment and will record changes as they happen.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
