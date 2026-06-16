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
    "index": 4781,
    "from": 1781596438.4966626,
    "to": 0.0,
    "compliant": true,
    "duration": 7872.4069356918335
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
  },
  {
    "index": 4774,
    "from": 1781593978.426208,
    "to": 1781595178.5604763,
    "compliant": true,
    "duration": 1200.134268283844
  },
  {
    "index": 4773,
    "from": 1781593799.0334685,
    "to": 1781593978.426208,
    "compliant": true,
    "duration": 179.39273953437805
  },
  {
    "index": 4772,
    "from": 1781593738.5721767,
    "to": 1781593799.0334685,
    "compliant": true,
    "duration": 60.461291790008545
  },
  {
    "index": 4771,
    "from": 1781592238.465858,
    "to": 1781593738.5721767,
    "compliant": true,
    "duration": 1500.1063187122345
  },
  {
    "index": 4770,
    "from": 1781592178.6246305,
    "to": 1781592238.465858,
    "compliant": true,
    "duration": 59.841227531433105
  },
  {
    "index": 4769,
    "from": 1781590498.431212,
    "to": 1781592178.6246305,
    "compliant": true,
    "duration": 1680.1934185028076
  },
  {
    "index": 4768,
    "from": 1781590138.5979598,
    "to": 1781590498.431212,
    "compliant": false,
    "duration": 359.8332521915436
  },
  {
    "index": 4767,
    "from": 1781535898.6708055,
    "to": 1781590138.5979598,
    "compliant": true,
    "duration": 54239.9271543026
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

