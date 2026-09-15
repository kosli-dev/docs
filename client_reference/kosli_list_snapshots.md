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
    "index": 5363,
    "from": 1789454518.4863305,
    "to": 0.0,
    "compliant": true,
    "duration": 11919.394330501556
  },
  {
    "index": 5362,
    "from": 1789454458.4640598,
    "to": 1789454518.4863305,
    "compliant": true,
    "duration": 60.02227067947388
  },
  {
    "index": 5361,
    "from": 1789453558.4911904,
    "to": 1789454458.4640598,
    "compliant": true,
    "duration": 899.9728693962097
  },
  {
    "index": 5360,
    "from": 1789453498.3979437,
    "to": 1789453558.4911904,
    "compliant": true,
    "duration": 60.09324669837952
  },
  {
    "index": 5359,
    "from": 1789369498.5293138,
    "to": 1789453498.3979437,
    "compliant": true,
    "duration": 83999.8686299324
  },
  {
    "index": 5358,
    "from": 1789369258.6142702,
    "to": 1789369498.5293138,
    "compliant": true,
    "duration": 239.915043592453
  },
  {
    "index": 5357,
    "from": 1789282078.311934,
    "to": 1789369258.6142702,
    "compliant": true,
    "duration": 87180.30233621597
  },
  {
    "index": 5356,
    "from": 1789282018.519421,
    "to": 1789282078.311934,
    "compliant": true,
    "duration": 59.79251289367676
  },
  {
    "index": 5355,
    "from": 1789194658.6698983,
    "to": 1789282018.519421,
    "compliant": true,
    "duration": 87359.84952282906
  },
  {
    "index": 5354,
    "from": 1789194598.7839112,
    "to": 1789194658.6698983,
    "compliant": true,
    "duration": 59.88598704338074
  },
  {
    "index": 5353,
    "from": 1789194538.4029229,
    "to": 1789194598.7839112,
    "compliant": true,
    "duration": 60.380988359451294
  },
  {
    "index": 5352,
    "from": 1789108858.5535865,
    "to": 1789194538.4029229,
    "compliant": true,
    "duration": 85679.84933638573
  },
  {
    "index": 5351,
    "from": 1789108798.4511206,
    "to": 1789108858.5535865,
    "compliant": true,
    "duration": 60.102465867996216
  },
  {
    "index": 5350,
    "from": 1789023418.5988352,
    "to": 1789108798.4511206,
    "compliant": true,
    "duration": 85379.85228538513
  },
  {
    "index": 5349,
    "from": 1789023358.6002493,
    "to": 1789023418.5988352,
    "compliant": true,
    "duration": 59.99858593940735
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

