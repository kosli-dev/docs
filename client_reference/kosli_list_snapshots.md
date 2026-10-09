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
    "index": 5440,
    "from": 1791532978.4470391,
    "to": 0.0,
    "compliant": true,
    "duration": 10104.519061088562
  },
  {
    "index": 5439,
    "from": 1791532918.396811,
    "to": 1791532978.4470391,
    "compliant": true,
    "duration": 60.050228118896484
  },
  {
    "index": 5438,
    "from": 1791446518.4396853,
    "to": 1791532918.396811,
    "compliant": true,
    "duration": 86399.95712566376
  },
  {
    "index": 5437,
    "from": 1791446458.464416,
    "to": 1791446518.4396853,
    "compliant": true,
    "duration": 59.97526931762695
  },
  {
    "index": 5436,
    "from": 1791364498.6102662,
    "to": 1791446458.464416,
    "compliant": true,
    "duration": 81959.85414981842
  },
  {
    "index": 5435,
    "from": 1791364438.7490525,
    "to": 1791364498.6102662,
    "compliant": true,
    "duration": 59.86121368408203
  },
  {
    "index": 5434,
    "from": 1791359158.482706,
    "to": 1791364438.7490525,
    "compliant": true,
    "duration": 5280.26634645462
  },
  {
    "index": 5433,
    "from": 1791359098.4814715,
    "to": 1791359158.482706,
    "compliant": true,
    "duration": 60.00123453140259
  },
  {
    "index": 5432,
    "from": 1791290338.5569851,
    "to": 1791359098.4814715,
    "compliant": true,
    "duration": 68759.9244863987
  },
  {
    "index": 5431,
    "from": 1791290278.418337,
    "to": 1791290338.5569851,
    "compliant": true,
    "duration": 60.13864803314209
  },
  {
    "index": 5430,
    "from": 1791288238.338127,
    "to": 1791290278.418337,
    "compliant": true,
    "duration": 2040.0802102088928
  },
  {
    "index": 5429,
    "from": 1791288178.539898,
    "to": 1791288238.338127,
    "compliant": true,
    "duration": 59.79822897911072
  },
  {
    "index": 5428,
    "from": 1791287938.6191223,
    "to": 1791288178.539898,
    "compliant": true,
    "duration": 239.92077565193176
  },
  {
    "index": 5427,
    "from": 1791287878.4187279,
    "to": 1791287938.6191223,
    "compliant": true,
    "duration": 60.20039439201355
  },
  {
    "index": 5426,
    "from": 1791287818.5233977,
    "to": 1791287878.4187279,
    "compliant": true,
    "duration": 59.89533019065857
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

