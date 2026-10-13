---
title: "kosli diff snapshots"
description: "Diff environment snapshots.  "
---

## Synopsis

```shell
kosli diff snapshots SNAPPISH_1 SNAPPISH_2 [flags]
```

Diff environment snapshots.  
Specify SNAPPISH_1 and SNAPPISH_2 by:
- environmentName
    - the latest snapshot for environmentName, at the time of the request
    - e.g., **prod**
- environmentName#N
    - the Nth snapshot, counting from 1
    - e.g., **prod#42**
- environmentName~N
    - the Nth snapshot behind the latest, at the time of the request
    - e.g., **prod~5**
- environmentName@\{YYYY-MM-DDTHH:MM:SS\}
    - the snapshot at specific moment in time in UTC
    - e.g., **prod@\{2023-10-02T12:00:00\}**
- environmentName@\{N.`hours|days|weeks|months`.ago\}
    - the snapshot at a time relative to the time of the request
    - e.g., **prod@\{2.hours.ago\}**


## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshots |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `-u`, `--show-unchanged` | bool | [defaulted] Show the unchanged artifacts present in both snapshots within the diff output. |


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

To view a live example of 'kosli diff snapshots' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli diff snapshots aws-beta aws-prod --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
{
  "snappish1": {
    "snapshot_id": "aws-beta#8716",
    "artifacts": [
      {
        "fingerprint": "077acb1cee6e27ab5b2bbbc3f22c4959d99901a560d2d17e064f6245eb6e2f0f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:50fd199@sha256:077acb1cee6e27ab5b2bbbc3f22c4959d99901a560d2d17e064f6245eb6e2f0f",
        "most_recent_timestamp": 1791805272,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/50fd199655303bfa344546c4dc0bd8ca67edac95",
        "instance_count": 1
      },
      {
        "fingerprint": "19ec5fa8d3a1d4140f41ec9ce85fce6ff45e9d670800c370e1c2f30200f94e4f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:3b59027@sha256:19ec5fa8d3a1d4140f41ec9ce85fce6ff45e9d670800c370e1c2f30200f94e4f",
        "most_recent_timestamp": 1791659761,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/3b59027fd20dcec38c72ef3aa04f4bfe3e8423f5",
        "instance_count": 1
      },
      {
        "fingerprint": "1fefe489906242ccf8d86fbbb213f9a322381221abddaca2501a38bfcbffd053",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:383e3a8@sha256:1fefe489906242ccf8d86fbbb213f9a322381221abddaca2501a38bfcbffd053",
        "most_recent_timestamp": 1791808475,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/383e3a8fb52c3122e7d819f35a6a1f3da2c34817",
        "instance_count": 1
      },
      {
        "fingerprint": "3a74612ac429c984212aa88a7029c018548825b219432fadbe32dbe9c2b3896e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:f988f2f@sha256:3a74612ac429c984212aa88a7029c018548825b219432fadbe32dbe9c2b3896e",
        "most_recent_timestamp": 1791659697,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/f988f2fc03966492f54b1a58b78c66b221609604",
        "instance_count": 1
      },
      {
        "fingerprint": "40423324f7159a96fddbe0b1d19f202cee7d730c1409d94fe58f11d41ba95783",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:76ab738@sha256:40423324f7159a96fddbe0b1d19f202cee7d730c1409d94fe58f11d41ba95783",
        "most_recent_timestamp": 1791653158,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/76ab7386c31b97d9ff7985663cb85fa7a7048359",
        "instance_count": 1
      },
      {
        "fingerprint": "5998101c453c93fb5122ada77c16a0013e0b5cf3dca00683236ed07aff1514c0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:221006e@sha256:5998101c453c93fb5122ada77c16a0013e0b5cf3dca00683236ed07aff1514c0",
        "most_recent_timestamp": 1791805688,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/221006eb9aaf720665a0014a8cbcc8efe7c180a5",
        "instance_count": 3
      },
      {
        "fingerprint": "69b1a9a10599734f7733def9dee3f3a207007220a49d7971f291d825e44fe1be",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:eb9f90d@sha256:69b1a9a10599734f7733def9dee3f3a207007220a49d7971f291d825e44fe1be",
        "most_recent_timestamp": 1791786929,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/eb9f90d8a22b94845fddb23949fad738cfb6e21f",
        "instance_count": 1
      },
      {
        "fingerprint": "9b08067c8e91b5e6703d99884207863d7f6faeb29b17a9701c98612ec0025eeb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2ceef98@sha256:9b08067c8e91b5e6703d99884207863d7f6faeb29b17a9701c98612ec0025eeb",
        "most_recent_timestamp": 1791663982,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/2ceef988c9fc3078310ee4547410de56d4c975c5",
        "instance_count": 1
      },
      {
        "fingerprint": "a328fc2e1beff1e171a04ec1b3b445b066bab6c46a539817265af43c7ee3ef89",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:eb9f90d@sha256:a328fc2e1beff1e171a04ec1b3b445b066bab6c46a539817265af43c7ee3ef89",
        "most_recent_timestamp": 1791786940,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/eb9f90d8a22b94845fddb23949fad738cfb6e21f",
        "instance_count": 1
      },
      {
        "fingerprint": "f199c463e8e115a3b9a6f8ac7765a4e5b92cc837cfd7cc87ae5dcc576fcb9d96",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:078bf55@sha256:f199c463e8e115a3b9a6f8ac7765a4e5b92cc837cfd7cc87ae5dcc576fcb9d96",
        "most_recent_timestamp": 1791803897,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/078bf554a5a66ab60f4e33649ac29aa73ce4dbb1",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5480",
    "artifacts": [
      {
        "fingerprint": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
        "most_recent_timestamp": 1791648279,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
        "instance_count": 1
      },
      {
        "fingerprint": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "most_recent_timestamp": 1791801879,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/b543342fa06b0ef415950745fddfff5a85f9d80d",
        "instance_count": 1
      },
      {
        "fingerprint": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
        "most_recent_timestamp": 1791648622,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e",
        "instance_count": 1
      },
      {
        "fingerprint": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "most_recent_timestamp": 1791648357,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "instance_count": 1
      },
      {
        "fingerprint": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
        "most_recent_timestamp": 1791648621,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8",
        "instance_count": 1
      },
      {
        "fingerprint": "807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:842bdad@sha256:807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
        "most_recent_timestamp": 1791648283,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/842bdad4a2fc94d0acfe996d059972b50037b304",
        "instance_count": 1
      },
      {
        "fingerprint": "896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b17fe49@sha256:896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
        "most_recent_timestamp": 1791648263,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
        "instance_count": 1
      },
      {
        "fingerprint": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
        "most_recent_timestamp": 1791648776,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
        "instance_count": 3
      },
      {
        "fingerprint": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
        "most_recent_timestamp": 1791648278,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
        "instance_count": 1
      },
      {
        "fingerprint": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "most_recent_timestamp": 1791648284,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "instance_count": 1
      }
    ]
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "most_recent_timestamp": 1791806445,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "instance_count": 3
      }
    ]
  }
}
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="compare the third latest snapshot in an environment to the latest">
```shell
kosli diff snapshots envName~3 envName 

```
</Accordion>
<Accordion title="compare snapshots of two different environments of the same type">
```shell
kosli diff snapshots envName1 envName2 

```
</Accordion>
<Accordion title="show the not-changed artifacts in both snapshots">
```shell
kosli diff snapshots envName1 envName2 
	--show-unchanged 

```
</Accordion>
<Accordion title="compare the snapshot from 2 weeks ago in an environment to the latest">
```shell
kosli diff snapshots envName@{2.weeks.ago} envName 
```
</Accordion>
</AccordionGroup>

