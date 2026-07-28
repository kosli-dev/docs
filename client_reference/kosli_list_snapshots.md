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
    "index": 5126,
    "from": 1785243478.598589,
    "to": 0.0,
    "compliant": true,
    "duration": 13834.632454156876
  },
  {
    "index": 5125,
    "from": 1785243418.5364106,
    "to": 1785243478.598589,
    "compliant": true,
    "duration": 60.06217837333679
  },
  {
    "index": 5124,
    "from": 1785241678.414592,
    "to": 1785243418.5364106,
    "compliant": true,
    "duration": 1740.1218185424805
  },
  {
    "index": 5123,
    "from": 1785241618.6033545,
    "to": 1785241678.414592,
    "compliant": true,
    "duration": 59.81123757362366
  },
  {
    "index": 5122,
    "from": 1785241318.4716694,
    "to": 1785241618.6033545,
    "compliant": true,
    "duration": 300.13168501853943
  },
  {
    "index": 5121,
    "from": 1785241258.6193466,
    "to": 1785241318.4716694,
    "compliant": true,
    "duration": 59.852322816848755
  },
  {
    "index": 5120,
    "from": 1785240718.5257201,
    "to": 1785241258.6193466,
    "compliant": true,
    "duration": 540.093626499176
  },
  {
    "index": 5119,
    "from": 1785240658.6597328,
    "to": 1785240718.5257201,
    "compliant": true,
    "duration": 59.8659873008728
  },
  {
    "index": 5118,
    "from": 1785236638.5786521,
    "to": 1785240658.6597328,
    "compliant": true,
    "duration": 4020.081080675125
  },
  {
    "index": 5117,
    "from": 1785236578.4785342,
    "to": 1785236638.5786521,
    "compliant": true,
    "duration": 60.100117921829224
  },
  {
    "index": 5116,
    "from": 1785224878.4373872,
    "to": 1785236578.4785342,
    "compliant": true,
    "duration": 11700.041146993637
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

