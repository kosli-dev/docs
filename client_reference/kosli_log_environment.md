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
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
    "sha256": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/spooler/compare/28636f69be43a7676d61db98b086eaff507d6e9c...afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/spooler-ci/fingerprint/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
        "html": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f?artifact_id=bf8d791d-6bcd-4297-b745-328db4df"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
    "sha256": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/5799bb754b5d0fa5469650050d1e0402e9297ed9...b543342fa06b0ef415950745fddfff5a85f9d80d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa?artifact_id=02ed2b7d-e77e-4543-946c-7f0eb3eb"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
    "sha256": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/009779d876c8b977e993fcf9ed1187e9c3bcdcc8...68636bed4906a15df27ee99e2afddd4377d3867e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8?artifact_id=3a46596a-b98c-4c2f-a72a-d8452f32"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
    "sha256": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/239086385550e2c369fd3aa1f656b56f362db8f7...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=6923c594-deee-4b7c-83e9-3165a9ed"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
    "sha256": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2...270c3c87aecb0e008e90879be753e67983e692c8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93?artifact_id=93be9d1e-6eff-4ff5-a077-ed2baf30"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:842bdad@sha256:807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
    "sha256": "807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/9b498758459dd636ff7dbca04367de3f547454f0...842bdad4a2fc94d0acfe996d059972b50037b304",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463?artifact_id=ec8bd3c0-ab13-4965-86f8-f877f334"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b17fe49@sha256:896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
    "sha256": "896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/69e4ccffb7596125f4bb09886437ca3dee4ac0cf...b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f?artifact_id=7b471a07-4b64-4ba5-a309-633e3281"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
    "sha256": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
    "description": "3 instances changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/376f811ff50beefefbfda03047b45ba8b62fccc0...ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b?artifact_id=c0267819-47af-42c9-bb43-4470c04f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
    "sha256": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/9c8c9cdb74d9aeeda67bae0f4063089bebc99efe...8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a?artifact_id=87445ff6-7ec9-4337-bf43-0e9b796b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
    "sha256": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
    "description": "3 instances changed",
    "reported_at": 1792045498.5715408,
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
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...83553f52e8de8a9766a64fced8fbfb3cd32318a3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=bb10f025-89b9-463a-9857-0a4a205b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5483,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
    "sha256": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
    "description": "1 instance changed",
    "reported_at": 1792045498.5715408,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/3b4ef042cde981a0668dec70ed3137041a51cbe6...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=349ebdb8-fe2c-41fb-a05d-49675a91"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5483",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5483"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5482,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
    "sha256": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
    "description": "1 instance changed",
    "reported_at": 1791960178.6282132,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/5799bb754b5d0fa5469650050d1e0402e9297ed9...b543342fa06b0ef415950745fddfff5a85f9d80d",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa?artifact_id=02ed2b7d-e77e-4543-946c-7f0eb3eb"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5482",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5482"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5482,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
    "sha256": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
    "description": "1 instance changed",
    "reported_at": 1791960178.6282132,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/239086385550e2c369fd3aa1f656b56f362db8f7...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=6923c594-deee-4b7c-83e9-3165a9ed"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5482",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5482"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5482,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
    "sha256": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
    "description": "3 instances changed",
    "reported_at": 1791960178.6282132,
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
    "code_diff": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...83553f52e8de8a9766a64fced8fbfb3cd32318a3",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=bb10f025-89b9-463a-9857-0a4a205b"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5482",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5482"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 5482,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
    "sha256": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
    "description": "1 instance changed",
    "reported_at": 1791960178.6282132,
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
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "changed",
    "code_diff": "https://github.com/cyber-dojo/web/compare/3b4ef042cde981a0668dec70ed3137041a51cbe6...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=349ebdb8-fe2c-41fb-a05d-49675a91"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/5482",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5482"
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

