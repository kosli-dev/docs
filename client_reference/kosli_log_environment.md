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
    "snapshot_index": 4608,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
    "sha256": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1779364918.4839022,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/eca92b4633994c93802e4f4c36ab50ba787f4c8c...8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a?artifact_id=eab81c14-3820-4a0c-a8d3-65562e1e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4608",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4608"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4608,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
    "sha256": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1779364918.4839022,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/ff9225b7868a17e9c98f3a714763ebd78bbc9019...eca92b4633994c93802e4f4c36ab50ba787f4c8c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d?artifact_id=78130d2f-c749-4273-b6a4-5b81264b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4608",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4608"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4607,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
    "sha256": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361978.695172,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/82ae3aee8f6b6c145cf50f6565815f1b125fbc6a...3f0c4e5a2578865b68f0486f0284f52013a038f6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473?artifact_id=c2b4a1d5-f3c2-45c9-bd1d-a439dd00"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4607",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4607"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4606,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
    "sha256": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1779361918.6583393,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/ff9225b7868a17e9c98f3a714763ebd78bbc9019...eca92b4633994c93802e4f4c36ab50ba787f4c8c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d?artifact_id=78130d2f-c749-4273-b6a4-5b81264b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4606",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4606"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4606,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ff9225b@sha256:1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
    "sha256": "1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1779361918.6583393,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef...ff9225b7868a17e9c98f3a714763ebd78bbc9019",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57?artifact_id=8df67ba3-b525-4b0d-88a4-2628061d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4606",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4606"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4606,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
    "sha256": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1779361918.6583393,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/3f0c4e5a2578865b68f0486f0284f52013a038f6...a300e4c15cff321ef952a60bbc3a4729772a2419",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=c8203f7c-be6e-49c7-8386-755b1efa"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4606",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4606"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4605,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aad3b92@sha256:24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
    "sha256": "24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361678.5192397,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/web/compare/4e30f2c13e5aedc4814360186742a689aba65f64...aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec?artifact_id=7cb7e8b4-28db-4b2b-95c6-a008cde2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4605",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4605"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4604,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:39b850a@sha256:fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
    "sha256": "fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361618.3886578,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/42c8bafd9e5f939070a775e87e86466f6e7497a8...39b850a3d527c047dab963bbaa396a14b644ffa1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9?artifact_id=fb74f297-ccd2-4ab3-8deb-b7d559ba"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4604",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4604"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4604,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:09cbd7a@sha256:a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
    "sha256": "a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361618.3886578,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/fd71a71146c5f8d0f83f2599b6acc4cd2664753c...09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9?artifact_id=6ab61b78-371d-4a85-90d0-3020ef08"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4604",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4604"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4604,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:02db0da@sha256:3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
    "sha256": "3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361618.3886578,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/0e3bf9403ab01fd96b7c15e3238d5426b39acbb6...02db0daf31f1a59d795a53b8f31c1e33e26e2475",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c?artifact_id=f3671bf7-728e-4b39-bfe8-c1643590"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4604",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4604"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4604,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:a644975@sha256:80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
    "sha256": "80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1779361618.3886578,
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
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/49dc284ab2db29817282ac6c7ecd7e1e643a9c23...a644975af4c0f7aa595bea651b4d9846cb747cd1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3?artifact_id=9c0ecdc2-a8cb-4030-a16a-4c74899c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4604",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4604"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4603,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
    "sha256": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1779361558.694262,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/39b850a3d527c047dab963bbaa396a14b644ffa1...e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534?artifact_id=1ab21e30-b72a-4b81-96f2-2c88ca7c"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4603",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4603"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4603,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
    "sha256": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
    "description": "2 instances started running (from 0 to 2)",
    "reported_at": 1779361558.694262,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/aad3b92b0be2cc2d47af89ec04266ae4a7f4617b...a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4?artifact_id=b745e3de-b475-495d-8c9d-f2e2c9d6"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4603",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4603"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4603,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
    "sha256": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1779361558.694262,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/a644975af4c0f7aa595bea651b4d9846cb747cd1...545cccbc91f4030fb4004421e1076bd7c2abbc93",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=e5eb4b27-0e03-408b-983c-52631c22"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4603",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4603"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4603,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
    "sha256": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1779361558.694262,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "started-compliant",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/02db0daf31f1a59d795a53b8f31c1e33e26e2475...16d155bdd120fe5a926504069dd18a98b8275fa8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=ca3a337f-0625-4fa1-a39e-f5e9fcf1"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4603",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4603"
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

