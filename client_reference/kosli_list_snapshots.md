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
    "index": 4522,
    "from": 1778779378.493324,
    "to": 0.0,
    "compliant": true,
    "duration": 442.7411513328552
  },
  {
    "index": 4521,
    "from": 1778779318.7576406,
    "to": 1778779378.493324,
    "compliant": true,
    "duration": 59.73568344116211
  },
  {
    "index": 4520,
    "from": 1778779018.4878175,
    "to": 1778779318.7576406,
    "compliant": true,
    "duration": 300.2698230743408
  },
  {
    "index": 4519,
    "from": 1778778958.525458,
    "to": 1778779018.4878175,
    "compliant": true,
    "duration": 59.96235942840576
  },
  {
    "index": 4518,
    "from": 1778778478.4860399,
    "to": 1778778958.525458,
    "compliant": true,
    "duration": 480.03941822052
  },
  {
    "index": 4517,
    "from": 1778778418.643466,
    "to": 1778778478.4860399,
    "compliant": true,
    "duration": 59.84257388114929
  },
  {
    "index": 4516,
    "from": 1778778178.642939,
    "to": 1778778418.643466,
    "compliant": true,
    "duration": 240.00052690505981
  },
  {
    "index": 4515,
    "from": 1778778118.5197313,
    "to": 1778778178.642939,
    "compliant": true,
    "duration": 60.123207807540894
  },
  {
    "index": 4514,
    "from": 1778777878.4407866,
    "to": 1778778118.5197313,
    "compliant": true,
    "duration": 240.07894468307495
  },
  {
    "index": 4513,
    "from": 1778777818.44366,
    "to": 1778777878.4407866,
    "compliant": true,
    "duration": 59.99712657928467
  },
  {
    "index": 4512,
    "from": 1778777338.4247878,
    "to": 1778777818.44366,
    "compliant": true,
    "duration": 480.01887226104736
  },
  {
    "index": 4511,
    "from": 1778777278.5717375,
    "to": 1778777338.4247878,
    "compliant": true,
    "duration": 59.853050231933594
  },
  {
    "index": 4510,
    "from": 1778776738.3930256,
    "to": 1778777278.5717375,
    "compliant": true,
    "duration": 540.1787118911743
  },
  {
    "index": 4509,
    "from": 1778776678.696267,
    "to": 1778776738.3930256,
    "compliant": true,
    "duration": 59.69675874710083
  },
  {
    "index": 4508,
    "from": 1778776438.7363236,
    "to": 1778776678.696267,
    "compliant": true,
    "duration": 239.95994329452515
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

