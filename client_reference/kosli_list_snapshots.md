---
title: "kosli list snapshots"
description: "List environment snapshots."
---

## Synopsis

```shell
kosli list snapshots ENV_NAME [flags]
```

List environment snapshots.
The results are paginated and ordered from latest to oldest.
By default, the page limit is 15 snapshots per page.

You can optionally specify an INTERVAL between two snapshot expressions with [expression]..[expression]. 

Expressions can be:
* ~N   N'th behind the latest snapshot  
* N    snapshot number N  
* NOW  the latest snapshot  

Either expression can be omitted to default to NOW.


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshots |
| `-i`, `--interval` | string | [optional] Expression to define specified snapshots range. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--reverse` | bool | [optional] Reverse the order of output list. |


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


## Live Example

To view a live example of 'kosli list snapshots' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli list snapshots aws-prod --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
[
  {
    "index": 5249,
    "from": 1787021218.5403302,
    "to": 0.0,
    "compliant": true,
    "duration": 48137.604617357254
  },
  {
    "index": 5248,
    "from": 1787021098.4627476,
    "to": 1787021218.5403302,
    "compliant": true,
    "duration": 120.07758259773254
  },
  {
    "index": 5247,
    "from": 1787020978.2979894,
    "to": 1787021098.4627476,
    "compliant": true,
    "duration": 120.16475820541382
  },
  {
    "index": 5246,
    "from": 1786935178.5993426,
    "to": 1787020978.2979894,
    "compliant": true,
    "duration": 85799.69864678383
  },
  {
    "index": 5245,
    "from": 1786935118.4628425,
    "to": 1786935178.5993426,
    "compliant": true,
    "duration": 60.136500120162964
  },
  {
    "index": 5244,
    "from": 1786934998.5150445,
    "to": 1786935118.4628425,
    "compliant": true,
    "duration": 119.94779801368713
  },
  {
    "index": 5243,
    "from": 1786934938.5676281,
    "to": 1786934998.5150445,
    "compliant": true,
    "duration": 59.94741630554199
  },
  {
    "index": 5242,
    "from": 1786934878.6721764,
    "to": 1786934938.5676281,
    "compliant": true,
    "duration": 59.89545178413391
  },
  {
    "index": 5241,
    "from": 1786848778.5561426,
    "to": 1786934878.6721764,
    "compliant": true,
    "duration": 86100.1160337925
  },
  {
    "index": 5240,
    "from": 1786848658.3665593,
    "to": 1786848778.5561426,
    "compliant": true,
    "duration": 120.18958330154419
  },
  {
    "index": 5239,
    "from": 1786848538.4219847,
    "to": 1786848658.3665593,
    "compliant": true,
    "duration": 119.94457459449768
  },
  {
    "index": 5238,
    "from": 1786761778.641311,
    "to": 1786848538.4219847,
    "compliant": true,
    "duration": 86759.7806737423
  },
  {
    "index": 5237,
    "from": 1786761658.6412923,
    "to": 1786761778.641311,
    "compliant": true,
    "duration": 120.00001859664917
  },
  {
    "index": 5236,
    "from": 1786761598.587937,
    "to": 1786761658.6412923,
    "compliant": true,
    "duration": 60.05335521697998
  },
  {
    "index": 5235,
    "from": 1786761538.4336553,
    "to": 1786761598.587937,
    "compliant": true,
    "duration": 60.15428185462952
  }
]
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list the last 15 snapshots for an environment">
```shell
kosli list snapshots yourEnvironmentName 

```
</Accordion>
<Accordion title="list the last 30 snapshots for an environment">
```shell
kosli list snapshots yourEnvironmentName 
	--page-limit 30 

```
</Accordion>
<Accordion title="list the last 30 snapshots for an environment (in JSON)">
```shell
kosli list snapshots yourEnvironmentName 
	--page-limit 30 
	--output json
```
</Accordion>
</AccordionGroup>

