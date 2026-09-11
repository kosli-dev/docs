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
    "snapshot_index": 5352,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "sha256": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "description": "1 instance changed",
    "reported_at": 1789108858.5535865,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/abdc61396b5031dbb1e90f5c9c190d303ff243e1...99d7b74f39e311d492902ad48dbe97da63f2c687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=205424b6-5741-4071-bd36-c26e83f6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5352",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5352"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
    "sha256": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/8e6b51867675d4b652a38353611cde1d8567fce0...5d1d4b6035691d7986e05ab263e521b3e711fa0c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=f5813ac8-1ad7-433a-beee-f90a065d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
    "sha256": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/ff9f292e809801d35246183988b7812826bc2760...6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=7ba704a0-8706-4f12-9eb8-776c7e5d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
    "sha256": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
    "description": "3 instances changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9...4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=612b9903-ce02-40a7-a329-77b10931"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
    "sha256": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/9030f8f46e738d94bd817727b8f8a9a54f106585...7c4708f675a7717376529273ec32d08cd93f5c26",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=326e1373-e805-48be-bfc7-6631db28"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
    "sha256": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f...5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=df1b0b8e-7efa-415e-860d-9123aa27"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "sha256": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/abdc61396b5031dbb1e90f5c9c190d303ff243e1...99d7b74f39e311d492902ad48dbe97da63f2c687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=205424b6-5741-4071-bd36-c26e83f6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
    "sha256": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65...bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=30338133-ceb7-4976-8956-e0b140cf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
    "sha256": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8...d01bb39495a1356eabe934bef84b92cc964a26f1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=6884abdb-afdd-4c56-aa14-94e8da5c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
    "sha256": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
    "description": "3 instances changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/cbe481c4b842f897e4e9e411cd78461a3a12a334...236898f12a3bcce3b60625dd71c6f817d4cc37c2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=9d418e45-a78d-462a-b8be-aaf2fc85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
    "sha256": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/b12a5c9b17023462d13e81381a69c7ef05f84dc2...86c839ee588f393d84a6b9c036478d10bb6f2a2d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=60d0583d-4388-4a0a-925d-5b47d9a8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5351,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
    "sha256": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
    "description": "1 instance changed",
    "reported_at": 1789108798.4511206,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de...2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=054eef05-3aee-49ae-9e4d-55f768b7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5351",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5351"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5350,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
    "sha256": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1789023418.5988352,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/3992c3ac326ff4472870fb49736a31967df95555...abdc61396b5031dbb1e90f5c9c190d303ff243e1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a?artifact_id=77dd7d10-64d9-4d28-a29a-bc7aaba0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5350",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5350"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5349,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "sha256": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1789023358.6002493,
    "pipeline": "creator-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "creator-ci",
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/abdc61396b5031dbb1e90f5c9c190d303ff243e1...99d7b74f39e311d492902ad48dbe97da63f2c687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=205424b6-5741-4071-bd36-c26e83f6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5349",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5349"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5348,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
    "sha256": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1789022878.756657,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/ff9f292e809801d35246183988b7812826bc2760...6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=7ba704a0-8706-4f12-9eb8-776c7e5d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5348",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5348"
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

