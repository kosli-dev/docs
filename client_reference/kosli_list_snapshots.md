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
    "index": 5525,
    "from": 1793005258.405105,
    "to": 0.0,
    "compliant": true,
    "duration": 16409.958983659744
  },
  {
    "index": 5524,
    "from": 1792997998.4215035,
    "to": 1793005258.405105,
    "compliant": true,
    "duration": 7259.983601570129
  },
  {
    "index": 5523,
    "from": 1792997938.5429544,
    "to": 1792997998.4215035,
    "compliant": true,
    "duration": 59.878549098968506
  },
  {
    "index": 5522,
    "from": 1792997878.4152775,
    "to": 1792997938.5429544,
    "compliant": true,
    "duration": 60.12767696380615
  },
  {
    "index": 5521,
    "from": 1792997818.570323,
    "to": 1792997878.4152775,
    "compliant": true,
    "duration": 59.84495449066162
  },
  {
    "index": 5520,
    "from": 1792911058.5671353,
    "to": 1792997818.570323,
    "compliant": true,
    "duration": 86760.0031876564
  },
  {
    "index": 5519,
    "from": 1792910938.5917454,
    "to": 1792911058.5671353,
    "compliant": true,
    "duration": 119.97538995742798
  },
  {
    "index": 5518,
    "from": 1792910878.4835958,
    "to": 1792910938.5917454,
    "compliant": true,
    "duration": 60.10814952850342
  },
  {
    "index": 5517,
    "from": 1792910818.6568332,
    "to": 1792910878.4835958,
    "compliant": true,
    "duration": 59.826762676239014
  },
  {
    "index": 5516,
    "from": 1792823338.4445558,
    "to": 1792910818.6568332,
    "compliant": true,
    "duration": 87480.21227741241
  },
  {
    "index": 5515,
    "from": 1792823278.4616466,
    "to": 1792823338.4445558,
    "compliant": true,
    "duration": 59.982909202575684
  },
  {
    "index": 5514,
    "from": 1792823218.4381535,
    "to": 1792823278.4616466,
    "compliant": true,
    "duration": 60.02349305152893
  },
  {
    "index": 5513,
    "from": 1792737118.3849633,
    "to": 1792823218.4381535,
    "compliant": true,
    "duration": 86100.05319023132
  },
  {
    "index": 5512,
    "from": 1792737058.6320403,
    "to": 1792737118.3849633,
    "compliant": true,
    "duration": 59.752923011779785
  },
  {
    "index": 5511,
    "from": 1792651018.4846509,
    "to": 1792737058.6320403,
    "compliant": true,
    "duration": 86040.14738941193
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

