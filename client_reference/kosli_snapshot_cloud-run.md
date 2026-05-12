---
title: "kosli snapshot cloud-run"
beta: false
deprecated: false
description: "Report a snapshot of Cloud Run services and jobs in a Google Cloud project and region to Kosli.  "
---

## Synopsis

```shell
kosli snapshot cloud-run ENVIRONMENT-NAME [flags]
```

Report a snapshot of Cloud Run services and jobs in a Google Cloud project and region to Kosli.  
Each Cloud Run service contributes one artifact per revision in its traffic
configuration. Each Cloud Run Job contributes one artifact, identified by the
image bound to the Job (Jobs do not have a revision/traffic-split model).
Idle Jobs (no currently-running Execution) are included.

GCP authentication uses Application Default Credentials. On a developer
machine, run `gcloud auth application-default login`; in GCE/GKE/Cloud Run
the metadata server / Workload Identity is used automatically. The caller
needs at least `roles/run.viewer` on the target project.

Skip all filtering flags to report every service and every job in the given
project + region. Use `--include` and/or `--include-regex` to snapshot only a
subset, OR `--exclude` and/or `--exclude-regex` to omit a subset; include and
exclude are mutually exclusive. Filters apply uniformly to both service and
job names and are case-sensitive.

Currently a hidden, in-development command. Use --dry-run to inspect the payload without sending it to Kosli.

## Flags
| Flag | Description |
| :--- | :--- |
|    -D, --dry-run  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|        --exclude strings  |  [optional] The comma-separated list of Cloud Run service or job names to exclude. Can't be used together with --include or --include-regex.  |
|        --exclude-regex strings  |  [optional] The comma-separated list of Cloud Run service or job name regex patterns to exclude. Can't be used together with --include or --include-regex.  |
|    -h, --help  |  help for cloud-run  |
|        --include strings  |  [optional] The comma-separated list of Cloud Run service or job names to snapshot. Can't be used together with --exclude or --exclude-regex.  |
|        --include-regex strings  |  [optional] The comma-separated list of Cloud Run service or job name regex patterns to snapshot. Can't be used together with --exclude or --exclude-regex.  |
|        --project string  |  [required] GCP project ID.  |
|        --region string  |  [required] GCP region (e.g. europe-west1).  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy http://proxy-server-ip:proxy-port  |  [optional] The HTTP proxy URL including protocol and port number. e.g. http://proxy-server-ip:proxy-port  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="report every Cloud Run service and job in a project + region">
```shell
kosli snapshot cloud-run yourEnvironmentName 
	--project yourGCPProject 
	--region yourGCPRegion 

```
</Accordion>
<Accordion title="report only the named services and jobs">
```shell
kosli snapshot cloud-run yourEnvironmentName 
	--project yourGCPProject 
	--region yourGCPRegion 
	--include hello-world,sandman-job 

```
</Accordion>
<Accordion title="report everything except the kosli-reporter job (the Job that runs this command)">
```shell
kosli snapshot cloud-run yourEnvironmentName 
	--project yourGCPProject 
	--region yourGCPRegion 
	--exclude kosli-reporter 
```
</Accordion>
</AccordionGroup>

