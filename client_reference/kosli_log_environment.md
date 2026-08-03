---
title: "kosli log environment"
description: "List environment events."
---

## Synopsis

```shell
kosli log environment ENV_NAME [flags]
```

List environment events.
The results are paginated and ordered from latest to oldest.
By default, the page limit is 15 events per page.

You can optionally specify an INTERVAL between two snapshot expressions with [expression]..[expression].

Expressions can be:
* ~N   N'th behind the latest snapshot
* N    snapshot number N
* NOW  the latest snapshot

Either expression can be omitted to default to NOW.

You can also filter events by range using --start/--end (snapshot index or time expression such as "NOW" or "1hour") or --start-ts/--end-ts (Unix timestamps).


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--end` | string | [optional] The end of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour). |
| `--end-ts` | float | [optional] The end of the events range as a Unix timestamp in seconds (integer or float). |
| `-h`, `--help` | bool | help for environment |
| `-i`, `--interval` | string | [optional] Expression to define specified snapshots range. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--repo` | strings | [optional] The name of a git repo as it is registered in Kosli. e.g kosli-dev/cli |
| `--reverse` | bool | [optional] Reverse the order of output list. |
| `--start` | string | [optional] The start of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour). |
| `--start-ts` | float | [optional] The start of the events range as a Unix timestamp in seconds (integer or float). |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Live Example

