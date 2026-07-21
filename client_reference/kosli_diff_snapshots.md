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
    "snapshot_id": "aws-beta#7781",
    "artifacts": [
      {
        "fingerprint": "21c27c255c0ed91aa9c3aeb98786cf28a0840fd7324dcfae5474970e6f134ad3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7e84b09@sha256:21c27c255c0ed91aa9c3aeb98786cf28a0840fd7324dcfae5474970e6f134ad3",
        "most_recent_timestamp": 1784312732,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/7e84b0929df3f8d90932b0c8c11bc806dfa5603f",
        "instance_count": 3
      },
      {
        "fingerprint": "278a29bc232ce0294ce46cd08bb3f3a28ce53ddc14e588e00f67f6a93173b916",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3aaa3a7@sha256:278a29bc232ce0294ce46cd08bb3f3a28ce53ddc14e588e00f67f6a93173b916",
        "most_recent_timestamp": 1784445403,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3aaa3a73514a94581455ff65cbc835501dce1090",
        "instance_count": 3
      },
      {
        "fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "most_recent_timestamp": 1784312340,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "instance_count": 1
      },
      {
        "fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "most_recent_timestamp": 1784312582,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "instance_count": 1
      },
      {
        "fingerprint": "c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a2e4638@sha256:c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "most_recent_timestamp": 1784312525,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/a2e4638aaa102446b8a6d1d519c5bc007e24f087",
        "instance_count": 1
      },
      {
        "fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "most_recent_timestamp": 1784312477,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
        "instance_count": 1
      },
      {
        "fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "most_recent_timestamp": 1784312473,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5062",
    "artifacts": [
      {
        "fingerprint": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
        "most_recent_timestamp": 1784352892,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3f0b9975f96b7f4e4aae0b4409cebda3209be164",
        "instance_count": 3
      },
      {
        "fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "most_recent_timestamp": 1783618204,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "instance_count": 1
      },
      {
        "fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "most_recent_timestamp": 1784183551,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
        "instance_count": 1
      },
      {
        "fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "most_recent_timestamp": 1783618126,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
        "instance_count": 1
      },
      {
        "fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "most_recent_timestamp": 1784184597,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615",
        "instance_count": 1
      },
      {
        "fingerprint": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "most_recent_timestamp": 1783757716,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a",
        "instance_count": 3
      },
      {
        "fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "most_recent_timestamp": 1783618209,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
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
        "fingerprint": "aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:76672a8@sha256:aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "most_recent_timestamp": 1784357070,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/76672a8b247049c3ce8c3140852e17be8f47d995",
        "instance_count": 1
      },
      {
        "fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "most_recent_timestamp": 1784355921,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
        "instance_count": 1
      },
      {
        "fingerprint": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "most_recent_timestamp": 1784443888,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72",
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

