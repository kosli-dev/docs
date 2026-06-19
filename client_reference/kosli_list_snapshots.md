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
    "index": 4798,
    "from": 1781862838.595731,
    "to": 0.0,
    "compliant": true,
    "duration": 32996.261266708374
  },
  {
    "index": 4797,
    "from": 1781862778.4942248,
    "to": 1781862838.595731,
    "compliant": true,
    "duration": 60.10150623321533
  },
  {
    "index": 4796,
    "from": 1781862658.6275043,
    "to": 1781862778.4942248,
    "compliant": true,
    "duration": 119.86672043800354
  },
  {
    "index": 4795,
    "from": 1781862598.434665,
    "to": 1781862658.6275043,
    "compliant": true,
    "duration": 60.19283938407898
  },
  {
    "index": 4794,
    "from": 1781862538.6870024,
    "to": 1781862598.434665,
    "compliant": true,
    "duration": 59.74766254425049
  },
  {
    "index": 4793,
    "from": 1781862478.568137,
    "to": 1781862538.6870024,
    "compliant": true,
    "duration": 60.11886548995972
  },
  {
    "index": 4792,
    "from": 1781852278.67235,
    "to": 1781862478.568137,
    "compliant": true,
    "duration": 10199.895787000656
  },
  {
    "index": 4791,
    "from": 1781852218.5682158,
    "to": 1781852278.67235,
    "compliant": true,
    "duration": 60.10413408279419
  },
  {
    "index": 4790,
    "from": 1781851978.4982789,
    "to": 1781852218.5682158,
    "compliant": true,
    "duration": 240.06993699073792
  },
  {
    "index": 4789,
    "from": 1781764378.5891397,
    "to": 1781851978.4982789,
    "compliant": true,
    "duration": 87599.90913915634
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

