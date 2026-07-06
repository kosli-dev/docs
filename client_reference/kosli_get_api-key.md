---
title: "kosli get api-key"
description: "Get an API key's metadata for a service account."
---

## Synopsis

```shell
kosli get api-key KEY-ID [flags]
```

Get an API key's metadata for a service account.

Only the metadata of the API key is returned; the key value itself is never
returned (it is only shown once, at creation or rotation time).

## Flags
| Flag | Description |
| :--- | :--- |
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
<Accordion title="get the metadata of an API key">
```shell
kosli get api-key yourApiKeyID 
	--service-account yourServiceAccountName 
```
</Accordion>
</AccordionGroup>

