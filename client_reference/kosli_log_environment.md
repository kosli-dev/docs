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
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:2fa0324@sha256:1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
    "sha256": "1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/139dc6d316a5e4b66755fecc926f2e25cd5c8208...2fa032402c47885c2fcf8036e2eee07ac73bdc41",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=eea73af9-c6cf-45f6-8ab3-7181c587"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
    "sha256": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/ae0c2f039480061d958cc007bc4c78e5b0f36a83...fc6b09be0518fbf8ab76815cb85b1745631e3659",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=329017a5-5366-400d-928a-193ea961"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
    "sha256": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/f7fd6b78302ad399252990b0b81f54d7416a402f...6d203a85ffda1513db4d86d4e48b1f969bd2f510",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=87705eca-ac37-4632-93de-c4f63539"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
    "sha256": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/17f61f83683a52ec1b9040127da582affb70e997...80b913e9f88902428a3567f75165d8b9d73b561a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=1f5af7a4-2ab5-4c78-982c-afb9c2b1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
    "sha256": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/9d1887776497e501bc8dcd46e508488bf5c8b0c8...26dcd06257a4bb00d594dbb5de05eefbb7b20379",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=494ad51d-feff-4795-9fec-f2a8b953"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
    "sha256": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
    "description": "3 instances changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/fbe04c6016bd7822a9b0b948043614186787194f...97ebee56e01ca3af95bfcae0c7c328eee8c56865",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=f065965e-194b-43a5-a688-00797359"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
    "sha256": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/a6e433a6fd3eb29c499b75310756420864b6c346...665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=5869dda9-7c8d-456f-a512-95c79667"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
    "sha256": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/c174ef247b1efb95812373fde2a8e8db3a9ede03...6ff6b4c71ab218d39065654bef32839b9226d21f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=26dd06bd-0d63-4775-a3d1-db332cf0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4945,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
    "sha256": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
    "description": "1 instance changed",
    "reported_at": 1783079338.7114732,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/ca386e022a6857ad4ea8cfcc765a574452555ac7...04e0e14bb8874ab521d35c97d6040133f0d2143a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=651b0c78-5926-41b5-ba5b-9aa87601"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4945",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4945"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4944,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
    "sha256": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1783075918.6314435,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/c174ef247b1efb95812373fde2a8e8db3a9ede03...6ff6b4c71ab218d39065654bef32839b9226d21f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=26dd06bd-0d63-4775-a3d1-db332cf0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4944",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4944"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4944,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:c174ef2@sha256:8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
    "sha256": "8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1783075918.6314435,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/2a3119f72fa7bf62bbc83a3d48266120085d03ab...c174ef247b1efb95812373fde2a8e8db3a9ede03",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005?artifact_id=97ef3680-a0d7-4f26-8132-ececb813"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4944",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4944"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4943,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "sha256": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1783075678.7158587,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/0867cd49ecfb556eb662e1942c500f0d4fc50bf4...ca386e022a6857ad4ea8cfcc765a574452555ac7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e5dd9397-3db0-4786-b854-e938e315"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4943",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4943"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4943,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fbe04c6@sha256:5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
    "sha256": "5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1783075678.7158587,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/web/compare/027b85ebccec65b35b0ba0e4da196b7738d4ba82...fbe04c6016bd7822a9b0b948043614186787194f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc?artifact_id=3f4633dc-937f-4b16-a7f2-54a06b45"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4943",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4943"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4943,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f7fd6b7@sha256:746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
    "sha256": "746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1783075678.7158587,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/df9af0c9a2a81ed7bfc429979121b8310bbe7138...f7fd6b78302ad399252990b0b81f54d7416a402f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115?artifact_id=d418a6ca-5e6b-4084-adbb-23fb155a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4943",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4943"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4942,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
    "sha256": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1783075618.6971846,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/ca386e022a6857ad4ea8cfcc765a574452555ac7...04e0e14bb8874ab521d35c97d6040133f0d2143a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=651b0c78-5926-41b5-ba5b-9aa87601"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4942",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4942"
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

