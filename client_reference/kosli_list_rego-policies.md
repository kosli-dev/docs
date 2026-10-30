---
title: "kosli list rego-policies"
tag: "BETA"
description: "List rego policies for an org."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli list rego-policies [flags]
```

List rego policies for an org.
The results are paginated; use `--page` and `--page-limit` to navigate the pages.
By default, the policies changed most recently are listed first.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for rego-policies |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--search` | string | [optional] Only list rego policies whose name or identifier contains this substring (case-insensitive). |
| `--sort` | string | [optional] The field to sort rego policies by. Valid values are: [updated_at, identifier]. (defaults to updated_at) |
| `--sort-direction` | string | [optional] The direction to sort rego policies in. Valid values are: [asc, desc]. (defaults to desc) |


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
<Accordion title="list the first page of rego policies for an org">
```shell
kosli list rego-policies 

```
</Accordion>
<Accordion title="list the second page of rego policies (50 per page) in JSON">
```shell
kosli list rego-policies 
	--page 2 
	--page-limit 50 
	--output json 

```
</Accordion>
<Accordion title="list rego policies whose name or identifier contains 'approved'">
```shell
kosli list rego-policies 
	--search approved 

```
</Accordion>
<Accordion title="list rego policies in identifier order">
```shell
kosli list rego-policies 
	--sort identifier 
	--sort-direction asc 
```
</Accordion>
</AccordionGroup>

