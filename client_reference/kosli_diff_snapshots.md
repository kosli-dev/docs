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
    "snapshot_id": "aws-beta#7529",
    "artifacts": [
      {
        "fingerprint": "5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fbe04c6@sha256:5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
        "most_recent_timestamp": 1782977630,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/fbe04c6016bd7822a9b0b948043614186787194f",
        "instance_count": 3
      },
      {
        "fingerprint": "746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f7fd6b7@sha256:746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
        "most_recent_timestamp": 1782982163,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f7fd6b78302ad399252990b0b81f54d7416a402f",
        "instance_count": 1
      },
      {
        "fingerprint": "8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:c174ef2@sha256:8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
        "most_recent_timestamp": 1782982210,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/c174ef247b1efb95812373fde2a8e8db3a9ede03",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4932",
    "artifacts": [
      {
        "fingerprint": "157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:df9af0c@sha256:157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
        "most_recent_timestamp": 1782969676,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/df9af0c9a2a81ed7bfc429979121b8310bbe7138",
        "instance_count": 1
      },
      {
        "fingerprint": "38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:027b85e@sha256:38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
        "most_recent_timestamp": 1782966800,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/027b85ebccec65b35b0ba0e4da196b7738d4ba82",
        "instance_count": 3
      },
      {
        "fingerprint": "eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2a3119f@sha256:eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
        "most_recent_timestamp": 1782831972,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/2a3119f72fa7bf62bbc83a3d48266120085d03ab",
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
        "fingerprint": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "most_recent_timestamp": 1782900828,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7",
        "instance_count": 1
      },
      {
        "fingerprint": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
        "most_recent_timestamp": 1782966801,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208",
        "instance_count": 1
      },
      {
        "fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "most_recent_timestamp": 1782963931,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
        "instance_count": 3
      },
      {
        "fingerprint": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
        "most_recent_timestamp": 1782973596,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8",
        "instance_count": 1
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
        "fingerprint": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
        "most_recent_timestamp": 1782833760,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997",
        "instance_count": 1
      },
      {
        "fingerprint": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
        "most_recent_timestamp": 1782966159,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83",
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

