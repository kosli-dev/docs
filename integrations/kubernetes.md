---
title: "Kubernetes"
description: "Track what is running in your Kubernetes clusters by deploying the Kosli reporter, which periodically snapshots pod images and reports them to Kosli."
---

The Kosli Kubernetes reporter gives you continuous visibility into the artifacts running in your clusters. It runs as a lightweight CronJob that periodically scans the pods in your cluster (or a subset of namespaces), collects the container image digests, and sends that information to Kosli as an [environment snapshot](/getting_started/environments).

Every time the set of running artifacts changes, Kosli records a new snapshot. This creates an immutable audit trail of what ran where and when — without requiring any changes to your application workloads.

## How the reporter works

The reporter is packaged as a [Helm chart](/helm/k8s_reporter) and deployed into the same cluster it monitors. Once installed it creates the following resources:

| Resource | Purpose |
|---|---|
| **CronJob** | Triggers the reporter on a configurable schedule (default: every 5 minutes). |
| **ServiceAccount & RBAC** | Grants the reporter read-only access to list pods — either cluster-wide or within specific namespaces. |
| **Secret reference** | Points to a Kubernetes Secret that holds your Kosli API token. |

Each time the CronJob fires, a short-lived pod starts, queries the Kubernetes API for running pods, extracts the container image digests and creation timestamps, and sends the data to Kosli. The pod then terminates. No data is stored inside the cluster.

<Info>
The reporter only needs `get` and `list` permissions on pods (and namespaces, when using namespace selectors). It does not modify any resources in your cluster.
</Info>

## What gets reported

For every running pod the reporter collects:

- Container image reference and SHA256 digest
- Pod creation timestamp

Kosli uses the image digest to link running artifacts back to the [flows and trails](/understand_kosli/concepts) that produced them. This lets you trace any running container image to its source commit, build attestations, and compliance status.

## Scoping what to report

You can control which parts of the cluster the reporter covers:

- **Entire cluster** — omit namespace selectors to report all pods across all namespaces.
- **Include specific namespaces** — list namespace names or regex patterns to limit reporting to matching namespaces.
- **Exclude specific namespaces** — exclude namespace names or regex patterns to report everything except matching namespaces.
- **Multiple environments** — configure several Kosli environments in a single reporter installation, each with its own namespace selectors.

This flexibility lets you map your cluster topology to Kosli environments however you need. For example, you might report production namespaces to one environment and staging namespaces to another, all from a single Helm release.

See the [Helm chart configuration reference](/helm/k8s_reporter#configurations) for the full list of options.

## Prerequisites

- A Kubernetes cluster (v1.21 or later)
- Helm v3.0+
- A [Kosli account](https://app.kosli.com/sign-up) and [API token](/getting_started/service-accounts)
- A Kosli environment of type **K8S** — see [creating environments](/getting_started/environments#create-an-environment)

## Setting up the reporter

<Steps>
  <Step title="Add the Kosli Helm repository">

  ```shell
  helm repo add kosli https://charts.kosli.com/ && helm repo update
  ```

  </Step>
  <Step title="Create a secret for the API token">

  ```shell
  kubectl create secret generic kosli-api-token --from-literal=key=YOUR_KOSLI_API_TOKEN
  ```

  <Warning>
  Make sure the secret value does not contain trailing whitespace.
  </Warning>

  </Step>
  <Step title="Create a values file">

  Create a `values.yaml` file. At minimum you need your Kosli organization name and at least one environment:

  ```yaml
  reporterConfig:
    kosliOrg: your-org-name
    environments:
      - name: your-environment-name
  ```

  To report only specific namespaces:

  ```yaml
  reporterConfig:
    kosliOrg: your-org-name
    environments:
      - name: your-environment-name
        namespaces: [app-namespace-1, app-namespace-2]
  ```

  </Step>
  <Step title="Install the chart">

  ```shell
  helm install kosli-reporter kosli/k8s-reporter -f values.yaml
  ```

  </Step>
  <Step title="Verify the installation">

  Confirm the CronJob was created:

  ```shell
  kubectl get cronjobs
  ```

  After the first scheduled run (default: within 5 minutes), check the Kosli app or CLI for your first snapshot:

  ```shell
  kosli list snapshots your-environment-name --org your-org-name
  ```

  </Step>
</Steps>

## Alternative reporting methods

If you cannot deploy the Helm chart inside the cluster, you can report snapshots from outside using the [`kosli snapshot k8s`](/client_reference/kosli_snapshot_k8s) CLI command. This is useful for:

- Quick local testing during development
- Environments where in-cluster deployments are restricted
- Running the reporter from a CI/CD scheduled job (e.g., GitHub Actions cron)

See the [Report Kubernetes environments](/tutorials/report_k8s_envs) tutorial for examples of each approach.

## Next steps

- [Report Kubernetes environments tutorial](/tutorials/report_k8s_envs) — step-by-step walkthrough of all reporting methods
- [Helm chart reference](/helm/k8s_reporter) — full configuration options
- [`kosli snapshot k8s` CLI reference](/client_reference/kosli_snapshot_k8s) — command flags and examples
- [Environment policies](/getting_started/policies) — define compliance requirements for your environments
