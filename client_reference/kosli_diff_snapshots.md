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
    "snapshot_id": "aws-beta#8581",
    "artifacts": [
      {
        "fingerprint": "57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7a96f63@sha256:57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
        "most_recent_timestamp": 1791096247,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/7a96f6335ac05b814cfed0947bed40e29fb14c92",
        "instance_count": 3
      },
      {
        "fingerprint": "5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c5dd4fa@sha256:5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
        "most_recent_timestamp": 1791018896,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c5dd4faa2f40a6a85afceae4565a43a6df553845",
        "instance_count": 1
      },
      {
        "fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
        "most_recent_timestamp": 1791207772,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 3
      },
      {
        "fingerprint": "a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2390863@sha256:a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
        "most_recent_timestamp": 1791207800,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 1
      },
      {
        "fingerprint": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "most_recent_timestamp": 1791207745,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "instance_count": 1
      },
      {
        "fingerprint": "b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9b49875@sha256:b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
        "most_recent_timestamp": 1791098334,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/9b498758459dd636ff7dbca04367de3f547454f0",
        "instance_count": 1
      },
      {
        "fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "most_recent_timestamp": 1791096151,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
        "instance_count": 1
      },
      {
        "fingerprint": "e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c415496@sha256:e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
        "most_recent_timestamp": 1790424894,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c415496d0e35cbca51c55d0401c141c982a8d711",
        "instance_count": 1
      },
      {
        "fingerprint": "efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8e32bc0@sha256:efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
        "most_recent_timestamp": 1791096547,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/8e32bc009dd16087e5160d309a9ce4303b7d895f",
        "instance_count": 1
      },
      {
        "fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "most_recent_timestamp": 1790940495,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5420",
    "artifacts": [
      {
        "fingerprint": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "most_recent_timestamp": 1790416559,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
        "instance_count": 1
      },
      {
        "fingerprint": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
        "most_recent_timestamp": 1790419520,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319",
        "instance_count": 1
      },
      {
        "fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "most_recent_timestamp": 1790416655,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced",
        "instance_count": 3
      },
      {
        "fingerprint": "5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:41b9d61@sha256:5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
        "most_recent_timestamp": 1790419855,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146",
        "instance_count": 1
      },
      {
        "fingerprint": "68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c267890@sha256:68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
        "most_recent_timestamp": 1790419509,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c267890b689f43e24679bfe9006ddc390447e7e7",
        "instance_count": 1
      },
      {
        "fingerprint": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "most_recent_timestamp": 1790419878,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb",
        "instance_count": 1
      },
      {
        "fingerprint": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "most_recent_timestamp": 1790419522,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c",
        "instance_count": 1
      },
      {
        "fingerprint": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
        "most_recent_timestamp": 1790419525,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a",
        "instance_count": 1
      },
      {
        "fingerprint": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
        "most_recent_timestamp": 1790419856,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
        "instance_count": 1
      },
      {
        "fingerprint": "cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5bdfa1d@sha256:cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
        "most_recent_timestamp": 1790416571,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f",
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
        "fingerprint": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
        "most_recent_timestamp": 1790419522,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/e302b99e045f21adf33ac13c793616cc2fb2ba00",
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

