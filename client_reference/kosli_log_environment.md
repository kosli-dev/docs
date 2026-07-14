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
    "snapshot_index": 5007,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
    "sha256": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1784014258.5595071,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/97ebee56e01ca3af95bfcae0c7c328eee8c56865...8d345854efbb1063d7546ef988dd771ed5445116",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f?artifact_id=022a327b-df37-4f2c-94f2-2f7c3fd0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5007",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5007"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5006,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5195398@sha256:f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459",
    "sha256": "f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1784014198.37591,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/web/compare/8d345854efbb1063d7546ef988dd771ed5445116...51953982aab0dae2f7ff684ebb4a76e5c132e777",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459?artifact_id=231d4126-b8bb-4db6-80e9-77922477"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5006",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5006"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5005,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "sha256": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "description": "3 instances changed",
    "reported_at": 1784003998.4861574,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5005",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5005"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5004,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
    "sha256": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
    "description": "1 instance changed",
    "reported_at": 1784003938.5445926,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/26dcd06257a4bb00d594dbb5de05eefbb7b20379...8beff9901ac67acb7afcab3408106208571a1124",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=ece4f8ca-6c19-4ca5-a482-dd4af708"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5004",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5004"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5004,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "sha256": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
    "description": "3 instances changed",
    "reported_at": 1784003938.5445926,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5004",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5004"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5003,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "sha256": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "description": "1 instance changed",
    "reported_at": 1784003878.547647,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5003",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5003"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5003,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "sha256": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
    "description": "1 instance changed",
    "reported_at": 1784003878.547647,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/80b913e9f88902428a3567f75165d8b9d73b561a...804f248d832dc34e564507b009c246dfb4f0c657",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=0e55e1be-fab1-475b-8aaa-b45ca6e2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5003",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5003"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5002,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
    "sha256": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
    "description": "1 instance changed",
    "reported_at": 1784003818.431919,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/cbf0063e279351ffb201b39296e9bfe892dc772f...9b711df71c76a1f293c2525ace65778036591baf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=0d448ff6-ac85-47bb-8d86-9dfab222"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5002",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5002"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5002,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e59370c@sha256:48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
    "sha256": "48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
    "description": "1 instance changed",
    "reported_at": 1784003818.431919,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/b8e6c03975a5701e3e8d198549f463989f1a00f4...e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=be95fb64-f609-4b67-b5cb-e0efe36e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5002",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5002"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5002,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "sha256": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
    "description": "1 instance changed",
    "reported_at": 1784003818.431919,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/04e0e14bb8874ab521d35c97d6040133f0d2143a...c6db342472238a7852b6ff31b04f9a6a6099f5cf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=ed104a44-8358-4883-beeb-ac3c8bb7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5002",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5002"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5001,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
    "sha256": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
    "description": "1 instance changed",
    "reported_at": 1784003758.5531633,
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
    "code_diff": "https://github.com/cyber-dojo/creator/compare/6ff6b4c71ab218d39065654bef32839b9226d21f...7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=aeec9b85-1a23-4579-b4a8-dbc98a05"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5001",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5001"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5001,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
    "sha256": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
    "description": "1 instance changed",
    "reported_at": 1784003758.5531633,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/cbf0063e279351ffb201b39296e9bfe892dc772f...9b711df71c76a1f293c2525ace65778036591baf",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=0d448ff6-ac85-47bb-8d86-9dfab222"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5001",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5001"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5001,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "sha256": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
    "description": "1 instance changed",
    "reported_at": 1784003758.5531633,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5001",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5001"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5001,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e59370c@sha256:48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
    "sha256": "48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
    "description": "1 instance changed",
    "reported_at": 1784003758.5531633,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/b8e6c03975a5701e3e8d198549f463989f1a00f4...e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=be95fb64-f609-4b67-b5cb-e0efe36e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5001",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5001"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5001,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
    "sha256": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
    "description": "1 instance changed",
    "reported_at": 1784003758.5531633,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/6d203a85ffda1513db4d86d4e48b1f969bd2f510...e4757683b74df7033c95aa544a7824b395c2f8bb",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=cc7c618f-d22e-4d95-b6f1-cea4fded"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5001",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5001"
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

