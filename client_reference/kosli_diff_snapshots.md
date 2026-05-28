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
    "snapshot_id": "aws-beta#6987",
    "artifacts": [
      {
        "fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "most_recent_timestamp": 1779956617,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
        "instance_count": 1
      },
      {
        "fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "most_recent_timestamp": 1779957276,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
        "instance_count": 1
      },
      {
        "fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "most_recent_timestamp": 1779956795,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "instance_count": 1
      },
      {
        "fingerprint": "c23a67482dd1b5dfb69590f8111d973b995c04c8bd337da20de886e957502e47",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87d749a@sha256:c23a67482dd1b5dfb69590f8111d973b995c04c8bd337da20de886e957502e47",
        "most_recent_timestamp": 1779955582,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/87d749a3e542ad865dd5da07c69ffe05fd109f4b",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4652",
    "artifacts": [
      {
        "fingerprint": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "most_recent_timestamp": 1779639453,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d",
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
        "fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "most_recent_timestamp": 1779361516,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
        "instance_count": 1
      },
      {
        "fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "most_recent_timestamp": 1779361527,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
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
        "fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "most_recent_timestamp": 1779809079,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2",
        "instance_count": 1
      },
      {
        "fingerprint": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
        "most_recent_timestamp": 1779731496,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77",
        "instance_count": 1
      },
      {
        "fingerprint": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
        "most_recent_timestamp": 1779624714,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2",
        "instance_count": 1
      },
      {
        "fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "most_recent_timestamp": 1779606194,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
        "instance_count": 3
      },
      {
        "fingerprint": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
        "most_recent_timestamp": 1779625987,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8",
        "instance_count": 3
      },
      {
        "fingerprint": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "most_recent_timestamp": 1779648032,
        "flow": "creator-ci",
        "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db",
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

