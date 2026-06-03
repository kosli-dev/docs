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
    "index": 4686,
    "from": 1780474738.6666076,
    "to": 0.0,
    "compliant": true,
    "duration": 4251.654977321625
  },
  {
    "index": 4685,
    "from": 1780474618.597512,
    "to": 1780474738.6666076,
    "compliant": true,
    "duration": 120.06909561157227
  },
  {
    "index": 4684,
    "from": 1780468558.77772,
    "to": 1780474618.597512,
    "compliant": true,
    "duration": 6059.819792032242
  },
  {
    "index": 4683,
    "from": 1780468498.4508533,
    "to": 1780468558.77772,
    "compliant": true,
    "duration": 60.3268666267395
  },
  {
    "index": 4682,
    "from": 1780468438.5424237,
    "to": 1780468498.4508533,
    "compliant": true,
    "duration": 59.90842962265015
  },
  {
    "index": 4681,
    "from": 1780468378.4966059,
    "to": 1780468438.5424237,
    "compliant": true,
    "duration": 60.045817852020264
  },
  {
    "index": 4680,
    "from": 1780389718.4421296,
    "to": 1780468378.4966059,
    "compliant": true,
    "duration": 78660.05447626114
  },
  {
    "index": 4679,
    "from": 1780389658.9039307,
    "to": 1780389718.4421296,
    "compliant": true,
    "duration": 59.538198947906494
  },
  {
    "index": 4678,
    "from": 1780381498.6433115,
    "to": 1780389658.9039307,
    "compliant": true,
    "duration": 8160.260619163513
  },
  {
    "index": 4677,
    "from": 1780381378.7255073,
    "to": 1780381498.6433115,
    "compliant": true,
    "duration": 119.91780424118042
  },
  {
    "index": 4676,
    "from": 1780381318.3665276,
    "to": 1780381378.7255073,
    "compliant": true,
    "duration": 60.35897970199585
  },
  {
    "index": 4675,
    "from": 1780381258.5755224,
    "to": 1780381318.3665276,
    "compliant": true,
    "duration": 59.79100513458252
  },
  {
    "index": 4674,
    "from": 1780381198.4530046,
    "to": 1780381258.5755224,
    "compliant": true,
    "duration": 60.122517824172974
  },
  {
    "index": 4673,
    "from": 1780333378.8471313,
    "to": 1780381198.4530046,
    "compliant": true,
    "duration": 47819.60587334633
  },
  {
    "index": 4672,
    "from": 1780333318.8874087,
    "to": 1780333378.8471313,
    "compliant": true,
    "duration": 59.9597225189209
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

