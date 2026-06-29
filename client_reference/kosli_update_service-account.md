---
title: "kosli update service-account"
description: "Update a service account."
---

## Synopsis

```shell
kosli update service-account SERVICE-ACCOUNT-NAME [flags]
```

Update a service account.

Only the flags you provide are changed; omitted fields are left untouched.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-d`, `--description` string  |  [optional] A description for the service account.  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for service-account  |
|        `--privilege` string  |  The privilege granted to the service account. One of: [admin, member, snapshotter, reader].  |


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
<Accordion title="update a service account's description">
```shell
kosli update service-account yourServiceAccountName 
	--description "new description" 

```
</Accordion>
<Accordion title="update a service account's privilege">
```shell
kosli update service-account yourServiceAccountName 
	--privilege member 
```
</Accordion>
</AccordionGroup>

