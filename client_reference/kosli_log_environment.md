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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
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
    "snapshot_index": 5616,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
    "sha256": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
    "description": "1 instance changed",
    "reported_at": 1795080718.4478593,
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
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=6509b70e-7a40-41f6-b28d-248a47ac"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5616",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5616"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5616,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
    "sha256": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
    "description": "3 instances changed",
    "reported_at": 1795080718.4478593,
    "pipeline": "web-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "web-ci",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=dbd74cdd-737f-4a42-b48c-9cb6e31d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5616",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5616"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5616,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
    "sha256": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
    "description": "1 instance changed",
    "reported_at": 1795080718.4478593,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9fcbc9ef1306b6fed965cecfd4ff778582015fa3...bd40ecfc45d8682a287d9200389b0a45b4d10e73",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=b99341a1-9cf9-44d5-9c69-ef3848e7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5616",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5616"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
    "sha256": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93...6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=f741ae29-7cc4-44e5-a2bd-9168c06b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
    "sha256": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
    "description": "3 instances changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e...799f82f087a0029f9b4c3a9d85db930752190e09",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=816fae65-4857-47e1-8a9a-82836f5e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
    "sha256": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c...4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=1889185f-3ca2-4ec7-87bc-b3ca1dce"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
    "sha256": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/4bb52cbbdefcd01d973f91b08fd9b5b386570c80...56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=6d758363-e084-4e25-bd81-2bb19e66"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
    "sha256": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=4a4c1d74-d625-49d3-a1db-8bc75ca9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
    "sha256": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6...530926abbebc41a1201839ccc5d8a4b1062315eb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=df8ba5d9-7719-4a38-8dac-3bf6b2d5"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5615,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
    "sha256": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
    "description": "1 instance changed",
    "reported_at": 1795080658.4572291,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/6baf18253638f0417e2dc20d71804cc6db5329c5...787de90aa159f24ec115fd42b3ddfbe44996171f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=1719331a-74d2-4463-8e44-91a0c49a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5615",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5615"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5614,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
    "sha256": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
    "description": "1 instance changed",
    "reported_at": 1795080598.4422882,
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
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93...6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=f741ae29-7cc4-44e5-a2bd-9168c06b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5614",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5614"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5614,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
    "sha256": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
    "description": "1 instance changed",
    "reported_at": 1795080598.4422882,
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
        "flow_name": "snyk-aws-beta-per-artifact",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=6509b70e-7a40-41f6-b28d-248a47ac"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5614",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5614"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5614,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
    "sha256": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
    "description": "3 instances changed",
    "reported_at": 1795080598.4422882,
    "pipeline": "web-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "web-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=dbd74cdd-737f-4a42-b48c-9cb6e31d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5614",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5614"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5614,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "sha256": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "description": "1 instance changed",
    "reported_at": 1795080598.4422882,
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
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/b52ea1fb0b04c2cda0bff8db8887d019a7a81637...a173ddba4169059477911c4fa0c73674407712a5",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=6d1a6233-1cf8-46ed-8e60-5959a5a3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5614",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5614"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5614,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
    "sha256": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
    "description": "1 instance changed",
    "reported_at": 1795080598.4422882,
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
        "flow_name": "snyk-aws-beta-per-artifact",
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9fcbc9ef1306b6fed965cecfd4ff778582015fa3...bd40ecfc45d8682a287d9200389b0a45b4d10e73",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=b99341a1-9cf9-44d5-9c69-ef3848e7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5614",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5614"
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

