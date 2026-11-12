---
title: "kosli list product-updates"
tag: "BETA"
description: "List Kosli product updates."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli list product-updates [flags]
```

List Kosli product updates.
Product updates are the new features and improvements published in Kosli's changelog.
Unread updates are listed first, then the newest. An update about a feature that is not
enabled for the org is left out. The first time you list them, in the CLI or in the Kosli app,
every update is marked as seen, so none is shown as unread; only updates published after that
start as unread. Dismiss those with `kosli dismiss product-updates`.
The update's summary is included in the JSON output.

Product updates are tracked per user, so the API token must belong to a member of the org.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for product-updates |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |


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
<Accordion title="list product updates">
```shell
kosli list product-updates 

```
</Accordion>
<Accordion title="list product updates in JSON">
```shell
kosli list product-updates 
	--output json 
```
</Accordion>
</AccordionGroup>

