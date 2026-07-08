---
title: "kosli get repo"
description: "Get a repo for an org."
---

## Synopsis

```shell
kosli get repo [REPO-NAME] [flags]
```

Get a repo for an org.
The repo is identified either by its name, specified as an argument
(e.g. "my-org/my-repo"), or unambiguously by its internal ID via --repo-id.
The output includes the repo's internal ID, which is the identifier used
to tag the repo (see: kosli tag).
Use --provider to disambiguate when multiple repos share the same name
across VCS providers.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for repo  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--provider` string  |  [optional] The VCS provider of the repo (e.g. github, gitlab). Required when multiple repos share the same name across providers.  |
|        `--repo-id` string  |  [optional] The repo's internal ID (as shown in the repo output). Identifies the repo unambiguously; cannot be combined with the REPO-NAME argument.  |


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
<Accordion title="get a repo">
```shell
kosli get repo my-org/my-repo 

```
</Accordion>
<Accordion title="get a repo whose name exists across multiple VCS providers">
```shell
kosli get repo my-org/my-repo 
	--provider github 

```
</Accordion>
<Accordion title="get a repo by its internal ID">
```shell
kosli get repo --repo-id yourRepoID 
```
</Accordion>
</AccordionGroup>

