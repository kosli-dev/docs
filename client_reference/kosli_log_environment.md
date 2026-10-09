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
    "snapshot_index": 5440,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "sha256": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "description": "1 instance changed",
    "reported_at": 1791532978.4470391,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/d01bb39495a1356eabe934bef84b92cc964a26f1...e302b99e045f21adf33ac13c793616cc2fb2ba00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=5da69929-83e9-451a-981e-a9b9c9db"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5440",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5440"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5440,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7a96f63@sha256:57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
    "sha256": "57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
    "description": "3 instances changed",
    "reported_at": 1791532978.4470391,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/6131d764b41b449d77e436598c953691d23eaced...7a96f6335ac05b814cfed0947bed40e29fb14c92",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=143f3ad8-2fab-4f18-ae17-88fa64b1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5440",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5440"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5440,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
    "sha256": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
    "description": "3 instances changed",
    "reported_at": 1791532978.4470391,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/5bdfa1df3baee4124759dcc71a617174e11ed51f...239086385550e2c369fd3aa1f656b56f362db8f7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=8c798531-5ed7-4c2d-9c6d-ec444dd8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5440",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5440"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5440,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2390863@sha256:a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
    "sha256": "a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
    "description": "1 instance changed",
    "reported_at": 1791532978.4470391,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/10ed49777abb7b3c7be0da1bd536c6b44f34533c...239086385550e2c369fd3aa1f656b56f362db8f7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=de08f569-3531-4bc6-8567-47fbbef9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5440",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5440"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3fb02b6@sha256:3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
    "sha256": "3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/c415496d0e35cbca51c55d0401c141c982a8d711...3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=9e147c56-48a1-4d72-9a46-6d20397a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c5dd4fa@sha256:5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
    "sha256": "5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9635c369db243bfccdd50a0f4abd8cae78c5693a...c5dd4faa2f40a6a85afceae4565a43a6df553845",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=834cb0b3-828e-4fb3-9d65-fb130696"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
    "sha256": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
    "description": "3 instances changed",
    "reported_at": 1791532918.396811,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/5bdfa1df3baee4124759dcc71a617174e11ed51f...239086385550e2c369fd3aa1f656b56f362db8f7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=8c798531-5ed7-4c2d-9c6d-ec444dd8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
    "sha256": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/41b9d6108dc358821dd12abbc2305e2457aad146...239086385550e2c369fd3aa1f656b56f362db8f7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=53075f10-16cd-40aa-941c-0e9a14ad"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9b49875@sha256:b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
    "sha256": "b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/8d428aa6c487aacc14f820314ab5749a861f1319...9b498758459dd636ff7dbca04367de3f547454f0",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=0b1dd4aa-371f-41db-9dc9-ca52d3a3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
    "sha256": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e...28636f69be43a7676d61db98b086eaff507d6e9c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=bf6bf5b8-e617-4938-acac-ced1cc03"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8e32bc0@sha256:efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
    "sha256": "efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4...8e32bc009dd16087e5160d309a9ce4303b7d895f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=e033c82e-2b65-400f-8656-ca4fa6cb"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5439,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
    "sha256": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
    "description": "1 instance changed",
    "reported_at": 1791532918.396811,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/9047099552a4db3aebbf4187ebf88931b8fec5fb...69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=7bb1f0f7-24cd-4f5c-a6aa-04828949"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5439",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5439"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5438,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "sha256": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
    "description": "1 instance changed",
    "reported_at": 1791446518.4396853,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5438",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5438"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5438,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3fb02b6@sha256:3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
    "sha256": "3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
    "description": "1 instance changed",
    "reported_at": 1791446518.4396853,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/c415496d0e35cbca51c55d0401c141c982a8d711...3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=9e147c56-48a1-4d72-9a46-6d20397a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5438",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5438"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5438,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7a96f63@sha256:57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
    "sha256": "57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
    "description": "3 instances changed",
    "reported_at": 1791446518.4396853,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/6131d764b41b449d77e436598c953691d23eaced...7a96f6335ac05b814cfed0947bed40e29fb14c92",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=143f3ad8-2fab-4f18-ae17-88fa64b1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5438",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5438"
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

