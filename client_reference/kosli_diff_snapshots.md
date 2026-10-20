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
    "snapshot_id": "aws-beta#8755",
    "artifacts": [
      {
        "fingerprint": "19ec5fa8d3a1d4140f41ec9ce85fce6ff45e9d670800c370e1c2f30200f94e4f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:3b59027@sha256:19ec5fa8d3a1d4140f41ec9ce85fce6ff45e9d670800c370e1c2f30200f94e4f",
        "most_recent_timestamp": 1791659761,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/3b59027fd20dcec38c72ef3aa04f4bfe3e8423f5",
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
        "fingerprint": "4fbb8f1c531b24dcb2a38c71c268e0b8d7244e650cb96ce042d62fb8c07cb85b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c6834ec@sha256:4fbb8f1c531b24dcb2a38c71c268e0b8d7244e650cb96ce042d62fb8c07cb85b",
        "most_recent_timestamp": 1792490710,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/c6834ecc2c5b9e5622428f14be5c4de3b49dde46",
        "instance_count": 1
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
        "fingerprint": "9bfba602d83bd955af9aa5ffa916f1e9372a289a2dbb1fea106c36d9c05917a0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6f7010e@sha256:9bfba602d83bd955af9aa5ffa916f1e9372a289a2dbb1fea106c36d9c05917a0",
        "most_recent_timestamp": 1792218615,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6f7010e50322dd2203bfde648fc5e3c37c08d2fb",
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
        "fingerprint": "edb4b2d8f6c0b04347f60a15016d0d80eee712308cfbf2ee791154f28683e22b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:70d7d8a@sha256:edb4b2d8f6c0b04347f60a15016d0d80eee712308cfbf2ee791154f28683e22b",
        "most_recent_timestamp": 1792052746,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/70d7d8ad958e6fd6d23694cf149adf67002f4b41",
        "instance_count": 1
      },
      {
        "fingerprint": "ff0385eda13f77c5c98caad5727914dc68aaf91c690534291d9fdee7930a261d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:16a3d97@sha256:ff0385eda13f77c5c98caad5727914dc68aaf91c690534291d9fdee7930a261d",
        "most_recent_timestamp": 1792218864,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/16a3d97abb292ea441f0854a276174538fe0cb2c",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5502",
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
        "fingerprint": "08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:ce9bf5f@sha256:08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
        "most_recent_timestamp": 1792485660,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
        "instance_count": 1
      },
      {
        "fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "most_recent_timestamp": 1791806445,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "instance_count": 3
      },
      {
        "fingerprint": "daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:edb38e8@sha256:daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
        "most_recent_timestamp": 1792486374,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
        "instance_count": 1
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

