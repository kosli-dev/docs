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
    "index": 4833,
    "from": 1782295018.5650613,
    "to": 0.0,
    "compliant": true,
    "duration": 1365.5056719779968
  },
  {
    "index": 4832,
    "from": 1782294958.7636094,
    "to": 1782295018.5650613,
    "compliant": true,
    "duration": 59.80145192146301
  },
  {
    "index": 4831,
    "from": 1782294898.7202442,
    "to": 1782294958.7636094,
    "compliant": false,
    "duration": 60.043365240097046
  },
  {
    "index": 4830,
    "from": 1782294418.6282794,
    "to": 1782294898.7202442,
    "compliant": true,
    "duration": 480.0919647216797
  },
  {
    "index": 4829,
    "from": 1782294298.6604407,
    "to": 1782294418.6282794,
    "compliant": true,
    "duration": 119.96783876419067
  },
  {
    "index": 4828,
    "from": 1782291479.0961432,
    "to": 1782294298.6604407,
    "compliant": true,
    "duration": 2819.564297437668
  },
  {
    "index": 4827,
    "from": 1782291418.655632,
    "to": 1782291479.0961432,
    "compliant": false,
    "duration": 60.44051122665405
  },
  {
    "index": 4826,
    "from": 1782291238.4836733,
    "to": 1782291418.655632,
    "compliant": false,
    "duration": 180.17195868492126
  },
  {
    "index": 4825,
    "from": 1782291178.7075284,
    "to": 1782291238.4836733,
    "compliant": false,
    "duration": 59.77614498138428
  },
  {
    "index": 4824,
    "from": 1782291118.6018608,
    "to": 1782291178.7075284,
    "compliant": false,
    "duration": 60.10566759109497
  },
  {
    "index": 4823,
    "from": 1782291058.5449996,
    "to": 1782291118.6018608,
    "compliant": false,
    "duration": 60.05686116218567
  },
  {
    "index": 4822,
    "from": 1782290520.7159784,
    "to": 1782291058.5449996,
    "compliant": false,
    "duration": 537.8290212154388
  },
  {
    "index": 4821,
    "from": 1782289737.7305799,
    "to": 1782290520.7159784,
    "compliant": true,
    "duration": 782.9853985309601
  },
  {
    "index": 4820,
    "from": 1782280318.4011729,
    "to": 1782289737.7305799,
    "compliant": true,
    "duration": 9419.3294069767
  },
  {
    "index": 4819,
    "from": 1782280258.6287673,
    "to": 1782280318.4011729,
    "compliant": true,
    "duration": 59.77240562438965
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

