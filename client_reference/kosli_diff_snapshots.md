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
    "snapshot_id": "aws-beta#8877",
    "artifacts": [
      {
        "fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "most_recent_timestamp": 1794649988,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "instance_count": 1
      },
      {
        "fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "most_recent_timestamp": 1794649853,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
        "instance_count": 3
      },
      {
        "fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "most_recent_timestamp": 1794649532,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 1
      },
      {
        "fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "most_recent_timestamp": 1794649610,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 3
      },
      {
        "fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "most_recent_timestamp": 1794650781,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
        "instance_count": 1
      },
      {
        "fingerprint": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
        "most_recent_timestamp": 1794645526,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/a173ddba4169059477911c4fa0c73674407712a5",
        "instance_count": 1
      },
      {
        "fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "most_recent_timestamp": 1794650862,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "instance_count": 1
      },
      {
        "fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "most_recent_timestamp": 1794649526,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "instance_count": 1
      },
      {
        "fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "most_recent_timestamp": 1794649628,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 1
      },
      {
        "fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "most_recent_timestamp": 1794650818,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
        "instance_count": 1
      },
      {
        "fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "most_recent_timestamp": 1794649634,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5597",
    "artifacts": [
      {
        "fingerprint": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "most_recent_timestamp": 1793178778,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "instance_count": 1
      },
      {
        "fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
        "most_recent_timestamp": 1793178783,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "instance_count": 1
      },
      {
        "fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "most_recent_timestamp": 1793178791,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
        "instance_count": 1
      },
      {
        "fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "most_recent_timestamp": 1793178869,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
        "instance_count": 1
      },
      {
        "fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
        "most_recent_timestamp": 1794043932,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
        "instance_count": 1
      },
      {
        "fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
        "most_recent_timestamp": 1793179128,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
        "instance_count": 1
      },
      {
        "fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
        "most_recent_timestamp": 1793179132,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
        "instance_count": 3
      },
      {
        "fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
        "most_recent_timestamp": 1793179259,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
        "instance_count": 1
      },
      {
        "fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
        "most_recent_timestamp": 1794043915,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
        "instance_count": 1
      },
      {
        "fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "most_recent_timestamp": 1793179343,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "instance_count": 3
      },
      {
        "fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
        "most_recent_timestamp": 1794043936,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5",
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

