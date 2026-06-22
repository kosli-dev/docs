---
title: "kosli create api-key"
description: "Create an API key for a service account."
---

## Synopsis

```shell
kosli create api-key [flags]
```

Create an API key for a service account.

The key value is only returned once, at creation time, so make sure to store it securely.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-d`, `--description` string  |  A description for the API key.  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-e`, `--expires-at` string  |  [optional] When the API key expires. Accepts an epoch timestamp or a date like '2026-06-04', '2026-06-04 15:04:05', or an RFC3339 timestamp. Defaults to no expiry.  |
|    `-h`, `--help`  |  help for api-key  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
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
<Accordion title="create an API key for a service account">
```shell
kosli create api-key 
	--service-account yourServiceAccountName 
	--description "key for CI" 

```
</Accordion>
<Accordion title="create an API key that expires on a given date">
```shell
kosli create api-key 
	--service-account yourServiceAccountName 
	--description "key for CI" 
	--expires-at 2026-12-31 
```
</Accordion>
</AccordionGroup>

