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

## Flags
| Flag | Description |
| :--- | :--- |
|    -h, --help  |  help for environments  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |


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

To view a live example of 'kosli list environments' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A  # read-only
kosli list environments --output=json
```

<Accordion title="View example output">
```json
[
  {
    "org": "cyber-dojo",
    "name": "aws-beta",
    "type": "ECS",
    "description": "The ECS cluster for staging cyber-dojo",
    "last_modified_at": 1777982784.1051183,
    "last_reported_at": 1777982784.1051183,
    "state": true,
    "include_scaling": false,
    "tags": {
      "url": "https://beta.cyber-dojo.org/"
    },
    "policies": [
      "build-process",
      "snyk-scan-aws-beta"
    ],
    "included_environments": null
  },
  {
    "org": "cyber-dojo",
    "name": "aws-prod",
    "type": "ECS",
    "description": "The ECS cluster for production cyber-dojo",
    "last_modified_at": 1777982818.589105,
    "last_reported_at": 1777982818.589105,
    "state": true,
    "include_scaling": false,
    "tags": {
      "url": "https://cyber-dojo.org/"
    },
    "policies": [
      "build-process",
      "snyk-scan-aws-prod"
    ],
    "included_environments": null
  },
  {
    "org": "cyber-dojo",
    "name": "production",
    "type": "logical",
    "description": "Production environments for cyber-dojo",
    "last_modified_at": 1723105767.5621033,
    "last_reported_at": null,
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
    "last_modified_at": 1764591277.5301485,
    "last_reported_at": 1744010496.9813983,
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
    "last_modified_at": 1764591277.811534,
    "last_reported_at": 1744010523.8133755,
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
</Accordion>

