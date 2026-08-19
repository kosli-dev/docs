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
    "snapshot_id": "aws-beta#8099",
    "artifacts": [
      {
        "fingerprint": "0f760ded7dc5144ede96da884c408f9b50bd2a239aa51137adb6c8a8d7bc7f36",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:6f922fe@sha256:0f760ded7dc5144ede96da884c408f9b50bd2a239aa51137adb6c8a8d7bc7f36",
        "most_recent_timestamp": 1786438033,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/6f922fefbf719bad93fe4ea6f3b232d8cf3ed36d",
        "instance_count": 1
      },
      {
        "fingerprint": "38af9d053f174ae9068d84158c2a36dca16bf3c8c5d64b77608462aec6cdd714",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:670a1f1@sha256:38af9d053f174ae9068d84158c2a36dca16bf3c8c5d64b77608462aec6cdd714",
        "most_recent_timestamp": 1787073596,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/670a1f1d8ab52c1fb5823bb2e66b77c45e71aaa5",
        "instance_count": 3
      },
      {
        "fingerprint": "45919ac3395a18573e5ca203e750ff2e5f0fb6239d6dd5a052075b3efb7ad7ef",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9b0d9fc@sha256:45919ac3395a18573e5ca203e750ff2e5f0fb6239d6dd5a052075b3efb7ad7ef",
        "most_recent_timestamp": 1786438417,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/9b0d9fc145d30c63dc9f9648c892a52d6e96d602",
        "instance_count": 3
      },
      {
        "fingerprint": "627562d3198ac9a5d782da3db07725d48500788c2c6d86c33a5f5e77c7ec148a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:074353d@sha256:627562d3198ac9a5d782da3db07725d48500788c2c6d86c33a5f5e77c7ec148a",
        "most_recent_timestamp": 1786437210,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/074353df2a7ea1ea386a78d16300ebac1dbe94fd",
        "instance_count": 1
      },
      {
        "fingerprint": "8e7fb4cfe9953032bde5488c656ad255e49adfdd5499df2dd795dd0d984842cc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c893dbc@sha256:8e7fb4cfe9953032bde5488c656ad255e49adfdd5499df2dd795dd0d984842cc",
        "most_recent_timestamp": 1787118467,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c893dbc197ef1328b5b0bc5aacb923c9beaf9e7b",
        "instance_count": 1
      },
      {
        "fingerprint": "94e3568d1b87a42b836bafdf9f1a197e46f72b6a880477a19068c0d75b978e37",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e7e5c9@sha256:94e3568d1b87a42b836bafdf9f1a197e46f72b6a880477a19068c0d75b978e37",
        "most_recent_timestamp": 1786438497,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e7e5c906b238c47901420b1fc471bbfb7dd8d32",
        "instance_count": 1
      },
      {
        "fingerprint": "a430dad3077449b1726c4c733d01e03c3e545c7db10b8c4e8b6f619aa823b949",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:60b9a56@sha256:a430dad3077449b1726c4c733d01e03c3e545c7db10b8c4e8b6f619aa823b949",
        "most_recent_timestamp": 1786438485,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/60b9a5602ea946503b421ab54bde8006b8499780",
        "instance_count": 1
      },
      {
        "fingerprint": "b59c2c9c63a3596a8edfa2e99defcddec0aa03bb7a0c2a4842ba2972a3bfb3f3",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:9b0aede@sha256:b59c2c9c63a3596a8edfa2e99defcddec0aa03bb7a0c2a4842ba2972a3bfb3f3",
        "most_recent_timestamp": 1786438381,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/9b0aedec956238c8bb8bee21a881b378041056b4",
        "instance_count": 1
      },
      {
        "fingerprint": "c1f2c03cea7a8b0f7f9c126881fbb1f9dd22120c77cf66981e9985ef3ce73f31",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:a88b337@sha256:c1f2c03cea7a8b0f7f9c126881fbb1f9dd22120c77cf66981e9985ef3ce73f31",
        "most_recent_timestamp": 1786632554,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/a88b337310cef9b1ee259d18db3d43fed5dd9e03",
        "instance_count": 1
      },
      {
        "fingerprint": "cb082e897305969d260656d0072538eb16f4db0b2e619a831f94bd36a432287a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ec2a405@sha256:cb082e897305969d260656d0072538eb16f4db0b2e619a831f94bd36a432287a",
        "most_recent_timestamp": 1786437703,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ec2a40576cbde05e9330bf03de403c3c04a63704",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5253",
    "artifacts": [
      {
        "fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "most_recent_timestamp": 1786425083,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "instance_count": 1
      },
      {
        "fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "most_recent_timestamp": 1786425086,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad",
        "instance_count": 1
      },
      {
        "fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "most_recent_timestamp": 1786425092,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7",
        "instance_count": 1
      },
      {
        "fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
        "most_recent_timestamp": 1786425419,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33",
        "instance_count": 3
      },
      {
        "fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "most_recent_timestamp": 1785241244,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "instance_count": 1
      },
      {
        "fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "most_recent_timestamp": 1786425173,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
        "instance_count": 1
      },
      {
        "fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "most_recent_timestamp": 1786425079,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02",
        "instance_count": 1
      },
      {
        "fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
        "most_recent_timestamp": 1786425079,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e",
        "instance_count": 1
      },
      {
        "fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "most_recent_timestamp": 1785241255,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "instance_count": 1
      },
      {
        "fingerprint": "f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:85cac88@sha256:f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
        "most_recent_timestamp": 1786425514,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/85cac880cb74678426eb2ed4dbf2538995404c5c",
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
        "fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "most_recent_timestamp": 1786425512,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
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

