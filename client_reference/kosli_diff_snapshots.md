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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## JSON output

With `--output json`, this command prints the response of the [Get environment diff](/api-reference/envdiff/get-environment-diff) API operation as the server returned it. The shape follows the server's published API spec, not the CLI version.

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
    "snapshot_id": "aws-beta#8953",
    "artifacts": [
      {
        "fingerprint": "1d80af3ba221ac55b3ad395101f97dfac398302efb5fbf05b651d36cf2d7240b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e6cdeac@sha256:1d80af3ba221ac55b3ad395101f97dfac398302efb5fbf05b651d36cf2d7240b",
        "most_recent_timestamp": 1795339101,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/e6cdeac08b7942c29838f5c699d76c5ebc05883d",
        "instance_count": 1
      },
      {
        "fingerprint": "5c2c1e9c5070059873557dc30dbf06401097cd90135ff3e4a9f8a1453b0dc3de",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:837321f@sha256:5c2c1e9c5070059873557dc30dbf06401097cd90135ff3e4a9f8a1453b0dc3de",
        "most_recent_timestamp": 1795346916,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/837321fea394a756ed04e95f1ddb2023f4c12c57",
        "instance_count": 1
      },
      {
        "fingerprint": "afccf5ef2417c30aa09f222be274a341a7d5f0feeeca1129ac75db1615a1543c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:46905cf@sha256:afccf5ef2417c30aa09f222be274a341a7d5f0feeeca1129ac75db1615a1543c",
        "most_recent_timestamp": 1795336509,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/46905cf41d90adef9744be06aaa2aff192e5dd5e",
        "instance_count": 1
      },
      {
        "fingerprint": "dcd9d1aee865849b3f21df705db9ad4ee78008daac99ef95fc1a13fddd806764",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:98fa081@sha256:dcd9d1aee865849b3f21df705db9ad4ee78008daac99ef95fc1a13fddd806764",
        "most_recent_timestamp": 1795337065,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/98fa0815fd447b2613db22a588c570bf767be623",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5646",
    "artifacts": [
      {
        "fingerprint": "1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c15feb2@sha256:1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
        "most_recent_timestamp": 1795105183,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/c15feb2710922b82ec50d2cf131da532e09e7dc9",
        "instance_count": 1
      },
      {
        "fingerprint": "48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b3940c2@sha256:48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
        "most_recent_timestamp": 1795105186,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/b3940c267183bbcee441756523576162575f8e01",
        "instance_count": 1
      },
      {
        "fingerprint": "4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:a0ffbb8@sha256:4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
        "most_recent_timestamp": 1795105415,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
        "instance_count": 3
      },
      {
        "fingerprint": "f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:0191adf@sha256:f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
        "most_recent_timestamp": 1795105649,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
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
        "fingerprint": "0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a1b031@sha256:0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
        "most_recent_timestamp": 1795105188,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/1a1b031d793c474599506ec12faac073df5b6647",
        "instance_count": 1
      },
      {
        "fingerprint": "626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2bf3642@sha256:626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
        "most_recent_timestamp": 1795105418,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
        "instance_count": 1
      },
      {
        "fingerprint": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "most_recent_timestamp": 1794908404,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/a173ddba4169059477911c4fa0c73674407712a5",
        "instance_count": 1
      },
      {
        "fingerprint": "82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2bf3642@sha256:82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
        "most_recent_timestamp": 1795105417,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
        "instance_count": 1
      },
      {
        "fingerprint": "97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bcb5902@sha256:97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
        "most_recent_timestamp": 1795105524,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/bcb5902178a74126ae2593f6c3189cacb9d049fb",
        "instance_count": 3
      },
      {
        "fingerprint": "aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:aad1254@sha256:aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
        "most_recent_timestamp": 1795105651,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/aad12541eaefc579b91f77059df895b032eba259",
        "instance_count": 1
      },
      {
        "fingerprint": "f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:cfb37e8@sha256:f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
        "most_recent_timestamp": 1795105743,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/cfb37e8c1a1634799f4518186603ce6da97d0958",
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

