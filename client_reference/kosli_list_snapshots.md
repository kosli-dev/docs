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
    "index": 5234,
    "from": 1786679818.4046729,
    "to": 0.0,
    "compliant": true,
    "duration": 40244.23185634613
  },
  {
    "index": 5233,
    "from": 1786679758.5206547,
    "to": 1786679818.4046729,
    "compliant": true,
    "duration": 59.88401818275452
  },
  {
    "index": 5232,
    "from": 1786679638.3800714,
    "to": 1786679758.5206547,
    "compliant": true,
    "duration": 120.14058327674866
  },
  {
    "index": 5231,
    "from": 1786679578.5574222,
    "to": 1786679638.3800714,
    "compliant": true,
    "duration": 59.822649240493774
  },
  {
    "index": 5230,
    "from": 1786679518.6214967,
    "to": 1786679578.5574222,
    "compliant": true,
    "duration": 59.93592548370361
  },
  {
    "index": 5229,
    "from": 1786598698.4780145,
    "to": 1786679518.6214967,
    "compliant": true,
    "duration": 80820.14348220825
  },
  {
    "index": 5228,
    "from": 1786593538.460407,
    "to": 1786598698.4780145,
    "compliant": true,
    "duration": 5160.017607450485
  },
  {
    "index": 5227,
    "from": 1786593418.452673,
    "to": 1786593538.460407,
    "compliant": true,
    "duration": 120.00773406028748
  },
  {
    "index": 5226,
    "from": 1786593358.5152867,
    "to": 1786593418.452673,
    "compliant": true,
    "duration": 59.93738627433777
  },
  {
    "index": 5225,
    "from": 1786593298.400066,
    "to": 1786593358.5152867,
    "compliant": true,
    "duration": 60.11522078514099
  },
  {
    "index": 5224,
    "from": 1786506718.3598936,
    "to": 1786593298.400066,
    "compliant": true,
    "duration": 86580.04017233849
  },
  {
    "index": 5223,
    "from": 1786506358.497881,
    "to": 1786506718.3598936,
    "compliant": true,
    "duration": 359.8620126247406
  },
  {
    "index": 5222,
    "from": 1786506298.5599546,
    "to": 1786506358.497881,
    "compliant": true,
    "duration": 59.937926292419434
  },
  {
    "index": 5221,
    "from": 1786506238.507325,
    "to": 1786506298.5599546,
    "compliant": true,
    "duration": 60.052629709243774
  },
  {
    "index": 5220,
    "from": 1786425598.492372,
    "to": 1786506238.507325,
    "compliant": true,
    "duration": 80640.01495289803
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

