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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
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
    "index": 5171,
    "from": 1785755158.5525944,
    "to": 0.0,
    "compliant": true,
    "duration": 19198.675785064697
  },
  {
    "index": 5170,
    "from": 1785755098.5952232,
    "to": 1785755158.5525944,
    "compliant": true,
    "duration": 59.9573712348938
  },
  {
    "index": 5169,
    "from": 1785744358.5353608,
    "to": 1785755098.5952232,
    "compliant": true,
    "duration": 10740.05986237526
  },
  {
    "index": 5168,
    "from": 1785744298.6376145,
    "to": 1785744358.5353608,
    "compliant": true,
    "duration": 59.897746324539185
  },
  {
    "index": 5167,
    "from": 1785736378.4882667,
    "to": 1785744298.6376145,
    "compliant": true,
    "duration": 7920.149347782135
  },
  {
    "index": 5166,
    "from": 1785734098.6068468,
    "to": 1785736378.4882667,
    "compliant": true,
    "duration": 2279.8814198970795
  },
  {
    "index": 5165,
    "from": 1785733978.6575258,
    "to": 1785734098.6068468,
    "compliant": true,
    "duration": 119.94932103157043
  },
  {
    "index": 5164,
    "from": 1785733858.4808197,
    "to": 1785733978.6575258,
    "compliant": true,
    "duration": 120.17670607566833
  },
  {
    "index": 5163,
    "from": 1785681958.5195231,
    "to": 1785733858.4808197,
    "compliant": true,
    "duration": 51899.96129655838
  },
  {
    "index": 5162,
    "from": 1785665578.7000751,
    "to": 1785681958.5195231,
    "compliant": true,
    "duration": 16379.819447994232
  },
  {
    "index": 5161,
    "from": 1785665518.499598,
    "to": 1785665578.7000751,
    "compliant": true,
    "duration": 60.2004771232605
  },
  {
    "index": 5160,
    "from": 1785665098.541603,
    "to": 1785665518.499598,
    "compliant": true,
    "duration": 419.95799493789673
  },
  {
    "index": 5159,
    "from": 1785665038.518144,
    "to": 1785665098.541603,
    "compliant": true,
    "duration": 60.0234591960907
  },
  {
    "index": 5158,
    "from": 1785659158.4421992,
    "to": 1785665038.518144,
    "compliant": true,
    "duration": 5880.075944662094
  },
  {
    "index": 5157,
    "from": 1785659098.5386167,
    "to": 1785659158.4421992,
    "compliant": true,
    "duration": 59.90358257293701
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

