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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
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
    "index": 5547,
    "from": 1793346418.5157776,
    "to": 0.0,
    "compliant": true,
    "duration": 20029.8227519989
  },
  {
    "index": 5546,
    "from": 1793346358.4476938,
    "to": 1793346418.5157776,
    "compliant": true,
    "duration": 60.06808376312256
  },
  {
    "index": 5545,
    "from": 1793346298.4698195,
    "to": 1793346358.4476938,
    "compliant": true,
    "duration": 59.97787427902222
  },
  {
    "index": 5544,
    "from": 1793259778.583906,
    "to": 1793346298.4698195,
    "compliant": true,
    "duration": 86519.88591361046
  },
  {
    "index": 5543,
    "from": 1793259718.4603333,
    "to": 1793259778.583906,
    "compliant": true,
    "duration": 60.12357258796692
  },
  {
    "index": 5542,
    "from": 1793259658.404256,
    "to": 1793259718.4603333,
    "compliant": true,
    "duration": 60.05607724189758
  },
  {
    "index": 5541,
    "from": 1793179798.4294283,
    "to": 1793259658.404256,
    "compliant": true,
    "duration": 79859.97482776642
  },
  {
    "index": 5540,
    "from": 1793179438.4668915,
    "to": 1793179798.4294283,
    "compliant": true,
    "duration": 359.9625368118286
  },
  {
    "index": 5539,
    "from": 1793179378.4504976,
    "to": 1793179438.4668915,
    "compliant": true,
    "duration": 60.0163938999176
  },
  {
    "index": 5538,
    "from": 1793179318.5280147,
    "to": 1793179378.4504976,
    "compliant": true,
    "duration": 59.92248296737671
  },
  {
    "index": 5537,
    "from": 1793179198.512384,
    "to": 1793179318.5280147,
    "compliant": true,
    "duration": 120.0156307220459
  },
  {
    "index": 5536,
    "from": 1793179138.48383,
    "to": 1793179198.512384,
    "compliant": true,
    "duration": 60.02855396270752
  },
  {
    "index": 5535,
    "from": 1793179078.485261,
    "to": 1793179138.48383,
    "compliant": true,
    "duration": 59.99856901168823
  },
  {
    "index": 5534,
    "from": 1793179018.5465324,
    "to": 1793179078.485261,
    "compliant": true,
    "duration": 59.93872857093811
  },
  {
    "index": 5533,
    "from": 1793178958.449324,
    "to": 1793179018.5465324,
    "compliant": true,
    "duration": 60.09720849990845
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

