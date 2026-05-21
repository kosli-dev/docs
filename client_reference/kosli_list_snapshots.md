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
    "index": 4608,
    "from": 1779364918.4839022,
    "to": 0.0,
    "compliant": true,
    "duration": 5331.443897247314
  },
  {
    "index": 4607,
    "from": 1779361978.695172,
    "to": 1779364918.4839022,
    "compliant": true,
    "duration": 2939.7887301445007
  },
  {
    "index": 4606,
    "from": 1779361918.6583393,
    "to": 1779361978.695172,
    "compliant": true,
    "duration": 60.03683280944824
  },
  {
    "index": 4605,
    "from": 1779361678.5192397,
    "to": 1779361918.6583393,
    "compliant": true,
    "duration": 240.1390995979309
  },
  {
    "index": 4604,
    "from": 1779361618.3886578,
    "to": 1779361678.5192397,
    "compliant": true,
    "duration": 60.130581855773926
  },
  {
    "index": 4603,
    "from": 1779361558.694262,
    "to": 1779361618.3886578,
    "compliant": true,
    "duration": 59.694395780563354
  },
  {
    "index": 4602,
    "from": 1779342958.470353,
    "to": 1779361558.694262,
    "compliant": true,
    "duration": 18600.223909139633
  },
  {
    "index": 4601,
    "from": 1779342898.637506,
    "to": 1779342958.470353,
    "compliant": true,
    "duration": 59.832846879959106
  },
  {
    "index": 4600,
    "from": 1779342838.5059407,
    "to": 1779342898.637506,
    "compliant": true,
    "duration": 60.13156533241272
  },
  {
    "index": 4599,
    "from": 1779309418.6612878,
    "to": 1779342838.5059407,
    "compliant": true,
    "duration": 33419.84465289116
  },
  {
    "index": 4598,
    "from": 1779309358.5359507,
    "to": 1779309418.6612878,
    "compliant": true,
    "duration": 60.12533712387085
  },
  {
    "index": 4597,
    "from": 1779273298.835737,
    "to": 1779309358.5359507,
    "compliant": true,
    "duration": 36059.70021367073
  },
  {
    "index": 4596,
    "from": 1779273238.532132,
    "to": 1779273298.835737,
    "compliant": true,
    "duration": 60.30360507965088
  },
  {
    "index": 4595,
    "from": 1779256438.4181411,
    "to": 1779273238.532132,
    "compliant": true,
    "duration": 16800.11399078369
  },
  {
    "index": 4594,
    "from": 1779256378.891493,
    "to": 1779256438.4181411,
    "compliant": true,
    "duration": 59.52664804458618
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

