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
    "index": 5370,
    "from": 1789713538.5480921,
    "to": 0.0,
    "compliant": true,
    "duration": 33619.4899930954
  },
  {
    "index": 5369,
    "from": 1789713418.5020027,
    "to": 1789713538.5480921,
    "compliant": true,
    "duration": 120.04608941078186
  },
  {
    "index": 5368,
    "from": 1789627258.417633,
    "to": 1789713418.5020027,
    "compliant": true,
    "duration": 86160.08436965942
  },
  {
    "index": 5367,
    "from": 1789627198.537616,
    "to": 1789627258.417633,
    "compliant": true,
    "duration": 59.880017042160034
  },
  {
    "index": 5366,
    "from": 1789541038.406661,
    "to": 1789627198.537616,
    "compliant": true,
    "duration": 86160.13095498085
  },
  {
    "index": 5365,
    "from": 1789540978.4072695,
    "to": 1789541038.406661,
    "compliant": true,
    "duration": 59.99939155578613
  },
  {
    "index": 5364,
    "from": 1789540918.5609164,
    "to": 1789540978.4072695,
    "compliant": true,
    "duration": 59.84635305404663
  },
  {
    "index": 5363,
    "from": 1789454518.4863305,
    "to": 1789540918.5609164,
    "compliant": true,
    "duration": 86400.07458591461
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

