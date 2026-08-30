---
title: "kosli create flow"
description: "Create or update a Kosli flow."
---

## Synopsis

```shell
kosli create flow FLOW-NAME [flags]
```

Create or update a Kosli flow.
You can specify flow parameters in flags.

`FLOW-NAME`s must start with a letter or number, and only contain letters, numbers, `.`, `-`, `_`, and `~`.


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--description` | string | [optional] The Kosli flow description. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for flow |
| `-t`, `--template` | strings | [defaulted] The comma-separated list of required compliance controls names. |
| `-f`, `--template-file` | string | [optional] The path to a yaml template file. Cannot be used together with `--use-empty-template` |
| `--use-empty-template` | bool | Use an empty template for the flow creation without specifying a file. Cannot be used together with `--template` or `--template-file` |
| `--visibility` | string | [deprecated] The visibility of the Kosli flow. This flag is deprecated and will be removed in a future version. (DEPRECATED: this flag is deprecated and will be removed in a future version.) |


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


## Live Examples in different CI systems

<Tabs>
	<Tab title="GitHub">
	View an example of the `kosli create flow` command in GitHub.

	In [this YAML file](https://github.com/cyber-dojo/runner/blob/976b63e8001ec7441ebc7737ca69f620d47e7ffe/.github/workflows/main.yml#L62)
	</Tab>
	<Tab title="GitLab">
	View an example of the `kosli create flow` command in GitLab.

	In [this YAML file](https://gitlab.com/cyber-dojo/creator/-/blob/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c/.gitlab/workflows/main.yml#L53)
	</Tab>
</Tabs>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="create/update a Kosli flow (with empty template)">
```shell
kosli create flow yourFlowName 
	--description yourFlowDescription 
	--use-empty-template 

```
</Accordion>
<Accordion title="create/update a Kosli flow (with template file)">
```shell
kosli create flow yourFlowName 
	--description yourFlowDescription 
	--template-file /path/to/your/template/file.yml 
```
</Accordion>
</AccordionGroup>

