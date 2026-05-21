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
    "snapshot_id": "aws-beta#6921",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4608",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
        "most_recent_timestamp": 1779361526,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
        "instance_count": 1
      },
      {
        "fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "most_recent_timestamp": 1779361878,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419",
        "instance_count": 1
      },
      {
        "fingerprint": "68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:75e174e@sha256:68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
        "most_recent_timestamp": 1779361531,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef",
        "instance_count": 1
      },
      {
        "fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "most_recent_timestamp": 1779361516,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
        "instance_count": 1
      },
      {
        "fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
        "most_recent_timestamp": 1779361600,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
        "instance_count": 3
      },
      {
        "fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
        "most_recent_timestamp": 1778762397,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
        "instance_count": 1
      },
      {
        "fingerprint": "8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:8c3fc7c@sha256:8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
        "most_recent_timestamp": 1779114165,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
        "instance_count": 1
      },
      {
        "fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "most_recent_timestamp": 1779361527,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
        "instance_count": 1
      },
      {
        "fingerprint": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
        "most_recent_timestamp": 1779364863,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
        "instance_count": 3
      },
      {
        "fingerprint": "e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:18fb270@sha256:e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
        "most_recent_timestamp": 1779309324,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d",
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

