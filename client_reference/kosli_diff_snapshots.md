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
    "snapshot_id": "aws-beta#7259",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4798",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
        "most_recent_timestamp": 1781862431,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691",
        "instance_count": 1
      },
      {
        "fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "most_recent_timestamp": 1781862427,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "instance_count": 3
      },
      {
        "fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "most_recent_timestamp": 1781862576,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
        "instance_count": 3
      },
      {
        "fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "most_recent_timestamp": 1781862763,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543",
        "instance_count": 1
      },
      {
        "fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "most_recent_timestamp": 1781590473,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/706526874659341458da5bb21903a6423c0a5a29",
        "instance_count": 1
      },
      {
        "fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "most_recent_timestamp": 1781862426,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "instance_count": 1
      },
      {
        "fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "most_recent_timestamp": 1781862505,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "instance_count": 1
      },
      {
        "fingerprint": "c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c1cd97e@sha256:c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
        "most_recent_timestamp": 1781862429,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c1cd97e11606d0a705df6619424c9ad8b07a57ca",
        "instance_count": 1
      },
      {
        "fingerprint": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "most_recent_timestamp": 1781862518,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
        "instance_count": 1
      },
      {
        "fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "most_recent_timestamp": 1781592148,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
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

