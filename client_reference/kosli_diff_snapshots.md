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
    "snapshot_id": "aws-beta#8212",
    "artifacts": [
      {
        "fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "most_recent_timestamp": 1787842273,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
        "instance_count": 1
      },
      {
        "fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "most_recent_timestamp": 1787838843,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "instance_count": 1
      },
      {
        "fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "most_recent_timestamp": 1787905359,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "instance_count": 3
      },
      {
        "fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "most_recent_timestamp": 1787838873,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "instance_count": 1
      },
      {
        "fingerprint": "42f74d552d375d0e991d8d39abf07432a1b449ae5bc8ae5f71ed319de5d34a5d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9f52d31@sha256:42f74d552d375d0e991d8d39abf07432a1b449ae5bc8ae5f71ed319de5d34a5d",
        "most_recent_timestamp": 1787293862,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/9f52d31fe193e246154b5c7c51d0b0cd9e2072c8",
        "instance_count": 1
      },
      {
        "fingerprint": "596f149446bad7e8b1dfef6dbf4d036457339b984b22a05082c75ef2bde3e236",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7f0fb7b@sha256:596f149446bad7e8b1dfef6dbf4d036457339b984b22a05082c75ef2bde3e236",
        "most_recent_timestamp": 1787895830,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/7f0fb7b049c2b9ceea5915b4fe780ca4090a289c",
        "instance_count": 3
      },
      {
        "fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "most_recent_timestamp": 1787903592,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "instance_count": 1
      },
      {
        "fingerprint": "71396a2c412c74a2d4c1760bfbb031f8dfc6e0e3883ebc31b4435b84b650f93b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fa3e5bd@sha256:71396a2c412c74a2d4c1760bfbb031f8dfc6e0e3883ebc31b4435b84b650f93b",
        "most_recent_timestamp": 1787838882,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/fa3e5bd70ef8934b073a8b77c2f99e6c22636156",
        "instance_count": 1
      },
      {
        "fingerprint": "97ff43a94b80b95ac2ac96c0fb5968537211d4953e280c96cf37f9c6b0ff0fb4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:85d6c9c@sha256:97ff43a94b80b95ac2ac96c0fb5968537211d4953e280c96cf37f9c6b0ff0fb4",
        "most_recent_timestamp": 1787838873,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/85d6c9c55ce1ed15a152200ce5002e06ba5ea71b",
        "instance_count": 1
      },
      {
        "fingerprint": "c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d64d2b1@sha256:c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
        "most_recent_timestamp": 1787835781,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/d64d2b11879179255f11dc991e81fbaf4a040264",
        "instance_count": 1
      },
      {
        "fingerprint": "c6f812210fa473dd413a730c93e20b3f4c00fde358a67623f1c01916858c8046",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:dbf0c0f@sha256:c6f812210fa473dd413a730c93e20b3f4c00fde358a67623f1c01916858c8046",
        "most_recent_timestamp": 1787837228,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/dbf0c0f13b6df5bc50b4616cc0f7c1c22bb91e24",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#5285",
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
        "fingerprint": "f362f331cd56af641d03b9f647795f95c3a0d597a5e7ff659788f9dfec4fe8d9",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7661027@sha256:f362f331cd56af641d03b9f647795f95c3a0d597a5e7ff659788f9dfec4fe8d9",
        "most_recent_timestamp": 1787665129,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/76610271f641f1a5634465e97f880dfe019e515e",
        "instance_count": 3
      },
      {
        "fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "most_recent_timestamp": 1786425512,
        "flow": "spooler-ci",
        "commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
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

