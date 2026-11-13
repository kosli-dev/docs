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
Only unread updates are listed; use `--all` to list the ones you have seen too, unread first,
then the newest. An update about a feature that is not enabled for the org is left out.
The first 10 are listed, as in the Kosli app; use `--limit` to list more, or `--limit 0` for
no limit. `--all` and `--limit` apply to the JSON output as well, which also holds each
update's summary. Its `unread_count` is always the total number of unread updates, however
many are listed.

An update is unread when you have not seen it and it was published in the last 12 months.
A user who signed up less than 7 days before first listing product updates, in the CLI or in
the Kosli app, starts with every update seen. Listing leaves updates unread: use `--dismiss`
to mark the unread updates listed as seen, or `kosli dismiss product-updates` later.

Product updates are tracked per user, so the API token must belong to a member of the org.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--all` | bool | [optional] List the product updates you have seen too, not only the unread ones. |
| `--dismiss` | bool | [optional] Mark the unread product updates listed as seen. |
| `-h`, `--help` | bool | help for product-updates |
| `--limit` | int | [defaulted] The maximum number of product updates to list. 0 means no limit. (default 10) |
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
<Accordion title="list unread product updates">
```shell
kosli list product-updates 

```
</Accordion>
<Accordion title="list unread product updates and mark them as seen">
```shell
kosli list product-updates 
	--dismiss 

```
</Accordion>
<Accordion title="list every product update, read ones included">
```shell
kosli list product-updates 
	--all 
	--limit 0 

```
</Accordion>
<Accordion title="list unread product updates in JSON">
```shell
kosli list product-updates 
	--output json 
```
</Accordion>
</AccordionGroup>

