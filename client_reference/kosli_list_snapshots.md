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
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshots |
| `-i`, `--interval` | string | [optional] Expression to define specified snapshots range. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--reverse` | bool | [optional] Reverse the order of output list. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## JSON output

With `--output json`, this command prints the response of the [List snapshots](/api-reference/snapshots/list-snapshots) API operation as the server returned it. The shape follows the server's published API spec, not the CLI version.

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
    "index": 5646,
    "from": 1795687438.5866702,
    "to": 0.0,
    "compliant": true,
    "duration": 4906.357538461685
  },
  {
    "index": 5645,
    "from": 1795687378.5496435,
    "to": 1795687438.5866702,
    "compliant": true,
    "duration": 60.03702664375305
  },
  {
    "index": 5644,
    "from": 1795687318.472094,
    "to": 1795687378.5496435,
    "compliant": true,
    "duration": 60.07754945755005
  },
  {
    "index": 5643,
    "from": 1795602478.4227748,
    "to": 1795687318.472094,
    "compliant": true,
    "duration": 84840.04931926727
  },
  {
    "index": 5642,
    "from": 1795602358.4271886,
    "to": 1795602478.4227748,
    "compliant": true,
    "duration": 119.99558615684509
  },
  {
    "index": 5641,
    "from": 1795602298.60226,
    "to": 1795602358.4271886,
    "compliant": true,
    "duration": 59.824928522109985
  },
  {
    "index": 5640,
    "from": 1795520278.6464095,
    "to": 1795602298.60226,
    "compliant": true,
    "duration": 82019.9558506012
  },
  {
    "index": 5639,
    "from": 1795520218.526166,
    "to": 1795520278.6464095,
    "compliant": true,
    "duration": 60.120243549346924
  },
  {
    "index": 5638,
    "from": 1795520158.6435392,
    "to": 1795520218.526166,
    "compliant": true,
    "duration": 59.88262677192688
  },
  {
    "index": 5637,
    "from": 1795427158.6235,
    "to": 1795520158.6435392,
    "compliant": true,
    "duration": 93000.02003908157
  },
  {
    "index": 5636,
    "from": 1795427098.4407387,
    "to": 1795427158.6235,
    "compliant": true,
    "duration": 60.182761430740356
  },
  {
    "index": 5635,
    "from": 1795427038.4670446,
    "to": 1795427098.4407387,
    "compliant": true,
    "duration": 59.97369408607483
  },
  {
    "index": 5634,
    "from": 1795337338.3972983,
    "to": 1795427038.4670446,
    "compliant": true,
    "duration": 89700.06974625587
  },
  {
    "index": 5633,
    "from": 1795337278.4823146,
    "to": 1795337338.3972983,
    "compliant": true,
    "duration": 59.91498374938965
  },
  {
    "index": 5632,
    "from": 1795337158.4429066,
    "to": 1795337278.4823146,
    "compliant": true,
    "duration": 120.03940796852112
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

