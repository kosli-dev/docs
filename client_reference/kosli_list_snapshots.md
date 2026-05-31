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
|        `--reverse`  |  [defaulted] Reverse the order of output list.  |


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
    "index": 4661,
    "from": 1780207378.4202626,
    "to": 0.0,
    "compliant": true,
    "duration": 13720.706392765045
  },
  {
    "index": 4660,
    "from": 1780207258.5312698,
    "to": 1780207378.4202626,
    "compliant": true,
    "duration": 119.88899278640747
  },
  {
    "index": 4659,
    "from": 1780207198.4493356,
    "to": 1780207258.5312698,
    "compliant": true,
    "duration": 60.081934213638306
  },
  {
    "index": 4658,
    "from": 1780119298.405238,
    "to": 1780207198.4493356,
    "compliant": true,
    "duration": 87900.04409766197
  },
  {
    "index": 4657,
    "from": 1780119238.8050067,
    "to": 1780119298.405238,
    "compliant": true,
    "duration": 59.6002311706543
  },
  {
    "index": 4656,
    "from": 1780119178.446403,
    "to": 1780119238.8050067,
    "compliant": true,
    "duration": 60.358603715896606
  },
  {
    "index": 4655,
    "from": 1780034338.6278179,
    "to": 1780119178.446403,
    "compliant": true,
    "duration": 84839.8185851574
  },
  {
    "index": 4654,
    "from": 1780034218.4264112,
    "to": 1780034338.6278179,
    "compliant": true,
    "duration": 120.20140671730042
  },
  {
    "index": 4653,
    "from": 1780034158.6275804,
    "to": 1780034218.4264112,
    "compliant": true,
    "duration": 59.79883074760437
  },
  {
    "index": 4652,
    "from": 1779947878.3978415,
    "to": 1780034158.6275804,
    "compliant": true,
    "duration": 86280.22973895073
  },
  {
    "index": 4651,
    "from": 1779947818.5869424,
    "to": 1779947878.3978415,
    "compliant": true,
    "duration": 59.81089901924133
  },
  {
    "index": 4650,
    "from": 1779947758.4962103,
    "to": 1779947818.5869424,
    "compliant": true,
    "duration": 60.09073209762573
  },
  {
    "index": 4649,
    "from": 1779947698.6234314,
    "to": 1779947758.4962103,
    "compliant": true,
    "duration": 59.87277889251709
  },
  {
    "index": 4648,
    "from": 1779861778.5774584,
    "to": 1779947698.6234314,
    "compliant": true,
    "duration": 85920.04597306252
  },
  {
    "index": 4647,
    "from": 1779861718.5674713,
    "to": 1779861778.5774584,
    "compliant": true,
    "duration": 60.009987115859985
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

