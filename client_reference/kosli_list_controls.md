---
title: "kosli list controls"
tag: "BETA"
description: "List controls for an org."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli list controls [flags]
```

List controls for an org.
The results are paginated; use --page and --page-limit to navigate the pages.

## Flags
| Flag | Description |
| :--- | :--- |
|        `--archived`  |  [optional] List archived controls instead of active ones.  |
|    `-h`, `--help`  |  help for controls  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--search` string  |  [optional] Only list controls whose name or identifier contains this substring (case-insensitive).  |
|        `--sort-direction` string  |  [optional] The direction to sort controls in. Valid values are: [asc, desc]. (defaults to asc)  |
|        `--tag` stringArray  |  [optional] Filter by tag, given as 'key' or 'key:value'. Can be repeated to match more than one tag.  |


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
<Accordion title="list the first page of controls for an org">
```shell
kosli list controls 

```
</Accordion>
<Accordion title="list the second page of controls (10 per page) in JSON">
```shell
kosli list controls 
	--page 2 
	--page-limit 10 
	--output json 

```
</Accordion>
<Accordion title="list controls whose name or identifier contains 'sdlc'">
```shell
kosli list controls 
	--search sdlc 

```
</Accordion>
<Accordion title="list controls tagged framework=finos-sdlc (--tag can be repeated)">
```shell
kosli list controls 
	--tag framework:finos-sdlc 

```
</Accordion>
<Accordion title="list archived controls instead of active ones">
```shell
kosli list controls 
	--archived 

```
</Accordion>
<Accordion title="list controls sorted in descending name order">
```shell
kosli list controls 
	--sort-direction desc 
```
</Accordion>
</AccordionGroup>

