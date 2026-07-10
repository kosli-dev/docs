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
    "index": 4981,
    "from": 1783662598.552843,
    "to": 0.0,
    "compliant": true,
    "duration": 35057.17760062218
  },
  {
    "index": 4980,
    "from": 1783662478.6077144,
    "to": 1783662598.552843,
    "compliant": true,
    "duration": 119.94512867927551
  },
  {
    "index": 4979,
    "from": 1783662418.4245424,
    "to": 1783662478.6077144,
    "compliant": true,
    "duration": 60.18317198753357
  },
  {
    "index": 4978,
    "from": 1783618558.4237978,
    "to": 1783662418.4245424,
    "compliant": true,
    "duration": 43860.00074458122
  },
  {
    "index": 4977,
    "from": 1783618498.5929904,
    "to": 1783618558.4237978,
    "compliant": true,
    "duration": 59.83080744743347
  },
  {
    "index": 4976,
    "from": 1783618318.5544238,
    "to": 1783618498.5929904,
    "compliant": true,
    "duration": 180.03856658935547
  },
  {
    "index": 4975,
    "from": 1783618258.807386,
    "to": 1783618318.5544238,
    "compliant": true,
    "duration": 59.74703788757324
  },
  {
    "index": 4974,
    "from": 1783618198.4632592,
    "to": 1783618258.807386,
    "compliant": true,
    "duration": 60.34412670135498
  },
  {
    "index": 4973,
    "from": 1783618138.688982,
    "to": 1783618198.4632592,
    "compliant": true,
    "duration": 59.774277210235596
  },
  {
    "index": 4972,
    "from": 1783576438.7264173,
    "to": 1783618138.688982,
    "compliant": true,
    "duration": 41699.9625647068
  },
  {
    "index": 4971,
    "from": 1783576258.5836413,
    "to": 1783576438.7264173,
    "compliant": true,
    "duration": 180.14277601242065
  },
  {
    "index": 4970,
    "from": 1783576198.5023923,
    "to": 1783576258.5836413,
    "compliant": true,
    "duration": 60.08124899864197
  },
  {
    "index": 4969,
    "from": 1783486618.5418699,
    "to": 1783576198.5023923,
    "compliant": true,
    "duration": 89579.96052241325
  },
  {
    "index": 4968,
    "from": 1783486558.4013338,
    "to": 1783486618.5418699,
    "compliant": true,
    "duration": 60.140536069869995
  },
  {
    "index": 4967,
    "from": 1783486498.5434582,
    "to": 1783486558.4013338,
    "compliant": true,
    "duration": 59.85787558555603
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

