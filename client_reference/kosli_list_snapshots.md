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
    "index": 4749,
    "from": 1781167678.669744,
    "to": 0.0,
    "compliant": true,
    "duration": 6018.875128746033
  },
  {
    "index": 4748,
    "from": 1781159278.7947195,
    "to": 1781167678.669744,
    "compliant": true,
    "duration": 8399.875024557114
  },
  {
    "index": 4747,
    "from": 1781159218.5704055,
    "to": 1781159278.7947195,
    "compliant": true,
    "duration": 60.22431397438049
  },
  {
    "index": 4746,
    "from": 1781071618.6346955,
    "to": 1781159218.5704055,
    "compliant": true,
    "duration": 87599.93570995331
  },
  {
    "index": 4745,
    "from": 1781071558.3442817,
    "to": 1781071618.6346955,
    "compliant": true,
    "duration": 60.29041385650635
  },
  {
    "index": 4744,
    "from": 1780984438.437869,
    "to": 1781071558.3442817,
    "compliant": true,
    "duration": 87119.90641260147
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

