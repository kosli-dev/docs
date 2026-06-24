---
title: "kosli log environment"
description: "List environment events."
---

## Synopsis

```shell
kosli log environment ENV_NAME [flags]
```

List environment events.
The results are paginated and ordered from latest to oldest.
By default, the page limit is 15 events per page.

You can optionally specify an INTERVAL between two snapshot expressions with [expression]..[expression].

Expressions can be:
* ~N   N'th behind the latest snapshot
* N    snapshot number N
* NOW  the latest snapshot

Either expression can be omitted to default to NOW.

You can also filter events by range using --start/--end (snapshot index or time expression such as "NOW" or "1hour") or --start-ts/--end-ts (Unix timestamps).


## Flags
| Flag | Description |
| :--- | :--- |
|        `--end` string  |  [optional] The end of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour).  |
|        `--end-ts` float  |  [optional] The end of the events range as a Unix timestamp in seconds (integer or float).  |
|    `-h`, `--help`  |  help for environment  |
|    `-i`, `--interval` string  |  [optional] Expression to define specified snapshots range.  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|        `--page` int  |  [defaulted] The page number of a response. (default 1)  |
|    `-n`, `--page-limit` int  |  [defaulted] The number of elements per page. (default 15)  |
|        `--repo` strings  |  [optional] The name of a git repo as it is registered in Kosli. e.g kosli-dev/cli  |
|        `--reverse`  |  [optional] Reverse the order of output list.  |
|        `--start` string  |  [optional] The start of the events range. Can be a snapshot index (integer) or a time expression (e.g. NOW, 1hour).  |
|        `--start-ts` float  |  [optional] The start of the events range as a Unix timestamp in seconds (integer or float).  |


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

