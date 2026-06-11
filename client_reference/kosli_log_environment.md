---
title: "kosli log environment"
beta: false
deprecated: false
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
| Flag | Description |
| :--- | :--- |
|        `--end` string  |  [optional] The end of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour).  |
|        `--end-ts` float  |  [optional] The end of the events range as a Unix timestamp in seconds (integer or float).  |
|    `-h`, `--help`  |  help for environment  |
|    `-i`, `--interval` string  |  [optional] Expression to define specified snapshots range.  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--repo` strings  |  [optional] The name of a git repo as it is registered in Kosli. e.g kosli-dev/cli  |
|        `--reverse`  |  [optional] Reverse the order of output list.  |
|        `--start` string  |  [optional] The start of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour).  |
|        `--start-ts` float  |  [optional] The start of the events range as a Unix timestamp in seconds (integer or float).  |


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
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
    "sha256": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/16d155bdd120fe5a926504069dd18a98b8275fa8...9513e77858d775950f22173d0afd0634b2ac20b9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=ed68d54a-2549-4822-9dc5-96dad6c1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
    "sha256": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/f2e8fa718ca3b72527625bd182beb2950bea3a77...43d2a72431124e9fcf47bf866621ba3fd8e7f618",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=66b5c45a-22d2-4f37-8688-beeeb449"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
    "sha256": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/a11b7588b2d2333e1346f1a2bb100395f11f42d2...68d791f93dc161fd8dba63e49b7fe9f909cbe758",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=174dfb75-db2f-40b0-901a-8a02499c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
    "sha256": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
    "description": "3 instances changed",
    "reported_at": 1781167678.669744,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/517657b9dec6ac7ff431ca5d9b2de72fded5c295...8863c10c2c93d3539672e0bf75bd9925f8778564",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735?artifact_id=65fd4674-3e05-441a-8bd3-71492624"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
    "sha256": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/545cccbc91f4030fb4004421e1076bd7c2abbc93...76355112651c4ee66d6ee47f67e35459616f0dae",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=f94caaee-8681-4ead-acb2-8ea7c803"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
    "sha256": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
    "description": "3 instances changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bc8fb51346a42e17a4d3669f3ea11908782a43d1...bc5fbc14361ce7a6281b6110049d90a03f69d786",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1?artifact_id=665ba644-8f04-4330-a5e7-7a9c03ba"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
    "sha256": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/ebf104fc1c073c7462a6ec381af70f639e4b8ba0...cdaac807f3282bd0bba056d906d5536074297a04",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4?artifact_id=daaf8e44-a0d4-46df-af10-a134861d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
    "sha256": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/a300e4c15cff321ef952a60bbc3a4729772a2419...d3e5850912655f2b18a68129f5f3a6480fe305ef",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=7c413c73-ba1e-4707-b6d3-ced83312"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2036886@sha256:e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
    "sha256": "e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/3a066186b7fbbcec0130419518c5bb81b50e71db...20368865b1ba0532f99f69641bbb96e6334cb545",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=d5d4dc83-f3c0-4a50-b5cb-fdc4f610"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4749,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
    "sha256": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
    "description": "1 instance changed",
    "reported_at": 1781167678.669744,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/0a839a472d41bf860d1d6dc3ded45ff63144018d...f3c679170776733c60dc485e076b7cb515caa7a4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=a92f3bf6-3316-405e-aee8-51af645c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4749",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4749"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4748,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
    "sha256": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
    "description": "1 instance changed",
    "reported_at": 1781159278.7947195,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/0a839a472d41bf860d1d6dc3ded45ff63144018d...f3c679170776733c60dc485e076b7cb515caa7a4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=a92f3bf6-3316-405e-aee8-51af645c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4748",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4748"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4748,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
    "sha256": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
    "description": "3 instances changed",
    "reported_at": 1781159278.7947195,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/517657b9dec6ac7ff431ca5d9b2de72fded5c295...8863c10c2c93d3539672e0bf75bd9925f8778564",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735?artifact_id=65fd4674-3e05-441a-8bd3-71492624"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4748",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4748"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4748,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2036886@sha256:e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
    "sha256": "e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
    "description": "1 instance changed",
    "reported_at": 1781159278.7947195,
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/3a066186b7fbbcec0130419518c5bb81b50e71db...20368865b1ba0532f99f69641bbb96e6334cb545",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=d5d4dc83-f3c0-4a50-b5cb-fdc4f610"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4748",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4748"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4748,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
    "sha256": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
    "description": "3 instances changed",
    "reported_at": 1781159278.7947195,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bc8fb51346a42e17a4d3669f3ea11908782a43d1...bc5fbc14361ce7a6281b6110049d90a03f69d786",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1?artifact_id=665ba644-8f04-4330-a5e7-7a9c03ba"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4748",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4748"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4748,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
    "sha256": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
    "description": "1 instance changed",
    "reported_at": 1781159278.7947195,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/ebf104fc1c073c7462a6ec381af70f639e4b8ba0...cdaac807f3282bd0bba056d906d5536074297a04",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4?artifact_id=daaf8e44-a0d4-46df-af10-a134861d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4748",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4748"
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

