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
|        --http-proxy http://proxy-server-ip:proxy-port  |  [optional] The HTTP proxy URL including protocol and port number. e.g. http://proxy-server-ip:proxy-port  |
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
    "index": 4366,
    "from": 1778128438.445219,
    "to": 0.0,
    "compliant": true,
    "duration": 21556.08734035492
  },
  {
    "index": 4365,
    "from": 1778128378.4063118,
    "to": 1778128438.445219,
    "compliant": true,
    "duration": 60.038907289505005
  },
  {
    "index": 4364,
    "from": 1778128318.5241542,
    "to": 1778128378.4063118,
    "compliant": true,
    "duration": 59.88215756416321
  },
  {
    "index": 4363,
    "from": 1778081218.4564807,
    "to": 1778128318.5241542,
    "compliant": true,
    "duration": 47100.06767344475
  },
  {
    "index": 4362,
    "from": 1778081158.4271605,
    "to": 1778081218.4564807,
    "compliant": true,
    "duration": 60.02932024002075
  },
  {
    "index": 4361,
    "from": 1778041978.4476647,
    "to": 1778081158.4271605,
    "compliant": true,
    "duration": 39179.97949576378
  },
  {
    "index": 4360,
    "from": 1778041918.62214,
    "to": 1778041978.4476647,
    "compliant": true,
    "duration": 59.82552480697632
  },
  {
    "index": 4359,
    "from": 1778041858.507459,
    "to": 1778041918.62214,
    "compliant": true,
    "duration": 60.114681005477905
  },
  {
    "index": 4358,
    "from": 1777997458.5117762,
    "to": 1778041858.507459,
    "compliant": true,
    "duration": 44399.99568271637
  },
  {
    "index": 4357,
    "from": 1777956838.5302956,
    "to": 1777997458.5117762,
    "compliant": true,
    "duration": 40619.98148059845
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

