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
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


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
    "snapshot_id": "aws-beta#6662",
    "artifacts": [
      {
        "fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "most_recent_timestamp": 1777883050,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "instance_count": 1
      },
      {
        "fingerprint": "5a59b16b0975773a0afeebc30426a86cc40fc12b80f9f42fc911c6d7f9285344",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ad3700e@sha256:5a59b16b0975773a0afeebc30426a86cc40fc12b80f9f42fc911c6d7f9285344",
        "most_recent_timestamp": 1778237609,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/ad3700ecacd79ea8ebef6689874804f1a2851d4c",
        "instance_count": 3
      },
      {
        "fingerprint": "e99c33d87e5e6d5098aecf627a89e1408e6ca8394eb2c8923823b74b5bb3567c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:6f7b1b0@sha256:e99c33d87e5e6d5098aecf627a89e1408e6ca8394eb2c8923823b74b5bb3567c",
        "most_recent_timestamp": 1777922159,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/6f7b1b00db599de210e13dd2f7e6d63a10fe6c7b",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4386",
    "artifacts": [
      {
        "fingerprint": "2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8768460@sha256:2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
        "most_recent_timestamp": 1778178487,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/8768460dc1c91de5f6485a7d3e36870b683edfc3",
        "instance_count": 3
      },
      {
        "fingerprint": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "most_recent_timestamp": 1777842905,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6",
        "instance_count": 3
      },
      {
        "fingerprint": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "most_recent_timestamp": 1776256761,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
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
        "fingerprint": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "most_recent_timestamp": 1776923862,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1",
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
        "fingerprint": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "most_recent_timestamp": 1776923200,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
        "instance_count": 1
      },
      {
        "fingerprint": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "most_recent_timestamp": 1778158856,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
        "instance_count": 1
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

