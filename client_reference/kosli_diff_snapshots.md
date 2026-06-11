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
    "snapshot_id": "aws-beta#7165",
    "artifacts": [
      {
        "fingerprint": "08e29de5dfee9117e82568fba94d785303565158ae26fb2db4edc2c57d5a3b91",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:4e4d89b@sha256:08e29de5dfee9117e82568fba94d785303565158ae26fb2db4edc2c57d5a3b91",
        "most_recent_timestamp": 1781037007,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/4e4d89b91df420a82cf278407e58bae32f45627d",
        "instance_count": 1
      },
      {
        "fingerprint": "314b016820058aa97e5489058505caf5a6b812e08bc8505de6c4e2c095b9c0f8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:4b4c6e6@sha256:314b016820058aa97e5489058505caf5a6b812e08bc8505de6c4e2c095b9c0f8",
        "most_recent_timestamp": 1780745954,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/4b4c6e63980752e4b37ee3456e5f4f4d3c5f0546",
        "instance_count": 1
      },
      {
        "fingerprint": "3c14a535b1f6701b77e3228f9a541a0f4a5c8ec2e5b3d8858b4886a9b8a2ef60",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:eb24e48@sha256:3c14a535b1f6701b77e3228f9a541a0f4a5c8ec2e5b3d8858b4886a9b8a2ef60",
        "most_recent_timestamp": 1780985296,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/eb24e489564d1e7dafbb7a17ef6da384dde59777",
        "instance_count": 3
      },
      {
        "fingerprint": "54e5e0254b877cb1e8a3ad625ba817e1a341825f236b079ef49e6b81fb0c57fb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:160a5de@sha256:54e5e0254b877cb1e8a3ad625ba817e1a341825f236b079ef49e6b81fb0c57fb",
        "most_recent_timestamp": 1780745614,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/160a5ded0a2c2ca3bac4ef3937fbd3b0af499dba",
        "instance_count": 1
      },
      {
        "fingerprint": "739f640ebd78b6f0b3e8aa5f10508e84a1424f19839cae0d808d451cdf1bf183",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:ff10dd6@sha256:739f640ebd78b6f0b3e8aa5f10508e84a1424f19839cae0d808d451cdf1bf183",
        "most_recent_timestamp": 1781093211,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/ff10dd6dda5cb61c5003ac6960c561f37515aa25",
        "instance_count": 1
      },
      {
        "fingerprint": "8c603813fc51aff8b151c20a8bb3291f33ccdb75616148ef9028d9af4468244b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d06808b@sha256:8c603813fc51aff8b151c20a8bb3291f33ccdb75616148ef9028d9af4468244b",
        "most_recent_timestamp": 1781083062,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/d06808b822d72533a014c6aad4225c834854adc2",
        "instance_count": 1
      },
      {
        "fingerprint": "9ec7c431a5a3b2c4c89313ddee32d734f1a2a368f4e124969d45dc5d1467df7d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:2c8ed71@sha256:9ec7c431a5a3b2c4c89313ddee32d734f1a2a368f4e124969d45dc5d1467df7d",
        "most_recent_timestamp": 1780745756,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/2c8ed71d71be0735bad97f42d3de44d7cea0d2bd",
        "instance_count": 1
      },
      {
        "fingerprint": "a64ce001d75001055cfb53ad374ef12ac7cf023c32ad11224c21baeb82ef54a7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:42725db@sha256:a64ce001d75001055cfb53ad374ef12ac7cf023c32ad11224c21baeb82ef54a7",
        "most_recent_timestamp": 1781169622,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/42725dbb208d993e5b7c75e975335c0a20646493",
        "instance_count": 1
      },
      {
        "fingerprint": "b895f49b10576f8945afe0d417a6f2e3b7604b897d70d3d53c229db39ab9ceb7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3ea308c@sha256:b895f49b10576f8945afe0d417a6f2e3b7604b897d70d3d53c229db39ab9ceb7",
        "most_recent_timestamp": 1781168746,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/3ea308cbf42237cc8e564c2d849ee53f69b355ad",
        "instance_count": 1
      },
      {
        "fingerprint": "bf41ad448f32a5ffdfc40fa906ed3d06adda95bbcef54f3ba1739b60fc33033b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:5559a2a@sha256:bf41ad448f32a5ffdfc40fa906ed3d06adda95bbcef54f3ba1739b60fc33033b",
        "most_recent_timestamp": 1781120540,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/5559a2a189654b055270f44312048e8244a7a847",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4749",
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
        "fingerprint": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "most_recent_timestamp": 1780898570,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/8863c10c2c93d3539672e0bf75bd9925f8778564",
        "instance_count": 3
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
        "fingerprint": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "most_recent_timestamp": 1780724058,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/bc5fbc14361ce7a6281b6110049d90a03f69d786",
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
        "fingerprint": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "most_recent_timestamp": 1780898567,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/cdaac807f3282bd0bba056d906d5536074297a04",
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

