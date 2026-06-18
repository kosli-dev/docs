---
title: "kosli list snapshots"
beta: false
deprecated: false
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
    "index": 4789,
    "from": 1781764378.5891397,
    "to": 0.0,
    "compliant": true,
    "duration": 38157.75528383255
  },
  {
    "index": 4788,
    "from": 1781764318.4655225,
    "to": 1781764378.5891397,
    "compliant": true,
    "duration": 60.12361717224121
  },
  {
    "index": 4787,
    "from": 1781764198.6089904,
    "to": 1781764318.4655225,
    "compliant": true,
    "duration": 119.8565320968628
  },
  {
    "index": 4786,
    "from": 1781764138.425254,
    "to": 1781764198.6089904,
    "compliant": true,
    "duration": 60.1837363243103
  },
  {
    "index": 4785,
    "from": 1781764018.5686495,
    "to": 1781764138.425254,
    "compliant": true,
    "duration": 119.85660457611084
  },
  {
    "index": 4784,
    "from": 1781679118.686044,
    "to": 1781764018.5686495,
    "compliant": true,
    "duration": 84899.88260555267
  },
  {
    "index": 4783,
    "from": 1781678878.4909782,
    "to": 1781679118.686044,
    "compliant": true,
    "duration": 240.19506573677063
  },
  {
    "index": 4782,
    "from": 1781678698.538556,
    "to": 1781678878.4909782,
    "compliant": true,
    "duration": 179.9524221420288
  },
  {
    "index": 4781,
    "from": 1781596438.4966626,
    "to": 1781678698.538556,
    "compliant": true,
    "duration": 82260.04189348221
  },
  {
    "index": 4780,
    "from": 1781596378.6927845,
    "to": 1781596438.4966626,
    "compliant": true,
    "duration": 59.80387806892395
  },
  {
    "index": 4779,
    "from": 1781596318.7251499,
    "to": 1781596378.6927845,
    "compliant": true,
    "duration": 59.96763467788696
  },
  {
    "index": 4778,
    "from": 1781596198.6164858,
    "to": 1781596318.7251499,
    "compliant": true,
    "duration": 120.10866403579712
  },
  {
    "index": 4777,
    "from": 1781596138.474564,
    "to": 1781596198.6164858,
    "compliant": true,
    "duration": 60.14192175865173
  },
  {
    "index": 4776,
    "from": 1781596078.5283337,
    "to": 1781596138.474564,
    "compliant": true,
    "duration": 59.94623041152954
  },
  {
    "index": 4775,
    "from": 1781595178.5604763,
    "to": 1781596078.5283337,
    "compliant": true,
    "duration": 899.9678573608398
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

