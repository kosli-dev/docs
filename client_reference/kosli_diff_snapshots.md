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
    "snapshot_id": "aws-beta#7328",
    "artifacts": []
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4833",
    "artifacts": []
  },
  "changed": {
    "artifacts": []
  },
  "not-changed": {
    "artifacts": [
      {
        "fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
        "most_recent_timestamp": 1782291042,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348",
        "instance_count": 1
      },
      {
        "fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
        "most_recent_timestamp": 1782291138,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8",
        "instance_count": 1
      },
      {
        "fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "most_recent_timestamp": 1782291046,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1",
        "instance_count": 1
      },
      {
        "fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "most_recent_timestamp": 1782291119,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564",
        "instance_count": 1
      },
      {
        "fingerprint": "5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:05fa6c1@sha256:5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
        "most_recent_timestamp": 1782291406,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
        "instance_count": 3
      },
      {
        "fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "most_recent_timestamp": 1782291377,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
        "instance_count": 1
      },
      {
        "fingerprint": "c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:33b1b15@sha256:c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
        "most_recent_timestamp": 1782291127,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/33b1b15247724eee83ab795f3d586b4eac93b456",
        "instance_count": 1
      },
      {
        "fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
        "most_recent_timestamp": 1782291036,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4",
        "instance_count": 3
      },
      {
        "fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "most_recent_timestamp": 1782291366,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9",
        "instance_count": 1
      },
      {
        "fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
        "most_recent_timestamp": 1782291043,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00",
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

