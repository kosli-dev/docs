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
|    -h, --help  |  help for snapshots  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|    -u, --show-unchanged  |  [defaulted] Show the unchanged artifacts present in both snapshots within the diff output.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout.  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |
|    -q, --quiet  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both --quiet and --debug are set, --debug wins.  |


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
    "snapshot_id": "aws-beta#6740",
    "artifacts": [
      {
        "fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
        "most_recent_timestamp": 1778511262,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4424",
    "artifacts": [
      {
        "fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
        "most_recent_timestamp": 1778502490,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0",
        "instance_count": 3
      }
    ]
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
        "most_recent_timestamp": 1778502485,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269",
        "instance_count": 1
      },
      {
        "fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "most_recent_timestamp": 1778502489,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "instance_count": 1
      },
      {
        "fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
        "most_recent_timestamp": 1778502501,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a",
        "instance_count": 1
      },
      {
        "fingerprint": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "most_recent_timestamp": 1776923208,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5",
        "instance_count": 1
      },
      {
        "fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
        "most_recent_timestamp": 1778245549,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
        "instance_count": 3
      },
      {
        "fingerprint": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
        "most_recent_timestamp": 1776923213,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a",
        "instance_count": 1
      },
      {
        "fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
        "most_recent_timestamp": 1778502825,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4",
        "instance_count": 1
      },
      {
        "fingerprint": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
        "most_recent_timestamp": 1776923539,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3",
        "instance_count": 1
      },
      {
        "fingerprint": "f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:db53382@sha256:f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
        "most_recent_timestamp": 1778081137,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677",
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

