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
    "snapshot_id": "aws-beta#7441",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4879",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:0635840@sha256:054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
        "most_recent_timestamp": 1782629848,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/06358409a6a8b8accb35c5fd07082d359ee4947a",
        "instance_count": 1
      },
      {
        "fingerprint": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
        "most_recent_timestamp": 1782391599,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4",
        "instance_count": 1
      },
      {
        "fingerprint": "373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:5fbd867@sha256:373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
        "most_recent_timestamp": 1782390814,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
        "instance_count": 1
      },
      {
        "fingerprint": "51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:521b7c3@sha256:51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
        "most_recent_timestamp": 1782391337,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/521b7c30720e903fa909ae36b7ea9b2f962aa63f",
        "instance_count": 1
      },
      {
        "fingerprint": "8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:23ca301@sha256:8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
        "most_recent_timestamp": 1782391343,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/23ca301f1baa78b2c2784261991015597319ee94",
        "instance_count": 1
      },
      {
        "fingerprint": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
        "most_recent_timestamp": 1782391265,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
        "instance_count": 1
      },
      {
        "fingerprint": "9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:340cd0e@sha256:9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
        "most_recent_timestamp": 1782391257,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/340cd0e960f59711fd21ee7f23d613401c9ee589",
        "instance_count": 3
      },
      {
        "fingerprint": "ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:bc0f871@sha256:ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
        "most_recent_timestamp": 1782391613,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
        "instance_count": 1
      },
      {
        "fingerprint": "e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:077d6f5@sha256:e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
        "most_recent_timestamp": 1782391337,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/077d6f50114958e0d62d0f56f8258a4d02a93e02",
        "instance_count": 3
      },
      {
        "fingerprint": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "most_recent_timestamp": 1782391598,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997",
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

