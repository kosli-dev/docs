---
title: "kosli create environment"
description: "Create or update a Kosli environment."
---

## Synopsis

```shell
kosli create environment ENVIRONMENT-NAME [flags]
```

Create or update a Kosli environment.

``--type`` must match the type of environment you wish to record snapshots from.
The following types are supported:
  - k8s        - Kubernetes
  - ecs        - Amazon Elastic Container Service
  - s3         - Amazon S3 object storage
  - lambda     - AWS Lambda serverless
  - docker     - Docker images
  - azure-apps - Azure app services
  - server     - Generic type
  - logical    - Logical grouping of real environments

Logical environments are used for grouping of physical environments. For instance **prod-aws** and **prod-s3** can
be grouped into logical environment **prod**. Logical environments are view-only, you can not report snapshots
to them.

`ENVIRONMENT-NAME`s must start with a letter or number, and only contain letters, numbers, `.`, `-` and `_`.


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-d`, `--description` | string | [optional] The environment description. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `--exclude-scaling` | bool | [optional] Exclude scaling events for snapshots. Snapshots with scaling changes will not result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `-h`, `--help` | bool | help for environment |
| `--include-scaling` | bool | [optional] Include scaling events for snapshots. Snapshots with scaling changes will result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `--included-environments` | strings | [optional] Comma separated list of environments to include in logical environment |
| `--require-provenance` | bool | [defaulted] Require provenance for all artifacts running in environment snapshots. (DEPRECATED: this flag is deprecated and will be removed in a future version. Use policies instead.) |
| `-t`, `--type` | string | The type of environment. Valid types are: [K8S, ECS, S3, lambda, server, docker, azure-apps, cloud-run, logical]. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="create a Kosli environment">
```shell
kosli create environment yourEnvironmentName
	--type K8S 
	--description "my new env" 

```
</Accordion>
<Accordion title="create a Kosli logical environment">
```shell
kosli create environment yourLogicalEnvironmentName
	--type logical 
	--included-environments realEnv1,realEnv2,realEnv3
	--description "my full prod" 
```
</Accordion>
</AccordionGroup>

