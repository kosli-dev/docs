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
    "snapshot_index": 4879,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:5fbd867@sha256:373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
    "sha256": "373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
    "description": "1 instance changed",
    "reported_at": 1782714538.5522528,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/a35d09232116daff39d0f939cb133edc5750e2a1...5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=f0403484-7d4c-48b4-be71-9847ddfa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4879",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4879"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4879,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:340cd0e@sha256:9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
    "sha256": "9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
    "description": "3 instances changed",
    "reported_at": 1782714538.5522528,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/31a8d2291414e8912ea703982ab07b4966740154...340cd0e960f59711fd21ee7f23d613401c9ee589",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=0097b3f1-e098-4b77-b5d4-226879d8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4879",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4879"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4879,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
    "sha256": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
    "description": "1 instance changed",
    "reported_at": 1782714538.5522528,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/3e563eacf76b48caaf2f19f29472544199df8a00...6960ff7cc90425329e6def0adae4d5129dca9997",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=3f4df7b6-febd-4caf-8c8d-eef8083e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4879",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4879"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4878,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:5fbd867@sha256:373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
    "sha256": "373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
    "description": "1 instance changed",
    "reported_at": 1782714478.5875318,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/a35d09232116daff39d0f939cb133edc5750e2a1...5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=f0403484-7d4c-48b4-be71-9847ddfa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4878",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4878"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4878,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
    "sha256": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
    "description": "1 instance changed",
    "reported_at": 1782714478.5875318,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/3e563eacf76b48caaf2f19f29472544199df8a00...6960ff7cc90425329e6def0adae4d5129dca9997",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=3f4df7b6-febd-4caf-8c8d-eef8083e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4878",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4878"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4877,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
    "sha256": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
    "description": "1 instance changed",
    "reported_at": 1782714418.585481,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/75485ee4a18794755de633775a7b56b2b00cd7c9...88239b96c7bb1f0c99af688010f5aed4097ae7b4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=675642dc-0cc9-41e0-8dda-e67a6e64"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4877",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4877"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4877,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:521b7c3@sha256:51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
    "sha256": "51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
    "description": "1 instance changed",
    "reported_at": 1782714418.585481,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/514f79a280dee08bf889a4a4fdf41c9d2f231348...521b7c30720e903fa909ae36b7ea9b2f962aa63f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=1a3dbd1b-5cc1-4d75-9fff-2317ce97"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4877",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4877"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4877,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:23ca301@sha256:8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "sha256": "8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "description": "1 instance changed",
    "reported_at": 1782714418.585481,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/bb8a712de74f2fe3edf48169ca072d4eff997564...23ca301f1baa78b2c2784261991015597319ee94",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=426b6c00-c2b9-4cf2-864e-6df73e38"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4877",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4877"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4877,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:bc0f871@sha256:ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
    "sha256": "ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
    "description": "1 instance changed",
    "reported_at": 1782714418.585481,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa...bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=68982b48-8123-417a-a218-dd4b913c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4877",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4877"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4876,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:0635840@sha256:054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
    "sha256": "054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
    "description": "1 instance changed",
    "reported_at": 1782714358.666861,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/c1815fc4abb602f840a9e1e643692a143094148e...06358409a6a8b8accb35c5fd07082d359ee4947a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=fe6f0961-0fb5-43ec-a90f-0b243a39"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4876",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4876"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4876,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:23ca301@sha256:8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "sha256": "8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "description": "1 instance changed",
    "reported_at": 1782714358.666861,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/bb8a712de74f2fe3edf48169ca072d4eff997564...23ca301f1baa78b2c2784261991015597319ee94",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=426b6c00-c2b9-4cf2-864e-6df73e38"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4876",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4876"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4876,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
    "sha256": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
    "description": "1 instance changed",
    "reported_at": 1782714358.666861,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/9034c75cdb2846757cff32d24e1c5e91f40060a8...0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=58bda834-0bae-4c5a-9cd0-7f326e24"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4876",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4876"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4876,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:077d6f5@sha256:e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
    "sha256": "e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
    "description": "3 instances changed",
    "reported_at": 1782714358.666861,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/42ca333501c90d2cf36ce24035aa0a468e287da4...077d6f50114958e0d62d0f56f8258a4d02a93e02",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=8e4d1ac0-3457-4938-bfab-98373251"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4876",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4876"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4875,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:521b7c3@sha256:51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
    "sha256": "51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
    "description": "1 instance changed",
    "reported_at": 1782714298.56245,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/514f79a280dee08bf889a4a4fdf41c9d2f231348...521b7c30720e903fa909ae36b7ea9b2f962aa63f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=1a3dbd1b-5cc1-4d75-9fff-2317ce97"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4875",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4875"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4875,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:23ca301@sha256:8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "sha256": "8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
    "description": "1 instance changed",
    "reported_at": 1782714298.56245,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/bb8a712de74f2fe3edf48169ca072d4eff997564...23ca301f1baa78b2c2784261991015597319ee94",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=426b6c00-c2b9-4cf2-864e-6df73e38"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4875",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4875"
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

