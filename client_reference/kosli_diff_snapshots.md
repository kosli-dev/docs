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
    "snapshot_id": "aws-beta#8812",
    "artifacts": [
      {
        "fingerprint": "8446d65644ec150a1951d54b6d98d3b16f9601b3286453f9b71e9bc0f51a36db",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:665a327@sha256:8446d65644ec150a1951d54b6d98d3b16f9601b3286453f9b71e9bc0f51a36db",
        "most_recent_timestamp": 1793183899,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/665a32786fc179fa55a289b7d73d5272a6dc5884",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5547",
    "artifacts": [
      {
        "fingerprint": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
        "most_recent_timestamp": 1793179363,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/573bc849ed628bf0230b94be375122cf51b3f48f",
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
        "fingerprint": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
        "most_recent_timestamp": 1793179016,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/38062992c27234fbb3784c9730b0f7229a2dda66",
        "instance_count": 1
      },
      {
        "fingerprint": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
        "most_recent_timestamp": 1793179036,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
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
        "fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "most_recent_timestamp": 1793179343,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "instance_count": 3
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

