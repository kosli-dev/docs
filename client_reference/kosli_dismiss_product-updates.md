---
title: "kosli dismiss product-updates"
tag: "BETA"
description: "Dismiss Kosli product updates, marking them as seen."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli dismiss product-updates {PRODUCT-UPDATE-ID [PRODUCT-UPDATE-ID...] | --all} [flags]
```

Dismiss Kosli product updates, marking them as seen.
A dismissed product update is no longer unread for you. Give the ids of the updates to
dismiss, as listed by `kosli list product-updates`, or use `--all` to dismiss every unread update.
An id of an update the org cannot see is ignored.

Product updates are tracked per user, so the API token must belong to a member of the org.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--all` | bool | [optional] Dismiss every unread product update, instead of giving their ids. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for product-updates |


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
<Accordion title="dismiss one product update">
```shell
kosli dismiss product-updates yourProductUpdateID 

```
</Accordion>
<Accordion title="dismiss several product updates">
```shell
kosli dismiss product-updates yourProductUpdateID1 yourProductUpdateID2 

```
</Accordion>
<Accordion title="dismiss every unread product update">
```shell
kosli dismiss product-updates 
	--all 
```
</Accordion>
</AccordionGroup>

