---
title: "kosli list api-keys"
description: "List API keys for a service account."
---

## Synopsis

```shell
kosli list api-keys [flags]
```

List API keys for a service account.

Only the metadata of each active API key is returned; the key values themselves are never
listed (they are only shown once, at creation or rotation time).

## Flags
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for api-keys  |
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
<Accordion title="list the API keys for a service account">
```shell
kosli list api-keys 
	--service-account yourServiceAccountName 
```
</Accordion>
</AccordionGroup>

