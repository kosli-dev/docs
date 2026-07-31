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
    "index": 5143,
    "from": 1785488758.445761,
    "to": 0.0,
    "compliant": true,
    "duration": 7183.661288738251
  },
  {
    "index": 5142,
    "from": 1785488698.5792832,
    "to": 1785488758.445761,
    "compliant": true,
    "duration": 59.866477727890015
  },
  {
    "index": 5141,
    "from": 1785474718.4306936,
    "to": 1785488698.5792832,
    "compliant": true,
    "duration": 13980.148589611053
  },
  {
    "index": 5140,
    "from": 1785474598.4708273,
    "to": 1785474718.4306936,
    "compliant": true,
    "duration": 119.9598662853241
  },
  {
    "index": 5139,
    "from": 1785474478.4712877,
    "to": 1785474598.4708273,
    "compliant": true,
    "duration": 119.99953961372375
  },
  {
    "index": 5138,
    "from": 1785386758.6525679,
    "to": 1785474478.4712877,
    "compliant": true,
    "duration": 87719.81871986389
  },
  {
    "index": 5137,
    "from": 1785386638.4935195,
    "to": 1785386758.6525679,
    "compliant": true,
    "duration": 120.15904831886292
  },
  {
    "index": 5136,
    "from": 1785386578.4141178,
    "to": 1785386638.4935195,
    "compliant": true,
    "duration": 60.07940173149109
  },
  {
    "index": 5135,
    "from": 1785386518.396874,
    "to": 1785386578.4141178,
    "compliant": true,
    "duration": 60.0172438621521
  },
  {
    "index": 5134,
    "from": 1785310558.4611607,
    "to": 1785386518.396874,
    "compliant": true,
    "duration": 75959.93571329117
  },
  {
    "index": 5133,
    "from": 1785305338.459451,
    "to": 1785310558.4611607,
    "compliant": true,
    "duration": 5220.001709699631
  },
  {
    "index": 5132,
    "from": 1785301138.4848077,
    "to": 1785305338.459451,
    "compliant": true,
    "duration": 4199.974643230438
  },
  {
    "index": 5131,
    "from": 1785301078.6254478,
    "to": 1785301138.4848077,
    "compliant": true,
    "duration": 59.85935997962952
  },
  {
    "index": 5130,
    "from": 1785301018.7636228,
    "to": 1785301078.6254478,
    "compliant": true,
    "duration": 59.86182498931885
  },
  {
    "index": 5129,
    "from": 1785300958.5618691,
    "to": 1785301018.7636228,
    "compliant": true,
    "duration": 60.20175361633301
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

