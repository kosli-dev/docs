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
    "snapshot_id": "aws-beta#7649",
    "artifacts": [
      {
        "fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "most_recent_timestamp": 1783539093,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "instance_count": 1
      },
      {
        "fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "most_recent_timestamp": 1783606120,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
        "instance_count": 1
      },
      {
        "fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "most_recent_timestamp": 1783538813,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "instance_count": 1
      },
      {
        "fingerprint": "6e10030b8176ee0f17f74a1ca59a22ae05ab74affa7221b4e685d70a6db100a0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:9900d7e@sha256:6e10030b8176ee0f17f74a1ca59a22ae05ab74affa7221b4e685d70a6db100a0",
        "most_recent_timestamp": 1783538560,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/9900d7eae155e4434028345208d4049143612e8e",
        "instance_count": 3
      },
      {
        "fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "most_recent_timestamp": 1783540473,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
        "instance_count": 1
      },
      {
        "fingerprint": "86c346b9d28ffba48419f0d36db13d0262dc923d3794da851dd61e324b033b5f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:da04517@sha256:86c346b9d28ffba48419f0d36db13d0262dc923d3794da851dd61e324b033b5f",
        "most_recent_timestamp": 1783536067,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/da045178c3d695ff19e914004d546dcc31a918a6",
        "instance_count": 1
      },
      {
        "fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "most_recent_timestamp": 1783536467,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
        "instance_count": 1
      },
      {
        "fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "most_recent_timestamp": 1783538983,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/627315ab66d5250fec7ec574b073f1095879a8a4",
        "instance_count": 3
      },
      {
        "fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "most_recent_timestamp": 1783539683,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/b8e6c03975a5701e3e8d198549f463989f1a00f4",
        "instance_count": 1
      },
      {
        "fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "most_recent_timestamp": 1783536888,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4972",
    "artifacts": [
      {
        "fingerprint": "1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:2fa0324@sha256:1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
        "most_recent_timestamp": 1783075531,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/2fa032402c47885c2fcf8036e2eee07ac73bdc41",
        "instance_count": 1
      },
      {
        "fingerprint": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
        "most_recent_timestamp": 1783075526,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659",
        "instance_count": 1
      },
      {
        "fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
        "most_recent_timestamp": 1783075608,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510",
        "instance_count": 1
      },
      {
        "fingerprint": "579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:28fc01e@sha256:579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
        "most_recent_timestamp": 1783325295,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/28fc01e77500cdb35522d5f27aad95b501a03cdc",
        "instance_count": 3
      },
      {
        "fingerprint": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
        "most_recent_timestamp": 1783075521,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a",
        "instance_count": 1
      },
      {
        "fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
        "most_recent_timestamp": 1783075532,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379",
        "instance_count": 1
      },
      {
        "fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
        "most_recent_timestamp": 1783075624,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865",
        "instance_count": 3
      },
      {
        "fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "most_recent_timestamp": 1783075863,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
        "instance_count": 1
      },
      {
        "fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "most_recent_timestamp": 1783075605,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
        "instance_count": 1
      },
      {
        "fingerprint": "c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cbf0063@sha256:c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
        "most_recent_timestamp": 1783329868,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f",
        "instance_count": 1
      }
    ]
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": []
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

