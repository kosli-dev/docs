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
|    -h, --help  |  help for snapshots  |
|    -i, --interval string  |  [optional] Expression to define specified snapshots range.  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        --page int  |  [defaulted] The page number of a response. (default 1)  |
|    -n, --page-limit int  |  [defaulted] The number of elements per page. (default 15)  |
|        --reverse  |  [defaulted] Reverse the order of output list.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout.  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |
|    -q, --quiet  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both --quiet and --debug are set, --debug wins.  |


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
    "index": 4404,
    "from": 1778502898.4686973,
    "to": 0.0,
    "compliant": true,
    "duration": 444.1671814918518
  },
  {
    "index": 4403,
    "from": 1778502838.4516687,
    "to": 1778502898.4686973,
    "compliant": true,
    "duration": 60.01702857017517
  },
  {
    "index": 4402,
    "from": 1778502598.3867438,
    "to": 1778502838.4516687,
    "compliant": true,
    "duration": 240.06492495536804
  },
  {
    "index": 4401,
    "from": 1778502538.6356485,
    "to": 1778502598.3867438,
    "compliant": true,
    "duration": 59.75109529495239
  },
  {
    "index": 4400,
    "from": 1778501398.7131987,
    "to": 1778502538.6356485,
    "compliant": true,
    "duration": 1139.9224498271942
  },
  {
    "index": 4399,
    "from": 1778501338.7537856,
    "to": 1778501398.7131987,
    "compliant": true,
    "duration": 59.959413051605225
  },
  {
    "index": 4398,
    "from": 1778475478.487778,
    "to": 1778501338.7537856,
    "compliant": true,
    "duration": 25860.26600766182
  },
  {
    "index": 4397,
    "from": 1778475418.4505246,
    "to": 1778475478.487778,
    "compliant": true,
    "duration": 60.03725337982178
  },
  {
    "index": 4396,
    "from": 1778388178.6246667,
    "to": 1778475418.4505246,
    "compliant": true,
    "duration": 87239.82585787773
  },
  {
    "index": 4395,
    "from": 1778388118.4850988,
    "to": 1778388178.6246667,
    "compliant": true,
    "duration": 60.139567852020264
  },
  {
    "index": 4394,
    "from": 1778300518.4226332,
    "to": 1778388118.4850988,
    "compliant": true,
    "duration": 87600.06246566772
  },
  {
    "index": 4393,
    "from": 1778300458.706285,
    "to": 1778300518.4226332,
    "compliant": true,
    "duration": 59.71634817123413
  },
  {
    "index": 4392,
    "from": 1778245978.41778,
    "to": 1778300458.706285,
    "compliant": true,
    "duration": 54480.28850507736
  },
  {
    "index": 4391,
    "from": 1778245918.504205,
    "to": 1778245978.41778,
    "compliant": true,
    "duration": 59.91357493400574
  },
  {
    "index": 4390,
    "from": 1778245618.5221512,
    "to": 1778245918.504205,
    "compliant": true,
    "duration": 299.98205375671387
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

