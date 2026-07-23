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
    "snapshot_index": 5069,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "sha256": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1784790118.4310617,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5069",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5069"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5068,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:2e200e4@sha256:919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067",
    "sha256": "919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1784790058.6402347,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/88b7eeacb488a5117ac568408363ac59a146f41a...2e200e4e3ee5b6dc4968bac67c27431e46be992c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067?artifact_id=ac186b3c-a669-4002-86ad-432aeedd"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5068",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5068"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5067,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "sha256": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "description": "3 instances changed",
    "reported_at": 1784782978.3652897,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5067",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5067"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5067,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "sha256": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "description": "1 instance changed",
    "reported_at": 1784782978.3652897,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5067",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5067"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "sha256": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "description": "3 instances changed",
    "reported_at": 1784782798.6282318,
    "pipeline": "web-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "web-ci",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/bdf01beca687a34db9689499bd805cfc752a1747...3f0b9975f96b7f4e4aae0b4409cebda3209be164",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=0f00c8a9-1489-416c-b64f-5819890f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "sha256": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "sha256": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/9b711df71c76a1f293c2525ace65778036591baf...7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=5c293d3e-84a1-42dd-8215-6abd8d8d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "sha256": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/80b913e9f88902428a3567f75165d8b9d73b561a...804f248d832dc34e564507b009c246dfb4f0c657",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=0e55e1be-fab1-475b-8aaa-b45ca6e2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:76672a8@sha256:aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
    "sha256": "aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/7e00b70f8911edf1c480ba9a8b9c2a280260cb08...76672a8b247049c3ce8c3140852e17be8f47d995",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=3cb9c270-d59b-4b28-b16a-b23d89d2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
    "sha256": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/8beff9901ac67acb7afcab3408106208571a1124...335ddfa139708c37908dd594a0502bc6d88f8615",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=5f3d2a2e-acdb-4414-a1e7-ebca7c32"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "sha256": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/e4757683b74df7033c95aa544a7824b395c2f8bb...5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=53e5b750-6f87-43db-a8a3-e1f5b1db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "sha256": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/04e0e14bb8874ab521d35c97d6040133f0d2143a...c6db342472238a7852b6ff31b04f9a6a6099f5cf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=ed104a44-8358-4883-beeb-ac3c8bb7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5066,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "sha256": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "description": "1 instance changed",
    "reported_at": 1784782798.6282318,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5066",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5066"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5065,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "sha256": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "description": "3 instances changed",
    "reported_at": 1784696218.587319,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5065",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5065"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5064,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "sha256": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "description": "1 instance changed",
    "reported_at": 1784696098.485834,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5064",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5064"
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

