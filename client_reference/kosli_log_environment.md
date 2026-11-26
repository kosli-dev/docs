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


## JSON output

With `--output json`, this command prints the response of the [List environment events](/api-reference/environments/list-environment-events) API operation as the server returned it. The shape follows the server's published API spec, not the CLI version.

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
    "snapshot_index": 5646,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2bf3642@sha256:626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
    "sha256": "626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
    "description": "1 instance changed",
    "reported_at": 1795687438.5866702,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=d5b49703-6e49-4c2b-a26e-09f227c9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5646",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5646,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "sha256": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "description": "1 instance changed",
    "reported_at": 1795687438.5866702,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5646",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5646,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2bf3642@sha256:82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
    "sha256": "82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
    "description": "1 instance changed",
    "reported_at": 1795687438.5866702,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=a56a9821-03d8-46d8-a58d-c0f189c9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5646",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5646,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bcb5902@sha256:97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
    "sha256": "97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
    "description": "3 instances changed",
    "reported_at": 1795687438.5866702,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...bcb5902178a74126ae2593f6c3189cacb9d049fb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=66d77503-6993-4ecd-8da5-edab1814"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5646",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5646,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:0191adf@sha256:f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
    "sha256": "f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
    "description": "1 instance changed",
    "reported_at": 1795687438.5866702,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/6b3ef8b0e2436e882515c3a7310b84dee24bde2f...0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=11cf8b7e-ae89-4065-ac14-29fca4fa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5646",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a1b031@sha256:0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
    "sha256": "0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/bd40ecfc45d8682a287d9200389b0a45b4d10e73...1a1b031d793c474599506ec12faac073df5b6647",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=048a5579-4e40-45e2-8465-a2e72e55"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b3940c2@sha256:48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
    "sha256": "48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/787de90aa159f24ec115fd42b3ddfbe44996171f...b3940c267183bbcee441756523576162575f8e01",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=43b1823b-0ade-4eba-8849-f1b7a0f4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2bf3642@sha256:626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
    "sha256": "626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=d5b49703-6e49-4c2b-a26e-09f227c9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "sha256": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/b52ea1fb0b04c2cda0bff8db8887d019a7a81637...a173ddba4169059477911c4fa0c73674407712a5",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=6d1a6233-1cf8-46ed-8e60-5959a5a3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2bf3642@sha256:82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
    "sha256": "82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=a56a9821-03d8-46d8-a58d-c0f189c9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bcb5902@sha256:97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
    "sha256": "97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
    "description": "3 instances changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...bcb5902178a74126ae2593f6c3189cacb9d049fb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=66d77503-6993-4ecd-8da5-edab1814"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:aad1254@sha256:aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
    "sha256": "aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/4726aeaf7f611b7e4c2c5be6140a6423055d1db9...aad12541eaefc579b91f77059df895b032eba259",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=e0ba195d-c8fd-47f4-a19d-77568fe4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5645,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:cfb37e8@sha256:f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
    "sha256": "f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
    "description": "1 instance changed",
    "reported_at": 1795687378.5496435,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/530926abbebc41a1201839ccc5d8a4b1062315eb...cfb37e8c1a1634799f4518186603ce6da97d0958",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=f6712d86-2289-4ed3-81fc-83c3d50a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5645",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5645"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5644,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c15feb2@sha256:1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
    "sha256": "1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
    "description": "1 instance changed",
    "reported_at": 1795687318.472094,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213...c15feb2710922b82ec50d2cf131da532e09e7dc9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=4dc14438-0e15-40e3-bd64-5754a198"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5644",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5644"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5644,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:a0ffbb8@sha256:4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
    "sha256": "4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
    "description": "3 instances changed",
    "reported_at": 1795687318.472094,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/799f82f087a0029f9b4c3a9d85db930752190e09...a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=462ca1fd-0679-480b-a21d-3d199429"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5644",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5644"
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

