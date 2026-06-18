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
    "snapshot_id": "aws-beta#7240",
    "artifacts": [
      {
        "fingerprint": "024abeaf878f55e501869bdfcef2651d04084fa5492a6c515c5146d6a4ebd756",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7d472fe@sha256:024abeaf878f55e501869bdfcef2651d04084fa5492a6c515c5146d6a4ebd756",
        "most_recent_timestamp": 1781439988,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/7d472fe23646dcf286e7845258598d9846df636b",
        "instance_count": 1
      },
      {
        "fingerprint": "4ab912309304956f1b462acd0313170d4eef00fd46ee06921c7a60978001273d",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b909280@sha256:4ab912309304956f1b462acd0313170d4eef00fd46ee06921c7a60978001273d",
        "most_recent_timestamp": 1781436253,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/b909280dcfac31d336ec145a90d73e0904dd2bb7",
        "instance_count": 1
      },
      {
        "fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "most_recent_timestamp": 1781436120,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "instance_count": 3
      },
      {
        "fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "most_recent_timestamp": 1781597233,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
        "instance_count": 3
      },
      {
        "fingerprint": "b62ed52cf05c8482962b91ab0ac5334719e692634286723ddcd41f7bf60d9305",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:063682d@sha256:b62ed52cf05c8482962b91ab0ac5334719e692634286723ddcd41f7bf60d9305",
        "most_recent_timestamp": 1781440008,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/063682da313984cd0d9c6c0e111eb1090aa03f9b",
        "instance_count": 1
      },
      {
        "fingerprint": "baec4fc23097cbc40348caa9b7fdcf6bfbeec8f48fc697bf3e7002460a605874",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:eeb4288@sha256:baec4fc23097cbc40348caa9b7fdcf6bfbeec8f48fc697bf3e7002460a605874",
        "most_recent_timestamp": 1781439984,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/eeb4288778e41b2d7d54d333d6b09514a947f693",
        "instance_count": 1
      },
      {
        "fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "most_recent_timestamp": 1781440688,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "instance_count": 1
      },
      {
        "fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "most_recent_timestamp": 1781436093,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "instance_count": 1
      }
    ]
  },
  "snappish2": {
    "snapshot_id": "aws-prod#4781",
    "artifacts": [
      {
        "fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "most_recent_timestamp": 1781590572,
        "flow": "web-ci",
        "commit_url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
        "instance_count": 3
      },
      {
        "fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "most_recent_timestamp": 1781590577,
        "flow": "runner-ci",
        "commit_url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904",
        "instance_count": 3
      },
      {
        "fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "most_recent_timestamp": 1781590471,
        "flow": "dashboard-ci",
        "commit_url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338",
        "instance_count": 1
      },
      {
        "fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "most_recent_timestamp": 1781590460,
        "flow": "differ-ci",
        "commit_url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08",
        "instance_count": 1
      },
      {
        "fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "most_recent_timestamp": 1781590480,
        "flow": "languages-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda",
        "instance_count": 1
      },
      {
        "fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "most_recent_timestamp": 1781590462,
        "flow": "custom-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
        "instance_count": 1
      },
      {
        "fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "most_recent_timestamp": 1781590465,
        "flow": "exercises-start-points-ci",
        "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
        "instance_count": 1
      },
      {
        "fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "most_recent_timestamp": 1781590483,
        "flow": "saver-ci",
        "commit_url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
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
        "fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
        "most_recent_timestamp": 1781590473,
        "flow": "nginx-ci",
        "commit_url": "https://github.com/cyber-dojo/nginx/commit/706526874659341458da5bb21903a6423c0a5a29",
        "instance_count": 1
      },
      {
        "fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "most_recent_timestamp": 1781592148,
        "flow": "creator-ci",
        "commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
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

