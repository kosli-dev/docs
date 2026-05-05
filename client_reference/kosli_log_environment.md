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
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. 'http://proxy-server-ip:proxy-port'  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


## Live Example

To view a live example of 'kosli log environment' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A  # read-only
kosli log environment aws-prod --output=json
```

<Accordion title="View example output">
```json
[
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4357,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:95ab455@sha256:1eea61094353db37c7ef3e9582e63f3427c5e01fe76b8210db985144d10088cf",
    "sha256": "1eea61094353db37c7ef3e9582e63f3427c5e01fe76b8210db985144d10088cf",
    "description": "1 instance started running (from 0 to 1)",
    "reported_at": 1777956838.5302956,
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
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/a97ed054e38d484a0015cd658f1d593c03ea2a61...95ab455dd7301b20c744f50b1cd015e4396aedce",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/1eea61094353db37c7ef3e9582e63f3427c5e01fe76b8210db985144d10088cf",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/1eea61094353db37c7ef3e9582e63f3427c5e01fe76b8210db985144d10088cf?artifact_id=c6ff1415-5cd1-48d0-a0df-cbcbcc5e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4357",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4357"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4357,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a97ed05@sha256:8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "sha256": "8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "description": "1 instance stopped running (from 1 to 0)",
    "reported_at": 1777956838.5302956,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "exited",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/98e8281ec23d94507d02b8d335b2dd8064e2149b...a97ed054e38d484a0015cd658f1d593c03ea2a61",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e?artifact_id=a62586e6-58ba-4a88-84cf-1d49694f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4357",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4357"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4356,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "sha256": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
    "description": "1 instance changed",
    "reported_at": 1777954558.5092592,
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4356",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4356"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4356,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:a2ffba5@sha256:b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
    "sha256": "b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
    "description": "3 instances changed",
    "reported_at": 1777954558.5092592,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/bcf912346ae0a104698da4560e82d5eb277fc0e9...a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=fe3ed5e5-0ed1-4cb8-8d5a-57d636d7"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4356",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4356"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
    "sha256": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd...b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=8a73edbf-8c34-4371-a0a1-001dffd2"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a97ed05@sha256:8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "sha256": "8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/98e8281ec23d94507d02b8d335b2dd8064e2149b...a97ed054e38d484a0015cd658f1d593c03ea2a61",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e?artifact_id=a62586e6-58ba-4a88-84cf-1d49694f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
    "sha256": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
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
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "sha256": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
    "description": "3 instances changed",
    "reported_at": 1777954498.4239645,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98...1999d1303424879336b04fa3310256554aa6cfa6",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=359b4539-989d-48f5-88eb-8a553baf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:92c0996@sha256:1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
    "sha256": "1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/0b77a6402320cd10c30cf5bbf6486aa1a448443a...92c0996cd9ae7642eb0769f928abe6cb6c391751",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=3666aa1b-a19b-4ab5-a625-fa6afa9d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "sha256": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/632127a7f162ad1ac02305a2940888264034364b...a6ece2b597888f7ab149759daadda08e3afab0c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=1281066d-38ba-432c-92c2-f3d7003e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4355,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
    "sha256": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
    "description": "1 instance changed",
    "reported_at": 1777954498.4239645,
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
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/83ea563b423559eaf750dd680fc2329e59f60e3b...447231c2018bc0690735b4ee110ca46431162fd5",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=98831c77-04a8-4427-9cf8-03950550"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4355",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4355"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4354,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:92c0996@sha256:1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
    "sha256": "1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
    "description": "1 instance changed",
    "reported_at": 1777954438.5998223,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/0b77a6402320cd10c30cf5bbf6486aa1a448443a...92c0996cd9ae7642eb0769f928abe6cb6c391751",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=3666aa1b-a19b-4ab5-a625-fa6afa9d"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4354",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4354"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4354,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a97ed05@sha256:8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "sha256": "8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
    "description": "1 instance changed",
    "reported_at": 1777954438.5998223,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/98e8281ec23d94507d02b8d335b2dd8064e2149b...a97ed054e38d484a0015cd658f1d593c03ea2a61",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8ba20a0fbdc3d234fb0dac28a9865b6ee719906d06229f9f15b2078a3f6f332e?artifact_id=a62586e6-58ba-4a88-84cf-1d49694f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4354",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4354"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4354,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "sha256": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
    "description": "1 instance changed",
    "reported_at": 1777954438.5998223,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/632127a7f162ad1ac02305a2940888264034364b...a6ece2b597888f7ab149759daadda08e3afab0c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=1281066d-38ba-432c-92c2-f3d7003e"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4354",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4354"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4354,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
    "sha256": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
    "description": "1 instance changed",
    "reported_at": 1777954438.5998223,
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
        "flow_name": "snyk-vulns-aws-prod",
        "deployments": null
      },
      {
        "flow_name": "snyk-vulns-aws-beta",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/83ea563b423559eaf750dd680fc2329e59f60e3b...447231c2018bc0690735b4ee110ca46431162fd5",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=98831c77-04a8-4427-9cf8-03950550"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4354",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4354"
      }
    }
  }
]
```
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

