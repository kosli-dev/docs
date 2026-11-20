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
    "index": 5629,
    "from": 1795165858.5129378,
    "to": 0.0,
    "compliant": true,
    "duration": 5008.192062616348
  },
  {
    "index": 5628,
    "from": 1795165798.3513625,
    "to": 1795165858.5129378,
    "compliant": true,
    "duration": 60.16157531738281
  },
  {
    "index": 5627,
    "from": 1795165738.488801,
    "to": 1795165798.3513625,
    "compliant": true,
    "duration": 59.86256146430969
  },
  {
    "index": 5626,
    "from": 1795165678.4643247,
    "to": 1795165738.488801,
    "compliant": false,
    "duration": 60.024476289749146
  },
  {
    "index": 5625,
    "from": 1795105798.4498813,
    "to": 1795165678.4643247,
    "compliant": true,
    "duration": 59880.01444339752
  },
  {
    "index": 5624,
    "from": 1795105738.3652306,
    "to": 1795105798.4498813,
    "compliant": true,
    "duration": 60.08465075492859
  },
  {
    "index": 5623,
    "from": 1795105678.5140104,
    "to": 1795105738.3652306,
    "compliant": true,
    "duration": 59.85122013092041
  },
  {
    "index": 5622,
    "from": 1795105618.4046922,
    "to": 1795105678.5140104,
    "compliant": true,
    "duration": 60.109318256378174
  },
  {
    "index": 5621,
    "from": 1795105558.4810343,
    "to": 1795105618.4046922,
    "compliant": true,
    "duration": 59.92365789413452
  },
  {
    "index": 5620,
    "from": 1795105498.5133078,
    "to": 1795105558.4810343,
    "compliant": true,
    "duration": 59.96772646903992
  },
  {
    "index": 5619,
    "from": 1795105438.5261724,
    "to": 1795105498.5133078,
    "compliant": true,
    "duration": 59.98713541030884
  },
  {
    "index": 5618,
    "from": 1795105258.3714306,
    "to": 1795105438.5261724,
    "compliant": true,
    "duration": 180.1547417640686
  },
  {
    "index": 5617,
    "from": 1795105198.4445667,
    "to": 1795105258.3714306,
    "compliant": true,
    "duration": 59.9268639087677
  },
  {
    "index": 5616,
    "from": 1795080718.4478593,
    "to": 1795105198.4445667,
    "compliant": true,
    "duration": 24479.996707439423
  },
  {
    "index": 5615,
    "from": 1795080658.4572291,
    "to": 1795080718.4478593,
    "compliant": true,
    "duration": 59.99063014984131
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

