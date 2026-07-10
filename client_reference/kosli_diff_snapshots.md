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
    "snapshot_id": "aws-beta#7668",
    "artifacts": [
      {
        "fingerprint": "6677d3b6cd162d7888981232e9fcbb6fca2c04307fa1838eaaece489a393de39",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:946e5c3@sha256:6677d3b6cd162d7888981232e9fcbb6fca2c04307fa1838eaaece489a393de39",
        "most_recent_timestamp": 1783674435,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/946e5c370f39ca436cf1d3e2016ceef220af2b43",
        "instance_count": 1
      },
      {
        "fingerprint": "79abecc3fd3780433938403e3c1de3c8a53e475dd59d68e2f6cc749b65976f43",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:87db5af@sha256:79abecc3fd3780433938403e3c1de3c8a53e475dd59d68e2f6cc749b65976f43",
        "most_recent_timestamp": 1783661860,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/87db5afce1f292dfd2376b046ecbe1abcbf26d04",
        "instance_count": 3
      },
      {
        "fingerprint": "add714273f53b1fca369e9ce43b59b28b2e38e6fc283ae1ff2056ebb13c6a792",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:80473e8@sha256:add714273f53b1fca369e9ce43b59b28b2e38e6fc283ae1ff2056ebb13c6a792",
        "most_recent_timestamp": 1783672438,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/80473e87329962dd1924b51d541620c15d68658b",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4981",
    "artifacts": [
      {
        "fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "most_recent_timestamp": 1783618467,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "instance_count": 1
      },
      {
        "fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "most_recent_timestamp": 1783618197,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "instance_count": 1
      },
      {
        "fingerprint": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
        "most_recent_timestamp": 1783618209,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116",
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
        "fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "most_recent_timestamp": 1783618458,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
        "instance_count": 1
      },
      {
        "fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "most_recent_timestamp": 1783618204,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "instance_count": 1
      },
      {
        "fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "most_recent_timestamp": 1783618126,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
        "instance_count": 1
      },
      {
        "fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "most_recent_timestamp": 1783618126,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
        "instance_count": 1
      },
      {
        "fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "most_recent_timestamp": 1783618119,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/627315ab66d5250fec7ec574b073f1095879a8a4",
        "instance_count": 3
      },
      {
        "fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "most_recent_timestamp": 1783618492,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/b8e6c03975a5701e3e8d198549f463989f1a00f4",
        "instance_count": 1
      },
      {
        "fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "most_recent_timestamp": 1783618209,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
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

