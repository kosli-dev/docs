---
title: "kosli update control"
tag: "BETA"
description: "Update a Kosli control."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli update control CONTROL-IDENTIFIER [flags]
```

Update a Kosli control.

Only the flags you provide are changed; omitted fields are left untouched.
Providing `--link` replaces all of the control's existing links.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-d`, `--description` string  |  [optional] The control description.  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for control  |
|        `--link` stringToString  |  [optional] A link for the control, given as 'name=url'. Can be repeated. Replaces all existing links.  |
|    `-n`, `--name` string  |  [optional] The new control name.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    `-a`, `--api-token` string  |  The Kosli API token.  |
|    `-c`, `--config-file` string  |  [optional] The Kosli config file path. (default "kosli")  |
|        `--debug`  |  [optional] Print debug logs to stdout.  |
|    `-H`, `--host` string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        `--http-proxy` string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    `-r`, `--max-api-retries` int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        `--org` string  |  The Kosli organization.  |
|    `-q`, `--quiet`  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins.  |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="update a control's name">
```shell
kosli update control yourControlIdentifier 
	--name "New control name" 

```
</Accordion>
<Accordion title="update a control's description and links">
```shell
kosli update control yourControlIdentifier 
	--description "what this control checks" 
	--link runbook=https://example.com/runbook 
```
</Accordion>
</AccordionGroup>

