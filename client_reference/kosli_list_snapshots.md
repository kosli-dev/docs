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
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshots |
| `-i`, `--interval` | string | [optional] Expression to define specified snapshots range. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--reverse` | bool | [optional] Reverse the order of output list. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


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
    "index": 5401,
    "from": 1790581078.5249808,
    "to": 0.0,
    "compliant": true,
    "duration": 27063.261297941208
  },
  {
    "index": 5400,
    "from": 1790580898.5000987,
    "to": 1790581078.5249808,
    "compliant": true,
    "duration": 180.02488207817078
  },
  {
    "index": 5399,
    "from": 1790492818.399003,
    "to": 1790580898.5000987,
    "compliant": true,
    "duration": 88080.10109567642
  },
  {
    "index": 5398,
    "from": 1790492758.6070654,
    "to": 1790492818.399003,
    "compliant": true,
    "duration": 59.791937589645386
  },
  {
    "index": 5397,
    "from": 1790419978.581526,
    "to": 1790492758.6070654,
    "compliant": true,
    "duration": 72780.0255393982
  },
  {
    "index": 5396,
    "from": 1790419918.5861778,
    "to": 1790419978.581526,
    "compliant": true,
    "duration": 59.99534821510315
  },
  {
    "index": 5395,
    "from": 1790419858.4481485,
    "to": 1790419918.5861778,
    "compliant": true,
    "duration": 60.13802933692932
  },
  {
    "index": 5394,
    "from": 1790419618.489072,
    "to": 1790419858.4481485,
    "compliant": true,
    "duration": 239.95907640457153
  },
  {
    "index": 5393,
    "from": 1790419558.382832,
    "to": 1790419618.489072,
    "compliant": true,
    "duration": 60.106240034103394
  },
  {
    "index": 5392,
    "from": 1790416738.4799883,
    "to": 1790419558.382832,
    "compliant": true,
    "duration": 2819.9028437137604
  },
  {
    "index": 5391,
    "from": 1790416618.4809058,
    "to": 1790416738.4799883,
    "compliant": true,
    "duration": 119.99908256530762
  },
  {
    "index": 5390,
    "from": 1790404738.5018032,
    "to": 1790416618.4809058,
    "compliant": true,
    "duration": 11879.979102611542
  },
  {
    "index": 5389,
    "from": 1790404678.482143,
    "to": 1790404738.5018032,
    "compliant": true,
    "duration": 60.019660234451294
  },
  {
    "index": 5388,
    "from": 1790334598.8884814,
    "to": 1790404678.482143,
    "compliant": true,
    "duration": 70079.5936615467
  },
  {
    "index": 5387,
    "from": 1790334538.4884212,
    "to": 1790334598.8884814,
    "compliant": true,
    "duration": 60.400060176849365
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

