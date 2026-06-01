---
title: "kosli log environment"
beta: false
deprecated: false
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
|        `--reverse`  |  [defaulted] Reverse the order of output list.  |
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
    "snapshot_index": 4663,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
    "sha256": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
    "description": "1 instance changed",
    "reported_at": 1780295698.4615376,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/3f0c4e5a2578865b68f0486f0284f52013a038f6...a300e4c15cff321ef952a60bbc3a4729772a2419",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=c8203f7c-be6e-49c7-8386-755b1efa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4663",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4663"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4663,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
    "sha256": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
    "description": "3 instances changed",
    "reported_at": 1780295698.4615376,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/8ddbce96e5c898779c653c1ac1872fb5643a6bc2...576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=3884ff27-d621-48bf-8c89-3228169b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4663",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4663"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4663,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
    "sha256": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
    "description": "1 instance changed",
    "reported_at": 1780295698.4615376,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/fd9c3f5f40529596ffe8641b379e46bba036cf5e...26438788f75a9a39db985b87100b9b32a2d962a2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=853d1420-fd3e-439b-ab85-549ba34d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4663",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4663"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4663,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
    "sha256": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
    "description": "1 instance changed",
    "reported_at": 1780295698.4615376,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/75e174eb5045e8dd5c72079d2e2032a1488c51ef...f2e8fa718ca3b72527625bd182beb2950bea3a77",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=02347f6a-ae14-4473-879e-7d4c10b7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4663",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4663"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
    "sha256": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
    "description": "1 instance changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38...a11b7588b2d2333e1346f1a2bb100395f11f42d2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=f723473e-93e9-4367-9110-76bbc5a1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "sha256": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "description": "1 instance changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4...3a066186b7fbbcec0130419518c5bb81b50e71db",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=2eb0aee4-1eca-40b7-a914-1f9e9338"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
    "sha256": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
    "description": "3 instances changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847...d9ac74a950cadda60541db9781e9458832ffd6f8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=045a2c84-f7fc-4601-96f5-0f068ec4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
    "sha256": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
    "description": "1 instance changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/a644975af4c0f7aa595bea651b4d9846cb747cd1...545cccbc91f4030fb4004421e1076bd7c2abbc93",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=e5eb4b27-0e03-408b-983c-52631c22"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
    "sha256": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
    "description": "1 instance changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/02db0daf31f1a59d795a53b8f31c1e33e26e2475...16d155bdd120fe5a926504069dd18a98b8275fa8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=ca3a337f-0625-4fa1-a39e-f5e9fcf1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4662,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
    "sha256": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
    "description": "1 instance changed",
    "reported_at": 1780295638.5399928,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/18fb2702a5109248489b8a562399101f803b3d8d...0a839a472d41bf860d1d6dc3ded45ff63144018d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=4fdc2f6b-8933-4edd-959d-0bd53cbf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4662",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4662"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4661,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "sha256": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "description": "1 instance changed",
    "reported_at": 1780207378.4202626,
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4...3a066186b7fbbcec0130419518c5bb81b50e71db",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=2eb0aee4-1eca-40b7-a914-1f9e9338"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4661",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4661"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4660,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
    "sha256": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
    "description": "1 instance changed",
    "reported_at": 1780207258.5312698,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/fd9c3f5f40529596ffe8641b379e46bba036cf5e...26438788f75a9a39db985b87100b9b32a2d962a2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=853d1420-fd3e-439b-ab85-549ba34d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4660",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4660"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4660,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "sha256": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
    "description": "1 instance changed",
    "reported_at": 1780207258.5312698,
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4...3a066186b7fbbcec0130419518c5bb81b50e71db",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=2eb0aee4-1eca-40b7-a914-1f9e9338"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4660",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4660"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4660,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
    "sha256": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
    "description": "3 instances changed",
    "reported_at": 1780207258.5312698,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/8ddbce96e5c898779c653c1ac1872fb5643a6bc2...576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=3884ff27-d621-48bf-8c89-3228169b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4660",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4660"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4660,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
    "sha256": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
    "description": "1 instance changed",
    "reported_at": 1780207258.5312698,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/18fb2702a5109248489b8a562399101f803b3d8d...0a839a472d41bf860d1d6dc3ded45ff63144018d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=4fdc2f6b-8933-4edd-959d-0bd53cbf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4660",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4660"
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

