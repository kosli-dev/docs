---
title: "kosli create attestation-type"
description: "Create or update a Kosli custom attestation type."
---

## Synopsis

```shell
kosli create attestation-type TYPE-NAME [flags]
```

Create or update a Kosli custom attestation type.
You can specify attestation type parameters in flags.

`TYPE-NAME` must start with a letter or number, and only contain letters, numbers, `.`, `-`, `_`, and `~`.

`--schema` is a path to a file containing a JSON schema which will be used to validate attestations made using this type.  
The schema is used to specify the structure of the attestation data, e.g. any fields that are required or 
the expected type of the data.
See an example schema file 
[here](https://github.com/cyber-dojo/kosli-attestation-types/blob/f9130c58d3a8151b0b0e7c5db284e4380eb2d2cf/metrics-coverage.schema.json).

`--jq` defines an evaluation rule, given in jq-format, for this attestation type. The flag can be repeated in order to add additional rules.  
These rules specify acceptable values for attestation data, e.g. `.age >= 21` or `.failing_tests == 0`.  
When a custom attestation is reported, the provided data is evaluated according to the rules defined in its attestation-type. 
All rules must return `true` for the evaluation to pass and the attestation to be determined compliant.

`--summary` defines one entry of the summary shown for attestations of this type, given as
`'NAME=EXPRESSION'` where the expression is a jq expression evaluated against the attestation data.
The flag can be repeated to add further entries, which are displayed in the order given, e.g.
`--summary "Critical=.critical_count" --summary "Tool=.scanner.name"`.
Each value is split on its first `=` only, so jq expressions containing `==` are unaffected.

`--summary-json` is an alternative to `--summary` for summaries that are easier to express as JSON,
given as a JSON array of `\{"name": ..., "expression": ...\}` entries, e.g.
`'[\{"name":"Critical","expression":".critical_count"\}]'`. The two summary flags cannot be combined.

Attestation types created without a summary fall back to the jq evaluation rules checklist.


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-d`, `--description` | string | [optional] The attestation type description. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for attestation-type |
| `--jq` | stringArray | [optional] The attestation type evaluation JQ rules. |
| `-s`, `--schema` | string | [optional] Path to the attestation type schema in JSON Schema format. |
| `--summary` | stringArray | [optional] An attestation type summary entry, given as 'NAME=EXPRESSION'. Can be repeated. Cannot be used with `--summary-json`. |
| `--summary-json` | string | [optional] The attestation type summary, given as a JSON array of \{name, expression\} entries, e.g. '[\{"name":"Critical","expression":".critical_count"\}]'. Cannot be used with `--summary`. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Live Examples in different CI systems

<Tabs>
	<Tab title="GitHub">
	View an example of the `kosli create attestation-type` command in GitHub.

	In [this YAML file](https://github.com/cyber-dojo/kosli-attestation-types/blob/e115b88d482df7563cb10ac4fe80bdc34aad1209/.github/workflows/main.yml#L50)
	</Tab>
</Tabs>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="create/update a custom attestation type with no schema no evaluation rules">
```shell
kosli create attestation-type customTypeName

```
</Accordion>
<Accordion title="create/update a custom attestation type with schema and jq evaluation rules">
```shell
kosli create attestation-type customTypeName 
    --description "Attest that a person meets the age requirements." 
    --schema person-schema.json 
    --jq ".age >= 18"
    --jq ".age < 65"

```
</Accordion>
<Accordion title="create/update a custom attestation type with a summary">
```shell
kosli create attestation-type customTypeName 
    --schema scan-schema.json 
    --summary "Critical=.critical_count" 
    --summary "Tool=.scanner.name"

```
</Accordion>
<Accordion title="create/update a custom attestation type with a summary given as JSON">
```shell
kosli create attestation-type customTypeName 
    --schema scan-schema.json 
    --summary-json '[{"name":"Critical","expression":".critical_count"},{"name":"Tool","expression":".scanner.name"}]'
```
</Accordion>
</AccordionGroup>

