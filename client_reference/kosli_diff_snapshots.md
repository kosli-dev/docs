---
title: "kosli diff snapshots"
beta: false
deprecated: false
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
| Flag | Description |
| :--- | :--- |
|    `-h`, `--help`  |  help for snapshots  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|    `-u`, `--show-unchanged`  |  [defaulted] Show the unchanged artifacts present in both snapshots within the diff output.  |


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
    "snapshot_id": "aws-beta#7063",
    "artifacts": [
      {
        "fingerprint": "5ab910de0f6a327085431b5e16dcd911c70d2ac430882c43c37cb015e048e4ad",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:cc9c4c6@sha256:5ab910de0f6a327085431b5e16dcd911c70d2ac430882c43c37cb015e048e4ad",
        "most_recent_timestamp": 1780386951,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/cc9c4c68d246c0905dbb098ec16e1414b0924fb1",
        "instance_count": 1
      },
      {
        "fingerprint": "5b10bf1589cad05052876a75fd62bcf17561223991cc8db7012b29a226d2f88c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a4fb95f@sha256:5b10bf1589cad05052876a75fd62bcf17561223991cc8db7012b29a226d2f88c",
        "most_recent_timestamp": 1780387092,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/a4fb95fa3918623cc1de607b79f5067be1477aaa",
        "instance_count": 1
      },
      {
        "fingerprint": "76e1cbefd32538597a222cebe3630f4f8d06c9725c0737d5e0341e5c5afe8271",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:ed5d914@sha256:76e1cbefd32538597a222cebe3630f4f8d06c9725c0737d5e0341e5c5afe8271",
        "most_recent_timestamp": 1780386969,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/ed5d914779af0b68b06f16c32c168ec8dec7a3f4",
        "instance_count": 1
      },
      {
        "fingerprint": "f1339239a1e7bb64cc61f87466681596536668ca9598d9bc56f84d53a16fb648",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:91520be@sha256:f1339239a1e7bb64cc61f87466681596536668ca9598d9bc56f84d53a16fb648",
        "most_recent_timestamp": 1780392142,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/91520be0f6251e879b3f101f4e89b3d1b2176adc",
        "instance_count": 1
      },
      {
        "fingerprint": "f9e382ad3cfe0b06fde5039f8ea5750b7a29119eddfc715214f68d5b515df9b6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9d0bafc@sha256:f9e382ad3cfe0b06fde5039f8ea5750b7a29119eddfc715214f68d5b515df9b6",
        "most_recent_timestamp": 1780387082,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/9d0bafc92fa3efa56485c6d1cda74288bd31ae68",
        "instance_count": 1
      },
      {
        "fingerprint": "fd20e3ccbc6045854871cb0fe65a72569772c82434b419e430bbaa8b99dcfdb6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:40f1c0b@sha256:fd20e3ccbc6045854871cb0fe65a72569772c82434b419e430bbaa8b99dcfdb6",
        "most_recent_timestamp": 1780385110,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/40f1c0bd780da381b19b44c6edd5295dea27e510",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4686",
    "artifacts": [
      {
        "fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "most_recent_timestamp": 1780332951,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
        "instance_count": 1
      },
      {
        "fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "most_recent_timestamp": 1780333031,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
        "instance_count": 1
      },
      {
        "fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
        "most_recent_timestamp": 1780332962,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758",
        "instance_count": 1
      },
      {
        "fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "most_recent_timestamp": 1780333290,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "instance_count": 1
      },
      {
        "fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "most_recent_timestamp": 1780333321,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4",
        "instance_count": 1
      },
      {
        "fingerprint": "df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:ebf104f@sha256:df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
        "most_recent_timestamp": 1780333308,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
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
        "fingerprint": "9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc8fb51@sha256:9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
        "most_recent_timestamp": 1780332952,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/bc8fb51346a42e17a4d3669f3ea11908782a43d1",
        "instance_count": 3
      },
      {
        "fingerprint": "a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:517657b@sha256:a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
        "most_recent_timestamp": 1780333034,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/517657b9dec6ac7ff431ca5d9b2de72fded5c295",
        "instance_count": 3
      },
      {
        "fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
        "most_recent_timestamp": 1780332956,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618",
        "instance_count": 1
      },
      {
        "fingerprint": "e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2036886@sha256:e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
        "most_recent_timestamp": 1780389628,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/20368865b1ba0532f99f69641bbb96e6334cb545",
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

