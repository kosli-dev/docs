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
    "index": 5007,
    "from": 1784014258.5595071,
    "to": 0.0,
    "compliant": true,
    "duration": 30843.68912911415
  },
  {
    "index": 5006,
    "from": 1784014198.37591,
    "to": 1784014258.5595071,
    "compliant": true,
    "duration": 60.18359708786011
  },
  {
    "index": 5005,
    "from": 1784003998.4861574,
    "to": 1784014198.37591,
    "compliant": true,
    "duration": 10199.889752626419
  },
  {
    "index": 5004,
    "from": 1784003938.5445926,
    "to": 1784003998.4861574,
    "compliant": true,
    "duration": 59.9415647983551
  },
  {
    "index": 5003,
    "from": 1784003878.547647,
    "to": 1784003938.5445926,
    "compliant": true,
    "duration": 59.99694561958313
  },
  {
    "index": 5002,
    "from": 1784003818.431919,
    "to": 1784003878.547647,
    "compliant": true,
    "duration": 60.11572790145874
  },
  {
    "index": 5001,
    "from": 1784003758.5531633,
    "to": 1784003818.431919,
    "compliant": true,
    "duration": 59.87875580787659
  },
  {
    "index": 5000,
    "from": 1783919458.6314104,
    "to": 1784003758.5531633,
    "compliant": true,
    "duration": 84299.92175292969
  },
  {
    "index": 4999,
    "from": 1783919398.441605,
    "to": 1783919458.6314104,
    "compliant": true,
    "duration": 60.18980526924133
  },
  {
    "index": 4998,
    "from": 1783919338.4484332,
    "to": 1783919398.441605,
    "compliant": true,
    "duration": 59.99317193031311
  },
  {
    "index": 4997,
    "from": 1783919278.5154655,
    "to": 1783919338.4484332,
    "compliant": true,
    "duration": 59.93296766281128
  },
  {
    "index": 4996,
    "from": 1783853098.455609,
    "to": 1783919278.5154655,
    "compliant": true,
    "duration": 66180.0598564148
  },
  {
    "index": 4995,
    "from": 1783853038.6230137,
    "to": 1783853098.455609,
    "compliant": true,
    "duration": 59.832595348358154
  },
  {
    "index": 4994,
    "from": 1783851298.54696,
    "to": 1783853038.6230137,
    "compliant": true,
    "duration": 1740.0760536193848
  },
  {
    "index": 4993,
    "from": 1783851178.4482923,
    "to": 1783851298.54696,
    "compliant": true,
    "duration": 120.09866786003113
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