To view a live example of 'kosli log environment' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli log environment aws-prod --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
[
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5171,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e39ff7@sha256:778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
    "sha256": "778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785755158.5525944,
    "pipeline": "dashboard-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "dashboard-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/7448cb7ff6b26757ecb9f855889cb2196491916a...0e39ff79ccab8804f4bfdff993b5df786bf47426",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c?artifact_id=9b675d1d-480c-4289-83f4-337b4088"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5171",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5171"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5170,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
    "sha256": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785755098.5952232,
    "pipeline": "dashboard-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "dashboard-ci",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/0e39ff79ccab8804f4bfdff993b5df786bf47426...da7bacefac23b0983d2b9f39d87508e0f85b1167",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=04894b11-8736-4651-9824-7e882b54"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5170",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5170"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5169,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
    "sha256": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785744358.5353608,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/58aae36fc3a059c66402e904d866058140ac892e...bc3fd56aa1076613dc6631f817fb336424824506",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744?artifact_id=d486ebc0-6213-433e-8bdc-f2e18766"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5169",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5169"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5168,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c221bb1@sha256:d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
    "sha256": "d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785744298.6376145,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/bc3fd56aa1076613dc6631f817fb336424824506...c221bb1cdea95e14bc2df052e894756a9d96c378",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355?artifact_id=071c9aea-36bf-4284-9394-80b05793"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5168",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5168"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5167,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
    "sha256": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785736378.4882667,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/58aae36fc3a059c66402e904d866058140ac892e...bc3fd56aa1076613dc6631f817fb336424824506",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744?artifact_id=d486ebc0-6213-433e-8bdc-f2e18766"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5167",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5167"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5167,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:58aae36@sha256:6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
    "sha256": "6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785736378.4882667,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/a2e4638aaa102446b8a6d1d519c5bc007e24f087...58aae36fc3a059c66402e904d866058140ac892e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e?artifact_id=0130c5c2-9e8a-4190-9b15-26956972"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5167",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5167"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5166,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
    "sha256": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
    "description": "1 instance changed",
    "reported_at": 1785734098.6068468,
    "pipeline": "spooler-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "spooler-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/e4d9d0868e299522b207696e19c07966a09bf08a...c81791fd10558a59f83876137fb021abcd89f262",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=28274720-dc6e-4b52-b48e-4418ecaa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5166",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5166"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5166,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "sha256": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "description": "3 instances changed",
    "reported_at": 1785734098.6068468,
    "pipeline": "runner-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "runner-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b...19f873464a01f28ecd588504ffe03529119d6297",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=046fc54c-c295-45b3-bac0-81d40282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5166",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5166"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5166,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "sha256": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "description": "1 instance changed",
    "reported_at": 1785734098.6068468,
    "pipeline": "languages-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "languages-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/c6db342472238a7852b6ff31b04f9a6a6099f5cf...6a7f7be81022f7ed3fa8383f016b55af86e2af23",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=796c3a9f-ee70-45ca-8a69-4be16335"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5166",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5166"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5165,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "sha256": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "description": "1 instance changed",
    "reported_at": 1785733978.6575258,
    "pipeline": "custom-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "custom-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/d37aace7598ee943ba0bd5e51f224335cbdf0a3e...790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=653e13a5-2f2a-4a23-be4e-1693fc77"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5165",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5165"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5165,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
    "sha256": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
    "description": "1 instance changed",
    "reported_at": 1785733978.6575258,
    "pipeline": "saver-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "saver-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e...595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=8cfcfa9a-8b26-401b-8c06-945fff4f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5165",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5165"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5165,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
    "sha256": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
    "description": "1 instance changed",
    "reported_at": 1785733978.6575258,
    "pipeline": "creator-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "creator-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/07ed087071878b405ac1cf7fe77e5d8c70ce3a4b...89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=e6a23489-6ea9-44f6-b4de-577edc06"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5165",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5165"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5165,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "sha256": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "description": "1 instance changed",
    "reported_at": 1785733978.6575258,
    "pipeline": "exercises-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "exercises-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/804f248d832dc34e564507b009c246dfb4f0c657...258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffb671be-6388-4f6a-ae64-8ba95d82"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5165",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5165"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5165,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
    "sha256": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
    "description": "1 instance changed",
    "reported_at": 1785733978.6575258,
    "pipeline": "differ-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "differ-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/1b7ea87a174a1a290600b469dc1029ec4c974320...10e162d4e1294815375a31121f14d57e13183b34",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=7e8c883e-f5ed-4df1-81d0-6b2959ee"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5165",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5165"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5164,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:58aae36@sha256:6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
    "sha256": "6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
    "description": "1 instance changed",
    "reported_at": 1785733858.4808197,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/a2e4638aaa102446b8a6d1d519c5bc007e24f087...58aae36fc3a059c66402e904d866058140ac892e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/6c120dc138ea38130a6ceb7d4addb6b8a75263d118aef339de76af783208aa1e?artifact_id=0130c5c2-9e8a-4190-9b15-26956972"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5164",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5164"
      }
    }
  }
]
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list the last 15 events for an environment">
```shell
kosli log environment yourEnvironmentName 

```
</Accordion>
<Accordion title="list the last 30 events for an environment">
```shell
kosli log environment yourEnvironmentName 
	--page-limit 30 

```
</Accordion>
<Accordion title="list the last 30 events for an environment (in JSON)">
```shell
kosli log environment yourEnvironmentName 
	--page-limit 30 
	--output json

```
</Accordion>
<Accordion title="list events for an environment filtered by repo">
```shell
kosli log environment yourEnvironmentName 
	--repo yourOrg/yourRepo 

```
</Accordion>
<Accordion title="list events for an environment filtered by multiple repos">
```shell
kosli log environment yourEnvironmentName 
	--repo yourOrg/yourRepo1 
	--repo yourOrg/yourRepo2 

```
</Accordion>
<Accordion title="list events starting from snapshot 5">
```shell
kosli log environment yourEnvironmentName 
	--start 5 

```
</Accordion>
<Accordion title="list events between two time expressions">
```shell
kosli log environment yourEnvironmentName 
	--start 1hour 
	--end NOW 

```
</Accordion>
<Accordion title="list events between two Unix timestamps">
```shell
kosli log environment yourEnvironmentName 
	--start-ts 1700000000 
	--end-ts 1700086400 
```
</Accordion>
</AccordionGroup>

