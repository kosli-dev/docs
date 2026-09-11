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
    "index": 5352,
    "from": 1789108858.5535865,
    "to": 0.0,
    "compliant": true,
    "duration": 30143.66504883766
  },
  {
    "index": 5351,
    "from": 1789108798.4511206,
    "to": 1789108858.5535865,
    "compliant": true,
    "duration": 60.102465867996216
  },
  {
    "index": 5350,
    "from": 1789023418.5988352,
    "to": 1789108798.4511206,
    "compliant": true,
    "duration": 85379.85228538513
  },
  {
    "index": 5349,
    "from": 1789023358.6002493,
    "to": 1789023418.5988352,
    "compliant": true,
    "duration": 59.99858593940735
  },
  {
    "index": 5348,
    "from": 1789022878.756657,
    "to": 1789023358.6002493,
    "compliant": true,
    "duration": 479.8435924053192
  },
  {
    "index": 5347,
    "from": 1789022818.5234735,
    "to": 1789022878.756657,
    "compliant": true,
    "duration": 60.23318338394165
  },
  {
    "index": 5346,
    "from": 1789022458.3400946,
    "to": 1789022818.5234735,
    "compliant": false,
    "duration": 360.18337893486023
  },
  {
    "index": 5345,
    "from": 1789022398.786734,
    "to": 1789022458.3400946,
    "compliant": true,
    "duration": 59.55336046218872
  },
  {
    "index": 5344,
    "from": 1788964738.4864616,
    "to": 1789022398.786734,
    "compliant": true,
    "duration": 57660.30027246475
  },
  {
    "index": 5343,
    "from": 1788957658.4472558,
    "to": 1788964738.4864616,
    "compliant": true,
    "duration": 7080.039205789566
  },
  {
    "index": 5342,
    "from": 1788945958.5053656,
    "to": 1788957658.4472558,
    "compliant": true,
    "duration": 11699.941890239716
  },
  {
    "index": 5341,
    "from": 1788945898.464788,
    "to": 1788945958.5053656,
    "compliant": true,
    "duration": 60.04057765007019
  },
  {
    "index": 5340,
    "from": 1788936118.496684,
    "to": 1788945898.464788,
    "compliant": true,
    "duration": 9779.96810388565
  },
  {
    "index": 5339,
    "from": 1788935998.397991,
    "to": 1788936118.496684,
    "compliant": true,
    "duration": 120.09869313240051
  },
  {
    "index": 5338,
    "from": 1788867598.4601083,
    "to": 1788935998.397991,
    "compliant": true,
    "duration": 68399.93788266182
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

