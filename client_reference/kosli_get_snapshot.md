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
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshot |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |


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
  "index": 5611,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1794992818.4600863,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5611",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
                    "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
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
      "fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
      "creationTimestamp": [
        1794908746
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "787de90aa159f24ec115fd42b3ddfbe44996171f",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=1719331a-74d2-4463-8e44-91a0c49a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/6baf18253638f0417e2dc20d71804cc6db5329c5...787de90aa159f24ec115fd42b3ddfbe44996171f",
        "previous_git_commit": "6baf18253638f0417e2dc20d71804cc6db5329c5",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5",
        "previous_fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 259610.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
          "template_reference_name": "saver",
          "git_commit": "787de90aa159f24ec115fd42b3ddfbe44996171f",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
          "git_commit_info": {
            "sha1": "787de90aa159f24ec115fd42b3ddfbe44996171f",
            "message": "Dockerfile - Automated base-image update (#470)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649136.0,
            "url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=1719331a-74d2-4463-8e44-91a0c49a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/6baf18253638f0417e2dc20d71804cc6db5329c5...787de90aa159f24ec115fd42b3ddfbe44996171f",
            "previous_git_commit": "6baf18253638f0417e2dc20d71804cc6db5329c5",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5",
            "previous_fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 259610.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "saver",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=ce1f8e13-1ccc-40e7-bf1a-da430408",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-43",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3259474.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
          "template_reference_name": "saver",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=50b2d52b-8475-4910-a5ce-38683a10",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -76759.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
          "template_reference_name": "saver",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f?artifact_id=1fabcd48-1cce-4f66-80b0-b57f9d8f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -76759.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b250d5357c3647fa9a01f0e0c6c69280",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
                    "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
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
      "fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
      "creationTimestamp": [
        1794908743
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "530926abbebc41a1201839ccc5d8a4b1062315eb",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=df8ba5d9-7719-4a38-8dac-3bf6b2d5",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6...530926abbebc41a1201839ccc5d8a4b1062315eb",
        "previous_git_commit": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
        "previous_fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 258341.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
          "template_reference_name": "exercises-start-points",
          "git_commit": "530926abbebc41a1201839ccc5d8a4b1062315eb",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
          "git_commit_info": {
            "sha1": "530926abbebc41a1201839ccc5d8a4b1062315eb",
            "message": "Merge pull request #161 from cyber-dojo/update-base-image-e854e8f\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794650402.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=df8ba5d9-7719-4a38-8dac-3bf6b2d5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6...530926abbebc41a1201839ccc5d8a4b1062315eb",
            "previous_git_commit": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
            "previous_fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 258341.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "exercises-start-points",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=7f9ebcdd-2a6e-476e-805e-4bb52947",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 3259471.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
          "template_reference_name": "exercises-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=ad02a55d-04a0-4035-9441-3c3fbcd2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -76762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
          "template_reference_name": "exercises-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9?artifact_id=e3eb0b72-7fb5-4912-8945-f5b40a60",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -76762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fd95e51e40624e2aafb804abb26010a1",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
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
      "fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
      "creationTimestamp": [
        1794908645
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
      "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=4a4c1d74-d625-49d3-a1db-8bc75ca9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_fingerprint": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 259537.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "template_reference_name": "creator",
          "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
          "git_commit_info": {
            "sha1": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "message": "Dockerfile - Automated base-image update (#478)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649108.0,
            "url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=4a4c1d74-d625-49d3-a1db-8bc75ca9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_fingerprint": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 259537.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "web",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=72b25346-bfa5-4f03-b7a6-0ac498ff",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3259373.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=46020b9f-44bf-4fad-b541-f55e181d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -76860.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a?artifact_id=20948ac0-4c4c-47a6-ae5e-01ace645",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -76860.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4ac5a8937a1a4da08c527cc03c02796d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
                    "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
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
      "fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
      "creationTimestamp": [
        1794908500
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=b99341a1-9cf9-44d5-9c69-ef3848e7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9fcbc9ef1306b6fed965cecfd4ff778582015fa3...bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "previous_git_commit": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
        "previous_fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 258090.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
          "template_reference_name": "languages-start-points",
          "git_commit": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
          "git_commit_info": {
            "sha1": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
            "message": "Merge pull request #306 from cyber-dojo/update-base-image-e854e8f\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794650410.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=b99341a1-9cf9-44d5-9c69-ef3848e7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9fcbc9ef1306b6fed965cecfd4ff778582015fa3...bd40ecfc45d8682a287d9200389b0a45b4d10e73",
            "previous_git_commit": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
            "previous_fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 258090.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "languages-start-points",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=4361d06d-2030-4ecc-8b82-608f0580",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 3259228.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
          "template_reference_name": "languages-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=d9b4e470-a94f-4fc6-b070-99d39793",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -77005.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
          "template_reference_name": "languages-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0?artifact_id=3bd5b39a-a2c2-4821-bd17-286f8c54",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -77005.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/55530818c842460d8c52197b03b1acfb",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
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
      "fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
      "creationTimestamp": [
        1794908247,
        1794908253,
        1794908253
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
      "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=dbd74cdd-737f-4a42-b48c-9cb6e31d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 259139.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "template_reference_name": "web",
          "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
          "git_commit_info": {
            "sha1": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "message": "Dockerfile - Automated base-image update (#478)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649108.0,
            "url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=dbd74cdd-737f-4a42-b48c-9cb6e31d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 259139.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "web",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=e3a0bb12-39bd-4217-87a3-487cb208",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3258975.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=59ef0e5f-441d-43e1-8b56-1cff3335",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -77258.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642?artifact_id=734d6173-5960-472c-b967-fd04c30c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -77258.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/95a9a88838664b1a930a458ab869722b",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
                    "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
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
      "fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
      "creationTimestamp": [
        1794908167
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
      "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=6509b70e-7a40-41f6-b28d-248a47ac",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 259059.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "template_reference_name": "dashboard",
          "git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
          "commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
          "git_commit_info": {
            "sha1": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "message": "Dockerfile - Automated base-image update (#478)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649108.0,
            "url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=6509b70e-7a40-41f6-b28d-248a47ac",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/fd680a809587fa6e4071fe874d63192f65f251c1...049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 259059.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "web",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=caa81af8-10ea-4f8c-9b2f-390c8176",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3258895.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=76411d7a-cbae-41bd-8275-793f1c2e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -77338.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
          "template_reference_name": "web",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858?artifact_id=ad17141e-36b2-4acf-8434-f14efeb0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -77338.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/dc290073634146729d702297674fb959",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
                    "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
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
      "fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
      "creationTimestamp": [
        1794908162,
        1794908162,
        1794908166
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "799f82f087a0029f9b4c3a9d85db930752190e09",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=816fae65-4857-47e1-8a9a-82836f5e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e...799f82f087a0029f9b4c3a9d85db930752190e09",
        "previous_git_commit": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
        "previous_fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 258938.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
          "template_reference_name": "runner",
          "git_commit": "799f82f087a0029f9b4c3a9d85db930752190e09",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
          "git_commit_info": {
            "sha1": "799f82f087a0029f9b4c3a9d85db930752190e09",
            "message": "Dockerfile - Automated base-image update (#331)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649224.0,
            "url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=816fae65-4857-47e1-8a9a-82836f5e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e...799f82f087a0029f9b4c3a9d85db930752190e09",
            "previous_git_commit": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
            "previous_fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 258938.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "runner",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=e54e2f7c-81b9-4613-adfe-74d50045",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 3258890.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
          "template_reference_name": "runner",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=931ca5cf-022a-4e2f-9986-c489dbd2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -77343.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
          "template_reference_name": "runner",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17?artifact_id=40cd3ef1-0b8b-42e6-9860-efcc8e51",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -77343.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f353597b8b024145a265354d7c627d9f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
                    "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
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
      "fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
      "creationTimestamp": [
        1794908165
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=f741ae29-7cc4-44e5-a2bd-9168c06b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93...6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "previous_git_commit": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
        "previous_fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 258935.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
          "template_reference_name": "differ",
          "git_commit": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
          "git_commit_info": {
            "sha1": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
            "message": "Dockerfile - Automated base-image update (#526)",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649230.0,
            "url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=f741ae29-7cc4-44e5-a2bd-9168c06b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93...6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
            "previous_git_commit": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
            "previous_fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 258935.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "differ",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=c8eb90ba-dba8-4d52-84a0-17b3a5d3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-43",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3258893.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
          "template_reference_name": "differ",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=a02c113e-1081-4ba7-8267-f4119df3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -77340.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
          "template_reference_name": "differ",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea?artifact_id=a0bd580e-766b-4fb5-bbdb-e144502e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -77340.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2cb0a6ece60240a59ac0adf275671958",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
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
      "fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
      "creationTimestamp": [
        1794908607
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=6d758363-e084-4e25-bd81-2bb19e66",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/4bb52cbbdefcd01d973f91b08fd9b5b386570c80...56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "previous_git_commit": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
        "previous_fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 259489.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
          "template_reference_name": "spooler",
          "git_commit": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
          "git_commit_info": {
            "sha1": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
            "message": "Merge pull request #30 from cyber-dojo/update-base-image-7821b64\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794649118.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=6d758363-e084-4e25-bd81-2bb19e66",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/4bb52cbbdefcd01d973f91b08fd9b5b386570c80...56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
            "previous_git_commit": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
            "previous_fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 259489.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "spooler",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=2d44b0c1-213e-4bfa-99c2-11447c61",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 3259335.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
          "template_reference_name": "spooler",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=8f583461-6a40-45b3-bd1e-8b6e6dca",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": -76898.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
          "template_reference_name": "spooler",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7?artifact_id=bab2194b-d97d-4129-b53b-8dea3c0a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": -76898.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5e8dbd6e0a9944ed8fdd677c8380570e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a173ddb@sha256:7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
                    "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
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
      "fingerprint": "7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
      "creationTimestamp": [
        1794908404
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "a173ddba4169059477911c4fa0c73674407712a5",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/a173ddba4169059477911c4fa0c73674407712a5",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=6d1a6233-1cf8-46ed-8e60-5959a5a3",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/b52ea1fb0b04c2cda0bff8db8887d019a7a81637...a173ddba4169059477911c4fa0c73674407712a5",
        "previous_git_commit": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
        "previous_fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 264142.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "a173ddba4169059477911c4fa0c73674407712a5",
          "template_reference_name": "nginx",
          "git_commit": "a173ddba4169059477911c4fa0c73674407712a5",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/a173ddba4169059477911c4fa0c73674407712a5",
          "git_commit_info": {
            "sha1": "a173ddba4169059477911c4fa0c73674407712a5",
            "message": "Merge pull request #190 from cyber-dojo/run-workflow-161\n\nBuild new image to pickup fix for new libxslt vuln",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794644262.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/a173ddba4169059477911c4fa0c73674407712a5"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=6d1a6233-1cf8-46ed-8e60-5959a5a3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/b52ea1fb0b04c2cda0bff8db8887d019a7a81637...a173ddba4169059477911c4fa0c73674407712a5",
            "previous_git_commit": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
            "previous_fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 264142.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "nginx",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=288157e3-5922-45fa-bff5-74cbca79",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-43",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 3259132.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
          "template_reference_name": "nginx",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=c343b668-b5f3-40c8-a818-246f61b9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -77101.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329",
          "template_reference_name": "nginx",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=d7b39410-035b-4869-9d2b-b73e8084",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -77101.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/0a90a8e809fc4d259ce8872bd6e4cfd6",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
                    "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-44",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
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
      "fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
      "creationTimestamp": [
        1794908401
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=1889185f-3ca2-4ec7-87bc-b3ca1dce",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c...4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
        "previous_git_commit": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
        "previous_fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 258007.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
          "template_reference_name": "custom-start-points",
          "git_commit": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
          "git_commit_info": {
            "sha1": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
            "message": "Merge pull request #158 from cyber-dojo/update-base-image-e854e8f\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1794650394.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=1889185f-3ca2-4ec7-87bc-b3ca1dce",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c...4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
            "previous_git_commit": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
            "previous_fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 258007.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-44",
          "template_reference_name": "custom-start-points",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=708a1c34-7cd6-473d-aa63-be590ad9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 3259129.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
          "template_reference_name": "custom-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=00286c09-b06e-4eb9-a59f-0a1dd949",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -77104.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
          "template_reference_name": "custom-start-points",
          "git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
          "git_commit_info": {
            "sha1": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "message": "Merge pull request #8 from cyber-dojo/fail-find-artifacts-on-pipe-error\n\nSurface kosli failures and read the primary host",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1794985505.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68?artifact_id=065595f3-4ca3-443b-bdd8-51dc6394",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7ec3715a952611112bb259ed92b6986335183ff3...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7ec3715a952611112bb259ed92b6986335183ff3",
            "previous_fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -77104.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/be821a9d0061420c902f1b3c499a4395",
        "cluster_name": null,
        "service_name": null
      }
    }
  ],
  "applied_policies": [
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

