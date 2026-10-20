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
    "index": 5502,
    "from": 1792486738.3284767,
    "to": 0.0,
    "compliant": true,
    "duration": 6121.206284284592
  },
  {
    "index": 5501,
    "from": 1792486678.5622876,
    "to": 1792486738.3284767,
    "compliant": true,
    "duration": 59.766189098358154
  },
  {
    "index": 5500,
    "from": 1792486438.5668814,
    "to": 1792486678.5622876,
    "compliant": true,
    "duration": 239.99540615081787
  },
  {
    "index": 5499,
    "from": 1792486378.5379567,
    "to": 1792486438.5668814,
    "compliant": true,
    "duration": 60.02892470359802
  },
  {
    "index": 5498,
    "from": 1792485718.5164247,
    "to": 1792486378.5379567,
    "compliant": true,
    "duration": 660.0215320587158
  },
  {
    "index": 5497,
    "from": 1792484518.653232,
    "to": 1792485718.5164247,
    "compliant": true,
    "duration": 1199.8631925582886
  },
  {
    "index": 5496,
    "from": 1792478158.4201236,
    "to": 1792484518.653232,
    "compliant": true,
    "duration": 6360.233108520508
  },
  {
    "index": 5495,
    "from": 1792478098.5997808,
    "to": 1792478158.4201236,
    "compliant": true,
    "duration": 59.820342779159546
  },
  {
    "index": 5494,
    "from": 1792478038.6036036,
    "to": 1792478098.5997808,
    "compliant": true,
    "duration": 59.996177196502686
  },
  {
    "index": 5493,
    "from": 1792392538.480199,
    "to": 1792478038.6036036,
    "compliant": true,
    "duration": 85500.12340450287
  },
  {
    "index": 5492,
    "from": 1792392478.3824074,
    "to": 1792392538.480199,
    "compliant": true,
    "duration": 60.09779167175293
  },
  {
    "index": 5491,
    "from": 1792392418.3523822,
    "to": 1792392478.3824074,
    "compliant": true,
    "duration": 60.030025243759155
  },
  {
    "index": 5490,
    "from": 1792305358.4213169,
    "to": 1792392418.3523822,
    "compliant": true,
    "duration": 87059.93106532097
  },
  {
    "index": 5489,
    "from": 1792305298.4235237,
    "to": 1792305358.4213169,
    "compliant": true,
    "duration": 59.997793197631836
  },
  {
    "index": 5488,
    "from": 1792217398.689756,
    "to": 1792305298.4235237,
    "compliant": true,
    "duration": 87899.73376774788
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

