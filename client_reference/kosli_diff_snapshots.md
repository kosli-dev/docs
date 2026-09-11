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
    "snapshot_id": "aws-beta#8350",
    "artifacts": [
      {
        "fingerprint": "1d819a21e793bffbe50a39c9b6b8c4154e0b4271051931839dc8a2fa0c564e2a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2e1a942@sha256:1d819a21e793bffbe50a39c9b6b8c4154e0b4271051931839dc8a2fa0c564e2a",
        "most_recent_timestamp": 1788966072,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/2e1a942c3d17cae29db3bc94336f06773e3573c3",
        "instance_count": 1
      },
      {
        "fingerprint": "1ff25328272b6a1c85d6751e326b2d941cf927a040a41e2e3cb96b606b01709f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:c61d934@sha256:1ff25328272b6a1c85d6751e326b2d941cf927a040a41e2e3cb96b606b01709f",
        "most_recent_timestamp": 1788966002,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/c61d9342b4008c664ffdabaf851538ede9085b76",
        "instance_count": 1
      },
      {
        "fingerprint": "7a8cbbe05f8659a3ad37e537756c313dcb10e25e49ed1a1c9a656bde472ce887",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:75d91ed@sha256:7a8cbbe05f8659a3ad37e537756c313dcb10e25e49ed1a1c9a656bde472ce887",
        "most_recent_timestamp": 1788966515,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/75d91edd753298bf7e4f9b07ae20ba16707dea5f",
        "instance_count": 3
      },
      {
        "fingerprint": "7b246678863435a956925627616acd8969d0f23b3b9f3db375e7ed0f68e3373a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:de3178a@sha256:7b246678863435a956925627616acd8969d0f23b3b9f3db375e7ed0f68e3373a",
        "most_recent_timestamp": 1788966207,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/de3178a3d647276644a0dde662af8a53005c97d2",
        "instance_count": 1
      },
      {
        "fingerprint": "b250b0603dd70628fdf46ff1e73cb29491febf5f4e127728f2a2e4a7aad2ee02",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:8c3bffd@sha256:b250b0603dd70628fdf46ff1e73cb29491febf5f4e127728f2a2e4a7aad2ee02",
        "most_recent_timestamp": 1788965787,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/8c3bffd55590a7d6c180980b263117096a9add32",
        "instance_count": 1
      },
      {
        "fingerprint": "ba00a3efafbea83322e018ae78fd97defd8f018c794a135859dcc02a7e70bd5c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:da21200@sha256:ba00a3efafbea83322e018ae78fd97defd8f018c794a135859dcc02a7e70bd5c",
        "most_recent_timestamp": 1789113338,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/da2120004a066092cc36c0f8d20f5186106b3d04",
        "instance_count": 1
      },
      {
        "fingerprint": "ba63a80521117f0778ca0e2f564fffba0926292eeeaf0a9e1103952fafbec472",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:a339a8f@sha256:ba63a80521117f0778ca0e2f564fffba0926292eeeaf0a9e1103952fafbec472",
        "most_recent_timestamp": 1788965009,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/a339a8f19075445057a1466a44ca241f093384e4",
        "instance_count": 1
      },
      {
        "fingerprint": "dbd68f81c38a9bdbccac20e2ca5c23c6377a7093b0c7e5730156431eb06d64cf",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:06dc33a@sha256:dbd68f81c38a9bdbccac20e2ca5c23c6377a7093b0c7e5730156431eb06d64cf",
        "most_recent_timestamp": 1788979049,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/06dc33ad1a46960bd685d00be993098a74a6dca0",
        "instance_count": 1
      },
      {
        "fingerprint": "e5197f0eda74fc1a6311f8745ef9d8eecefcbf3e75eb1179dc1c1c44075608ae",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:1e3d084@sha256:e5197f0eda74fc1a6311f8745ef9d8eecefcbf3e75eb1179dc1c1c44075608ae",
        "most_recent_timestamp": 1788966462,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/1e3d084c20f92afd8747d3d1f70c00b30d07c5fe",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5352",
    "artifacts": [
      {
        "fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
        "most_recent_timestamp": 1789022826,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/5d1d4b6035691d7986e05ab263e521b3e711fa0c",
        "instance_count": 1
      },
      {
        "fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "most_recent_timestamp": 1789022830,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
        "instance_count": 1
      },
      {
        "fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
        "most_recent_timestamp": 1789022816,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26",
        "instance_count": 1
      },
      {
        "fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
        "most_recent_timestamp": 1789022819,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
        "instance_count": 1
      },
      {
        "fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
        "most_recent_timestamp": 1789022826,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
        "instance_count": 1
      },
      {
        "fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
        "most_recent_timestamp": 1789022822,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1",
        "instance_count": 1
      },
      {
        "fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
        "most_recent_timestamp": 1789022884,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/236898f12a3bcce3b60625dd71c6f817d4cc37c2",
        "instance_count": 3
      },
      {
        "fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
        "most_recent_timestamp": 1789022818,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d",
        "instance_count": 1
      },
      {
        "fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
        "most_recent_timestamp": 1789022811,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
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
        "fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
        "most_recent_timestamp": 1789022877,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
        "instance_count": 3
      },
      {
        "fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "most_recent_timestamp": 1789023319,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687",
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

