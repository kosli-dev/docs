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
    "snapshot_id": "aws-beta#8249",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5309",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
        "most_recent_timestamp": 1788255749,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
        "instance_count": 1
      },
      {
        "fingerprint": "06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:84e986a@sha256:06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
        "most_recent_timestamp": 1788255396,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
        "instance_count": 1
      },
      {
        "fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
        "most_recent_timestamp": 1788255750,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
        "instance_count": 1
      },
      {
        "fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "most_recent_timestamp": 1788255387,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
        "instance_count": 1
      },
      {
        "fingerprint": "28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a357ebd@sha256:28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
        "most_recent_timestamp": 1788255750,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/a357ebd85acdd54968fa0192405aaf2e289d27c9",
        "instance_count": 1
      },
      {
        "fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "most_recent_timestamp": 1788255398,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "instance_count": 1
      },
      {
        "fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "most_recent_timestamp": 1788074889,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "instance_count": 3
      },
      {
        "fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "most_recent_timestamp": 1788255396,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "instance_count": 1
      },
      {
        "fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "most_recent_timestamp": 1788255396,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "instance_count": 1
      },
      {
        "fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
        "most_recent_timestamp": 1788255844,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
        "instance_count": 3
      },
      {
        "fingerprint": "c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d64d2b1@sha256:c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "most_recent_timestamp": 1788256052,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/d64d2b11879179255f11dc991e81fbaf4a040264",
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

