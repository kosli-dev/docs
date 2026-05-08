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
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
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
    "index": 4386,
    "from": 1778225998.5296352,
    "to": 0.0,
    "compliant": true,
    "duration": 16900.322019815445
  },
  {
    "index": 4385,
    "from": 1778225938.458091,
    "to": 1778225998.5296352,
    "compliant": true,
    "duration": 60.07154417037964
  },
  {
    "index": 4384,
    "from": 1778223958.5125732,
    "to": 1778225938.458091,
    "compliant": true,
    "duration": 1979.9455177783966
  },
  {
    "index": 4383,
    "from": 1778223898.548935,
    "to": 1778223958.5125732,
    "compliant": true,
    "duration": 59.96363830566406
  },
  {
    "index": 4382,
    "from": 1778213818.5191746,
    "to": 1778223898.548935,
    "compliant": true,
    "duration": 10080.029760360718
  },
  {
    "index": 4381,
    "from": 1778213758.4011989,
    "to": 1778213818.5191746,
    "compliant": true,
    "duration": 60.11797571182251
  },
  {
    "index": 4380,
    "from": 1778178538.4365702,
    "to": 1778213758.4011989,
    "compliant": true,
    "duration": 35219.96462869644
  },
  {
    "index": 4379,
    "from": 1778158918.5020123,
    "to": 1778178538.4365702,
    "compliant": true,
    "duration": 19619.934557914734
  },
  {
    "index": 4378,
    "from": 1778158858.590836,
    "to": 1778158918.5020123,
    "compliant": true,
    "duration": 59.9111762046814
  },
  {
    "index": 4377,
    "from": 1778157598.4368508,
    "to": 1778158858.590836,
    "compliant": true,
    "duration": 1260.1539852619171
  },
  {
    "index": 4376,
    "from": 1778157538.6015975,
    "to": 1778157598.4368508,
    "compliant": true,
    "duration": 59.83525323867798
  },
  {
    "index": 4375,
    "from": 1778157478.5209992,
    "to": 1778157538.6015975,
    "compliant": true,
    "duration": 60.0805983543396
  },
  {
    "index": 4374,
    "from": 1778157118.5120325,
    "to": 1778157478.5209992,
    "compliant": true,
    "duration": 360.00896668434143
  },
  {
    "index": 4373,
    "from": 1778157058.6630018,
    "to": 1778157118.5120325,
    "compliant": true,
    "duration": 59.84903073310852
  },
  {
    "index": 4372,
    "from": 1778156278.425921,
    "to": 1778157058.6630018,
    "compliant": true,
    "duration": 780.2370808124542
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

