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
    "snapshot_id": "aws-beta#8886",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5611",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "most_recent_timestamp": 1794908165,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "instance_count": 1
      },
      {
        "fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "most_recent_timestamp": 1794908166,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
        "instance_count": 3
      },
      {
        "fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "most_recent_timestamp": 1794908167,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 1
      },
      {
        "fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "most_recent_timestamp": 1794908253,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 3
      },
      {
        "fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "most_recent_timestamp": 1794908401,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
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
        "fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "most_recent_timestamp": 1794908500,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "instance_count": 1
      },
      {
        "fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "most_recent_timestamp": 1794908607,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "instance_count": 1
      },
      {
        "fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "most_recent_timestamp": 1794908645,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "instance_count": 1
      },
      {
        "fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "most_recent_timestamp": 1794908743,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
        "instance_count": 1
      },
      {
        "fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "most_recent_timestamp": 1794908746,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
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

