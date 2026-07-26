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
    "index": 5102,
    "from": 1785042598.396489,
    "to": 0.0,
    "compliant": true,
    "duration": 53762.95841002464
  },
  {
    "index": 5101,
    "from": 1785042538.4093528,
    "to": 1785042598.396489,
    "compliant": true,
    "duration": 59.987136125564575
  },
  {
    "index": 5100,
    "from": 1785042478.3455539,
    "to": 1785042538.4093528,
    "compliant": true,
    "duration": 60.063798904418945
  },
  {
    "index": 5099,
    "from": 1785042418.5663874,
    "to": 1785042478.3455539,
    "compliant": true,
    "duration": 59.77916646003723
  },
  {
    "index": 5098,
    "from": 1785042358.4207563,
    "to": 1785042418.5663874,
    "compliant": true,
    "duration": 60.145631074905396
  },
  {
    "index": 5097,
    "from": 1784963398.5259354,
    "to": 1785042358.4207563,
    "compliant": true,
    "duration": 78959.89482092857
  },
  {
    "index": 5096,
    "from": 1784963278.4685986,
    "to": 1784963398.5259354,
    "compliant": true,
    "duration": 120.05733680725098
  },
  {
    "index": 5095,
    "from": 1784963218.5628068,
    "to": 1784963278.4685986,
    "compliant": true,
    "duration": 59.90579175949097
  },
  {
    "index": 5094,
    "from": 1784962918.7634475,
    "to": 1784963218.5628068,
    "compliant": true,
    "duration": 299.79935932159424
  },
  {
    "index": 5093,
    "from": 1784962858.582333,
    "to": 1784962918.7634475,
    "compliant": true,
    "duration": 60.18111443519592
  },
  {
    "index": 5092,
    "from": 1784961538.4107828,
    "to": 1784962858.582333,
    "compliant": true,
    "duration": 1320.1715502738953
  },
  {
    "index": 5091,
    "from": 1784955418.416456,
    "to": 1784961538.4107828,
    "compliant": true,
    "duration": 6119.99432682991
  },
  {
    "index": 5090,
    "from": 1784955358.4916215,
    "to": 1784955418.416456,
    "compliant": true,
    "duration": 59.92483448982239
  },
  {
    "index": 5089,
    "from": 1784955298.4261715,
    "to": 1784955358.4916215,
    "compliant": true,
    "duration": 60.065449953079224
  },
  {
    "index": 5088,
    "from": 1784955238.4201362,
    "to": 1784955298.4261715,
    "compliant": true,
    "duration": 60.00603532791138
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

