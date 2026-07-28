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
    "snapshot_id": "aws-beta#7866",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5126",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "most_recent_timestamp": 1785236539,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
        "instance_count": 1
      },
      {
        "fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "most_recent_timestamp": 1785138609,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297",
        "instance_count": 3
      },
      {
        "fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "most_recent_timestamp": 1785241244,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "instance_count": 1
      },
      {
        "fingerprint": "a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:92c624e@sha256:a20359795934beb03d992ba5a8f8b95ca637e609284e5a84781bdcbb1b861975",
        "most_recent_timestamp": 1785224823,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/92c624eabb024729fb2af6cdbe354db11ee3882f",
        "instance_count": 1
      },
      {
        "fingerprint": "aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:76672a8@sha256:aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
        "most_recent_timestamp": 1784357070,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/76672a8b247049c3ce8c3140852e17be8f47d995",
        "instance_count": 1
      },
      {
        "fingerprint": "af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2779354@sha256:af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
        "most_recent_timestamp": 1785243412,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/2779354a4fda0eeb90fd43f32211836d99f6bde1",
        "instance_count": 3
      },
      {
        "fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "most_recent_timestamp": 1785241263,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "instance_count": 1
      },
      {
        "fingerprint": "c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a2e4638@sha256:c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
        "most_recent_timestamp": 1785241259,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/a2e4638aaa102446b8a6d1d519c5bc007e24f087",
        "instance_count": 1
      },
      {
        "fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "most_recent_timestamp": 1785241593,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
        "instance_count": 1
      },
      {
        "fingerprint": "c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0fb0be4@sha256:c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
        "most_recent_timestamp": 1785241255,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0fb0be439480821efb926a5079e39ce5941eaa48",
        "instance_count": 1
      },
      {
        "fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "most_recent_timestamp": 1785241255,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
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

