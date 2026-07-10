---
title: "kosli list repos"
description: "List repos for an org."
---

## Synopsis

```shell
kosli list repos [flags]
```

List repos for an org. The results are always paginated:
by default the first page is returned with 15 repos per page. Use --page to select
a page and --page-limit to change the page size (maximum 50).
The list can be filtered by name with --name (exact match), by name substring with
--search (case-insensitive, mutually exclusive with --name), by VCS provider with
--provider, by external repo ID with --repo-id, and by tags with --tag.
Results are sorted by repo name; use --sort-direction to choose asc or desc.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for repos  |
|        `--name` string  |  [optional] The repo name to filter by (exact match).  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--provider` string  |  [optional] The VCS provider to filter repos by (e.g. github, gitlab).  |
|        `--repo-id` string  |  [optional] The external repo ID to filter repos by.  |
|        `--search` string  |  [optional] Filter repos whose name contains this substring (case-insensitive). Mutually exclusive with `--name`.  |
|        `--sort-direction` string  |  [optional] The direction to sort repos by name. Valid values are: [asc, desc]. (defaults to asc)  |
|        `--tag` stringArray  |  [optional] Only list repos that have this tag, given as 'key' or 'key:value'. Can be repeated to match more than one tag.  |


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
<Accordion title="list repos for an org (first page, 15 per page)">
```shell
kosli list repos 

```
</Accordion>
<Accordion title="list repos filtered by name (exact match on the full repo name)">
```shell
kosli list repos 
	--name my-org/my-repo 

```
</Accordion>
<Accordion title="list repos whose name contains a substring (case-insensitive)">
```shell
kosli list repos 
	--search cli 

```
</Accordion>
<Accordion title="list repos filtered by VCS provider (in JSON)">
```shell
kosli list repos 
	--provider github 
	--output json

```
</Accordion>
<Accordion title="list repos tagged with team=platform">
```shell
kosli list repos 
	--tag team:platform 

```
</Accordion>
<Accordion title="list repos sorted by name, Z–A">
```shell
kosli list repos 
	--sort-direction desc 

```
</Accordion>
<Accordion title="show the second page of repos (25 per page)">
```shell
kosli list repos 
	--page-limit 25 
	--page 2 
```
</Accordion>
</AccordionGroup>

