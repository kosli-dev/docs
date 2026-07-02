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
    "snapshot_index": 4932,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "sha256": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1782973678.4485867,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/6960ff7cc90425329e6def0adae4d5129dca9997...5812bb564e572c9e33aef2789d2687f1a999a687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=b0c5a0c3-e982-43a4-b906-de850bf4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4932",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4932"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4931,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
    "sha256": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1782973618.6021194,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/5812bb564e572c9e33aef2789d2687f1a999a687...9d1887776497e501bc8dcd46e508488bf5c8b0c8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb?artifact_id=2253016a-6669-4742-a9ac-19e2c25a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4931",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4931"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4930,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:027b85e@sha256:38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
    "sha256": "38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
    "description": "3 instances changed",
    "reported_at": 1782971758.5585485,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a...027b85ebccec65b35b0ba0e4da196b7738d4ba82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=df97a2c6-d2eb-4465-b276-084bd7a7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4930",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4930"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4929,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "sha256": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "description": "1 instance changed",
    "reported_at": 1782971518.9605753,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/6960ff7cc90425329e6def0adae4d5129dca9997...5812bb564e572c9e33aef2789d2687f1a999a687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=b0c5a0c3-e982-43a4-b906-de850bf4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4929",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4929"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "sha256": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "description": "1 instance changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/0867cd49ecfb556eb662e1942c500f0d4fc50bf4...ca386e022a6857ad4ea8cfcc765a574452555ac7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e5dd9397-3db0-4786-b854-e938e315"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:df9af0c@sha256:157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
    "sha256": "157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
    "description": "1 instance changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/f62bce8337416d4f785ca825999e3045382b5e5d...df9af0c9a2a81ed7bfc429979121b8310bbe7138",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=149f3e12-210d-48b5-af42-01085ab2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
    "sha256": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
    "description": "1 instance changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/670c9632fe81e69d2cf48aa1dc21347b562fb042...139dc6d316a5e4b66755fecc926f2e25cd5c8208",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=03592b11-2821-4d18-b7cb-7e4442a7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
    "sha256": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
    "description": "3 instances changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/84d9fee0524e602c1d7529bf18279fc78486bdb0...552f300213a65ee0c8c773474d75b26b2d723575",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=3136a438-a076-4242-8e2f-d6595cfe"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
    "sha256": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
    "description": "1 instance changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/88239b96c7bb1f0c99af688010f5aed4097ae7b4...17f61f83683a52ec1b9040127da582affb70e997",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=1157cd4a-b91c-4788-b572-22996ccd"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4928,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
    "sha256": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
    "description": "1 instance changed",
    "reported_at": 1782971458.530566,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/2b7b7759d2f5f8246a5d0e9ea99def087a7e2817...ae0c2f039480061d958cc007bc4c78e5b0f36a83",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=23d32989-6594-441a-8baa-ba54c633"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4928",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4928"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4927,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
    "sha256": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
    "description": "1 instance changed",
    "reported_at": 1782971338.646279,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/a6e433a6fd3eb29c499b75310756420864b6c346...665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=5869dda9-7c8d-456f-a512-95c79667"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4927",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4927"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4926,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "sha256": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "description": "1 instance changed",
    "reported_at": 1782971159.2597198,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/0867cd49ecfb556eb662e1942c500f0d4fc50bf4...ca386e022a6857ad4ea8cfcc765a574452555ac7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e5dd9397-3db0-4786-b854-e938e315"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4926",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4926"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4926,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:027b85e@sha256:38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
    "sha256": "38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
    "description": "3 instances changed",
    "reported_at": 1782971159.2597198,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a...027b85ebccec65b35b0ba0e4da196b7738d4ba82",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=df97a2c6-d2eb-4465-b276-084bd7a7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4926",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4926"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4926,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
    "sha256": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
    "description": "3 instances changed",
    "reported_at": 1782971159.2597198,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/84d9fee0524e602c1d7529bf18279fc78486bdb0...552f300213a65ee0c8c773474d75b26b2d723575",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=3136a438-a076-4242-8e2f-d6595cfe"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4926",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4926"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4926,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "sha256": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
    "description": "1 instance changed",
    "reported_at": 1782971159.2597198,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/6960ff7cc90425329e6def0adae4d5129dca9997...5812bb564e572c9e33aef2789d2687f1a999a687",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=b0c5a0c3-e982-43a4-b906-de850bf4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4926",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4926"
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

