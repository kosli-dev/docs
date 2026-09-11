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
  "index": 5352,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1789108858.5535865,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5352",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
                    "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-165",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
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
      "fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
      "creationTimestamp": [
        1789023319
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "99d7b74f39e311d492902ad48dbe97da63f2c687",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=205424b6-5741-4071-bd36-c26e83f6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/abdc61396b5031dbb1e90f5c9c190d303ff243e1...99d7b74f39e311d492902ad48dbe97da63f2c687",
        "previous_git_commit": "abdc61396b5031dbb1e90f5c9c190d303ff243e1",
        "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/abdc61396b5031dbb1e90f5c9c190d303ff243e1",
        "previous_trail_name": "abdc61396b5031dbb1e90f5c9c190d303ff243e1",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 3383.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
          "template_reference_name": "creator",
          "git_commit": "99d7b74f39e311d492902ad48dbe97da63f2c687",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687",
          "git_commit_info": {
            "sha1": "99d7b74f39e311d492902ad48dbe97da63f2c687",
            "message": "Remove upgrade notice (#60)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1789019936.0,
            "url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=205424b6-5741-4071-bd36-c26e83f6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/abdc61396b5031dbb1e90f5c9c190d303ff243e1...99d7b74f39e311d492902ad48dbe97da63f2c687",
            "previous_git_commit": "abdc61396b5031dbb1e90f5c9c190d303ff243e1",
            "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/abdc61396b5031dbb1e90f5c9c190d303ff243e1",
            "previous_trail_name": "abdc61396b5031dbb1e90f5c9c190d303ff243e1",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 3383.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-165",
          "template_reference_name": "creator",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=a6ea2552-c978-4a49-a9c1-91f3402a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 3706325.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
          "template_reference_name": "creator",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=8538b0e6-c57c-4137-9e81-53163437",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_trail_name": "creator-ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 77664.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
          "template_reference_name": "creator",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424?artifact_id=55242b51-f519-487f-beb5-9d02017c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_trail_name": "creator-ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 77664.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f5fb12ba8c944853886ff4f0faffde50",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
                    "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
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
      "fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
      "creationTimestamp": [
        1789022826,
        1789022880,
        1789022884
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
      "commit_url": "https://github.com/cyber-dojo/web/commit/236898f12a3bcce3b60625dd71c6f817d4cc37c2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=9d418e45-a78d-462a-b8be-aaf2fc85",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/cbe481c4b842f897e4e9e411cd78461a3a12a334...236898f12a3bcce3b60625dd71c6f817d4cc37c2",
        "previous_git_commit": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "previous_fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "previous_trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 88708.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
          "template_reference_name": "web",
          "git_commit": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
          "commit_url": "https://github.com/cyber-dojo/web/commit/236898f12a3bcce3b60625dd71c6f817d4cc37c2",
          "git_commit_info": {
            "sha1": "236898f12a3bcce3b60625dd71c6f817d4cc37c2",
            "message": "Dockerfile - Automated base-image update (#425)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778385.0,
            "url": "https://github.com/cyber-dojo/web/commit/236898f12a3bcce3b60625dd71c6f817d4cc37c2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=9d418e45-a78d-462a-b8be-aaf2fc85",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/cbe481c4b842f897e4e9e411cd78461a3a12a334...236898f12a3bcce3b60625dd71c6f817d4cc37c2",
            "previous_git_commit": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
            "previous_fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
            "previous_trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 88708.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "web",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=2db7454f-b774-4c13-b755-516ec573",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-161",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3550099.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
          "template_reference_name": "web",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=f65df9d1-cb49-4f5a-a751-785138de",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_artifact_compliance_state": "NON-COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -78562.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
          "template_reference_name": "web",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418?artifact_id=60234182-f1d9-4d59-aa4e-2d29180f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -78562.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f800bdc877ff4579aff38aae2a2b8db9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
                    "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
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
      "fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
      "creationTimestamp": [
        1789022821,
        1789022872,
        1789022877
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=612b9903-ce02-40a7-a329-77b10931",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9...4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
        "previous_git_commit": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
        "previous_fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
        "previous_trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 88837.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
          "template_reference_name": "runner",
          "git_commit": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
          "git_commit_info": {
            "sha1": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
            "message": "Dockerfile - Automated base-image update (#312)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778348.0,
            "url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=612b9903-ce02-40a7-a329-77b10931",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9...4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
            "previous_git_commit": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
            "previous_fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
            "previous_trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 88837.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "runner",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=bf1d6fdd-5fa4-410f-a897-ad33e40a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 3550191.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
          "template_reference_name": "runner",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=fbdfe540-f0e7-4b68-9bab-b752fe2a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -78470.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
          "template_reference_name": "runner",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f?artifact_id=f448662b-6bdd-4d64-80ef-3072846d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:d7541d3@sha256:fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "runner-fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -78470.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ecc3523886774c3791136a12495d567c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
                    "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
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
      "fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
      "creationTimestamp": [
        1789022830
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=7ba704a0-8706-4f12-9eb8-776c7e5d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/ff9f292e809801d35246183988b7812826bc2760...6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
        "previous_git_commit": "ff9f292e809801d35246183988b7812826bc2760",
        "previous_fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
        "previous_trail_name": "ff9f292e809801d35246183988b7812826bc2760",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 89179.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
          "template_reference_name": "dashboard",
          "git_commit": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
          "git_commit_info": {
            "sha1": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
            "message": "Dockerfile - Automated base-image update (#438)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778346.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=7ba704a0-8706-4f12-9eb8-776c7e5d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/ff9f292e809801d35246183988b7812826bc2760...6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
            "previous_git_commit": "ff9f292e809801d35246183988b7812826bc2760",
            "previous_fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
            "previous_trail_name": "ff9f292e809801d35246183988b7812826bc2760",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 89179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "dashboard",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=26333282-8be1-4a1a-b142-1b3c958b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 3550531.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
          "template_reference_name": "dashboard",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=6cdd9974-d138-48f0-b02b-88a08901",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -78130.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
          "template_reference_name": "dashboard",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29?artifact_id=de8c1b00-91bd-4bd0-908a-4544ec15",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -78130.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1009a1194f024e6ea07508acbedf904a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
                    "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
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
      "fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
      "creationTimestamp": [
        1789022826
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/5d1d4b6035691d7986e05ab263e521b3e711fa0c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=f5813ac8-1ad7-433a-beee-f90a065d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8e6b51867675d4b652a38353611cde1d8567fce0...5d1d4b6035691d7986e05ab263e521b3e711fa0c",
        "previous_git_commit": "8e6b51867675d4b652a38353611cde1d8567fce0",
        "previous_fingerprint": "77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8e6b518@sha256:77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8e6b51867675d4b652a38353611cde1d8567fce0",
        "previous_trail_name": "8e6b51867675d4b652a38353611cde1d8567fce0",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 6198.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
          "template_reference_name": "languages-start-points",
          "git_commit": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/5d1d4b6035691d7986e05ab263e521b3e711fa0c",
          "git_commit_info": {
            "sha1": "5d1d4b6035691d7986e05ab263e521b3e711fa0c",
            "message": "Merge pull request #267 from cyber-dojo/update-base-image-a2388c1\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788860897.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/5d1d4b6035691d7986e05ab263e521b3e711fa0c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=f5813ac8-1ad7-433a-beee-f90a065d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8e6b51867675d4b652a38353611cde1d8567fce0...5d1d4b6035691d7986e05ab263e521b3e711fa0c",
            "previous_git_commit": "8e6b51867675d4b652a38353611cde1d8567fce0",
            "previous_fingerprint": "77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8e6b518@sha256:77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8e6b51867675d4b652a38353611cde1d8567fce0",
            "previous_trail_name": "8e6b51867675d4b652a38353611cde1d8567fce0",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 6198.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "languages-start-points",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=c7b16f07-078b-4f71-8d61-93bbfaa4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8e6b518@sha256:77bd283ca309eb2e7c88d8634ba19c66637c7030cae8129d6835cc4d450d742d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-163",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 3550101.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
          "template_reference_name": "languages-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=8d6316ab-1e65-4138-8695-27110838",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a357ebd@sha256:28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -78560.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
          "template_reference_name": "languages-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909?artifact_id=a5af66a8-baad-4d53-8da3-7f160ded",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -78560.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/3654ae3b0ab3441e8826520bdebee1b4",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
                    "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
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
      "fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
      "creationTimestamp": [
        1789022826
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=30338133-ceb7-4976-8956-e0b140cf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65...bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
        "previous_git_commit": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
        "previous_fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
        "previous_trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 981.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
          "template_reference_name": "nginx",
          "git_commit": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
          "git_commit_info": {
            "sha1": "bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
            "message": "Merge pull request #171 from cyber-dojo/run-workflow-to-pickup-lib-updates\n\nRun workflow to pick up new snyk vuln fixes",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788866107.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/bd3938c88623bff4f02e1c2f12e97f7cd60523e3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=30338133-ceb7-4976-8956-e0b140cf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65...bd3938c88623bff4f02e1c2f12e97f7cd60523e3",
            "previous_git_commit": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
            "previous_fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
            "previous_trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 981.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "nginx",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=6054ab54-4c97-4a31-8dc1-6cd7f492",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 3550094.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
          "template_reference_name": "nginx",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=6c3dc579-a9b1-413e-9738-5087e69c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -78567.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
          "template_reference_name": "nginx",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5?artifact_id=50bee95d-36db-441e-af26-4c0f1566",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -78567.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4dd7dd50d39444e68bc2bbea87eb0786",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
                    "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
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
      "fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
      "creationTimestamp": [
        1789022822
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "d01bb39495a1356eabe934bef84b92cc964a26f1",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=6884abdb-afdd-4c56-aa14-94e8da5c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8...d01bb39495a1356eabe934bef84b92cc964a26f1",
        "previous_git_commit": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "previous_fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "previous_trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 6537.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
          "template_reference_name": "exercises-start-points",
          "git_commit": "d01bb39495a1356eabe934bef84b92cc964a26f1",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1",
          "git_commit_info": {
            "sha1": "d01bb39495a1356eabe934bef84b92cc964a26f1",
            "message": "Merge pull request #151 from cyber-dojo/update-base-image-a2388c1\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788860901.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=6884abdb-afdd-4c56-aa14-94e8da5c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8...d01bb39495a1356eabe934bef84b92cc964a26f1",
            "previous_git_commit": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
            "previous_fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
            "previous_trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 6537.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "exercises-start-points",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=d5da77dd-d12b-47e0-ac66-ef5e5a75",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 3550444.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
          "template_reference_name": "exercises-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=78955e83-729d-430a-9024-c86c519b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -78217.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
          "template_reference_name": "exercises-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31?artifact_id=229c5332-8a88-4699-8e97-58d01849",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -78217.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ff1e094fcede458dbf94d752ad3bee18",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
                    "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
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
      "fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
      "creationTimestamp": [
        1789022819
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=df1b0b8e-7efa-415e-860d-9123aa27",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f...5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
        "previous_git_commit": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "previous_fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "previous_trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 89076.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
          "template_reference_name": "spooler",
          "git_commit": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
          "git_commit_info": {
            "sha1": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
            "message": "Merge pull request #20 from cyber-dojo/update-base-image-949edc1\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778354.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=df1b0b8e-7efa-415e-860d-9123aa27",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f...5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
            "previous_git_commit": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
            "previous_fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
            "previous_trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 89076.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "spooler",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=fc124522-a5f3-403a-a97c-75cedd2a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 3550436.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
          "template_reference_name": "spooler",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=3b1ea734-03a4-471e-b9f5-f1125b84",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": -78225.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
          "template_reference_name": "spooler",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f?artifact_id=83a46bf5-cc72-4dee-9f55-00c021c1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -78225.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/116f5564a14740798d58d386b69889b7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
                    "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
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
      "fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
      "creationTimestamp": [
        1789022818
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=60d0583d-4388-4a0a-925d-5b47d9a8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/b12a5c9b17023462d13e81381a69c7ef05f84dc2...86c839ee588f393d84a6b9c036478d10bb6f2a2d",
        "previous_git_commit": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "previous_fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "previous_trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 6352.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
          "template_reference_name": "custom-start-points",
          "git_commit": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d",
          "git_commit_info": {
            "sha1": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
            "message": "Merge pull request #145 from cyber-dojo/update-base-image-a2388c1\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788860905.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=60d0583d-4388-4a0a-925d-5b47d9a8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/b12a5c9b17023462d13e81381a69c7ef05f84dc2...86c839ee588f393d84a6b9c036478d10bb6f2a2d",
            "previous_git_commit": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
            "previous_fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
            "previous_trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 6352.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "custom-start-points",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=6fd3fc32-bd41-4fcc-8a19-d45ae3ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 3550263.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
          "template_reference_name": "custom-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=2a293eb4-5c35-4b7c-92d5-b32ca0ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -78398.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
          "template_reference_name": "custom-start-points",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e?artifact_id=635c66c3-625f-44dd-98b0-d9906fa7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -78398.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/02b628eb907844948b7633bd9a68db2c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
                    "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
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
      "fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
      "creationTimestamp": [
        1789022816
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "7c4708f675a7717376529273ec32d08cd93f5c26",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=326e1373-e805-48be-bfc7-6631db28",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/9030f8f46e738d94bd817727b8f8a9a54f106585...7c4708f675a7717376529273ec32d08cd93f5c26",
        "previous_git_commit": "9030f8f46e738d94bd817727b8f8a9a54f106585",
        "previous_fingerprint": "6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:9030f8f@sha256:6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/9030f8f46e738d94bd817727b8f8a9a54f106585",
        "previous_trail_name": "9030f8f46e738d94bd817727b8f8a9a54f106585",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 89107.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
          "template_reference_name": "saver",
          "git_commit": "7c4708f675a7717376529273ec32d08cd93f5c26",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26",
          "git_commit_info": {
            "sha1": "7c4708f675a7717376529273ec32d08cd93f5c26",
            "message": "Dockerfile - Automated base-image update (#446)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778339.0,
            "url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=326e1373-e805-48be-bfc7-6631db28",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/9030f8f46e738d94bd817727b8f8a9a54f106585...7c4708f675a7717376529273ec32d08cd93f5c26",
            "previous_git_commit": "9030f8f46e738d94bd817727b8f8a9a54f106585",
            "previous_fingerprint": "6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:9030f8f@sha256:6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/9030f8f46e738d94bd817727b8f8a9a54f106585",
            "previous_trail_name": "9030f8f46e738d94bd817727b8f8a9a54f106585",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 89107.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "saver",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=8fb8e719-d3c3-41e3-8c3d-330a1bf8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:9030f8f@sha256:6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-162",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3550452.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
          "template_reference_name": "saver",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=01d2ba7c-c06f-40a8-8dfc-5b71d5f9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:9030f8f@sha256:6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "saver-6f6be2c6ce42d0d96b320f84f6bd8cbf6f22fc01b8f32fda047f682494c1c733",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -78209.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
          "template_reference_name": "saver",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc?artifact_id=f91367c3-bdd4-4f8c-89df-7ebad571",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -78209.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/89078662eaed4dce813ab87e8faac4af",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
                    "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-35",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
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
      "fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
      "creationTimestamp": [
        1789022811
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=054eef05-3aee-49ae-9e4d-55f768b7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de...2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
        "previous_git_commit": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
        "previous_fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
        "previous_trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 88615.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
          "template_reference_name": "differ",
          "git_commit": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
          "git_commit_info": {
            "sha1": "2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
            "message": "Dockerfile - Automated base-image update (#474)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788778834.0,
            "url": "https://github.com/cyber-dojo/differ/commit/2e9bd969b50fff6b86578d69b7139f2d688ef6e2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=054eef05-3aee-49ae-9e4d-55f768b7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de...2e9bd969b50fff6b86578d69b7139f2d688ef6e2",
            "previous_git_commit": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
            "previous_fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
            "previous_trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 88615.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-35",
          "template_reference_name": "differ",
          "git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
          "git_commit_info": {
            "sha1": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316994.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=516eb6d4-9435-429b-87f2-51edb16f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-34",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3550455.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
          "template_reference_name": "differ",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=9fc7c402-1e99-4822-a233-50a7becb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -78206.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
          "template_reference_name": "differ",
          "git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
          "git_commit_info": {
            "sha1": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "message": "Merge pull request #4 from cyber-dojo/take-both-age-instants-from-one-trail-read\n\nMeasure a vuln's age on the Kosli server's clock alone",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1788945655.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409?artifact_id=47b639ae-b6f8-446f-a5e0-d78cde5e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -78206.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/796c685a73274536b400dd72e3dea728",
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

