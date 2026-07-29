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
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for snapshots  |
|    `-i`, `--interval` string  |  [optional] Expression to define specified snapshots range.  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--reverse`  |  [optional] Reverse the order of output list.  |


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
    "index": 5134,
    "from": 1785310558.4611607,
    "to": 0.0,
    "compliant": true,
    "duration": 13650.749610424042
  },
  {
    "index": 5133,
    "from": 1785305338.459451,
    "to": 1785310558.4611607,
    "compliant": true,
    "duration": 5220.001709699631
  },
  {
    "index": 5132,
    "from": 1785301138.4848077,
    "to": 1785305338.459451,
    "compliant": true,
    "duration": 4199.974643230438
  },
  {
    "index": 5131,
    "from": 1785301078.6254478,
    "to": 1785301138.4848077,
    "compliant": true,
    "duration": 59.85935997962952
  },
  {
    "index": 5130,
    "from": 1785301018.7636228,
    "to": 1785301078.6254478,
    "compliant": true,
    "duration": 59.86182498931885
  },
  {
    "index": 5129,
    "from": 1785300958.5618691,
    "to": 1785301018.7636228,
    "compliant": true,
    "duration": 60.20175361633301
  },
  {
    "index": 5128,
    "from": 1785300898.3949952,
    "to": 1785300958.5618691,
    "compliant": true,
    "duration": 60.166873931884766
  },
  {
    "index": 5127,
    "from": 1785300838.4479997,
    "to": 1785300898.3949952,
    "compliant": true,
    "duration": 59.94699549674988
  },
  {
    "index": 5126,
    "from": 1785243478.598589,
    "to": 1785300838.4479997,
    "compliant": true,
    "duration": 57359.84941077232
  },
  {
    "index": 5125,
    "from": 1785243418.5364106,
    "to": 1785243478.598589,
    "compliant": true,
    "duration": 60.06217837333679
  },
  {
    "index": 5124,
    "from": 1785241678.414592,
    "to": 1785243418.5364106,
    "compliant": true,
    "duration": 1740.1218185424805
  },
  {
    "index": 5123,
    "from": 1785241618.6033545,
    "to": 1785241678.414592,
    "compliant": true,
    "duration": 59.81123757362366
  },
  {
    "index": 5122,
    "from": 1785241318.4716694,
    "to": 1785241618.6033545,
    "compliant": true,
    "duration": 300.13168501853943
  },
  {
    "index": 5121,
    "from": 1785241258.6193466,
    "to": 1785241318.4716694,
    "compliant": true,
    "duration": 59.852322816848755
  },
  {
    "index": 5120,
    "from": 1785240718.5257201,
    "to": 1785241258.6193466,
    "compliant": true,
    "duration": 540.093626499176
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

