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
    "index": 5582,
    "from": 1794213778.5473795,
    "to": 0.0,
    "compliant": true,
    "duration": 37842.050629377365
  },
  {
    "index": 5581,
    "from": 1794213718.4508975,
    "to": 1794213778.5473795,
    "compliant": true,
    "duration": 60.096482038497925
  },
  {
    "index": 5580,
    "from": 1794213658.394714,
    "to": 1794213718.4508975,
    "compliant": true,
    "duration": 60.05618333816528
  },
  {
    "index": 5579,
    "from": 1794125038.5439694,
    "to": 1794213658.394714,
    "compliant": true,
    "duration": 88619.85074472427
  },
  {
    "index": 5578,
    "from": 1794124798.5460305,
    "to": 1794125038.5439694,
    "compliant": true,
    "duration": 239.99793887138367
  },
  {
    "index": 5577,
    "from": 1794124738.387191,
    "to": 1794124798.5460305,
    "compliant": true,
    "duration": 60.15883946418762
  },
  {
    "index": 5576,
    "from": 1794124678.505433,
    "to": 1794124738.387191,
    "compliant": true,
    "duration": 59.881757974624634
  },
  {
    "index": 5575,
    "from": 1794043978.4395454,
    "to": 1794124678.505433,
    "compliant": true,
    "duration": 80700.06588768959
  },
  {
    "index": 5574,
    "from": 1794043918.5908046,
    "to": 1794043978.4395454,
    "compliant": true,
    "duration": 59.84874081611633
  },
  {
    "index": 5573,
    "from": 1794037738.502973,
    "to": 1794043918.5908046,
    "compliant": true,
    "duration": 6180.087831497192
  },
  {
    "index": 5572,
    "from": 1794037678.4261587,
    "to": 1794037738.502973,
    "compliant": true,
    "duration": 60.07681441307068
  },
  {
    "index": 5571,
    "from": 1793953918.4942262,
    "to": 1794037678.4261587,
    "compliant": true,
    "duration": 83759.93193244934
  },
  {
    "index": 5570,
    "from": 1793953858.4407423,
    "to": 1793953918.4942262,
    "compliant": true,
    "duration": 60.053483963012695
  },
  {
    "index": 5569,
    "from": 1793867518.4103153,
    "to": 1793953858.4407423,
    "compliant": true,
    "duration": 86340.03042697906
  },
  {
    "index": 5568,
    "from": 1793867458.551026,
    "to": 1793867518.4103153,
    "compliant": true,
    "duration": 59.85928916931152
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

