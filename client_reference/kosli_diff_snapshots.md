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
    "snapshot_id": "aws-beta#6791",
    "artifacts": [
      {
        "fingerprint": "cb0479a7e2f82caa574621b385cc154c181ddf16f55da1db82d5487bff118181",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:d776fb0@sha256:cb0479a7e2f82caa574621b385cc154c181ddf16f55da1db82d5487bff118181",
        "most_recent_timestamp": 1778767645,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/d776fb0df0af42b2877a786542ed4aad4472fd6a",
        "instance_count": 3
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4522",
    "artifacts": [
      {
        "fingerprint": "f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ebab7f1@sha256:f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
        "most_recent_timestamp": 1778762599,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
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
        "fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
        "most_recent_timestamp": 1778762392,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a",
        "instance_count": 1
      },
      {
        "fingerprint": "08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:82ae3ae@sha256:08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
        "most_recent_timestamp": 1778762402,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
        "instance_count": 1
      },
      {
        "fingerprint": "4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:4e30f2c@sha256:4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
        "most_recent_timestamp": 1778762571,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/4e30f2c13e5aedc4814360186742a689aba65f64",
        "instance_count": 3
      },
      {
        "fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
        "most_recent_timestamp": 1778779325,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
        "instance_count": 1
      },
      {
        "fingerprint": "6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f5630da@sha256:6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
        "most_recent_timestamp": 1778762401,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f5630dab81ccd7e1a06cecdef60d903669964d3b",
        "instance_count": 1
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
        "fingerprint": "dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:fd71a71@sha256:dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
        "most_recent_timestamp": 1778762570,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
        "instance_count": 1
      },
      {
        "fingerprint": "e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:42c8baf@sha256:e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
        "most_recent_timestamp": 1778762482,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/42c8bafd9e5f939070a775e87e86466f6e7497a8",
        "instance_count": 1
      },
      {
        "fingerprint": "f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f3cf3ba@sha256:f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
        "most_recent_timestamp": 1778762407,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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

