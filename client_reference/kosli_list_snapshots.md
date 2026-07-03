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
    "index": 4945,
    "from": 1783079338.7114732,
    "to": 0.0,
    "compliant": true,
    "duration": 21013.273769378662
  },
  {
    "index": 4944,
    "from": 1783075918.6314435,
    "to": 1783079338.7114732,
    "compliant": true,
    "duration": 3420.0800297260284
  },
  {
    "index": 4943,
    "from": 1783075678.7158587,
    "to": 1783075918.6314435,
    "compliant": true,
    "duration": 239.91558480262756
  },
  {
    "index": 4942,
    "from": 1783075618.6971846,
    "to": 1783075678.7158587,
    "compliant": true,
    "duration": 60.01867413520813
  },
  {
    "index": 4941,
    "from": 1783075558.551832,
    "to": 1783075618.6971846,
    "compliant": true,
    "duration": 60.145352602005005
  },
  {
    "index": 4940,
    "from": 1783063918.6405253,
    "to": 1783075558.551832,
    "compliant": true,
    "duration": 11639.911306619644
  },
  {
    "index": 4939,
    "from": 1783057378.5601928,
    "to": 1783063918.6405253,
    "compliant": true,
    "duration": 6540.080332517624
  },
  {
    "index": 4938,
    "from": 1783057318.3987007,
    "to": 1783057378.5601928,
    "compliant": true,
    "duration": 60.161492109298706
  },
  {
    "index": 4937,
    "from": 1783057258.5624893,
    "to": 1783057318.3987007,
    "compliant": true,
    "duration": 59.83621144294739
  },
  {
    "index": 4936,
    "from": 1783057198.5704908,
    "to": 1783057258.5624893,
    "compliant": true,
    "duration": 59.99199843406677
  },
  {
    "index": 4935,
    "from": 1783056958.493694,
    "to": 1783057198.5704908,
    "compliant": true,
    "duration": 240.07679677009583
  },
  {
    "index": 4934,
    "from": 1782983098.518337,
    "to": 1783056958.493694,
    "compliant": true,
    "duration": 73859.97535705566
  },
  {
    "index": 4933,
    "from": 1782983038.7445812,
    "to": 1782983098.518337,
    "compliant": true,
    "duration": 59.7737557888031
  },
  {
    "index": 4932,
    "from": 1782973678.4485867,
    "to": 1782983038.7445812,
    "compliant": true,
    "duration": 9360.295994520187
  },
  {
    "index": 4931,
    "from": 1782973618.6021194,
    "to": 1782973678.4485867,
    "compliant": true,
    "duration": 59.84646725654602
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

