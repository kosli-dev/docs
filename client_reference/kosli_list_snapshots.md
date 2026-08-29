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
    "index": 5285,
    "from": 1787991898.5420277,
    "to": 0.0,
    "compliant": true,
    "duration": 8434.692311048508
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
  },
  {
    "index": 5277,
    "from": 1787665138.622218,
    "to": 1787665198.4042735,
    "compliant": true,
    "duration": 59.782055616378784
  },
  {
    "index": 5276,
    "from": 1787626078.5962257,
    "to": 1787665138.622218,
    "compliant": true,
    "duration": 39060.025992155075
  },
  {
    "index": 5275,
    "from": 1787626018.4113095,
    "to": 1787626078.5962257,
    "compliant": true,
    "duration": 60.184916257858276
  },
  {
    "index": 5274,
    "from": 1787540038.5204227,
    "to": 1787626018.4113095,
    "compliant": true,
    "duration": 85979.8908867836
  },
  {
    "index": 5273,
    "from": 1787539978.524768,
    "to": 1787540038.5204227,
    "compliant": true,
    "duration": 59.995654582977295
  },
  {
    "index": 5272,
    "from": 1787486638.4653506,
    "to": 1787539978.524768,
    "compliant": true,
    "duration": 53340.05941748619
  },
  {
    "index": 5271,
    "from": 1787486578.4888847,
    "to": 1787486638.4653506,
    "compliant": true,
    "duration": 59.976465940475464
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

