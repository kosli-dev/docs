---
title: "kosli archive rego-policy"
description: "Archive a rego policy."
---

## Synopsis

```shell
kosli archive rego-policy POLICY-IDENTIFIER [flags]
```

Archive a rego policy.
An archived rego policy is left out of `kosli list rego-policies` unless `--archived` is given.
Archiving creates no version: its versions stay readable with `kosli get rego-policy`, an
evaluation of it still runs, and its identifier stays taken. Only an org admin can archive.
Restore it with `kosli unarchive rego-policy`.


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for rego-policy |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="archive a rego policy">
```shell
kosli archive rego-policy yourPolicyIdentifier 
```
</Accordion>
</AccordionGroup>

