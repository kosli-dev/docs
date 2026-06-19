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
    "snapshot_index": 4798,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
    "sha256": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862838.595731,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/68d791f93dc161fd8dba63e49b7fe9f909cbe758...8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=bf5cf82a-8413-437c-97b0-1977ba2c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4798",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4798"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4797,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
    "sha256": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1781862778.4942248,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600...fbae360261d949b25a66a927921e757d4d064543",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=6df95847-0740-4e9e-8795-c960e47b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4797",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4797"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4796,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
    "sha256": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862658.6275043,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bc5fbc14361ce7a6281b6110049d90a03f69d786...9cc2a80e1306376b88039715dfdcfc161a0e3904",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=73a8e588-a383-4eb5-a88c-a1db6160"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4796",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4796"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4795,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
    "sha256": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862598.434665,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/76355112651c4ee66d6ee47f67e35459616f0dae...b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=4d62c06d-f9a2-4bfb-a8aa-a8d36ab8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4795",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4795"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4795,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
    "sha256": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862598.434665,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/f3c679170776733c60dc485e076b7cb515caa7a4...87f560f87fb2bc242ee5c58d74d0e209d71cd338",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=bd23bb89-f867-46b2-9139-1f7fc8b3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4795",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4795"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4794,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
    "sha256": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1781862538.6870024,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d...11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443?artifact_id=6e7dfa64-c5c1-4a47-98f2-5e61c7b4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4794",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4794"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4794,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "sha256": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
    "description": "2 instances started running (from 0 to 2)",
    "reported_at": 1781862538.6870024,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/9cc2a80e1306376b88039715dfdcfc161a0e3904...c248c8e2175307f6906e4a016d09b21d177923bd",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=2596689f-18f2-4c1b-b176-64e8b46f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4794",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4794"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4794,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "sha256": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1781862538.6870024,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/87f560f87fb2bc242ee5c58d74d0e209d71cd338...ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ff697a42-4717-4727-b9de-e3d77870"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4794",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4794"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
    "sha256": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862478.568137,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/d3e5850912655f2b18a68129f5f3a6480fe305ef...6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=954d759d-077a-4359-b51f-54c7f182"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
    "sha256": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862478.568137,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/43d2a72431124e9fcf47bf866621ba3fd8e7f618...981dcfc34f584d46afb46b217b47ce68f2f14a08",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=03312679-db2a-4f55-a323-7cdb2c89"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
    "sha256": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1781862478.568137,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9513e77858d775950f22173d0afd0634b2ac20b9...7e86fede3e42d573de92fed483559b8317ce2dda",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=8f51b5c2-8561-491c-a91e-248d6452"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "sha256": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1781862478.568137,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/981dcfc34f584d46afb46b217b47ce68f2f14a08...3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=c25bc6ba-cbfd-4ad5-b5ab-d4bca4e9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "sha256": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1781862478.568137,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/8863c10c2c93d3539672e0bf75bd9925f8778564...f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=ed664433-201f-41ac-938b-5931b5f4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
    "sha256": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1781862478.568137,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/web/compare/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c...47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=87b6ce7f-f34c-485b-8d6f-15a460ab"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4793,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c1cd97e@sha256:c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
    "sha256": "c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1781862478.568137,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/7e86fede3e42d573de92fed483559b8317ce2dda...c1cd97e11606d0a705df6619424c9ad8b07a57ca",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe?artifact_id=8064d7d2-d257-43e9-a609-0eb172f5"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4793",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4793"
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

