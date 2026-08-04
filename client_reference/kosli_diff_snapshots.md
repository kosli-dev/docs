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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
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
    "snapshot_id": "aws-beta#7978",
    "artifacts": [
      {
        "fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "most_recent_timestamp": 1785764779,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "instance_count": 1
      },
      {
        "fingerprint": "2cfdbea64e0451b0de2213eca4abe14adce61b1cd6003e99aa8c5e6148528c94",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a1d4103@sha256:2cfdbea64e0451b0de2213eca4abe14adce61b1cd6003e99aa8c5e6148528c94",
        "most_recent_timestamp": 1785654145,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/a1d410386c7fdc15ef48a626d6f59dded1cf1964",
        "instance_count": 3
      },
      {
        "fingerprint": "8771b2dbc5cc61aad59602e6c1b67e56496f9b6883a6bd0b3c6b85bc0dbfa052",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fda4677@sha256:8771b2dbc5cc61aad59602e6c1b67e56496f9b6883a6bd0b3c6b85bc0dbfa052",
        "most_recent_timestamp": 1785754253,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/fda467737fbb8ca1c6cb3639ebabe853fc3d74da",
        "instance_count": 1
      },
      {
        "fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "most_recent_timestamp": 1785764812,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
        "instance_count": 1
      },
      {
        "fingerprint": "bc1a1b5ffc66fee2004451dccdc0c2ad1ab566f665d93c63287e02ee88c3805e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:061da97@sha256:bc1a1b5ffc66fee2004451dccdc0c2ad1ab566f665d93c63287e02ee88c3805e",
        "most_recent_timestamp": 1785757608,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/061da97f094e86f4a3ecbd17d0c3a7925256dd0f",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5177",
    "artifacts": [
      {
        "fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
        "most_recent_timestamp": 1785755094,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167",
        "instance_count": 1
      },
      {
        "fingerprint": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
        "most_recent_timestamp": 1785681913,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
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
        "fingerprint": "d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c221bb1@sha256:d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
        "most_recent_timestamp": 1785744284,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/c221bb1cdea95e14bc2df052e894756a9d96c378",
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
        "fingerprint": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "most_recent_timestamp": 1785310509,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262",
        "instance_count": 1
      },
      {
        "fingerprint": "8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:48bb369@sha256:8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
        "most_recent_timestamp": 1785831945,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
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
        "fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
        "most_recent_timestamp": 1785559130,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
        "instance_count": 1
      },
      {
        "fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "most_recent_timestamp": 1785241255,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "instance_count": 1
      },
      {
        "fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
        "most_recent_timestamp": 1785559134,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34",
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

