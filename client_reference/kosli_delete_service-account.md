---
title: "kosli delete service-account"
description: "Delete one or more service accounts."
---

## Synopsis

```shell
kosli delete service-account SERVICE-ACCOUNT-NAME [SERVICE-ACCOUNT-NAME...] [flags]
```

Delete one or more service accounts.

This permanently removes the service account(s) identified by SERVICE-ACCOUNT-NAME
from the organization, along with their API keys. Deletion is immediate and
cannot be undone. You are asked to confirm before deletion; use
`--assume-yes`/`--yes` to skip the confirmation prompt.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-y`, `--assume-yes`  |  [optional] Skip the confirmation prompt and delete the service account without asking. (alias: `--yes`)  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for service-account  |


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
<Accordion title="delete a service account (asks for confirmation)">
```shell
kosli delete service-account yourServiceAccountName 

```
</Accordion>
<Accordion title="delete multiple service accounts at once">
```shell
kosli delete service-account sa1 sa2 

```
</Accordion>
<Accordion title="delete a service account without confirmation">
```shell
kosli delete service-account yourServiceAccountName 
	--assume-yes 
```
</Accordion>
</AccordionGroup>

