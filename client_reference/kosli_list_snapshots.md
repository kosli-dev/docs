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
    "index": 5611,
    "from": 1794992818.4600863,
    "to": 0.0,
    "compliant": true,
    "duration": 83397.24960541725
  },
  {
    "index": 5610,
    "from": 1794992758.6266255,
    "to": 1794992818.4600863,
    "compliant": true,
    "duration": 59.83346080780029
  },
  {
    "index": 5609,
    "from": 1794992698.5444195,
    "to": 1794992758.6266255,
    "compliant": true,
    "duration": 60.08220601081848
  },
  {
    "index": 5608,
    "from": 1794992638.4076312,
    "to": 1794992698.5444195,
    "compliant": true,
    "duration": 60.1367883682251
  },
  {
    "index": 5607,
    "from": 1794908818.402605,
    "to": 1794992638.4076312,
    "compliant": true,
    "duration": 83820.00502610207
  },
  {
    "index": 5606,
    "from": 1794908758.5395436,
    "to": 1794908818.402605,
    "compliant": true,
    "duration": 59.86306142807007
  },
  {
    "index": 5605,
    "from": 1794908698.3588533,
    "to": 1794908758.5395436,
    "compliant": true,
    "duration": 60.1806902885437
  },
  {
    "index": 5604,
    "from": 1794908638.4735532,
    "to": 1794908698.3588533,
    "compliant": true,
    "duration": 59.885300159454346
  },
  {
    "index": 5603,
    "from": 1794908578.3854952,
    "to": 1794908638.4735532,
    "compliant": true,
    "duration": 60.08805799484253
  },
  {
    "index": 5602,
    "from": 1794908518.5095682,
    "to": 1794908578.3854952,
    "compliant": true,
    "duration": 59.87592697143555
  },
  {
    "index": 5601,
    "from": 1794908458.4642582,
    "to": 1794908518.5095682,
    "compliant": true,
    "duration": 60.04531002044678
  },
  {
    "index": 5600,
    "from": 1794908338.6199315,
    "to": 1794908458.4642582,
    "compliant": true,
    "duration": 119.84432673454285
  },
  {
    "index": 5599,
    "from": 1794908278.5685644,
    "to": 1794908338.6199315,
    "compliant": true,
    "duration": 60.05136704444885
  },
  {
    "index": 5598,
    "from": 1794908218.4002056,
    "to": 1794908278.5685644,
    "compliant": true,
    "duration": 60.16835880279541
  },
  {
    "index": 5597,
    "from": 1794818218.491466,
    "to": 1794908218.4002056,
    "compliant": true,
    "duration": 89999.9087395668
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

