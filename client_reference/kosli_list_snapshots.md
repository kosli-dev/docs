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
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for snapshots  |
|    `-i`, `--interval` string  |  [optional] Expression to define specified snapshots range.  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--reverse`  |  [optional] Reverse the order of output list.  |


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
    "index": 4960,
    "from": 1783329958.5858161,
    "to": 0.0,
    "compliant": true,
    "duration": 21776.646351337433
  },
  {
    "index": 4959,
    "from": 1783329898.4900227,
    "to": 1783329958.5858161,
    "compliant": true,
    "duration": 60.09579348564148
  },
  {
    "index": 4958,
    "from": 1783325398.5364711,
    "to": 1783329898.4900227,
    "compliant": true,
    "duration": 4499.953551530838
  },
  {
    "index": 4957,
    "from": 1783325338.6830802,
    "to": 1783325398.5364711,
    "compliant": true,
    "duration": 59.85339093208313
  },
  {
    "index": 4956,
    "from": 1783318438.5819647,
    "to": 1783325338.6830802,
    "compliant": true,
    "duration": 6900.101115465164
  },
  {
    "index": 4955,
    "from": 1783318378.577469,
    "to": 1783318438.5819647,
    "compliant": true,
    "duration": 60.00449562072754
  },
  {
    "index": 4954,
    "from": 1783318258.5637438,
    "to": 1783318378.577469,
    "compliant": true,
    "duration": 120.01372528076172
  },
  {
    "index": 4953,
    "from": 1783230718.3802922,
    "to": 1783318258.5637438,
    "compliant": true,
    "duration": 87540.18345165253
  },
  {
    "index": 4952,
    "from": 1783230658.4344573,
    "to": 1783230718.3802922,
    "compliant": true,
    "duration": 59.94583487510681
  },
  {
    "index": 4951,
    "from": 1783230538.7431004,
    "to": 1783230658.4344573,
    "compliant": true,
    "duration": 119.69135689735413
  },
  {
    "index": 4950,
    "from": 1783147918.6154184,
    "to": 1783230538.7431004,
    "compliant": true,
    "duration": 82620.1276819706
  },
  {
    "index": 4949,
    "from": 1783143178.674288,
    "to": 1783147918.6154184,
    "compliant": true,
    "duration": 4739.941130399704
  },
  {
    "index": 4948,
    "from": 1783143118.472487,
    "to": 1783143178.674288,
    "compliant": true,
    "duration": 60.20180106163025
  },
  {
    "index": 4947,
    "from": 1783143058.4538293,
    "to": 1783143118.472487,
    "compliant": true,
    "duration": 60.01865768432617
  },
  {
    "index": 4946,
    "from": 1783142998.3936846,
    "to": 1783143058.4538293,
    "compliant": true,
    "duration": 60.060144662857056
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

