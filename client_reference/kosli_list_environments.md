---
title: "kosli list environments"
beta: false
deprecated: false
description: "List environments for an org."
---

## Synopsis

```shell
kosli list environments [flags]
```

List environments for an org.
By default, all environments are returned in one response.
When --page or --page-limit is set, the results are paginated and the response includes pagination metadata.
The list can be filtered by name, type, space and tags, and sorted with --sort and --sort-direction.

## Flags
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for environments  |
|        `--name` string  |  [optional] Only list environments whose name contains this substring (case-insensitive).  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--sort` string  |  [optional] The field to sort environments by. Valid values are: [name, last_modified_at, last_changed_at]. (defaults to name)  |
|        `--sort-direction` string  |  [optional] The direction to sort environments in. Valid values are: [asc, desc]. (defaults to asc)  |
|        `--space-id` strings  |  [optional] Only list environments in the space with this ID. Can be repeated to match more than one space.  |
|        `--tag` strings  |  [optional] Only list environments that have this tag, given as 'key' or 'key:value'. Can be repeated to match more than one tag.  |
|        `--type` strings  |  [optional] Only list environments of this type. Valid types are: [K8S, ECS, S3, lambda, server, docker, azure-apps, cloud-run, logical]. Can be repeated to match more than one type.  |


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

To view a live example of 'kosli list environments' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli list environments --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
[
  {
    "org": "cyber-dojo",
    "name": "aws-beta",
    "type": "ECS",
    "description": "The ECS cluster for staging cyber-dojo",
    "last_modified_at": 1781604264.0449266,
    "last_reported_at": 1781604264.0449266,
    "last_changed_at": 1781597303.9477544,
    "state": true,
    "include_scaling": false,
    "tags": {
      "url": "https://beta.cyber-dojo.org/"
    },
    "policies": [
      "provenance",
      "pull-request",
      "snyk-scan-aws-beta",
      "trail-compliance-aws-beta"
    ],
    "included_environments": null
  },
  {
    "org": "cyber-dojo",
    "name": "aws-prod",
    "type": "ECS",
    "description": "The ECS cluster for production cyber-dojo",
    "last_modified_at": 1781604298.5932145,
    "last_reported_at": 1781604298.5932145,
    "last_changed_at": 1781596438.4966626,
    "state": true,
    "include_scaling": false,
    "tags": {
      "url": "https://cyber-dojo.org/"
    },
    "policies": [
      "production-promotion",
      "provenance",
      "pull-request",
      "snyk-scan-aws-prod",
      "trail-compliance-aws-prod"
    ],
    "included_environments": null
  },
  {
    "org": "cyber-dojo",
    "name": "production",
    "type": "logical",
    "description": "Production environments for cyber-dojo",
    "last_modified_at": 1781596438.4966626,
    "last_reported_at": null,
    "last_changed_at": 1781596438.4966626,
    "state": true,
    "include_scaling": false,
    "tags": {},
    "policies": null,
    "included_environments": [
      "aws-prod",
      "terraform-state-differ-prod"
    ]
  },
  {
    "org": "cyber-dojo",
    "name": "terraform-state-differ-beta",
    "type": "S3",
    "description": "Terraform state file of the differ service for staging cyber-dojo",
    "last_modified_at": 1764591277.5828784,
    "last_reported_at": 1744010496.9813983,
    "last_changed_at": 1764591277.5828784,
    "state": true,
    "include_scaling": false,
    "tags": {},
    "policies": [
      "auto-generated-no-provenance-required"
    ],
    "included_environments": null
  },
  {
    "org": "cyber-dojo",
    "name": "terraform-state-differ-prod",
    "type": "S3",
    "description": "Terraform state file of the differ service for production cyber-dojo",
    "last_modified_at": 1764591277.864438,
    "last_reported_at": 1744010523.8133755,
    "last_changed_at": 1764591277.864438,
    "state": true,
    "include_scaling": false,
    "tags": {},
    "policies": [
      "auto-generated-no-provenance-required"
    ],
    "included_environments": null
  }
]
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list all environments for an org">
```shell
kosli list environments 

```
</Accordion>
<Accordion title="show the second page of environments, 25 per page">
```shell
kosli list environments 
	--page 2 
	--page-limit 25 

```
</Accordion>
<Accordion title="list environments whose name contains a substring (in JSON)">
```shell
kosli list environments 
	--name prod 
	--output json 

```
</Accordion>
<Accordion title="list K8S and ECS environments tagged with team=platform">
```shell
kosli list environments 
	--type K8S 
	--type ECS 
	--tag team:platform 

```
</Accordion>
<Accordion title="list environments sorted by when they last changed, newest first">
```shell
kosli list environments 
	--sort last_changed_at 
	--sort-direction desc 
```
</Accordion>
</AccordionGroup>

