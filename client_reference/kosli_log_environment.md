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
    "snapshot_index": 5234,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:85cac88@sha256:f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
    "sha256": "f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
    "description": "3 instances changed",
    "reported_at": 1786679818.4046729,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3...85cac880cb74678426eb2ed4dbf2538995404c5c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=d4d2a067-63c8-4403-a6f5-554e6fef"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5234",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5234"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
    "sha256": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/10e162d4e1294815375a31121f14d57e13183b34...108cccf9bccf9af5d455db66c250480b53cbecc7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=50b8cff6-1888-4c76-b31a-fdd7a311"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
    "sha256": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
    "description": "3 instances changed",
    "reported_at": 1786679758.5206547,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e...5e4b9873df93525c041c386c06e0ab8fc36b6f33",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=f658e6e3-9ce8-462f-a29e-a2cc6f7b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "sha256": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/d37aace7598ee943ba0bd5e51f224335cbdf0a3e...790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=653e13a5-2f2a-4a23-be4e-1693fc77"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
    "sha256": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/89019f6d8059406e56fa499b2dec2dbf93f4d5c7...83357f112ef5c10b157cb84732c77965cc8ddc48",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=11539f6a-befb-4b79-9484-fd9f25d3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
    "sha256": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/6a7f7be81022f7ed3fa8383f016b55af86e2af23...068b3424c7da843a4f2d428d2e4915f33efc4a02",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=4154b9c8-14cc-426f-abc5-05220611"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "sha256": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/804f248d832dc34e564507b009c246dfb4f0c657...258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffb671be-6388-4f6a-ae64-8ba95d82"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5233,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
    "sha256": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
    "description": "1 instance changed",
    "reported_at": 1786679758.5206547,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/c81791fd10558a59f83876137fb021abcd89f262...dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=df2dcc5e-bb07-40e8-b013-9ac60f42"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5233",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5233"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5232,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
    "sha256": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
    "description": "1 instance changed",
    "reported_at": 1786679638.3800714,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/5ce2769937a4014a853787d7b3d89ec30b6ac967...fb791742054fa28dd89269aac8002ebfd7b3386e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=b9778ac6-6d83-4954-98ba-a3e60a22"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5232",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5232"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5231,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
    "sha256": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
    "description": "1 instance changed",
    "reported_at": 1786679578.5574222,
    "pipeline": "saver-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "saver-ci",
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/595e902fa2f5844d9ce0612a5c9295cd8dab5b97...36f0420f728fe61e44a3ab0043cf9a3d70863cad",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=01bf7de8-52fc-4585-a4b6-abf82047"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5231",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5231"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5230,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
    "sha256": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
    "description": "1 instance changed",
    "reported_at": 1786679518.6214967,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/da7bacefac23b0983d2b9f39d87508e0f85b1167...2b300f450f72006f6a9000aaf9cd04485f1e8095",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=a805b555-f25a-4828-89d2-a28881c8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5230",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5230"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5230,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
    "sha256": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
    "description": "1 instance changed",
    "reported_at": 1786679518.6214967,
    "pipeline": "saver-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "saver-ci",
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/595e902fa2f5844d9ce0612a5c9295cd8dab5b97...36f0420f728fe61e44a3ab0043cf9a3d70863cad",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=01bf7de8-52fc-4585-a4b6-abf82047"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5230",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5230"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5230,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
    "sha256": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
    "description": "1 instance changed",
    "reported_at": 1786679518.6214967,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/c81791fd10558a59f83876137fb021abcd89f262...dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=df2dcc5e-bb07-40e8-b013-9ac60f42"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5230",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5230"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5229,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
    "sha256": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
    "description": "1 instance changed",
    "reported_at": 1786598698.4780145,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/6a7f7be81022f7ed3fa8383f016b55af86e2af23...068b3424c7da843a4f2d428d2e4915f33efc4a02",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=4154b9c8-14cc-426f-abc5-05220611"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5229",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5229"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5229,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:85cac88@sha256:f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
    "sha256": "f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
    "description": "3 instances changed",
    "reported_at": 1786598698.4780145,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3...85cac880cb74678426eb2ed4dbf2538995404c5c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=d4d2a067-63c8-4403-a6f5-554e6fef"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5229",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5229"
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

