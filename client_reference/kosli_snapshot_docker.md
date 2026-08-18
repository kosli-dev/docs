---
title: "kosli snapshot docker"
description: "Report a snapshot of running containers from docker host to Kosli.  "
---

## Synopsis

```shell
kosli snapshot docker ENVIRONMENT-NAME [flags]
```

Report a snapshot of running containers from docker host to Kosli.  
The reported data includes container image digests 
and creation timestamps. Containers running images which have not
been pushed to or pulled from a registry will be ignored.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for docker |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-A`, `--auto-environment` | bool | [optional] Create the environment (with the type inferred from the snapshot subcommand) if it does not already exist, before reporting the snapshot. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
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
<Accordion title="report what is running in a docker host">
```shell
kosli snapshot docker yourEnvironmentName 

```
</Accordion>
<Accordion title="report a docker snapshot, creating the environment first if it does not exist">
```shell
kosli snapshot docker yourEnvironmentName 
	--auto-environment 
	--environment-description "Production docker host" 
```
</Accordion>
</AccordionGroup>

