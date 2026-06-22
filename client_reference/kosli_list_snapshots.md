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
    "index": 4814,
    "from": 1782112078.6734855,
    "to": 0.0,
    "compliant": true,
    "duration": 13318.868420124054
  },
  {
    "index": 4813,
    "from": 1782112018.5396478,
    "to": 1782112078.6734855,
    "compliant": true,
    "duration": 60.13383769989014
  },
  {
    "index": 4812,
    "from": 1782111958.6034238,
    "to": 1782112018.5396478,
    "compliant": true,
    "duration": 59.93622398376465
  },
  {
    "index": 4811,
    "from": 1782111898.6284199,
    "to": 1782111958.6034238,
    "compliant": true,
    "duration": 59.97500395774841
  },
  {
    "index": 4810,
    "from": 1782044818.6092193,
    "to": 1782111898.6284199,
    "compliant": true,
    "duration": 67080.01920056343
  },
  {
    "index": 4809,
    "from": 1782044398.7556682,
    "to": 1782044818.6092193,
    "compliant": true,
    "duration": 419.8535511493683
  },
  {
    "index": 4808,
    "from": 1782044338.5470552,
    "to": 1782044398.7556682,
    "compliant": true,
    "duration": 60.20861291885376
  },
  {
    "index": 4807,
    "from": 1782023758.6546373,
    "to": 1782044338.5470552,
    "compliant": true,
    "duration": 20579.892417907715
  },
  {
    "index": 4806,
    "from": 1782023698.5212252,
    "to": 1782023758.6546373,
    "compliant": true,
    "duration": 60.13341212272644
  },
  {
    "index": 4805,
    "from": 1782023638.8251116,
    "to": 1782023698.5212252,
    "compliant": true,
    "duration": 59.69611358642578
  },
  {
    "index": 4804,
    "from": 1782023578.4854655,
    "to": 1782023638.8251116,
    "compliant": true,
    "duration": 60.339646100997925
  },
  {
    "index": 4803,
    "from": 1781935498.6820252,
    "to": 1782023578.4854655,
    "compliant": true,
    "duration": 88079.80344033241
  },
  {
    "index": 4802,
    "from": 1781935438.6180487,
    "to": 1781935498.6820252,
    "compliant": true,
    "duration": 60.063976526260376
  },
  {
    "index": 4801,
    "from": 1781935378.4333878,
    "to": 1781935438.6180487,
    "compliant": true,
    "duration": 60.18466091156006
  },
  {
    "index": 4800,
    "from": 1781935318.586741,
    "to": 1781935378.4333878,
    "compliant": true,
    "duration": 59.846646785736084
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

