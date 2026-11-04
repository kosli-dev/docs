---
title: "kosli evaluate policy"
tag: "BETA"
description: "Evaluate a policy against a trail in Kosli."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli evaluate policy [flags]
```

Evaluate a policy against a trail in Kosli.
The policy is evaluated where the trail is stored, against the trail as Kosli
recorded it, and the verdict is printed here.

Name what to evaluate with `--context trail=`flow`/`trail``, repeated once per
trail. Trails named in one command are all evaluated at the same instant.

Name the policy with one of:
  - `--identifier`: a rego policy published to Kosli. Its current version, the
    highest-numbered valid one, is evaluated, and the evaluation cites that version.
    Append `@v`n``, as in `pr-approved@v2`, to evaluate version n instead, which
    must be valid; publishing a newer version does not change what it runs.
  - `--path`: the policy's files on this machine, sent with the evaluation.

`--path` takes a Rego file or a directory, and can be given more than once,
so a policy and a shared library are sent together from wherever each is kept.
Every `--path` joins one bundle. A file is keyed by its own name, and a file
in a directory by its path relative to that directory. Files in dot-directories,
such as `.git`, are left out; every other file travels, so notes such as
`README.md` stay with the policy.

Of what travels, the evaluator loads only:
  - Rego modules: `*.rego`, other than tests (`*_test.rego`). Modules import
    each other by package, so where each file sits does not matter.
  - Data files: `data.json`, `data.yaml`, `data.yml`, `*.ergo.yaml` and
    `*.ergo.yml`. Each is read into `data` at its directory's path in the
    bundle, so `controls/x/data.yaml` becomes `data.controls.x`. A data file
    cannot write `data.params`, which belongs to `--params`.
Every other file is carried but not read.

Two loaded files under one name are refused, naming both. For any other file the
first `--path` given wins, and the copy left behind is named on stderr.

The policy package is the one that declares `allow`; every other package is a
library. Where several packages declare `allow`, annotate an entrypoint in exactly
one of them to say which is the policy. In the policy package:
  - `allow` is always evaluated, whether annotated or not. It must be a boolean
    for every input, so give it a default (`default allow := false`): an undefined
    `allow` fails the evaluation rather than denying.
  - Every rule annotated with `# METADATA` and `# entrypoint: true` is evaluated
    too, and returned under its rule name in `result.outputs`, such as
    `violations` or `report`. A rule undefined for this input is left out.
  - Every other rule is evaluated only as far as those rules need it.
An entrypoint annotated outside the policy package, or on a function, is refused.

Pass `--control` to record the outcome as a decision against that control, in the
`--flow` and `--trail` given. The decision is recorded where the policy runs, so
the verdict is never asserted from here. Without `--control` nothing is recorded.
Only a published policy can record a decision, so `--control` needs `--identifier`.

Use `--params` to pass values the policy reads as `data.params`. For a
published policy, they must match the params schema of the version evaluated.
Pass `--assert` to exit with a non-zero status when the policy denies.
The policy that ran is printed with the verdict: a published policy by its
identifier, version and digest, and an inline one by its digest.
Use `--output json` to print the evaluation as Kosli returns it.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--assert` | bool | [optional] Exit with a non-zero status when the policy denies. Without it the verdict is printed and the command exits 0. |
| `--context` | stringArray | What to evaluate, as trail=`flow`/`trail`. Repeat it to evaluate several trails at one instant. |
| `--control` | string | [optional] Record the outcome as a decision against this control. Only a published policy (`--identifier`) can record one. Without it nothing is recorded. |
| `--fingerprint` | string | [optional] The SHA256 fingerprint of the artifact the decision is about. Without it the decision is about the trail. |
| `-f`, `--flow` | string | [conditional] The Kosli flow the decision is recorded in. Only required with `--control`. |
| `-h`, `--help` | bool | help for policy |
| `--identifier` | string | Identifier of a rego policy published to Kosli. Its current version is evaluated, or version n given as `identifier`@v`n`. |
| `--name` | string | [defaulted] The attestation name the decision is recorded under. Defaults to `control`-decision. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--params` | string | [optional] Policy parameters as inline JSON or @file.json. Available in policies as data.params. |
| `-p`, `--path` | stringArray | Path of a Rego policy file, or of a directory sent as one bundle. Repeat it to send a policy with libraries kept elsewhere. |
| `--policy` | stringArray | Deprecated alias of `--path`. (DEPRECATED: use `--path` instead) |
| `--trail` | string | [conditional] The Kosli trail the decision is recorded in. Only required with `--control`. |


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
<Accordion title="evaluate a policy against a trail">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--path yourPolicyFile.rego 

```
</Accordion>
<Accordion title="evaluate the current version of a published rego policy against a trail">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--identifier yourPolicyIdentifier 

```
</Accordion>
<Accordion title="evaluate version 2 of a published rego policy, whatever its current version">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--identifier yourPolicyIdentifier@v2 

```
</Accordion>
<Accordion title="evaluate a policy directory with a shared library kept elsewhere">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--path yourPolicyDirectory 
	--path path/to/ergo/ergo.rego 

```
</Accordion>
<Accordion title="evaluate several trails at one instant">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--context trail=anotherFlowName/anotherTrailName 
	--path yourPolicyFile.rego 

```
</Accordion>
<Accordion title="evaluate a policy with parameters (inline JSON or @file.json)">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--path yourPolicyFile.rego 
	--params '{"protected_branch": "master"}' 

```
</Accordion>
<Accordion title="evaluate a published policy and record the outcome as a decision">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--identifier yourPolicyIdentifier 
	--control yourControlIdentifier 
	--fingerprint yourArtifactFingerprint 

```
</Accordion>
<Accordion title="evaluate a policy and fail the step when it denies">
```shell
kosli evaluate policy 
	--context trail=yourFlowName/yourTrailName 
	--path yourPolicyFile.rego 
	--assert 
```
</Accordion>
</AccordionGroup>

