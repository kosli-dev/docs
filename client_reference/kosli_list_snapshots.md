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
    "index": 5513,
    "from": 1792737118.3849633,
    "to": 0.0,
    "compliant": true,
    "duration": 10883.02959227562
  },
  {
    "index": 5512,
    "from": 1792737058.6320403,
    "to": 1792737118.3849633,
    "compliant": true,
    "duration": 59.752923011779785
  },
  {
    "index": 5511,
    "from": 1792651018.4846509,
    "to": 1792737058.6320403,
    "compliant": true,
    "duration": 86040.14738941193
  },
  {
    "index": 5510,
    "from": 1792650958.4733,
    "to": 1792651018.4846509,
    "compliant": true,
    "duration": 60.011350870132446
  },
  {
    "index": 5509,
    "from": 1792569838.5199676,
    "to": 1792650958.4733,
    "compliant": true,
    "duration": 81119.95333242416
  },
  {
    "index": 5508,
    "from": 1792564498.3512611,
    "to": 1792569838.5199676,
    "compliant": true,
    "duration": 5340.168706417084
  },
  {
    "index": 5507,
    "from": 1792564438.5642035,
    "to": 1792564498.3512611,
    "compliant": true,
    "duration": 59.787057638168335
  },
  {
    "index": 5506,
    "from": 1792493818.5519311,
    "to": 1792564438.5642035,
    "compliant": true,
    "duration": 70620.01227235794
  },
  {
    "index": 5505,
    "from": 1792493758.3103483,
    "to": 1792493818.5519311,
    "compliant": true,
    "duration": 60.2415828704834
  },
  {
    "index": 5504,
    "from": 1792493458.279001,
    "to": 1792493758.3103483,
    "compliant": true,
    "duration": 300.0313472747803
  },
  {
    "index": 5503,
    "from": 1792493398.504113,
    "to": 1792493458.279001,
    "compliant": true,
    "duration": 59.774888038635254
  },
  {
    "index": 5502,
    "from": 1792486738.3284767,
    "to": 1792493398.504113,
    "compliant": true,
    "duration": 6660.175636291504
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

