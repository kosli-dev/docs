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
    "index": 5414,
    "from": 1790926378.5148618,
    "to": 0.0,
    "compliant": true,
    "duration": 16086.717691659927
  },
  {
    "index": 5413,
    "from": 1790926318.4624424,
    "to": 1790926378.5148618,
    "compliant": true,
    "duration": 60.05241942405701
  },
  {
    "index": 5412,
    "from": 1790840878.4856288,
    "to": 1790926318.4624424,
    "compliant": true,
    "duration": 85439.97681355476
  },
  {
    "index": 5411,
    "from": 1790840818.3694565,
    "to": 1790840878.4856288,
    "compliant": true,
    "duration": 60.116172313690186
  },
  {
    "index": 5410,
    "from": 1790840758.6974003,
    "to": 1790840818.3694565,
    "compliant": true,
    "duration": 59.67205619812012
  },
  {
    "index": 5409,
    "from": 1790759338.4899325,
    "to": 1790840758.6974003,
    "compliant": true,
    "duration": 81420.20746779442
  },
  {
    "index": 5408,
    "from": 1790759278.5924852,
    "to": 1790759338.4899325,
    "compliant": true,
    "duration": 59.89744734764099
  },
  {
    "index": 5407,
    "from": 1790757958.5971544,
    "to": 1790759278.5924852,
    "compliant": true,
    "duration": 1319.9953308105469
  },
  {
    "index": 5406,
    "from": 1790753098.4294415,
    "to": 1790757958.5971544,
    "compliant": true,
    "duration": 4860.167712926865
  },
  {
    "index": 5405,
    "from": 1790752978.523531,
    "to": 1790753098.4294415,
    "compliant": true,
    "duration": 119.90591049194336
  },
  {
    "index": 5404,
    "from": 1790752918.4068623,
    "to": 1790752978.523531,
    "compliant": true,
    "duration": 60.116668701171875
  },
  {
    "index": 5403,
    "from": 1790667118.4618428,
    "to": 1790752918.4068623,
    "compliant": true,
    "duration": 85799.94501948357
  },
  {
    "index": 5402,
    "from": 1790667058.5996144,
    "to": 1790667118.4618428,
    "compliant": true,
    "duration": 59.86222839355469
  },
  {
    "index": 5401,
    "from": 1790581078.5249808,
    "to": 1790667058.5996144,
    "compliant": true,
    "duration": 85980.07463359833
  },
  {
    "index": 5400,
    "from": 1790580898.5000987,
    "to": 1790581078.5249808,
    "compliant": true,
    "duration": 180.02488207817078
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

