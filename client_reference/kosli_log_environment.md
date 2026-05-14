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


## Flags
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for environment  |
|    `-i`, `--interval` string  |  [optional] Expression to define specified snapshots range.  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--repo` strings  |  [optional] The name of a git repo as it is registered in Kosli. e.g kosli-dev/cli  |
|        `--reverse`  |  [defaulted] Reverse the order of output list.  |


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
    "snapshot_index": 4522,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778779378.493324,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4522",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4522"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4521,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778779318.7576406,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4521",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4521"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4520,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778779018.4878175,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4520",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4520"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4519,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778778958.525458,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4519",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4519"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4518,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778778478.4860399,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4518",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4518"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4517,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778778418.643466,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4517",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4517"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4516,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778778178.642939,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4516",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4516"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4515,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778778118.5197313,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4515",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4515"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4514,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778777878.4407866,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4514",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4514"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4513,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778777818.44366,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4513",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4513"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4512,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778777338.4247878,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4512",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4512"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4511,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778777278.5717375,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4511",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4511"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4510,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778776738.3930256,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4510",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4510"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4509,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778776678.696267,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4509",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4509"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4508,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "sha256": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778776438.7363236,
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
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4508",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4508"
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
</AccordionGroup>

