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
    "index": 5588,
    "from": 1794385498.3975194,
    "to": 0.0,
    "compliant": true,
    "duration": 32666.80686354637
  },
  {
    "index": 5587,
    "from": 1794385438.6523466,
    "to": 1794385498.3975194,
    "compliant": true,
    "duration": 59.74517273902893
  },
  {
    "index": 5586,
    "from": 1794385378.5887642,
    "to": 1794385438.6523466,
    "compliant": true,
    "duration": 60.06358242034912
  },
  {
    "index": 5585,
    "from": 1794385318.4644277,
    "to": 1794385378.5887642,
    "compliant": true,
    "duration": 60.12433648109436
  },
  {
    "index": 5584,
    "from": 1794300778.5744529,
    "to": 1794385318.4644277,
    "compliant": true,
    "duration": 84539.88997483253
  },
  {
    "index": 5583,
    "from": 1794300718.4335883,
    "to": 1794300778.5744529,
    "compliant": true,
    "duration": 60.140864610672
  },
  {
    "index": 5582,
    "from": 1794213778.5473795,
    "to": 1794300718.4335883,
    "compliant": true,
    "duration": 86939.88620877266
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

