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
    "index": 5597,
    "from": 1794818218.491466,
    "to": 0.0,
    "compliant": true,
    "duration": 8440.950122833252
  },
  {
    "index": 5596,
    "from": 1794818158.4816425,
    "to": 1794818218.491466,
    "compliant": true,
    "duration": 60.00982356071472
  },
  {
    "index": 5595,
    "from": 1794731278.5234597,
    "to": 1794818158.4816425,
    "compliant": true,
    "duration": 86879.95818281174
  },
  {
    "index": 5594,
    "from": 1794645958.4260314,
    "to": 1794731278.5234597,
    "compliant": true,
    "duration": 85320.09742832184
  },
  {
    "index": 5593,
    "from": 1794643438.396102,
    "to": 1794645958.4260314,
    "compliant": true,
    "duration": 2520.0299293994904
  },
  {
    "index": 5592,
    "from": 1794643378.4765232,
    "to": 1794643438.396102,
    "compliant": true,
    "duration": 59.91957879066467
  },
  {
    "index": 5591,
    "from": 1794643318.3213007,
    "to": 1794643378.4765232,
    "compliant": true,
    "duration": 60.15522241592407
  },
  {
    "index": 5590,
    "from": 1794559618.3613522,
    "to": 1794643318.3213007,
    "compliant": true,
    "duration": 83699.95994853973
  },
  {
    "index": 5589,
    "from": 1794559558.5302055,
    "to": 1794559618.3613522,
    "compliant": true,
    "duration": 59.83114671707153
  },
  {
    "index": 5588,
    "from": 1794385498.3975194,
    "to": 1794559558.5302055,
    "compliant": true,
    "duration": 174060.13268613815
  },
  {
    "index": 5587,
    "from": 1794385438.6523466,
    "to": 1794385498.3975194,
    "compliant": true,
    "duration": 59.74517273902893
  },
  {
    "index": 5586,
    "from": 1794385378.5887642,
    "to": 1794385438.6523466,
    "compliant": true,
    "duration": 60.06358242034912
  },
  {
    "index": 5585,
    "from": 1794385318.4644277,
    "to": 1794385378.5887642,
    "compliant": true,
    "duration": 60.12433648109436
  },
  {
    "index": 5584,
    "from": 1794300778.5744529,
    "to": 1794385318.4644277,
    "compliant": true,
    "duration": 84539.88997483253
  },
  {
    "index": 5583,
    "from": 1794300718.4335883,
    "to": 1794300778.5744529,
    "compliant": true,
    "duration": 60.140864610672
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

