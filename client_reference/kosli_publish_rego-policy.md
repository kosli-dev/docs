---
title: "kosli publish rego-policy"
tag: "BETA"
description: "Publish a new version of a rego policy in a Kosli org."
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli publish rego-policy IDENTIFIER [flags]
```

Publish a new version of a rego policy in a Kosli org.
The policy is addressed by IDENTIFIER, which decisions cite and which cannot be
changed after the first publish. `--name` is required on the first publish only.
Only an org admin can publish.

`--path` takes a Rego file or a directory on this machine, and can be given
more than once, so a policy and a shared library are published together from
wherever each is kept. Every `--path` joins one bundle, by the same rules as
`kosli evaluate policy --path`: files in dot-directories are left out, and the
bundle can hold at most 100 files and 1 MiB.

Each publish stores the next version, with `--comment` kept on it. A change to
the files or to `--input-schema` makes a new version. When the files and the
input schema are the same as the newest version, and that version is pending or
valid, nothing new is stored and that version is reported. A change to only
`--name` or `--description` makes no new version.

Kosli validates each version after it is stored, and the command waits up to 30
seconds for the result:
  - valid: the version can be evaluated. The command exits 0.
  - rejected: the policy is at fault, for example it does not compile. The
    command prints the reason and exits 1.
  - failed: Kosli could not validate the version. Publish again to retry. The
    command exits 1.
If the wait expires, the command exits 1 and says how to read the version later.
With `--output json`, the version is always printed: with the reason for a
rejected or failed one, and as pending when the wait expires.

An evaluation runs the highest-numbered valid version, so a rejected or failed
version leaves the policy in service unchanged.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--comment` | string | [optional] Why this version is published. It is kept with the version. |
| `--description` | string | [optional] The description of the rego policy. Without it the current description is kept. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for rego-policy |
| `--input-schema` | string | The shape of the input the policy is written against: trail (one trail) or trails (a set of trails). |
| `--name` | string | [conditional] The display name of the rego policy. Only required when the identifier is new; without it the current name is kept. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `-p`, `--path` | stringArray | Path of a Rego policy file, or of a directory sent as one bundle. Repeat it to publish a policy with libraries kept elsewhere. |


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
<Accordion title="publish the first version of a rego policy from a directory">
```shell
kosli publish rego-policy pr-approved 
	--path ./policies/pr-approved/ 
	--input-schema trail 
	--name "Pull request approved" 
	--description "Every change reached main through an approved PR" 
	--comment "Initial version" 

```
</Accordion>
<Accordion title="publish a new version of an existing rego policy from one file">
```shell
kosli publish rego-policy pr-approved 
	--path ./policies/pr-approved.rego 
	--input-schema trail 
	--comment "Also require two approvers" 

```
</Accordion>
<Accordion title="publish a policy directory with a shared library kept elsewhere">
```shell
kosli publish rego-policy pr-approved 
	--path ./policies/pr-approved/ 
	--path path/to/ergo/ergo.rego 
	--input-schema trail 

```
</Accordion>
<Accordion title="publish a policy written against a set of trails, and print the version as JSON">
```shell
kosli publish rego-policy release-ready 
	--path ./policies/release-ready/ 
	--input-schema trails 
	--name "Release ready" 
	--output json 

```
</Accordion>
<Accordion title="show what would be published, without sending it">
```shell
kosli publish rego-policy pr-approved 
	--path ./policies/pr-approved/ 
	--input-schema trail 
	--dry-run 
```
</Accordion>
</AccordionGroup>

