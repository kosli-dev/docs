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
    "index": 4932,
    "from": 1782973678.4485867,
    "to": 0.0,
    "compliant": true,
    "duration": 8665.949182748795
  },
  {
    "index": 4931,
    "from": 1782973618.6021194,
    "to": 1782973678.4485867,
    "compliant": true,
    "duration": 59.84646725654602
  },
  {
    "index": 4930,
    "from": 1782971758.5585485,
    "to": 1782973618.6021194,
    "compliant": true,
    "duration": 1860.0435709953308
  },
  {
    "index": 4929,
    "from": 1782971518.9605753,
    "to": 1782971758.5585485,
    "compliant": true,
    "duration": 239.59797310829163
  },
  {
    "index": 4928,
    "from": 1782971458.530566,
    "to": 1782971518.9605753,
    "compliant": true,
    "duration": 60.43000936508179
  },
  {
    "index": 4927,
    "from": 1782971338.646279,
    "to": 1782971458.530566,
    "compliant": true,
    "duration": 119.88428688049316
  },
  {
    "index": 4926,
    "from": 1782971159.2597198,
    "to": 1782971338.646279,
    "compliant": true,
    "duration": 179.38655924797058
  },
  {
    "index": 4925,
    "from": 1782971107.9348025,
    "to": 1782971159.2597198,
    "compliant": true,
    "duration": 51.32491731643677
  },
  {
    "index": 4924,
    "from": 1782970978.561424,
    "to": 1782971107.9348025,
    "compliant": true,
    "duration": 129.37337851524353
  },
  {
    "index": 4923,
    "from": 1782970918.4267673,
    "to": 1782970978.561424,
    "compliant": true,
    "duration": 60.13465666770935
  },
  {
    "index": 4922,
    "from": 1782969778.638631,
    "to": 1782970918.4267673,
    "compliant": true,
    "duration": 1139.7881362438202
  },
  {
    "index": 4921,
    "from": 1782969718.5513308,
    "to": 1782969778.638631,
    "compliant": true,
    "duration": 60.087300300598145
  },
  {
    "index": 4920,
    "from": 1782966898.4576402,
    "to": 1782969718.5513308,
    "compliant": true,
    "duration": 2820.093690633774
  },
  {
    "index": 4919,
    "from": 1782966838.4397078,
    "to": 1782966898.4576402,
    "compliant": true,
    "duration": 60.017932415008545
  },
  {
    "index": 4918,
    "from": 1782966238.4659219,
    "to": 1782966838.4397078,
    "compliant": true,
    "duration": 599.9737858772278
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

