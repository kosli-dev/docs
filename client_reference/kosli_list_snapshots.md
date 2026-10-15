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
    "index": 5483,
    "from": 1792045498.5715408,
    "to": 0.0,
    "compliant": true,
    "duration": 94.7624032497406
  },
  {
    "index": 5482,
    "from": 1791960178.6282132,
    "to": 1792045498.5715408,
    "compliant": true,
    "duration": 85319.94332766533
  },
  {
    "index": 5481,
    "from": 1791960118.442488,
    "to": 1791960178.6282132,
    "compliant": true,
    "duration": 60.18572521209717
  },
  {
    "index": 5480,
    "from": 1791880018.4897547,
    "to": 1791960118.442488,
    "compliant": true,
    "duration": 80099.95273327827
  },
  {
    "index": 5479,
    "from": 1791879958.4310446,
    "to": 1791880018.4897547,
    "compliant": true,
    "duration": 60.0587100982666
  },
  {
    "index": 5478,
    "from": 1791879898.512249,
    "to": 1791879958.4310446,
    "compliant": true,
    "duration": 59.918795585632324
  },
  {
    "index": 5477,
    "from": 1791806518.5142465,
    "to": 1791879898.512249,
    "compliant": true,
    "duration": 73379.99800252914
  },
  {
    "index": 5476,
    "from": 1791806458.6975975,
    "to": 1791806518.5142465,
    "compliant": true,
    "duration": 59.816648960113525
  },
  {
    "index": 5475,
    "from": 1791801958.431194,
    "to": 1791806458.6975975,
    "compliant": true,
    "duration": 4500.266403436661
  },
  {
    "index": 5474,
    "from": 1791801898.3531857,
    "to": 1791801958.431194,
    "compliant": true,
    "duration": 60.07800841331482
  },
  {
    "index": 5473,
    "from": 1791791998.5119064,
    "to": 1791801898.3531857,
    "compliant": true,
    "duration": 9899.841279268265
  },
  {
    "index": 5472,
    "from": 1791791938.4854105,
    "to": 1791791998.5119064,
    "compliant": true,
    "duration": 60.026495933532715
  },
  {
    "index": 5471,
    "from": 1791709558.3357823,
    "to": 1791791938.4854105,
    "compliant": true,
    "duration": 82380.14962816238
  },
  {
    "index": 5470,
    "from": 1791704998.5335464,
    "to": 1791709558.3357823,
    "compliant": true,
    "duration": 4559.802235841751
  },
  {
    "index": 5469,
    "from": 1791648838.3290987,
    "to": 1791704998.5335464,
    "compliant": true,
    "duration": 56160.20444774628
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

