---
title: "kosli get rego-policy"
tag: "BETA"
description: "Get a rego policy, or one version of it."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli get rego-policy IDENTIFIER [flags]
```

Get a rego policy, or one version of it.
Without `--policy-version`, the policy is shown with its newest version and its current
version. The current version is the highest-numbered valid version, which is the
one an evaluation runs, so it can be older than the newest version.

With `--policy-version`, that version is shown with its status, its digest, who
published it and when, and the reason when it is rejected or failed. The command
exits 0 whatever the status of the version.

With `--download` and `--policy-version`, the bundle of that version is written to the
given file as a gzipped tar, unchanged and whatever the status of the version, in place
of printing it. An existing file is not overwritten.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--download` | string | [optional] The file to write the bundle of the version given by `--policy-version` to, as a gzipped tar. An existing file is not overwritten. |
| `-h`, `--help` | bool | help for rego-policy |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--policy-version` | int | [optional] The version of the rego policy to get. Without it, the policy and its current version are shown. |


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
<Accordion title="get a rego policy and its current version">
```shell
kosli get rego-policy pr-approved 

```
</Accordion>
<Accordion title="get version 3 of a rego policy">
```shell
kosli get rego-policy pr-approved 
	--policy-version 3 

```
</Accordion>
<Accordion title="download the bundle of version 3 of a rego policy to ./pr-approved-v3.tgz">
```shell
kosli get rego-policy pr-approved 
	--policy-version 3 
	--download ./pr-approved-v3.tgz 

```
</Accordion>
<Accordion title="get version 3 of a rego policy as JSON">
```shell
kosli get rego-policy pr-approved 
	--policy-version 3 
	--output json 
```
</Accordion>
</AccordionGroup>