To view a live example of 'kosli log environment' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli log environment aws-prod --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
[
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4833,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:05fa6c1@sha256:5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
    "sha256": "5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
    "description": "3 instances changed",
    "reported_at": 1782295018.5650613,
    "pipeline": "runner-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "runner-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/c248c8e2175307f6906e4a016d09b21d177923bd...05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=6d9685ea-4831-42e9-a40c-e91cafcf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4833",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4833"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4832,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
    "sha256": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
    "description": "1 instance changed",
    "reported_at": 1782294958.7636094,
    "pipeline": "exercises-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "exercises-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "became-compliant",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1...75485ee4a18794755de633775a7b56b2b00cd7c9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=0289c6f2-2ff3-466b-8b94-12e7c2b0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4832",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4832"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
    "sha256": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "exercises-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "exercises-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": false,
    "snapshot_compliance": false,
    "type": "became-non-compliant",
    "code_diff": "https://github.com/cyber-dojo/exercises-start-points/compare/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1...75485ee4a18794755de633775a7b56b2b00cd7c9",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/exercises-start-points-ci/fingerprint/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "html": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=0289c6f2-2ff3-466b-8b94-12e7c2b0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
    "sha256": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "creator-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "creator-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/creator/compare/34f14b6fc5d87ff95426046716ec8a09141c13a7...9034c75cdb2846757cff32d24e1c5e91f40060a8",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/creator-ci/fingerprint/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
        "html": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=e8a01a2b-b310-4700-bd41-33c1c4f0"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:33b1b15@sha256:c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
    "sha256": "c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "nginx-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "nginx-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/nginx/compare/635027125d65a253a9c98bfd97d22cb3abbefa5a...33b1b15247724eee83ab795f3d586b4eac93b456",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/nginx-ci/fingerprint/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
        "html": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=a6329b0b-72c5-43cd-a27a-e2f52c79"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
    "sha256": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "differ-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "differ-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/differ/compare/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1...3e563eacf76b48caaf2f19f29472544199df8a00",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/differ-ci/fingerprint/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
        "html": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=68ef150a-fe86-4b14-845b-7bcb814f"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
    "sha256": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "languages-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "languages-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/7eeaac4c57e26887e4d027aa3c815bc2f214f934...bb8a712de74f2fe3edf48169ca072d4eff997564",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=531ae2f0-0b5f-44b9-8253-159ba612"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
    "sha256": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "dashboard-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "dashboard-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/ff89dd9bd1bfc5441854450adcf25d5aad9508f4...0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=5bbbda58-e526-4b64-9f80-6adcda47"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
    "sha256": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
    "description": "3 instances changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "web-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "web-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/web/compare/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1...42ca333501c90d2cf36ce24035aa0a468e287da4",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/web-ci/fingerprint/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
        "html": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=ad37f417-d1a3-4744-a7b9-f2dec951"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
    "sha256": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "saver-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "saver-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/fbae360261d949b25a66a927921e757d4d064543...a35d09232116daff39d0f939cb133edc5750e2a1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=85ae3f6e-d663-406b-9d5a-fcf95308"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4831,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
    "sha256": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
    "description": "1 instance changed",
    "reported_at": 1782294898.7202442,
    "pipeline": "custom-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "custom-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-prod-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": false,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/custom-start-points/compare/843d6556ec718da1a1f51ce906c8c5bd6366d691...514f79a280dee08bf889a4a4fdf41c9d2f231348",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/custom-start-points-ci/fingerprint/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
        "html": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=b20812a6-ee26-4984-97e9-87c4be75"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4831",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4831"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4830,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:05fa6c1@sha256:5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
    "sha256": "5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
    "description": "3 instances changed",
    "reported_at": 1782294418.6282794,
    "pipeline": "runner-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "runner-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/runner/compare/c248c8e2175307f6906e4a016d09b21d177923bd...05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner-ci/fingerprint/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
        "html": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=6d9685ea-4831-42e9-a40c-e91cafcf"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4830",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4830"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4829,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
    "sha256": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
    "description": "1 instance changed",
    "reported_at": 1782294298.6604407,
    "pipeline": "languages-start-points-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "languages-start-points-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/languages-start-points/compare/7eeaac4c57e26887e4d027aa3c815bc2f214f934...bb8a712de74f2fe3edf48169ca072d4eff997564",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/languages-start-points-ci/fingerprint/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "html": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=531ae2f0-0b5f-44b9-8253-159ba612"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4829",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4829"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4829,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
    "sha256": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
    "description": "1 instance changed",
    "reported_at": 1782294298.6604407,
    "pipeline": "saver-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "saver-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/saver/compare/fbae360261d949b25a66a927921e757d4d064543...a35d09232116daff39d0f939cb133edc5750e2a1",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/saver-ci/fingerprint/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "html": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=85ae3f6e-d663-406b-9d5a-fcf95308"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4829",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4829"
      }
    }
  },
  {
    "environment_name": "aws-prod",
    "snapshot_index": 4829,
    "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
    "sha256": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
    "description": "1 instance changed",
    "reported_at": 1782294298.6604407,
    "pipeline": "dashboard-ci",
    "deployments": [],
    "flows": [
      {
        "flow_name": "dashboard-ci",
        "deployments": null
      },
      {
        "flow_name": "production-promotion",
        "deployments": null
      },
      {
        "flow_name": "snyk-aws-beta-per-artifact",
        "deployments": null
      }
    ],
    "artifact_compliance": true,
    "snapshot_compliance": true,
    "type": "updated-provenance",
    "code_diff": "https://github.com/cyber-dojo/dashboard/compare/ff89dd9bd1bfc5441854450adcf25d5aad9508f4...0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
    "_links": {
      "artifact": {
        "self": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/dashboard-ci/fingerprint/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "html": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=5bbbda58-e526-4b64-9f80-6adcda47"
      },
      "snapshot": {
        "self": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/4829",
        "html": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4829"
      }
    }
  }
]
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list the last 15 events for an environment">
```shell
kosli log environment yourEnvironmentName 

```
</Accordion>
<Accordion title="list the last 30 events for an environment">
```shell
kosli log environment yourEnvironmentName 
	--page-limit 30 

```
</Accordion>
<Accordion title="list the last 30 events for an environment (in JSON)">
```shell
kosli log environment yourEnvironmentName 
	--page-limit 30 
	--output json

```
</Accordion>
<Accordion title="list events for an environment filtered by repo">
```shell
kosli log environment yourEnvironmentName 
	--repo yourOrg/yourRepo 

```
</Accordion>
<Accordion title="list events for an environment filtered by multiple repos">
```shell
kosli log environment yourEnvironmentName 
	--repo yourOrg/yourRepo1 
	--repo yourOrg/yourRepo2 

```
</Accordion>
<Accordion title="list events starting from snapshot 5">
```shell
kosli log environment yourEnvironmentName 
	--start 5 

```
</Accordion>
<Accordion title="list events between two time expressions">
```shell
kosli log environment yourEnvironmentName 
	--start 1hour 
	--end NOW 

```
</Accordion>
<Accordion title="list events between two Unix timestamps">
```shell
kosli log environment yourEnvironmentName 
	--start-ts 1700000000 
	--end-ts 1700086400 
```
</Accordion>
</AccordionGroup>

