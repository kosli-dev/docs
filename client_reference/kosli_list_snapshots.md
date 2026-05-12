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
    "index": 4426,
    "from": 1778595958.7141137,
    "to": 0.0,
    "compliant": true,
    "duration": 3979.911393880844
  },
  {
    "index": 4425,
    "from": 1778592118.418746,
    "to": 1778595958.7141137,
    "compliant": true,
    "duration": 3840.295367717743
  },
  {
    "index": 4424,
    "from": 1778576398.7774363,
    "to": 1778592118.418746,
    "compliant": true,
    "duration": 15719.64130973816
  },
  {
    "index": 4423,
    "from": 1778576338.5502408,
    "to": 1778576398.7774363,
    "compliant": true,
    "duration": 60.227195501327515
  },
  {
    "index": 4422,
    "from": 1778576278.4894078,
    "to": 1778576338.5502408,
    "compliant": true,
    "duration": 60.06083297729492
  },
  {
    "index": 4421,
    "from": 1778571118.4238982,
    "to": 1778576278.4894078,
    "compliant": true,
    "duration": 5160.065509557724
  },
  {
    "index": 4420,
    "from": 1778571058.4603016,
    "to": 1778571118.4238982,
    "compliant": true,
    "duration": 59.96359658241272
  },
  {
    "index": 4419,
    "from": 1778565238.3916535,
    "to": 1778571058.4603016,
    "compliant": true,
    "duration": 5820.068648099899
  },
  {
    "index": 4418,
    "from": 1778565178.5140111,
    "to": 1778565238.3916535,
    "compliant": true,
    "duration": 59.87764239311218
  },
  {
    "index": 4417,
    "from": 1778564878.5484455,
    "to": 1778565178.5140111,
    "compliant": true,
    "duration": 299.9655656814575
  },
  {
    "index": 4416,
    "from": 1778564818.512333,
    "to": 1778564878.5484455,
    "compliant": true,
    "duration": 60.036112546920776
  },
  {
    "index": 4415,
    "from": 1778563138.549312,
    "to": 1778564818.512333,
    "compliant": true,
    "duration": 1679.9630208015442
  },
  {
    "index": 4414,
    "from": 1778563078.4776177,
    "to": 1778563138.549312,
    "compliant": true,
    "duration": 60.07169437408447
  },
  {
    "index": 4413,
    "from": 1778563018.531188,
    "to": 1778563078.4776177,
    "compliant": true,
    "duration": 59.94642972946167
  },
  {
    "index": 4412,
    "from": 1778560378.5140462,
    "to": 1778563018.531188,
    "compliant": true,
    "duration": 2640.0171418190002
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

