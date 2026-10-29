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
    "snapshot_index": 5544,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
    "sha256": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
    "description": "1 instance changed",
    "reported_at": 1793259778.583906,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=0e7140db-7422-4ea7-954b-fa840a0a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5544",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5544"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5544,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
    "sha256": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
    "description": "3 instances changed",
    "reported_at": 1793259778.583906,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/83553f52e8de8a9766a64fced8fbfb3cd32318a3...fd680a809587fa6e4071fe874d63192f65f251c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=05fa6306-e46c-490f-bda0-8c38d3c0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5544",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5544"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
    "sha256": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=0e7140db-7422-4ea7-954b-fa840a0a"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
    "sha256": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=9134bfd2-d550-4c10-93d3-bbd4f6c4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
    "sha256": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/68636bed4906a15df27ee99e2afddd4377d3867e...9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=4369d9e0-a55a-40ac-aab6-01719a95"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
    "sha256": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5...4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=96424b35-49cc-4dea-9efd-bc7e14c6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
    "sha256": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/c6834ecc2c5b9e5622428f14be5c4de3b49dde46...38062992c27234fbb3784c9730b0f7229a2dda66",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df?artifact_id=a83de5fc-80e0-4742-8b87-3aea8a0f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
    "sha256": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173...aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de?artifact_id=e3e7a070-c230-46ac-a216-a4e6661f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
    "sha256": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/8442c1b837d6dca9e349a6c3401437f11e6bd9f0...9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=9b49ae7a-d0e1-4e04-ba77-ec89b9dd"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
    "sha256": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
    "description": "3 instances changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e...bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=f418eb3f-416b-4def-861c-aaebadf6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
    "sha256": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/270c3c87aecb0e008e90879be753e67983e692c8...190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=f30b0455-6aa8-425e-ba1d-2ae2b497"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
    "sha256": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
    "description": "3 instances changed",
    "reported_at": 1793259718.4603333,
    "pipeline": "web-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "web-ci",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/83553f52e8de8a9766a64fced8fbfb3cd32318a3...fd680a809587fa6e4071fe874d63192f65f251c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=05fa6306-e46c-490f-bda0-8c38d3c0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5543,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
    "sha256": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
    "description": "1 instance changed",
    "reported_at": 1793259718.4603333,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/edb38e8b2a233345645ee339cdc9ed7b3b74fcd2...573bc849ed628bf0230b94be375122cf51b3f48f",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203?artifact_id=e65afc99-800c-4810-bf65-f0954120"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5543",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5543"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5542,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
    "sha256": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
    "description": "1 instance changed",
    "reported_at": 1793259658.404256,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/68636bed4906a15df27ee99e2afddd4377d3867e...9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=4369d9e0-a55a-40ac-aab6-01719a95"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5542",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5542"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5542,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
    "sha256": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
    "description": "1 instance changed",
    "reported_at": 1793259658.404256,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5...4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=96424b35-49cc-4dea-9efd-bc7e14c6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5542",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5542"
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

