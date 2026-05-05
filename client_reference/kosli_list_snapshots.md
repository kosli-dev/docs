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
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. 'http://proxy-server-ip:proxy-port'  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


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
    "index": 4357,
    "from": 1777956838.5302956,
    "to": 0.0,
    "compliant": true,
    "duration": 26497.173085689545
  },
  {
    "index": 4356,
    "from": 1777954558.5092592,
    "to": 1777956838.5302956,
    "compliant": true,
    "duration": 2280.02103638649
  },
  {
    "index": 4355,
    "from": 1777954498.4239645,
    "to": 1777954558.5092592,
    "compliant": true,
    "duration": 60.08529472351074
  },
  {
    "index": 4354,
    "from": 1777954438.5998223,
    "to": 1777954498.4239645,
    "compliant": true,
    "duration": 59.82414221763611
  },
  {
    "index": 4353,
    "from": 1777869538.5253296,
    "to": 1777954438.5998223,
    "compliant": true,
    "duration": 84900.07449269295
  },
  {
    "index": 4352,
    "from": 1777869478.5084555,
    "to": 1777869538.5253296,
    "compliant": true,
    "duration": 60.01687407493591
  },
  {
    "index": 4351,
    "from": 1777842958.6060224,
    "to": 1777869478.5084555,
    "compliant": true,
    "duration": 26519.902433156967
  },
  {
    "index": 4350,
    "from": 1777783138.5161338,
    "to": 1777842958.6060224,
    "compliant": true,
    "duration": 59820.08988857269
  },
  {
    "index": 4349,
    "from": 1777783085.6064026,
    "to": 1777783138.5161338,
    "compliant": true,
    "duration": 52.90973114967346
  },
  {
    "index": 4348,
    "from": 1777783018.5123496,
    "to": 1777783085.6064026,
    "compliant": true,
    "duration": 67.09405303001404
  },
  {
    "index": 4347,
    "from": 1777695478.6151357,
    "to": 1777783018.5123496,
    "compliant": true,
    "duration": 87539.89721393585
  },
  {
    "index": 4346,
    "from": 1777695418.5493166,
    "to": 1777695478.6151357,
    "compliant": true,
    "duration": 60.06581902503967
  },
  {
    "index": 4345,
    "from": 1777695358.5312326,
    "to": 1777695418.5493166,
    "compliant": true,
    "duration": 60.01808404922485
  },
  {
    "index": 4344,
    "from": 1777644058.4073718,
    "to": 1777695358.5312326,
    "compliant": true,
    "duration": 51300.12386083603
  },
  {
    "index": 4343,
    "from": 1777643998.3954618,
    "to": 1777644058.4073718,
    "compliant": true,
    "duration": 60.01190996170044
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

