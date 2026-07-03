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
    "snapshot_id": "aws-beta#7574",
    "artifacts": [
      {
        "fingerprint": "490c213eda69cb380990a8c12f48b19f108a368e321abcd99d6113e96413eb0d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:08ff66c@sha256:490c213eda69cb380990a8c12f48b19f108a368e321abcd99d6113e96413eb0d",
        "most_recent_timestamp": 1783083666,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/08ff66ccc6e7dc3a4ac3cd0675ace61e2027c531",
        "instance_count": 3
      },
      {
        "fingerprint": "cbc7b9d774d7db1fa15d86a06c77a0b48cc3d1b8c6bb0615a614bbef2925c4c3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:32ae42d@sha256:cbc7b9d774d7db1fa15d86a06c77a0b48cc3d1b8c6bb0615a614bbef2925c4c3",
        "most_recent_timestamp": 1783079637,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/32ae42d3ef6ac68cccf76cbe92e071fed8fd59ee",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4945",
    "artifacts": [
      {
        "fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "most_recent_timestamp": 1782963931,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
        "instance_count": 3
      },
      {
        "fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "most_recent_timestamp": 1783075863,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
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
        "fingerprint": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "most_recent_timestamp": 1782907144,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
        "instance_count": 1
      },
      {
        "fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "most_recent_timestamp": 1783075605,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
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

