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
    "index": 4652,
    "from": 1779947878.3978415,
    "to": 0.0,
    "compliant": true,
    "duration": 9532.48123884201
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
  },
  {
    "index": 4646,
    "from": 1779861658.485706,
    "to": 1779861718.5674713,
    "compliant": true,
    "duration": 60.08176517486572
  },
  {
    "index": 4645,
    "from": 1779861598.5274787,
    "to": 1779861658.485706,
    "compliant": true,
    "duration": 59.95822739601135
  },
  {
    "index": 4644,
    "from": 1779861538.6855698,
    "to": 1779861598.5274787,
    "compliant": true,
    "duration": 59.84190893173218
  },
  {
    "index": 4643,
    "from": 1779809158.6004539,
    "to": 1779861538.6855698,
    "compliant": true,
    "duration": 52380.08511590958
  },
  {
    "index": 4642,
    "from": 1779809098.5394728,
    "to": 1779809158.6004539,
    "compliant": true,
    "duration": 60.060981035232544
  },
  {
    "index": 4641,
    "from": 1779774718.560482,
    "to": 1779809098.5394728,
    "compliant": true,
    "duration": 34379.97899079323
  },
  {
    "index": 4640,
    "from": 1779774658.5274692,
    "to": 1779774718.560482,
    "compliant": true,
    "duration": 60.03301286697388
  },
  {
    "index": 4639,
    "from": 1779774598.5856533,
    "to": 1779774658.5274692,
    "compliant": true,
    "duration": 59.9418158531189
  },
  {
    "index": 4638,
    "from": 1779774538.5244129,
    "to": 1779774598.5856533,
    "compliant": true,
    "duration": 60.061240434646606
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

