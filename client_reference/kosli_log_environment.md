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
    "snapshot_index": 5126,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aaf06ae@sha256:30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
    "sha256": "30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1785243478.598589,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/web/compare/3f0b9975f96b7f4e4aae0b4409cebda3209be164...aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889?artifact_id=494b49a5-f26f-4602-8fce-8903d99d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5126",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5126"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5125,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2779354@sha256:af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
    "sha256": "af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1785243418.5364106,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/web/compare/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f...2779354a4fda0eeb90fd43f32211836d99f6bde1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=dc864446-cc9f-43e9-bf70-db7dc03b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5125",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5125"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5124,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
    "sha256": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241678.414592,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/8beff9901ac67acb7afcab3408106208571a1124...335ddfa139708c37908dd594a0502bc6d88f8615",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=5f3d2a2e-acdb-4414-a1e7-ebca7c32"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5124",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5124"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5123,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
    "sha256": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241618.6033545,
    "pipeline": "differ-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "differ-ci",
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/335ddfa139708c37908dd594a0502bc6d88f8615...1b7ea87a174a1a290600b469dc1029ec4c974320",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=53b144c7-33a3-4d8a-b416-37aea745"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5123",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5123"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a2e4638@sha256:c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
    "sha256": "c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241318.4716694,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47...a2e4638aaa102446b8a6d1d519c5bc007e24f087",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=c8c04d1b-0457-497c-a969-4d9c0b72"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "sha256": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241318.4716694,
    "pipeline": "languages-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "languages-start-points-ci",
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/c6db342472238a7852b6ff31b04f9a6a6099f5cf...6a7f7be81022f7ed3fa8383f016b55af86e2af23",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=796c3a9f-ee70-45ca-8a69-4be16335"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "sha256": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241318.4716694,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "sha256": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241318.4716694,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/9b711df71c76a1f293c2525ace65778036591baf...7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=5c293d3e-84a1-42dd-8215-6abd8d8d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "sha256": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241318.4716694,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/80b913e9f88902428a3567f75165d8b9d73b561a...804f248d832dc34e564507b009c246dfb4f0c657",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=0e55e1be-fab1-475b-8aaa-b45ca6e2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "sha256": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241318.4716694,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/e4757683b74df7033c95aa544a7824b395c2f8bb...5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=53e5b750-6f87-43db-a8a3-e1f5b1db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5122,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "sha256": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785241318.4716694,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/04e0e14bb8874ab521d35c97d6040133f0d2143a...c6db342472238a7852b6ff31b04f9a6a6099f5cf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=ed104a44-8358-4883-beeb-ac3c8bb7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5122",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5122"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5121,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "sha256": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241258.6193466,
    "pipeline": "custom-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "custom-start-points-ci",
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/d37aace7598ee943ba0bd5e51f224335cbdf0a3e...790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=653e13a5-2f2a-4a23-be4e-1693fc77"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5121",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5121"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5121,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0fb0be4@sha256:c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
    "sha256": "c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241258.6193466,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/5407827a19ff32c8d0e7ff2e8f18665e86e64f01...0fb0be439480821efb926a5079e39ce5941eaa48",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=e55cba1f-ce06-49ff-9701-62eb823d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5121",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5121"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5121,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "sha256": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785241258.6193466,
    "pipeline": "exercises-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "exercises-start-points-ci",
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/804f248d832dc34e564507b009c246dfb4f0c657...258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffb671be-6388-4f6a-ae64-8ba95d82"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5121",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5121"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5120,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "sha256": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1785240718.5257201,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/web/compare/bdf01beca687a34db9689499bd805cfc752a1747...3f0b9975f96b7f4e4aae0b4409cebda3209be164",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=0f00c8a9-1489-416c-b64f-5819890f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5120",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5120"
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

