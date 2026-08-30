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
    "index": 5292,
    "from": 1788074998.5362537,
    "to": 0.0,
    "compliant": true,
    "duration": 24053.718024015427
  },
  {
    "index": 5291,
    "from": 1788074938.4944596,
    "to": 1788074998.5362537,
    "compliant": true,
    "duration": 60.04179406166077
  },
  {
    "index": 5290,
    "from": 1788074758.3723075,
    "to": 1788074938.4944596,
    "compliant": true,
    "duration": 180.12215209007263
  },
  {
    "index": 5289,
    "from": 1788074698.548716,
    "to": 1788074758.3723075,
    "compliant": true,
    "duration": 59.823591470718384
  },
  {
    "index": 5288,
    "from": 1788074398.5222037,
    "to": 1788074698.548716,
    "compliant": true,
    "duration": 300.0265123844147
  },
  {
    "index": 5287,
    "from": 1788074338.5482786,
    "to": 1788074398.5222037,
    "compliant": true,
    "duration": 59.97392511367798
  },
  {
    "index": 5286,
    "from": 1788073858.501626,
    "to": 1788074338.5482786,
    "compliant": true,
    "duration": 480.0466525554657
  },
  {
    "index": 5285,
    "from": 1787991898.5420277,
    "to": 1788073858.501626,
    "compliant": true,
    "duration": 81959.95959830284
  },
  {
    "index": 5284,
    "from": 1787991838.452193,
    "to": 1787991898.5420277,
    "compliant": true,
    "duration": 60.089834690093994
  },
  {
    "index": 5283,
    "from": 1787923678.398171,
    "to": 1787991838.452193,
    "compliant": true,
    "duration": 68160.05402207375
  },
  {
    "index": 5282,
    "from": 1787923618.562095,
    "to": 1787923678.398171,
    "compliant": true,
    "duration": 59.83607602119446
  },
  {
    "index": 5281,
    "from": 1787923558.488644,
    "to": 1787923618.562095,
    "compliant": true,
    "duration": 60.07345104217529
  },
  {
    "index": 5280,
    "from": 1787832538.6775455,
    "to": 1787923558.488644,
    "compliant": true,
    "duration": 91019.81109833717
  },
  {
    "index": 5279,
    "from": 1787713198.4663308,
    "to": 1787832538.6775455,
    "compliant": true,
    "duration": 119340.21121478081
  },
  {
    "index": 5278,
    "from": 1787665198.4042735,
    "to": 1787713198.4663308,
    "compliant": true,
    "duration": 48000.0620572567
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

