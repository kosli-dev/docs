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
    "index": 5564,
    "from": 1793779378.4743404,
    "to": 0.0,
    "compliant": true,
    "duration": 17990.085461616516
  },
  {
    "index": 5563,
    "from": 1793779318.4284134,
    "to": 1793779378.4743404,
    "compliant": true,
    "duration": 60.04592704772949
  },
  {
    "index": 5562,
    "from": 1793779258.398902,
    "to": 1793779318.4284134,
    "compliant": true,
    "duration": 60.02951145172119
  },
  {
    "index": 5561,
    "from": 1793779198.5031774,
    "to": 1793779258.398902,
    "compliant": true,
    "duration": 59.8957245349884
  },
  {
    "index": 5560,
    "from": 1793694958.6025639,
    "to": 1793779198.5031774,
    "compliant": true,
    "duration": 84239.90061354637
  },
  {
    "index": 5559,
    "from": 1793694898.465248,
    "to": 1793694958.6025639,
    "compliant": true,
    "duration": 60.13731575012207
  },
  {
    "index": 5558,
    "from": 1793694838.4975502,
    "to": 1793694898.465248,
    "compliant": true,
    "duration": 59.967697858810425
  },
  {
    "index": 5557,
    "from": 1793607478.605342,
    "to": 1793694838.4975502,
    "compliant": true,
    "duration": 87359.89220833778
  },
  {
    "index": 5556,
    "from": 1793607418.5140078,
    "to": 1793607478.605342,
    "compliant": true,
    "duration": 60.091334104537964
  },
  {
    "index": 5555,
    "from": 1793607358.3453608,
    "to": 1793607418.5140078,
    "compliant": true,
    "duration": 60.168647050857544
  },
  {
    "index": 5554,
    "from": 1793607298.668322,
    "to": 1793607358.3453608,
    "compliant": true,
    "duration": 59.67703866958618
  },
  {
    "index": 5553,
    "from": 1793520538.4372106,
    "to": 1793607298.668322,
    "compliant": true,
    "duration": 86760.23111152649
  },
  {
    "index": 5552,
    "from": 1793520478.6044567,
    "to": 1793520538.4372106,
    "compliant": true,
    "duration": 59.83275389671326
  },
  {
    "index": 5551,
    "from": 1793520418.4927204,
    "to": 1793520478.6044567,
    "compliant": true,
    "duration": 60.11173629760742
  },
  {
    "index": 5550,
    "from": 1793520358.5846376,
    "to": 1793520418.4927204,
    "compliant": true,
    "duration": 59.908082723617554
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

