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
    "index": 4879,
    "from": 1782714538.5522528,
    "to": 0.0,
    "compliant": true,
    "duration": 34849.14031481743
  },
  {
    "index": 4878,
    "from": 1782714478.5875318,
    "to": 1782714538.5522528,
    "compliant": true,
    "duration": 59.96472096443176
  },
  {
    "index": 4877,
    "from": 1782714418.585481,
    "to": 1782714478.5875318,
    "compliant": true,
    "duration": 60.00205087661743
  },
  {
    "index": 4876,
    "from": 1782714358.666861,
    "to": 1782714418.585481,
    "compliant": true,
    "duration": 59.918619871139526
  },
  {
    "index": 4875,
    "from": 1782714298.56245,
    "to": 1782714358.666861,
    "compliant": true,
    "duration": 60.104411125183105
  },
  {
    "index": 4874,
    "from": 1782714238.7174664,
    "to": 1782714298.56245,
    "compliant": true,
    "duration": 59.84498357772827
  },
  {
    "index": 4873,
    "from": 1782629938.5827231,
    "to": 1782714238.7174664,
    "compliant": true,
    "duration": 84300.13474321365
  },
  {
    "index": 4872,
    "from": 1782629878.6141164,
    "to": 1782629938.5827231,
    "compliant": true,
    "duration": 59.96860671043396
  },
  {
    "index": 4871,
    "from": 1782626638.5474796,
    "to": 1782629878.6141164,
    "compliant": true,
    "duration": 3240.066636800766
  },
  {
    "index": 4870,
    "from": 1782626578.602863,
    "to": 1782626638.5474796,
    "compliant": true,
    "duration": 59.9446165561676
  },
  {
    "index": 4869,
    "from": 1782626518.4787986,
    "to": 1782626578.602863,
    "compliant": true,
    "duration": 60.124064445495605
  },
  {
    "index": 4868,
    "from": 1782626458.3743217,
    "to": 1782626518.4787986,
    "compliant": true,
    "duration": 60.10447692871094
  },
  {
    "index": 4867,
    "from": 1782539098.464014,
    "to": 1782626458.3743217,
    "compliant": true,
    "duration": 87359.9103076458
  },
  {
    "index": 4866,
    "from": 1782538738.5091877,
    "to": 1782539098.464014,
    "compliant": true,
    "duration": 359.95482635498047
  },
  {
    "index": 4865,
    "from": 1782538678.4353418,
    "to": 1782538738.5091877,
    "compliant": true,
    "duration": 60.073845863342285
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

