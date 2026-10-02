---
title: "kosli snapshot gke"
tag: "BETA"
description: "Report a snapshot of running pods in GKE clusters to Kosli, read from Cloud Asset Inventory.  "
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli snapshot gke ENVIRONMENT-NAME [flags]
```

Report a snapshot of running pods in GKE clusters to Kosli, read from Cloud Asset Inventory.  
Reads the pods of every GKE cluster in a Google Cloud project, folder or organization from
Cloud Asset Inventory, so it needs no kubeconfig, no Kubernetes RBAC and no network access to any
cluster control plane. The reported data matches `kosli snapshot k8s`: container image digests,
creation timestamps and owners of the Running and Failed pods.

GCP authentication uses Application Default Credentials. On a developer machine, run
`gcloud auth application-default login`; in GCE/GKE/Cloud Run the metadata server / Workload
Identity is used automatically. The Cloud Asset API (`cloudasset.googleapis.com`) must be enabled
in the quota project of the caller's credentials.

The caller needs `cloudasset.assets.listContainerPod` and `serviceusage.services.use` on the
project, folder or organization. Grant them through a custom role for least privilege:
`roles/cloudasset.viewer` also works, but it can list every asset type, including `k8s.io/Secret`.

Asset Inventory is eventually consistent, so a snapshot can lag behind recent pod changes.

Skip `--clusters`, `--clusters-regex` and `--locations` to report the pods of every cluster in
scope, and skip the namespace flags to report every namespace. Filters are case-sensitive.
With `--folder` or `--organization`, `--clusters` and `--clusters-regex` match cluster names in
every project under the scope.

The snapshot captures every pod that matches the filters, across all selected clusters, and
reports them to one environment. With no cluster or location filter, that is every GKE cluster
in the scope. The report does not record which cluster a pod runs in, so pods with the same
namespace and name in two clusters (e.g. StatefulSet pods such as `web-0`) cannot be told apart
by name. To keep clusters apart, snapshot each one with `--clusters` to its own environment.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--clusters` | strings | [optional] The comma-separated list of GKE cluster names to snapshot. Defaults to every cluster in scope. |
| `--clusters-regex` | strings | [optional] The comma-separated list of GKE cluster name regex patterns to snapshot. Defaults to every cluster in scope. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-x`, `--exclude-namespaces` | strings | [optional] The comma separated list of namespaces names to exclude from reporting artifacts info from. Can't be used together with `--namespaces` or `--namespaces-regex`. |
| `--exclude-namespaces-regex` | strings | [optional] The comma separated list of namespaces regex patterns to exclude from reporting artifacts info from. Can't be used together with `--namespaces` or `--namespaces-regex`. |
| `--folder` | string | [conditional] The Google Cloud folder ID to snapshot GKE pods from, covering every project under it. Exactly one of `--project`, `--folder` or `--organization` is required. |
| `-h`, `--help` | bool | help for gke |
| `--locations` | strings | [optional] The comma-separated list of GKE cluster locations (regions or zones, e.g. europe-west1,us-central1-a) to snapshot. A region also matches the zonal clusters in it. Defaults to every location. |
| `-n`, `--namespaces` | strings | [optional] The comma separated list of namespaces names to report artifacts info from. Can't be used together with `--exclude-namespaces` or `--exclude-namespaces-regex`. |
| `--namespaces-regex` | strings | [optional] The comma separated list of namespaces regex patterns to report artifacts info from. Can't be used together with `--exclude-namespaces` or `--exclude-namespaces-regex`. |
| `--organization` | string | [conditional] The Google Cloud organization ID to snapshot GKE pods from, covering every project under it. Exactly one of `--project`, `--folder` or `--organization` is required. |
| `--project` | string | [conditional] The Google Cloud project ID to snapshot GKE pods from. Exactly one of `--project`, `--folder` or `--organization` is required. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-A`, `--auto-environment` | bool | [optional] Create the environment (with the type inferred from the snapshot subcommand) if it does not already exist, before reporting the snapshot. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `--environment-description` | string | [optional] The environment description. |
| `--exclude-scaling` | bool | [optional] Exclude scaling events for snapshots. Snapshots with scaling changes will not result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `--include-scaling` | bool | [optional] Include scaling events for snapshots. Snapshots with scaling changes will result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="report the pods of every GKE cluster in a project">
```shell
kosli snapshot gke yourEnvironmentName 
	--project yourGCPProject 

```
</Accordion>
<Accordion title="report the pods of every GKE cluster in all projects under a folder">
```shell
kosli snapshot gke yourEnvironmentName 
	--folder yourGCPFolderID 

```
</Accordion>
<Accordion title="report the pods of one cluster to its own environment, excluding system namespaces">
```shell
kosli snapshot gke yourEnvironmentName 
	--project yourGCPProject 
	--clusters yourClusterName 
	--locations europe-west1 
	--exclude-namespaces-regex "^kube-,^gke-" 
```
</Accordion>
</AccordionGroup>

