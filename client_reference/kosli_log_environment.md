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
    "snapshot_index": 5116,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:92c624e@sha256:a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "sha256": "a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785224878.4373872,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/b592c3af03e9530c1d224686a1745e4a12e1df00...92c624eabb024729fb2af6cdbe354db11ee3882f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975?artifact_id=42025c9c-2608-4ef0-b140-84548282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5116",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5116"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5116,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:b592c3a@sha256:5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
    "sha256": "5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785224878.4373872,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/5451dae79163e5e06397eb2fe8792eceb8a17de5...b592c3af03e9530c1d224686a1745e4a12e1df00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e?artifact_id=60af6a2b-6351-40e9-8c44-6f73abc4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5116",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5116"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5115,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:b592c3a@sha256:5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
    "sha256": "5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1785215338.442852,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/5451dae79163e5e06397eb2fe8792eceb8a17de5...b592c3af03e9530c1d224686a1745e4a12e1df00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/5cd2a591370f45e0156411a484182215a0c403992b9aef2cfaacbeadb3ac2b3e?artifact_id=60af6a2b-6351-40e9-8c44-6f73abc4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5115",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5115"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5115,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5451dae@sha256:1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "sha256": "1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1785215338.442852,
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
    "code_diff": null,
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f?artifact_id=0d8ff1d2-a707-4bc0-9ce1-e37af354"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5115",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5115"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5114,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "sha256": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "description": "3 instances changed",
    "reported_at": 1785214438.378998,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5114",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5114"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5113,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "sha256": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
    "description": "3 instances changed",
    "reported_at": 1785214378.5198987,
    "pipeline": "runner-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "runner-ci",
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b...19f873464a01f28ecd588504ffe03529119d6297",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=046fc54c-c295-45b3-bac0-81d40282"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5113",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5113"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5113,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "sha256": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "description": "1 instance changed",
    "reported_at": 1785214378.5198987,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5113",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5113"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5112,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5451dae@sha256:1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "sha256": "1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "description": "1 instance changed",
    "reported_at": 1785214318.4842489,
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
    "code_diff": null,
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f?artifact_id=0d8ff1d2-a707-4bc0-9ce1-e37af354"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5112",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5112"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5451dae@sha256:1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "sha256": "1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": null,
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1b070a24ceafec25a9ed62bca61ac668b7e77381e1d4d8b755d22ceacc400c9f?artifact_id=0d8ff1d2-a707-4bc0-9ce1-e37af354"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "sha256": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "sha256": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:76672a8@sha256:aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
    "sha256": "aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/7e00b70f8911edf1c480ba9a8b9c2a280260cb08...76672a8b247049c3ce8c3140852e17be8f47d995",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=3cb9c270-d59b-4b28-b16a-b23d89d2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "sha256": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/e4757683b74df7033c95aa544a7824b395c2f8bb...5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=53e5b750-6f87-43db-a8a3-e1f5b1db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5111,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "sha256": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
    "description": "1 instance changed",
    "reported_at": 1785214258.6438735,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5111",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5111"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5110,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "sha256": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
    "description": "3 instances changed",
    "reported_at": 1785214198.674762,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5110",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5110"
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

