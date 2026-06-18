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
    "snapshot_index": 4781,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
    "sha256": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
    "description": "3 instances changed",
    "reported_at": 1781596438.4966626,
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
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bc5fbc14361ce7a6281b6110049d90a03f69d786...9cc2a80e1306376b88039715dfdcfc161a0e3904",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=73a8e588-a383-4eb5-a88c-a1db6160"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4781",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4781"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4781,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
    "sha256": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
    "description": "1 instance changed",
    "reported_at": 1781596438.4966626,
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/d3e5850912655f2b18a68129f5f3a6480fe305ef...6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=954d759d-077a-4359-b51f-54c7f182"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4781",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4781"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4780,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "sha256": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "description": "3 instances changed",
    "reported_at": 1781596378.6927845,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/8863c10c2c93d3539672e0bf75bd9925f8778564...f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=ed664433-201f-41ac-938b-5931b5f4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4780",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4780"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4780,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
    "sha256": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
    "description": "1 instance changed",
    "reported_at": 1781596378.6927845,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/f3c679170776733c60dc485e076b7cb515caa7a4...87f560f87fb2bc242ee5c58d74d0e209d71cd338",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=bd23bb89-f867-46b2-9139-1f7fc8b3"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4780",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4780"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4780,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
    "sha256": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
    "description": "1 instance changed",
    "reported_at": 1781596378.6927845,
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
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/76355112651c4ee66d6ee47f67e35459616f0dae...b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=4d62c06d-f9a2-4bfb-a8aa-a8d36ab8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4780",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4780"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4780,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
    "sha256": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
    "description": "1 instance changed",
    "reported_at": 1781596378.6927845,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9513e77858d775950f22173d0afd0634b2ac20b9...7e86fede3e42d573de92fed483559b8317ce2dda",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=8f51b5c2-8561-491c-a91e-248d6452"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4780",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4780"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4779,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
    "sha256": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
    "description": "1 instance changed",
    "reported_at": 1781596318.7251499,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/43d2a72431124e9fcf47bf866621ba3fd8e7f618...981dcfc34f584d46afb46b217b47ce68f2f14a08",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=03312679-db2a-4f55-a323-7cdb2c89"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4779",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4779"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4778,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
    "sha256": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
    "description": "1 instance changed",
    "reported_at": 1781596198.6164858,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/68d791f93dc161fd8dba63e49b7fe9f909cbe758...8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=bf5cf82a-8413-437c-97b0-1977ba2c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4778",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4778"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4778,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "sha256": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "description": "1 instance changed",
    "reported_at": 1781596198.6164858,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4778",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4778"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4778,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "sha256": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "description": "1 instance changed",
    "reported_at": 1781596198.6164858,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/cdaac807f3282bd0bba056d906d5536074297a04...706526874659341458da5bb21903a6423c0a5a29",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=0438395b-a9b0-4ee5-9b30-8cd146d9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4778",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4778"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4777,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "sha256": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "description": "1 instance changed",
    "reported_at": 1781596138.474564,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/cdaac807f3282bd0bba056d906d5536074297a04...706526874659341458da5bb21903a6423c0a5a29",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=0438395b-a9b0-4ee5-9b30-8cd146d9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4777",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4777"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4776,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "sha256": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "description": "1 instance changed",
    "reported_at": 1781596078.5283337,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/a288de54e3751244517d5e04fc73622e5363257d...34f14b6fc5d87ff95426046716ec8a09141c13a7",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=bafbb0d0-e794-4acf-bdf5-81262268"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4776",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4776"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4775,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "sha256": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
    "description": "1 instance changed",
    "reported_at": 1781595178.5604763,
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/cdaac807f3282bd0bba056d906d5536074297a04...706526874659341458da5bb21903a6423c0a5a29",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=0438395b-a9b0-4ee5-9b30-8cd146d9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4775",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4775"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4775,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "sha256": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
    "description": "1 instance changed",
    "reported_at": 1781595178.5604763,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4775",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4775"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4774,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "sha256": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
    "description": "3 instances changed",
    "reported_at": 1781593978.426208,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/8863c10c2c93d3539672e0bf75bd9925f8778564...f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=ed664433-201f-41ac-938b-5931b5f4"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4774",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4774"
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

