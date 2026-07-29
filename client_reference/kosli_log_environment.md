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
    "snapshot_index": 5134,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
    "sha256": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785310558.4611607,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/e4d9d0868e299522b207696e19c07966a09bf08a...c81791fd10558a59f83876137fb021abcd89f262",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=28274720-dc6e-4b52-b48e-4418ecaa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5134",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5134"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5134,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:e4d9d08@sha256:2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
    "sha256": "2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785310558.4611607,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/92c624eabb024729fb2af6cdbe354db11ee3882f...e4d9d0868e299522b207696e19c07966a09bf08a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204?artifact_id=d2a91db5-76a8-43df-988c-d57fda6c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5134",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5134"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5133,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:e4d9d08@sha256:2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
    "sha256": "2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785305338.459451,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/92c624eabb024729fb2af6cdbe354db11ee3882f...e4d9d0868e299522b207696e19c07966a09bf08a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204?artifact_id=d2a91db5-76a8-43df-988c-d57fda6c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5133",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5133"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5133,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:92c624e@sha256:a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "sha256": "a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785305338.459451,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/b592c3af03e9530c1d224686a1745e4a12e1df00...92c624eabb024729fb2af6cdbe354db11ee3882f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975?artifact_id=42025c9c-2608-4ef0-b140-84548282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5133",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5133"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5132,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "sha256": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "description": "3 instances changed",
    "reported_at": 1785301138.4848077,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5132",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5132"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5131,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
    "sha256": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
    "description": "1 instance changed",
    "reported_at": 1785301078.6254478,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/f4bb3412725258648a7cf5ce1a776609b4dade72...c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=1fb48da0-c9b7-4627-8597-827ecccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5131",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5131"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5131,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "sha256": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "description": "3 instances changed",
    "reported_at": 1785301078.6254478,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b...19f873464a01f28ecd588504ffe03529119d6297",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=046fc54c-c295-45b3-bac0-81d40282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5131",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5131"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5131,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a2e4638@sha256:c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
    "sha256": "c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
    "description": "1 instance changed",
    "reported_at": 1785301078.6254478,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47...a2e4638aaa102446b8a6d1d519c5bc007e24f087",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=c8c04d1b-0457-497c-a969-4d9c0b72"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5131",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5131"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5131,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0fb0be4@sha256:c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
    "sha256": "c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
    "description": "1 instance changed",
    "reported_at": 1785301078.6254478,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/5407827a19ff32c8d0e7ff2e8f18665e86e64f01...0fb0be439480821efb926a5079e39ce5941eaa48",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=e55cba1f-ce06-49ff-9701-62eb823d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5131",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5131"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5130,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2779354@sha256:af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
    "sha256": "af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
    "description": "3 instances changed",
    "reported_at": 1785301018.7636228,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f...2779354a4fda0eeb90fd43f32211836d99f6bde1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=dc864446-cc9f-43e9-bf70-db7dc03b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5130",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5130"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5129,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "sha256": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "description": "1 instance changed",
    "reported_at": 1785300958.5618691,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5129",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5129"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5129,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:92c624e@sha256:a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "sha256": "a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "description": "1 instance changed",
    "reported_at": 1785300958.5618691,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/b592c3af03e9530c1d224686a1745e4a12e1df00...92c624eabb024729fb2af6cdbe354db11ee3882f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975?artifact_id=42025c9c-2608-4ef0-b140-84548282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5129",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5129"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5129,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "sha256": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
    "description": "1 instance changed",
    "reported_at": 1785300958.5618691,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5129",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5129"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5129,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
    "sha256": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
    "description": "1 instance changed",
    "reported_at": 1785300958.5618691,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/335ddfa139708c37908dd594a0502bc6d88f8615...1b7ea87a174a1a290600b469dc1029ec4c974320",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=53b144c7-33a3-4d8a-b416-37aea745"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5129",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5129"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5128,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
    "sha256": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
    "description": "1 instance changed",
    "reported_at": 1785300898.3949952,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/f4bb3412725258648a7cf5ce1a776609b4dade72...c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=1fb48da0-c9b7-4627-8597-827ecccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5128",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5128"
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

