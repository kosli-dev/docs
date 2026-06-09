---
title: "kosli list snapshots"
beta: false
deprecated: false
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
|        `--reverse`  |  [defaulted] Reverse the order of output list.  |


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
    "index": 4744,
    "from": 1780984438.437869,
    "to": 0.0,
    "compliant": true,
    "duration": 18761.68947839737
  },
  {
    "index": 4743,
    "from": 1780984378.7307086,
    "to": 1780984438.437869,
    "compliant": true,
    "duration": 59.70716047286987
  },
  {
    "index": 4742,
    "from": 1780984318.462322,
    "to": 1780984378.7307086,
    "compliant": true,
    "duration": 60.26838660240173
  },
  {
    "index": 4741,
    "from": 1780934518.864066,
    "to": 1780984318.462322,
    "compliant": true,
    "duration": 49799.598256111145
  },
  {
    "index": 4740,
    "from": 1780934458.6713858,
    "to": 1780934518.864066,
    "compliant": true,
    "duration": 60.19268012046814
  },
  {
    "index": 4739,
    "from": 1780934398.9164453,
    "to": 1780934458.6713858,
    "compliant": true,
    "duration": 59.75494050979614
  },
  {
    "index": 4738,
    "from": 1780933918.5023239,
    "to": 1780934398.9164453,
    "compliant": true,
    "duration": 480.41412138938904
  },
  {
    "index": 4737,
    "from": 1780899838.5880492,
    "to": 1780933918.5023239,
    "compliant": true,
    "duration": 34079.914274692535
  },
  {
    "index": 4736,
    "from": 1780898638.4568684,
    "to": 1780899838.5880492,
    "compliant": true,
    "duration": 1200.1311807632446
  },
  {
    "index": 4735,
    "from": 1780898578.8734438,
    "to": 1780898638.4568684,
    "compliant": true,
    "duration": 59.58342456817627
  },
  {
    "index": 4734,
    "from": 1780816198.878704,
    "to": 1780898578.8734438,
    "compliant": true,
    "duration": 82379.99473977089
  },
  {
    "index": 4733,
    "from": 1780815898.5218282,
    "to": 1780816198.878704,
    "compliant": true,
    "duration": 300.35687589645386
  },
  {
    "index": 4732,
    "from": 1780815838.3792646,
    "to": 1780815898.5218282,
    "compliant": true,
    "duration": 60.142563581466675
  },
  {
    "index": 4731,
    "from": 1780815778.6067216,
    "to": 1780815838.3792646,
    "compliant": true,
    "duration": 59.77254295349121
  },
  {
    "index": 4730,
    "from": 1780812598.5177445,
    "to": 1780815778.6067216,
    "compliant": true,
    "duration": 3180.088977098465
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

