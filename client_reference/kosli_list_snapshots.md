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
    "index": 5116,
    "from": 1785224878.4373872,
    "to": 0.0,
    "compliant": true,
    "duration": 8750.01878452301
  },
  {
    "index": 5115,
    "from": 1785215338.442852,
    "to": 1785224878.4373872,
    "compliant": true,
    "duration": 9539.994535207748
  },
  {
    "index": 5114,
    "from": 1785214438.378998,
    "to": 1785215338.442852,
    "compliant": true,
    "duration": 900.0638539791107
  },
  {
    "index": 5113,
    "from": 1785214378.5198987,
    "to": 1785214438.378998,
    "compliant": true,
    "duration": 59.85909938812256
  },
  {
    "index": 5112,
    "from": 1785214318.4842489,
    "to": 1785214378.5198987,
    "compliant": true,
    "duration": 60.03564977645874
  },
  {
    "index": 5111,
    "from": 1785214258.6438735,
    "to": 1785214318.4842489,
    "compliant": true,
    "duration": 59.8403754234314
  },
  {
    "index": 5110,
    "from": 1785214198.674762,
    "to": 1785214258.6438735,
    "compliant": true,
    "duration": 59.96911144256592
  },
  {
    "index": 5109,
    "from": 1785214139.0560102,
    "to": 1785214198.674762,
    "compliant": true,
    "duration": 59.618751764297485
  },
  {
    "index": 5108,
    "from": 1785165658.472069,
    "to": 1785214139.0560102,
    "compliant": true,
    "duration": 48480.58394122124
  },
  {
    "index": 5107,
    "from": 1785138658.57735,
    "to": 1785165658.472069,
    "compliant": true,
    "duration": 26999.89471912384
  },
  {
    "index": 5106,
    "from": 1785131338.4268208,
    "to": 1785138658.57735,
    "compliant": true,
    "duration": 7320.1505291461945
  },
  {
    "index": 5105,
    "from": 1785131278.4151351,
    "to": 1785131338.4268208,
    "compliant": true,
    "duration": 60.011685609817505
  },
  {
    "index": 5104,
    "from": 1785130438.502333,
    "to": 1785131278.4151351,
    "compliant": true,
    "duration": 839.9128022193909
  },
  {
    "index": 5103,
    "from": 1785130318.4207122,
    "to": 1785130438.502333,
    "compliant": true,
    "duration": 120.08162069320679
  },
  {
    "index": 5102,
    "from": 1785042598.396489,
    "to": 1785130318.4207122,
    "compliant": true,
    "duration": 87720.02422332764
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

