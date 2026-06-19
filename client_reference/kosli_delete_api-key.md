---
title: "kosli delete api-key"
beta: false
deprecated: false
description: "Delete one or more API keys for a service account."
---

## Synopsis

```shell
kosli delete api-key KEY-ID [KEY-ID...] [flags]
```

Delete one or more API keys for a service account.

This permanently deletes the API key(s) identified by KEY-ID. Deletion is immediate and
cannot be undone. You are asked to confirm before the key is deleted; use
`--assume-yes`/`--yes` to skip the confirmation prompt.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-y`, `--assume-yes`  |  [optional] Skip the confirmation prompt and delete the API key without asking. (alias: `--yes`)  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for api-key  |
|    `-s`, `--service-account` string  |  The name of the service account whose API keys are managed.  |


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
<Accordion title="delete an API key for a service account (asks for confirmation)">
```shell
kosli delete api-key yourApiKeyID 
	--service-account yourServiceAccountName 

```
</Accordion>
<Accordion title="delete multiple API keys at once">
```shell
kosli delete api-key keyID1 keyID2 
	--service-account yourServiceAccountName 

```
</Accordion>
<Accordion title="delete an API key without confirmation">
```shell
kosli delete api-key yourApiKeyID 
	--service-account yourServiceAccountName 
	--assume-yes 
```
</Accordion>
</AccordionGroup>

