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
    "snapshot_id": "aws-beta#8612",
    "artifacts": [
      {
        "fingerprint": "1a553509f1da255fde3135ee4370d5a4e01792f728f198eef9ec2b913be8b260",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3b4ef04@sha256:1a553509f1da255fde3135ee4370d5a4e01792f728f198eef9ec2b913be8b260",
        "most_recent_timestamp": 1791373163,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "instance_count": 3
      },
      {
        "fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
        "most_recent_timestamp": 1791373221,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "instance_count": 1
      },
      {
        "fingerprint": "38b4430f1a0663014d541b34a1e179bfeff1d6031dfa55bbb0ab3ff89b363a77",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:0a1905d@sha256:38b4430f1a0663014d541b34a1e179bfeff1d6031dfa55bbb0ab3ff89b363a77",
        "most_recent_timestamp": 1791373522,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/0a1905d0a06d08403ec0c66cde09e534f3c18956",
        "instance_count": 1
      },
      {
        "fingerprint": "47a964d2b9dc0d68365405fa156cd5441e8940cdba5ea726aa3a133b4a5b5c7f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b2878c5@sha256:47a964d2b9dc0d68365405fa156cd5441e8940cdba5ea726aa3a133b4a5b5c7f",
        "most_recent_timestamp": 1791373971,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b2878c5d26679b8a15a6cae6f84f0d00b8c31f7a",
        "instance_count": 1
      },
      {
        "fingerprint": "50b327c98f15d46203cf92f2a71ecb86489c17c7833ac6af70df0e1bae9d2f94",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:be71103@sha256:50b327c98f15d46203cf92f2a71ecb86489c17c7833ac6af70df0e1bae9d2f94",
        "most_recent_timestamp": 1791539562,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/be71103c39a7e583340ab79688c7348e944a395a",
        "instance_count": 3
      },
      {
        "fingerprint": "7f3a2785e30856078bfdd627273284b01622abca591ecee898cd32da0b5784ad",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3b4ef04@sha256:7f3a2785e30856078bfdd627273284b01622abca591ecee898cd32da0b5784ad",
        "most_recent_timestamp": 1791373162,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "instance_count": 1
      },
      {
        "fingerprint": "81123901f1d806cfe4fc4d251d82a46539582163b3852f93418c721815ad65a4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd5de37@sha256:81123901f1d806cfe4fc4d251d82a46539582163b3852f93418c721815ad65a4",
        "most_recent_timestamp": 1791459746,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/bd5de37db0efe67df14b1710d67af499ac7a0999",
        "instance_count": 1
      },
      {
        "fingerprint": "9264149af68b23851f1615dbbaaa471de3f76af75f852dbc7b8d3a1e3270f32a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5e80258@sha256:9264149af68b23851f1615dbbaaa471de3f76af75f852dbc7b8d3a1e3270f32a",
        "most_recent_timestamp": 1791374029,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/5e802585c0d83f61d1405e7a7b01b1ba2b9a3b3a",
        "instance_count": 1
      },
      {
        "fingerprint": "dffbf5a77e8a3b15393a7c9a8c5efa97ec889bf3d3c79a2c48e79efd5b8c1127",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:8f6076f@sha256:dffbf5a77e8a3b15393a7c9a8c5efa97ec889bf3d3c79a2c48e79efd5b8c1127",
        "most_recent_timestamp": 1791373127,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/8f6076fce137b0b2eccf7548aa9ac6b775402bb6",
        "instance_count": 1
      },
      {
        "fingerprint": "e16c7c7e1ec2ca0b286f9580b22b8c8ddba61fcb59ca9bc02d97ce9ffb8049f2",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e14e470@sha256:e16c7c7e1ec2ca0b286f9580b22b8c8ddba61fcb59ca9bc02d97ce9ffb8049f2",
        "most_recent_timestamp": 1791373993,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/e14e4701d37584b79f6259432960159ceaa5816b",
        "instance_count": 1
      },
      {
        "fingerprint": "e1fab0b977c2b51127878e9a48db9b9df6613d36466b876e7ce91470bb311e67",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3de0343@sha256:e1fab0b977c2b51127878e9a48db9b9df6613d36466b876e7ce91470bb311e67",
        "most_recent_timestamp": 1791373930,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/3de03439fe739a891e793b40d11b97acb2bd2c00",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5440",
    "artifacts": [
      {
        "fingerprint": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "most_recent_timestamp": 1790419522,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/e302b99e045f21adf33ac13c793616cc2fb2ba00",
        "instance_count": 1
      },
      {
        "fingerprint": "3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3fb02b6@sha256:3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
        "most_recent_timestamp": 1791364437,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
        "instance_count": 1
      },
      {
        "fingerprint": "57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7a96f63@sha256:57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "most_recent_timestamp": 1791287540,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/7a96f6335ac05b814cfed0947bed40e29fb14c92",
        "instance_count": 3
      },
      {
        "fingerprint": "5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c5dd4fa@sha256:5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
        "most_recent_timestamp": 1791287456,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c5dd4faa2f40a6a85afceae4565a43a6df553845",
        "instance_count": 1
      },
      {
        "fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "most_recent_timestamp": 1791287842,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 3
      },
      {
        "fingerprint": "a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2390863@sha256:a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
        "most_recent_timestamp": 1791290238,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 1
      },
      {
        "fingerprint": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "most_recent_timestamp": 1791290226,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 1
      },
      {
        "fingerprint": "b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9b49875@sha256:b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
        "most_recent_timestamp": 1791287790,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/9b498758459dd636ff7dbca04367de3f547454f0",
        "instance_count": 1
      },
      {
        "fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "most_recent_timestamp": 1791287466,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
        "instance_count": 1
      },
      {
        "fingerprint": "efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8e32bc0@sha256:efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
        "most_recent_timestamp": 1791287798,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/8e32bc009dd16087e5160d309a9ce4303b7d895f",
        "instance_count": 1
      },
      {
        "fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "most_recent_timestamp": 1791287458,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
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

