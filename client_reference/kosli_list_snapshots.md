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
    "index": 5309,
    "from": 1788256325.6192138,
    "to": 0.0,
    "compliant": true,
    "duration": 4114.5881407260895
  },
  {
    "index": 5308,
    "from": 1788256258.609352,
    "to": 1788256325.6192138,
    "compliant": true,
    "duration": 67.00986170768738
  },
  {
    "index": 5307,
    "from": 1788256138.680238,
    "to": 1788256258.609352,
    "compliant": true,
    "duration": 119.92911410331726
  },
  {
    "index": 5306,
    "from": 1788256078.451175,
    "to": 1788256138.680238,
    "compliant": true,
    "duration": 60.22906303405762
  },
  {
    "index": 5305,
    "from": 1788255898.5005004,
    "to": 1788256078.451175,
    "compliant": true,
    "duration": 179.950674533844
  },
  {
    "index": 5304,
    "from": 1788255838.4418423,
    "to": 1788255898.5005004,
    "compliant": true,
    "duration": 60.05865812301636
  },
  {
    "index": 5303,
    "from": 1788255778.7566388,
    "to": 1788255838.4418423,
    "compliant": true,
    "duration": 59.685203552246094
  },
  {
    "index": 5302,
    "from": 1788255478.4228623,
    "to": 1788255778.7566388,
    "compliant": true,
    "duration": 300.333776473999
  },
  {
    "index": 5301,
    "from": 1788255418.2849495,
    "to": 1788255478.4228623,
    "compliant": true,
    "duration": 60.13791275024414
  },
  {
    "index": 5300,
    "from": 1788254758.42325,
    "to": 1788255418.2849495,
    "compliant": true,
    "duration": 659.8616995811462
  },
  {
    "index": 5299,
    "from": 1788253018.4181795,
    "to": 1788254758.42325,
    "compliant": true,
    "duration": 1740.0050704479218
  },
  {
    "index": 5298,
    "from": 1788251398.4699006,
    "to": 1788253018.4181795,
    "compliant": true,
    "duration": 1619.9482789039612
  },
  {
    "index": 5297,
    "from": 1788245458.5681827,
    "to": 1788251398.4699006,
    "compliant": true,
    "duration": 5939.90171790123
  },
  {
    "index": 5296,
    "from": 1788245398.8278637,
    "to": 1788245458.5681827,
    "compliant": true,
    "duration": 59.74031901359558
  },
  {
    "index": 5295,
    "from": 1788245338.6744468,
    "to": 1788245398.8278637,
    "compliant": true,
    "duration": 60.153416872024536
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

