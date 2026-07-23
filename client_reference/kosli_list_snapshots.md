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
    "index": 5069,
    "from": 1784790118.4310617,
    "to": 0.0,
    "compliant": true,
    "duration": 24885.544872045517
  },
  {
    "index": 5068,
    "from": 1784790058.6402347,
    "to": 1784790118.4310617,
    "compliant": true,
    "duration": 59.79082703590393
  },
  {
    "index": 5067,
    "from": 1784782978.3652897,
    "to": 1784790058.6402347,
    "compliant": true,
    "duration": 7080.274945020676
  },
  {
    "index": 5066,
    "from": 1784782798.6282318,
    "to": 1784782978.3652897,
    "compliant": true,
    "duration": 179.73705792427063
  },
  {
    "index": 5065,
    "from": 1784696218.587319,
    "to": 1784782798.6282318,
    "compliant": true,
    "duration": 86580.04091286659
  },
  {
    "index": 5064,
    "from": 1784696098.485834,
    "to": 1784696218.587319,
    "compliant": true,
    "duration": 120.10148501396179
  },
  {
    "index": 5063,
    "from": 1784696038.473212,
    "to": 1784696098.485834,
    "compliant": true,
    "duration": 60.01262187957764
  },
  {
    "index": 5062,
    "from": 1784609878.4986525,
    "to": 1784696038.473212,
    "compliant": true,
    "duration": 86159.97455954552
  },
  {
    "index": 5061,
    "from": 1784609758.4742362,
    "to": 1784609878.4986525,
    "compliant": true,
    "duration": 120.02441620826721
  },
  {
    "index": 5060,
    "from": 1784609698.6156423,
    "to": 1784609758.4742362,
    "compliant": true,
    "duration": 59.85859394073486
  },
  {
    "index": 5059,
    "from": 1784609638.5198727,
    "to": 1784609698.6156423,
    "compliant": true,
    "duration": 60.09576964378357
  },
  {
    "index": 5058,
    "from": 1784525098.4087725,
    "to": 1784609638.5198727,
    "compliant": true,
    "duration": 84540.11110019684
  },
  {
    "index": 5057,
    "from": 1784525038.351176,
    "to": 1784525098.4087725,
    "compliant": true,
    "duration": 60.05759644508362
  },
  {
    "index": 5056,
    "from": 1784524678.5200555,
    "to": 1784525038.351176,
    "compliant": true,
    "duration": 359.83112049102783
  },
  {
    "index": 5055,
    "from": 1784524558.4706209,
    "to": 1784524678.5200555,
    "compliant": true,
    "duration": 120.04943466186523
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

