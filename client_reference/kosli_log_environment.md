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
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
    "sha256": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/7c4708f675a7717376529273ec32d08cd93f5c26...1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=cba86481-c5e6-4b47-a242-dcbfa57d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "sha256": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/d01bb39495a1356eabe934bef84b92cc964a26f1...e302b99e045f21adf33ac13c793616cc2fb2ba00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=5da69929-83e9-451a-981e-a9b9c9db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
    "sha256": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
    "description": "3 instances changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/4b2bfc038576e2a7648090c4c1289fbc9ebfc481...6131d764b41b449d77e436598c953691d23eaced",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=f11c519e-c14e-41ca-b67a-a45c4c64"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
    "sha256": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/1455947f91ae9264f6cd078ef8fe3f3a0204603a...9047099552a4db3aebbf4187ebf88931b8fec5fb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=a06d8591-02de-464b-ba15-2e7e7158"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
    "sha256": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/99d7b74f39e311d492902ad48dbe97da63f2c687...10ed49777abb7b3c7be0da1bd536c6b44f34533c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=c204e0b1-78db-4898-a6eb-1c6e77e1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
    "sha256": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca...9635c369db243bfccdd50a0f4abd8cae78c5693a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=0faef22c-d2e1-4199-b115-f97f2dce"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
    "sha256": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
    "description": "1 instance changed",
    "reported_at": 1790581078.5249808,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a...cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=1e1ed13b-f217-41b2-9957-9b3eee58"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
    "sha256": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/7c4708f675a7717376529273ec32d08cd93f5c26...1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=cba86481-c5e6-4b47-a242-dcbfa57d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
    "sha256": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/a1af9ed1e38cdf8e447bd9d7de6b97e994876505...8d428aa6c487aacc14f820314ab5749a861f1319",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810?artifact_id=d206f015-1370-48df-9fed-00570e74"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "sha256": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/d01bb39495a1356eabe934bef84b92cc964a26f1...e302b99e045f21adf33ac13c793616cc2fb2ba00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=5da69929-83e9-451a-981e-a9b9c9db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
    "sha256": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
    "description": "3 instances changed",
    "reported_at": 1790580898.5000987,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/4b2bfc038576e2a7648090c4c1289fbc9ebfc481...6131d764b41b449d77e436598c953691d23eaced",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=f11c519e-c14e-41ca-b67a-a45c4c64"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:41b9d61@sha256:5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
    "sha256": "5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/6b20a423d5ce05139d4480e9ce67f40e3eda2e07...41b9d6108dc358821dd12abbc2305e2457aad146",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f?artifact_id=3a766a44-342a-42bb-8cdb-c782b4d4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c267890@sha256:68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
    "sha256": "68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/86c839ee588f393d84a6b9c036478d10bb6f2a2d...c267890b689f43e24679bfe9006ddc390447e7e7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a?artifact_id=4c117940-9594-43bf-b575-42a1cb69"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
    "sha256": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/1455947f91ae9264f6cd078ef8fe3f3a0204603a...9047099552a4db3aebbf4187ebf88931b8fec5fb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=a06d8591-02de-464b-ba15-2e7e7158"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
    "sha256": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
    "description": "1 instance changed",
    "reported_at": 1790580898.5000987,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/99d7b74f39e311d492902ad48dbe97da63f2c687...10ed49777abb7b3c7be0da1bd536c6b44f34533c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=c204e0b1-78db-4898-a6eb-1c6e77e1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5400"
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

