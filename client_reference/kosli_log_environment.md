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
    "snapshot_index": 4814,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "sha256": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "description": "3 instances changed",
    "reported_at": 1782112078.6734855,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/9cc2a80e1306376b88039715dfdcfc161a0e3904...c248c8e2175307f6906e4a016d09b21d177923bd",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=2596689f-18f2-4c1b-b176-64e8b46f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4814",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4814"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4813,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "sha256": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "description": "1 instance changed",
    "reported_at": 1782112018.5396478,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/a288de54e3751244517d5e04fc73622e5363257d...34f14b6fc5d87ff95426046716ec8a09141c13a7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=bafbb0d0-e794-4acf-bdf5-81262268"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4813",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4813"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4813,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "sha256": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "description": "3 instances changed",
    "reported_at": 1782112018.5396478,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/9cc2a80e1306376b88039715dfdcfc161a0e3904...c248c8e2175307f6906e4a016d09b21d177923bd",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=2596689f-18f2-4c1b-b176-64e8b46f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4813",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4813"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4813,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
    "sha256": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
    "description": "1 instance changed",
    "reported_at": 1782112018.5396478,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/c1cd97e11606d0a705df6619424c9ad8b07a57ca...7eeaac4c57e26887e4d027aa3c815bc2f214f934",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f?artifact_id=216380b8-1166-4cd0-a052-709e8f0f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4813",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4813"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4812,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "sha256": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "description": "1 instance changed",
    "reported_at": 1782111958.6034238,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/87f560f87fb2bc242ee5c58d74d0e209d71cd338...ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ff697a42-4717-4727-b9de-e3d77870"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4812",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4812"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4812,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "sha256": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "description": "1 instance changed",
    "reported_at": 1782111958.6034238,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/981dcfc34f584d46afb46b217b47ce68f2f14a08...3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=c25bc6ba-cbfd-4ad5-b5ab-d4bca4e9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4812",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4812"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
    "sha256": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/6b5c1598cc13c388a0fec71852e6b03bf0696e0b...843d6556ec718da1a1f51ce906c8c5bd6366d691",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b?artifact_id=a467f7de-b8f1-45fe-a7aa-3479ee90"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "sha256": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/87f560f87fb2bc242ee5c58d74d0e209d71cd338...ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ff697a42-4717-4727-b9de-e3d77870"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
    "sha256": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
    "description": "3 instances changed",
    "reported_at": 1782111898.6284199,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c...47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=87b6ce7f-f34c-485b-8d6f-15a460ab"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "sha256": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/a288de54e3751244517d5e04fc73622e5363257d...34f14b6fc5d87ff95426046716ec8a09141c13a7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=bafbb0d0-e794-4acf-bdf5-81262268"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
    "sha256": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d...11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443?artifact_id=6e7dfa64-c5c1-4a47-98f2-5e61c7b4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "sha256": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/981dcfc34f584d46afb46b217b47ce68f2f14a08...3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=c25bc6ba-cbfd-4ad5-b5ab-d4bca4e9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
    "sha256": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600...fbae360261d949b25a66a927921e757d4d064543",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=6df95847-0740-4e9e-8795-c960e47b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
    "sha256": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/c1cd97e11606d0a705df6619424c9ad8b07a57ca...7eeaac4c57e26887e4d027aa3c815bc2f214f934",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f?artifact_id=216380b8-1166-4cd0-a052-709e8f0f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4811,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:6350271@sha256:d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
    "sha256": "d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
    "description": "1 instance changed",
    "reported_at": 1782111898.6284199,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/706526874659341458da5bb21903a6423c0a5a29...635027125d65a253a9c98bfd97d22cb3abbefa5a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb?artifact_id=4c204b40-ff5f-45b1-843a-4b42fc65"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4811",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4811"
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

