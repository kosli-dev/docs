---
title: "kosli get snapshot"
description: "Get a specified environment snapshot.  "
---

## Synopsis

```shell
kosli get snapshot ENVIRONMENT-NAME-OR-EXPRESSION [flags]
```

Get a specified environment snapshot.  
ENVIRONMENT-NAME-OR-EXPRESSION can be specified as follows:
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
|    `-h`, `--help`  |  help for snapshot  |
|    `-o`, `--output` string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |


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

To view a live example of 'kosli get snapshot' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli get snapshot aws-prod --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
{
  "index": 4972,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1783576438.7264173,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4972",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:28fc01e@sha256:579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-116",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
      "creationTimestamp": [
        1783325287,
        1783325290,
        1783325295
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/28fc01e77500cdb35522d5f27aad95b501a03cdc",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4?artifact_id=11490640-912f-4740-8ac5-1890457d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/552f300213a65ee0c8c773474d75b26b2d723575...28fc01e77500cdb35522d5f27aad95b501a03cdc",
        "previous_git_commit": "552f300213a65ee0c8c773474d75b26b2d723575",
        "previous_fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
        "previous_trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 179002.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
          "template_reference_name": "runner",
          "git_commit": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/28fc01e77500cdb35522d5f27aad95b501a03cdc",
          "git_commit_info": {
            "sha1": "28fc01e77500cdb35522d5f27aad95b501a03cdc",
            "message": "Merge pull request #264 from cyber-dojo/remove-git-from-runner-image\n\nRemove git from the runner image to drop 18 Alpine libcurl CVEs",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783146285.0,
            "url": "https://github.com/cyber-dojo/runner/commit/28fc01e77500cdb35522d5f27aad95b501a03cdc"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4?artifact_id=11490640-912f-4740-8ac5-1890457d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/552f300213a65ee0c8c773474d75b26b2d723575...28fc01e77500cdb35522d5f27aad95b501a03cdc",
            "previous_git_commit": "552f300213a65ee0c8c773474d75b26b2d723575",
            "previous_fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
            "previous_trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 179002.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-116",
          "template_reference_name": "runner",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4?artifact_id=5e295bbe-2edd-4d3d-bb0a-08815e15",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-109",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 418179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
          "template_reference_name": "runner",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4?artifact_id=5ce38e2a-8bbd-4320-a5f3-fe8df4ad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:84d9fee@sha256:3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "runner-3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 525984.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4",
          "template_reference_name": "runner",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/579d2668834cf42f3004e005c295d340dfd3da5b33f394d3151c016dc9f074a4?artifact_id=cd8b9fa2-7a66-45ea-bb69-05e4c5e3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 525984.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9471569a6185428bbbf355b753498f43",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cbf0063@sha256:c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-118",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
      "creationTimestamp": [
        1783329868
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "cbf0063e279351ffb201b39296e9bfe892dc772f",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c?artifact_id=8305b55d-4d0c-4860-b2c5-2895665f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf...cbf0063e279351ffb201b39296e9bfe892dc772f",
        "previous_git_commit": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
        "previous_fingerprint": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
        "previous_trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 1032.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
          "template_reference_name": "nginx",
          "git_commit": "cbf0063e279351ffb201b39296e9bfe892dc772f",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f",
          "git_commit_info": {
            "sha1": "cbf0063e279351ffb201b39296e9bfe892dc772f",
            "message": "Merge pull request #153 from cyber-dojo/gate-tests-on-runner-health\n\nGate test containers on runner health and quiet urllib3 warning",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783328836.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c?artifact_id=8305b55d-4d0c-4860-b2c5-2895665f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf...cbf0063e279351ffb201b39296e9bfe892dc772f",
            "previous_git_commit": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
            "previous_fingerprint": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
            "previous_trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1032.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-118",
          "template_reference_name": "nginx",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c?artifact_id=70aa7fd1-2f35-4df5-a224-af3c72e2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c03b1c05559f7bf6e23c890bcbddd6262f008ae9...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
            "previous_fingerprint": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
            "previous_trail_name": "promotion-one-108",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 422760.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
          "template_reference_name": "nginx",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c?artifact_id=4a297bfe-1e77-4e87-9527-d378f2cc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_fingerprint": "8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:66c0766@sha256:8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_trail_name": "nginx-8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 530565.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
          "template_reference_name": "nginx",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c?artifact_id=737ed425-1fc4-49ff-8724-f777694b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 530565.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2769f645898d47daba74686447f4965e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
      "creationTimestamp": [
        1783075863
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "6ff6b4c71ab218d39065654bef32839b9226d21f",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=26dd06bd-0d63-4775-a3d1-db332cf0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/c174ef247b1efb95812373fde2a8e8db3a9ede03...6ff6b4c71ab218d39065654bef32839b9226d21f",
        "previous_git_commit": "c174ef247b1efb95812373fde2a8e8db3a9ede03",
        "previous_fingerprint": "8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:c174ef2@sha256:8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/c174ef247b1efb95812373fde2a8e8db3a9ede03",
        "previous_trail_name": "c174ef247b1efb95812373fde2a8e8db3a9ede03",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 14188.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
          "template_reference_name": "creator",
          "git_commit": "6ff6b4c71ab218d39065654bef32839b9226d21f",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
          "git_commit_info": {
            "sha1": "6ff6b4c71ab218d39065654bef32839b9226d21f",
            "message": "Dockerfile - Automated base-image update (#37)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783061675.0,
            "url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=26dd06bd-0d63-4775-a3d1-db332cf0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/c174ef247b1efb95812373fde2a8e8db3a9ede03...6ff6b4c71ab218d39065654bef32839b9226d21f",
            "previous_git_commit": "c174ef247b1efb95812373fde2a8e8db3a9ede03",
            "previous_fingerprint": "8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:c174ef2@sha256:8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/c174ef247b1efb95812373fde2a8e8db3a9ede03",
            "previous_trail_name": "c174ef247b1efb95812373fde2a8e8db3a9ede03",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 14188.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "creator",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=863376ee-2919-44bd-ac98-1f3ead0b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:c174ef2@sha256:8130ae297936df0b6b15cd5a561d71457a82a41acf7b2da27da113b8333c8005",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-28",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 168755.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
          "template_reference_name": "creator",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=f2ce0f30-79e0-4c5e-b7cf-26b98d06",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 276560.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
          "template_reference_name": "creator",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8?artifact_id=e3ad8f8f-461d-4861-9ac8-a37bd7cf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 276560.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/290a2fb12a09478b8ab339ff542d7390",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
      "creationTimestamp": [
        1783075535,
        1783075540,
        1783075624
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
      "commit_url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=f065965e-194b-43a5-a688-00797359",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/fbe04c6016bd7822a9b0b948043614186787194f...97ebee56e01ca3af95bfcae0c7c328eee8c56865",
        "previous_git_commit": "fbe04c6016bd7822a9b0b948043614186787194f",
        "previous_fingerprint": "5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fbe04c6@sha256:5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fbe04c6016bd7822a9b0b948043614186787194f",
        "previous_trail_name": "fbe04c6016bd7822a9b0b948043614186787194f",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 13875.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
          "template_reference_name": "web",
          "git_commit": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
          "commit_url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865",
          "git_commit_info": {
            "sha1": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
            "message": "Dockerfile - Automated base-image update (#377)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783061660.0,
            "url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=f065965e-194b-43a5-a688-00797359",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/fbe04c6016bd7822a9b0b948043614186787194f...97ebee56e01ca3af95bfcae0c7c328eee8c56865",
            "previous_git_commit": "fbe04c6016bd7822a9b0b948043614186787194f",
            "previous_fingerprint": "5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fbe04c6@sha256:5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fbe04c6016bd7822a9b0b948043614186787194f",
            "previous_trail_name": "fbe04c6016bd7822a9b0b948043614186787194f",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 13875.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "web",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=c4b87590-b427-449e-b571-f1d4c0d7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fbe04c6@sha256:5c05964970f34b50fff834c589f026967722784fb02622fe8cb769100189aefc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-28",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 168427.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
          "template_reference_name": "web",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=60d6053f-72d9-4149-9621-91539d41",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 276232.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
          "template_reference_name": "web",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab?artifact_id=52160d71-469a-444d-8da4-7acc6afa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 276232.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e363472d4edb40afb8214f90a3694610",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
      "creationTimestamp": [
        1783075608
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=87705eca-ac37-4632-93de-c4f63539",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f7fd6b78302ad399252990b0b81f54d7416a402f...6d203a85ffda1513db4d86d4e48b1f969bd2f510",
        "previous_git_commit": "f7fd6b78302ad399252990b0b81f54d7416a402f",
        "previous_fingerprint": "746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f7fd6b7@sha256:746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f7fd6b78302ad399252990b0b81f54d7416a402f",
        "previous_trail_name": "f7fd6b78302ad399252990b0b81f54d7416a402f",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 13944.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
          "template_reference_name": "dashboard",
          "git_commit": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510",
          "git_commit_info": {
            "sha1": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
            "message": "Dockerfile - Automated base-image update (#411)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783061664.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=87705eca-ac37-4632-93de-c4f63539",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f7fd6b78302ad399252990b0b81f54d7416a402f...6d203a85ffda1513db4d86d4e48b1f969bd2f510",
            "previous_git_commit": "f7fd6b78302ad399252990b0b81f54d7416a402f",
            "previous_fingerprint": "746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f7fd6b7@sha256:746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f7fd6b78302ad399252990b0b81f54d7416a402f",
            "previous_trail_name": "f7fd6b78302ad399252990b0b81f54d7416a402f",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 13944.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "dashboard",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=555079f1-357b-4a32-ae7a-7bc54bf8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f7fd6b7@sha256:746b907bc4bd5d5b685299448a0db9e838d6b003036e014467fc097ae8bbb115",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-28",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 168500.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
          "template_reference_name": "dashboard",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=1568178b-5932-4757-9934-d63d9a18",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 276305.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
          "template_reference_name": "dashboard",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc?artifact_id=b6e1ce03-9e3c-4e7b-99d1-d00697a7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 276305.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c6ffde8231994f30a62d590408ab2c62",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
      "creationTimestamp": [
        1783075605
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=651b0c78-5926-41b5-ba5b-9aa87601",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/ca386e022a6857ad4ea8cfcc765a574452555ac7...04e0e14bb8874ab521d35c97d6040133f0d2143a",
        "previous_git_commit": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
        "previous_fingerprint": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7",
        "previous_trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 894.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
          "template_reference_name": "languages-start-points",
          "git_commit": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
          "git_commit_info": {
            "sha1": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
            "message": "Merge pull request #240 from cyber-dojo/update-base-image-df28e04\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783074711.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=651b0c78-5926-41b5-ba5b-9aa87601",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/ca386e022a6857ad4ea8cfcc765a574452555ac7...04e0e14bb8874ab521d35c97d6040133f0d2143a",
            "previous_git_commit": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
            "previous_fingerprint": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7",
            "previous_trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 894.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "languages-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=954b3ac9-012b-4de3-8bca-660d22f4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/935669068568593a9658781a56bb6cab5686e136...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "935669068568593a9658781a56bb6cab5686e136",
            "previous_fingerprint": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/935669068568593a9658781a56bb6cab5686e136",
            "previous_trail_name": "promotion-one-106",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 168497.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
          "template_reference_name": "languages-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=7159ee85-fb1d-42f3-95ae-84e8d068",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 276302.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
          "template_reference_name": "languages-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c?artifact_id=92a3adb1-1f24-402d-8010-45b78e84",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 276302.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/118a5d27d65a480691a4825ea02ee2b3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
      "creationTimestamp": [
        1783075532
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=494ad51d-feff-4795-9fec-f2a8b953",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/9d1887776497e501bc8dcd46e508488bf5c8b0c8...26dcd06257a4bb00d594dbb5de05eefbb7b20379",
        "previous_git_commit": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
        "previous_fingerprint": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8",
        "previous_trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 13687.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
          "template_reference_name": "differ",
          "git_commit": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379",
          "git_commit_info": {
            "sha1": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
            "message": "Dockerfile - Automated base-image update (#423)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783061845.0,
            "url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=494ad51d-feff-4795-9fec-f2a8b953",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/9d1887776497e501bc8dcd46e508488bf5c8b0c8...26dcd06257a4bb00d594dbb5de05eefbb7b20379",
            "previous_git_commit": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
            "previous_fingerprint": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8",
            "previous_trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 13687.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "differ",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=69127bc9-04c4-481d-acc7-114577e6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-115",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 168424.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
          "template_reference_name": "differ",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=50b67af4-0e3a-429d-bcbd-cc3f042a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 276229.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
          "template_reference_name": "differ",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7?artifact_id=e37be1de-1b29-4cfa-8823-5159eed0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 276229.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/acbe6af657b94a548853a92851e4eae2",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:2fa0324@sha256:1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
      "creationTimestamp": [
        1783075531
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/2fa032402c47885c2fcf8036e2eee07ac73bdc41",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=eea73af9-c6cf-45f6-8ab3-7181c587",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/139dc6d316a5e4b66755fecc926f2e25cd5c8208...2fa032402c47885c2fcf8036e2eee07ac73bdc41",
        "previous_git_commit": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
        "previous_fingerprint": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208",
        "previous_trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 13873.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
          "template_reference_name": "saver",
          "git_commit": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/2fa032402c47885c2fcf8036e2eee07ac73bdc41",
          "git_commit_info": {
            "sha1": "2fa032402c47885c2fcf8036e2eee07ac73bdc41",
            "message": "Dockerfile - Automated base-image update (#421)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783061658.0,
            "url": "https://github.com/cyber-dojo/saver/commit/2fa032402c47885c2fcf8036e2eee07ac73bdc41"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=eea73af9-c6cf-45f6-8ab3-7181c587",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/139dc6d316a5e4b66755fecc926f2e25cd5c8208...2fa032402c47885c2fcf8036e2eee07ac73bdc41",
            "previous_git_commit": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
            "previous_fingerprint": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208",
            "previous_trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 13873.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "saver",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=b88b9d51-5534-45c4-baa9-ee01d4ce",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-111",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 168423.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
          "template_reference_name": "saver",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=eeb36073-374e-4a57-bda1-f1a219f0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 276228.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59",
          "template_reference_name": "saver",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1912e229b2a9e288d099af648ebcb993c16976284f61578a3730d35c33329b59?artifact_id=c19577cd-942c-4c9e-9a82-589ea6ec",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 276228.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c875762ad1a940fd9ed5218d13bbae4a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
      "creationTimestamp": [
        1783075526
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=329017a5-5366-400d-928a-193ea961",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/ae0c2f039480061d958cc007bc4c78e5b0f36a83...fc6b09be0518fbf8ab76815cb85b1745631e3659",
        "previous_git_commit": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
        "previous_fingerprint": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83",
        "previous_trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 870.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
          "template_reference_name": "custom-start-points",
          "git_commit": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659",
          "git_commit_info": {
            "sha1": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
            "message": "Merge pull request #135 from cyber-dojo/update-base-image-df28e04\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783074656.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=329017a5-5366-400d-928a-193ea961",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/ae0c2f039480061d958cc007bc4c78e5b0f36a83...fc6b09be0518fbf8ab76815cb85b1745631e3659",
            "previous_git_commit": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
            "previous_fingerprint": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83",
            "previous_trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 870.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "custom-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=41666ecd-79c5-401f-abf8-95e09dba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-110",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 168418.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=6570ff39-2250-4a66-aaa3-3ac4dc0f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 276223.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1?artifact_id=22f396e9-003a-4f27-bfa9-f324a75e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 276223.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/01b4e31ec5674ba4bded8e2bd9eb01c7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "pull_request",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 3,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": []
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.tags.kind == \"build\""
                  },
                  "name": "*",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0002"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
        },
        {
          "policy_version": 4,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-aws-prod-per-artifact\""
                  },
                  "name": "snyk-container-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": "SDLC-CTRL-0022"
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"production-promotion\""
                  },
                  "name": "snyk-scan",
                  "type": "decision",
                  "must_be_compliant": true,
                  "for_control": null
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        },
        {
          "policy_version": 2,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance-aws-prod"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
      "creationTimestamp": [
        1783075521
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "80b913e9f88902428a3567f75165d8b9d73b561a",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=1f5af7a4-2ab5-4c78-982c-afb9c2b1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/17f61f83683a52ec1b9040127da582affb70e997...80b913e9f88902428a3567f75165d8b9d73b561a",
        "previous_git_commit": "17f61f83683a52ec1b9040127da582affb70e997",
        "previous_fingerprint": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997",
        "previous_trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 861.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
          "template_reference_name": "exercises-start-points",
          "git_commit": "80b913e9f88902428a3567f75165d8b9d73b561a",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a",
          "git_commit_info": {
            "sha1": "80b913e9f88902428a3567f75165d8b9d73b561a",
            "message": "Merge pull request #143 from cyber-dojo/update-base-image-df28e04\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783074660.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=1f5af7a4-2ab5-4c78-982c-afb9c2b1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/17f61f83683a52ec1b9040127da582affb70e997...80b913e9f88902428a3567f75165d8b9d73b561a",
            "previous_git_commit": "17f61f83683a52ec1b9040127da582affb70e997",
            "previous_fingerprint": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997",
            "previous_trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 861.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-29",
          "template_reference_name": "exercises-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=67896d8a-420b-4418-9fd7-c92d1386",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_fingerprint": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_trail_name": "promotion-one-101",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 168413.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=df4f4128-0451-45a5-b82c-56a3eec2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 276218.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b?artifact_id=2eb6accf-bfed-4297-bbdc-e2ad18c9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 276218.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f5dc399074644ed8a5c79c8df8751214",
        "cluster_name": null,
        "service_name": null
      }
    }
  ],
  "applied_policies": [
    {
      "id": "0b0c4d5a-cc1f-4725-8f97-af256289",
      "name": "pull-request",
      "version": 3,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": false,
            "exceptions": []
          },
          "trail_compliance": {
            "required": false,
            "exceptions": []
          },
          "attestations": [
            {
              "if_condition": {
                "text": "flow.tags.kind == \"build\""
              },
              "name": "*",
              "type": "pull_request",
              "must_be_compliant": true,
              "for_control": null
            }
          ]
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "29f67c3c-1c1f-43f8-97e6-165a4080",
      "name": "provenance",
      "version": 3,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": true,
            "exceptions": []
          },
          "trail_compliance": {
            "required": false,
            "exceptions": []
          },
          "attestations": [
            {
              "if_condition": {
                "text": "flow.tags.kind == \"build\""
              },
              "name": "*",
              "type": "decision",
              "must_be_compliant": true,
              "for_control": "SDLC-CTRL-0002"
            }
          ]
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "93d8505f-bce5-4c7c-a2c8-f98236c8",
      "name": "snyk-scan-aws-prod",
      "version": 4,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": false,
            "exceptions": []
          },
          "trail_compliance": {
            "required": false,
            "exceptions": []
          },
          "attestations": [
            {
              "if_condition": {
                "text": "flow.name == \"snyk-aws-prod-per-artifact\""
              },
              "name": "snyk-container-scan",
              "type": "decision",
              "must_be_compliant": true,
              "for_control": "SDLC-CTRL-0022"
            }
          ]
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "bdb8a802-a406-4c76-b289-3fe30be3",
      "name": "production-promotion",
      "version": 2,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": false,
            "exceptions": []
          },
          "trail_compliance": {
            "required": false,
            "exceptions": []
          },
          "attestations": [
            {
              "if_condition": {
                "text": "flow.name == \"production-promotion\""
              },
              "name": "snyk-scan",
              "type": "decision",
              "must_be_compliant": true,
              "for_control": null
            }
          ]
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "ce498d25-69dc-4f30-a71e-aa333990",
      "name": "trail-compliance-aws-prod",
      "version": 2,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": false,
            "exceptions": []
          },
          "trail_compliance": {
            "required": true,
            "exceptions": [
              {
                "if_condition": {
                  "text": "exists(flow.tags.env) and flow.tags.env != \"aws-prod\""
                }
              }
            ]
          },
          "attestations": []
        }
      },
      "failing_artifacts": []
    }
  ]
}
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="get the latest snapshot of an environment">
```shell
kosli get snapshot yourEnvironmentName

```
</Accordion>
<Accordion title="get the SECOND latest snapshot of an environment">
```shell
kosli get snapshot yourEnvironmentName~1

```
</Accordion>
<Accordion title="get the snapshot number 23 of an environment">
```shell
kosli get snapshot yourEnvironmentName#23

```
</Accordion>
<Accordion title="get the environment snapshot at midday (UTC), on valentine's day of 2023">
```shell
kosli get snapshot yourEnvironmentName@{2023-02-14T12:00:00}

```
</Accordion>
<Accordion title="get the environment snapshot based on a relative time">
```shell
kosli get snapshot yourEnvironmentName@{3.weeks.ago}
```
</Accordion>
</AccordionGroup>

