---
title: "kosli get evaluation"
tag: "BETA"
description: "Get a server-side evaluation, or what it was given."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli get evaluation EVALUATION-ID [flags]
```

Get a server-side evaluation, or what it was given.
The evaluation is shown with its status, the policy it ran, the trails it was
asked about, its outcome when it completed, the error when it failed, and the
decision it recorded, if any. The command exits 0 whatever the outcome.

With `--show-input` and `--output json`, the document the policy read as `input` is
added under `.input`: each trail as it stood at the evaluation's request time.

With `--fixture` and `--dir`, what the evaluation was given is written to the
directory, so it can be replayed with stock OPA:
  - `input.json`: the document the policy read as `input`.
  - `data.json`: the params, which the policy reads as `data.params`.
  - `policy/`: the files of the policy that ran, at their paths in the bundle.
The directory must be empty or not exist yet. An evaluation that is still
pending can be written too, as its input does not depend on its outcome.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--dir` | string | [conditional] The directory `--fixture` writes to. It must be empty or not exist yet. Only needed with `--fixture`. |
| `--fixture` | bool | [optional] Write the evaluation's input, params and policy files to `--dir`, to replay it with OPA. |
| `-h`, `--help` | bool | help for evaluation |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--show-input` | bool | [optional] Add the document the policy read as input under .input. Needs `--output` json. |


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
<Accordion title="get an evaluation">
```shell
kosli get evaluation yourEvaluationID 

```
</Accordion>
<Accordion title="get an evaluation with the input its policy read">
```shell
kosli get evaluation yourEvaluationID 
	--show-input 
	--output json 

```
</Accordion>
<Accordion title="write what an evaluation was given to ./replay, and replay it with OPA">
```shell
kosli get evaluation yourEvaluationID 
	--fixture 
	--dir ./replay 
opa eval --input replay/input.json --data replay/data.json 
	--bundle replay/policy/ 'data.policy.allow'
```
</Accordion>
</AccordionGroup>

