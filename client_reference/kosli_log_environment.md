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
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:84e986a@sha256:06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
    "sha256": "06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/36f0420f728fe61e44a3ab0043cf9a3d70863cad...84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=a599cb04-5965-46a6-a774-24dc6341"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
    "sha256": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/fb791742054fa28dd89269aac8002ebfd7b3386e...27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=9045bb07-ea42-482f-99c3-4fe5b86f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
    "sha256": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/2b300f450f72006f6a9000aaf9cd04485f1e8095...ff9f292e809801d35246183988b7812826bc2760",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=aa6c0c1d-2d5d-4c98-9f9d-1160dd2f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a357ebd@sha256:28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
    "sha256": "28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/068b3424c7da843a4f2d428d2e4915f33efc4a02...a357ebd85acdd54968fa0192405aaf2e289d27c9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=8e028a8d-a1f2-4732-8663-47012b29"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
    "sha256": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/790d86b66f4d86ab47f5c521daf5039dc8aeef4d...b12a5c9b17023462d13e81381a69c7ef05f84dc2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=2aa23627-9e91-488e-b3ea-e4bf2e22"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
    "sha256": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
    "description": "3 instances changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/5e4b9873df93525c041c386c06e0ab8fc36b6f33...cbe481c4b842f897e4e9e411cd78461a3a12a334",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=41957e62-eaad-48d2-af40-46879efb"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
    "sha256": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/258b6d07d2b28ad5cb2ce6d29934997f72380f1a...f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=aa4300d4-b690-4d71-9596-6af987e1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
    "sha256": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
    "pipeline": "spooler-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "spooler-ci",
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb...90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=6df79438-91a2-4c2b-a945-52fb5218"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5309,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d64d2b1@sha256:c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
    "sha256": "c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
    "description": "1 instance changed",
    "reported_at": 1788256325.6192138,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/83357f112ef5c10b157cb84732c77965cc8ddc48...d64d2b11879179255f11dc991e81fbaf4a040264",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=61384b36-4d32-43f2-8d5d-a72e2e7e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5309",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5308,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
    "sha256": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
    "description": "1 instance changed",
    "reported_at": 1788256258.609352,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/108cccf9bccf9af5d455db66c250480b53cbecc7...bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=11345222-f37a-4f8d-8051-ec26a321"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5308",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5308"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5308,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
    "sha256": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
    "description": "3 instances changed",
    "reported_at": 1788256258.609352,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/976b63e8001ec7441ebc7737ca69f620d47e7ffe...ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=3b03ceaf-96a6-4afa-8aa2-179e5fe9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5308",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5308"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5307,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
    "sha256": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1788256138.680238,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/89019f6d8059406e56fa499b2dec2dbf93f4d5c7...83357f112ef5c10b157cb84732c77965cc8ddc48",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=11539f6a-befb-4b79-9484-fd9f25d3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5307",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5307"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5306,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d64d2b1@sha256:c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
    "sha256": "c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1788256078.451175,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/83357f112ef5c10b157cb84732c77965cc8ddc48...d64d2b11879179255f11dc991e81fbaf4a040264",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=61384b36-4d32-43f2-8d5d-a72e2e7e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5306",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5306"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5305,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:976b63e@sha256:01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
    "sha256": "01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1788255898.5005004,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/d7541d3fb2c548bd68a81f812b5a6c95fcf9a1bd...976b63e8001ec7441ebc7737ca69f620d47e7ffe",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9?artifact_id=e63d6d6b-d7ee-4fad-a66a-32a4ebba"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5305",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5305"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5304,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
    "sha256": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1788255838.4418423,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/10e162d4e1294815375a31121f14d57e13183b34...108cccf9bccf9af5d455db66c250480b53cbecc7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=50b8cff6-1888-4c76-b31a-fdd7a311"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5304",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5304"
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

