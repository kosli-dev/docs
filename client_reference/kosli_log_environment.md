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
|    -h, --help  |  help for environment  |
|    -i, --interval string  |  [optional] Expression to define specified snapshots range.  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        --page int  |  [defaulted] The page number of a response. (default 1)  |
|    -n, --page-limit int  |  [defaulted] The number of elements per page. (default 15)  |
|        --repo strings  |  [optional] The name of a git repo as it is registered in Kosli. e.g kosli-dev/cli  |
|        --reverse  |  [defaulted] Reverse the order of output list.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout.  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |
|    -q, --quiet  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both --quiet and --debug are set, --debug wins.  |


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
    "snapshot_index": 4404,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "sha256": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778502898.4686973,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/632127a7f162ad1ac02305a2940888264034364b...a6ece2b597888f7ab149759daadda08e3afab0c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=1281066d-38ba-432c-92c2-f3d7003e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4404",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4404"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4403,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
    "sha256": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778502838.4516687,
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
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/a6ece2b597888f7ab149759daadda08e3afab0c1...89b113a1531ed1a88cd466d67a8e107ee88672d4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=a745299f-f8f0-4b68-89b3-173aafe8"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4403",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4403"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4402,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
    "sha256": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778502598.3867438,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/92c0996cd9ae7642eb0769f928abe6cb6c391751...cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed?artifact_id=680cd12d-e9b5-4a2a-8abf-1e75a370"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4402",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4402"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
    "sha256": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778502538.6356485,
    "pipeline": "creator-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "creator-ci",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c...b3152a10de1f36b7dbe2818c0918af06fd3aca61",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=36be2954-6f6d-4a7b-b705-fc3e7466"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "sha256": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778502538.6356485,
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
        "flow_name": "snyk-vulns-archived-at-1776759327",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/f89742ee5f0477a7c729bfdeadc84dcbd70492b2...65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=c5d209a3-9139-4f5b-a553-c6351091"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
    "sha256": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1778502538.6356485,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd...b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=8a73edbf-8c34-4371-a0a1-001dffd2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
    "sha256": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
    "description": "3 instances started running (from 0 to 3)",
    "reported_at": 1778502538.6356485,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/1999d1303424879336b04fa3310256554aa6cfa6...c175db1be81803bc9587ccb3175723d450468ab0",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6?artifact_id=088ed687-0522-4341-9042-0bd99b1f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
    "sha256": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778502538.6356485,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
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
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/b1ce55beb190397c80d3ba0536f6b97bb5f468f6...498bf29ef05ecc0986874ca8a8949fd2a39ad269",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=6d83c4b2-39dd-4eba-9f37-dcdda1d9"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
    "sha256": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1778502538.6356485,
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
    "code_diff": "https://github.com/cyber-dojo/saver/compare/cfb0d52610ab73011f325c4bb5bf0b54fb51031c...af7241f29969110655505267dc8ce7f9644fbf6a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=dfd55d86-8f32-4b13-94a9-99033f50"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4401,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "sha256": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "description": "3 instances stopped running (from 3 to 0)",
    "reported_at": 1778502538.6356485,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98...1999d1303424879336b04fa3310256554aa6cfa6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=359b4539-989d-48f5-88eb-8a553baf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4401",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4401"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4400,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "sha256": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "description": "1 instance changed",
    "reported_at": 1778501398.7131987,
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
        "flow_name": "snyk-vulns-archived-at-1776759327",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
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
    "code_diff": "https://gitlab.com/cyber-dojo/creator/-/compare/f89742ee5f0477a7c729bfdeadc84dcbd70492b2...65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=c5d209a3-9139-4f5b-a553-c6351091"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4400",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4400"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4399,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
    "sha256": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
    "description": "1 instance changed",
    "reported_at": 1778501338.7537856,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
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
    "code_diff": "https://github.com/cyber-dojo/differ/compare/c9bbaa1eceb4b8bdffa065ea7034de23d3364919...30dffd09c3f896a322c65029247abcea3019c43a",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=046919b1-42dd-47f8-8569-912d0259"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4399",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4399"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4399,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
    "sha256": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
    "description": "1 instance changed",
    "reported_at": 1778501338.7537856,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/92c0996cd9ae7642eb0769f928abe6cb6c391751...cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed?artifact_id=680cd12d-e9b5-4a2a-8abf-1e75a370"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4399",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4399"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4399,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
    "sha256": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
    "description": "1 instance changed",
    "reported_at": 1778501338.7537856,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
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
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/8adb92a471e3f5caf65481155d45121a865b67a7...9dd6c657bc443c45c19e81165ff99286e237cfe3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=f1d404d2-81f9-4f7a-9a01-9742e3e2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4399",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4399"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4399,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "sha256": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "description": "3 instances changed",
    "reported_at": 1778501338.7537856,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98...1999d1303424879336b04fa3310256554aa6cfa6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=359b4539-989d-48f5-88eb-8a553baf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4399",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4399"
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

