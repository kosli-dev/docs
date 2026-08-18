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
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
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
  "index": 5249,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1787021218.5403302,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5249",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:85cac88@sha256:f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
                    "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
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
      "fingerprint": "f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
      "creationTimestamp": [
        1786425437,
        1786425461,
        1786425514
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "85cac880cb74678426eb2ed4dbf2538995404c5c",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/85cac880cb74678426eb2ed4dbf2538995404c5c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=d4d2a067-63c8-4403-a6f5-554e6fef",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3...85cac880cb74678426eb2ed4dbf2538995404c5c",
        "previous_git_commit": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
        "previous_fingerprint": "8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:48bb369@sha256:8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
        "previous_trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 171942.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "85cac880cb74678426eb2ed4dbf2538995404c5c",
          "template_reference_name": "runner",
          "git_commit": "85cac880cb74678426eb2ed4dbf2538995404c5c",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/85cac880cb74678426eb2ed4dbf2538995404c5c",
          "git_commit_info": {
            "sha1": "85cac880cb74678426eb2ed4dbf2538995404c5c",
            "message": "Merge pull request #277 from cyber-dojo/fix-exit-non-zero\n\nMake exit_non_zero actually exit",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786253495.0,
            "url": "https://github.com/cyber-dojo/runner/commit/85cac880cb74678426eb2ed4dbf2538995404c5c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=d4d2a067-63c8-4403-a6f5-554e6fef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3...85cac880cb74678426eb2ed4dbf2538995404c5c",
            "previous_git_commit": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
            "previous_fingerprint": "8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:48bb369@sha256:8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
            "previous_trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 171942.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
          "template_reference_name": "runner",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=00b52efb-82ba-4573-b73e-1a4387c5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1108486.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=9a0fba00-e298-410d-aeea-99249451",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:48bb369@sha256:8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-154",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1108443.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096",
          "template_reference_name": "runner",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f3cdc22a599ddb789e7791389a5a58b43fd9c30d3af079aec392d5962d181096?artifact_id=ab875660-aa6a-466c-b224-ec94bca3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -176956.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e13cf5bfd5a04a88afd3b2d02a1a3eaa",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
                    "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
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
      "fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
      "creationTimestamp": [
        1786425512
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=df2dcc5e-bb07-40e8-b013-9ac60f42",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/c81791fd10558a59f83876137fb021abcd89f262...dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
        "previous_git_commit": "c81791fd10558a59f83876137fb021abcd89f262",
        "previous_fingerprint": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262",
        "previous_trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 171872.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
          "template_reference_name": "spooler",
          "git_commit": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
          "git_commit_info": {
            "sha1": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
            "message": "Merge pull request #14 from cyber-dojo/fix-exit-non-zero\n\nMake exit_non_zero actually exit",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786253640.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=df2dcc5e-bb07-40e8-b013-9ac60f42",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/c81791fd10558a59f83876137fb021abcd89f262...dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
            "previous_git_commit": "c81791fd10558a59f83876137fb021abcd89f262",
            "previous_fingerprint": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262",
            "previous_trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 171872.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=3c4a58c5-2e1f-4f22-b774-45e5f2b0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promotion-one-145",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 1108518.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
          "template_reference_name": "spooler",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=4028a69a-8f9a-4855-9716-f1fc77c9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -176881.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
          "template_reference_name": "spooler",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0?artifact_id=e5d56e7c-c459-4cb4-8004-387e9ea3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -176881.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d965b62fd5c64cd98456881feb1352c7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
                    "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
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
      "fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
      "creationTimestamp": [
        1786425419,
        1786425419,
        1786425419
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
      "commit_url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=f658e6e3-9ce8-462f-a29e-a2cc6f7b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e...5e4b9873df93525c041c386c06e0ab8fc36b6f33",
        "previous_git_commit": "0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
        "previous_fingerprint": "1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:0c31ab4@sha256:1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
        "previous_trail_name": "0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 58766.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
          "template_reference_name": "web",
          "git_commit": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
          "commit_url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33",
          "git_commit_info": {
            "sha1": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
            "message": "Name the creation-event rule instead of restating it (#417)\n\nDeciding whether the review navigator's activity test (events.length > 1)\n  agreed with the dashboard's (any event with index != 0) meant reading five\n  files and saver's event-placement code, because the same fact - event 0 is\n  the kata's creation, anything after it is something someone did - was spelled\n  differently at every site. The two rules do agree, but nothing in the code\n  said so, so the only way to find out was to go and check.\n\n  cd.lib now carries isCreationEvent(event) and hasActivity(events), each\n  documenting the invariant it rests on: an event's index is its position in the\n  array, because saver places every write at head+1. The review partials ask\n  through them rather than restating index==0 or length==1.\n\n  Two sites keep their own spelling on purpose. previousIndex's index == 0 reads\n  as array arithmetic rather than the creation rule, and kata_app has the only\n  Ruby site in this repo, so a predicate there would add indirection without\n  removing duplication.\n\n  The avatars_tests fixtures now hold real event objects rather than bare\n  integers, because the rule reads an event's index. Those tests still do not\n  run: there is no jest here and require('./avatars') resolves to nothing.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786366653.0,
            "url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=f658e6e3-9ce8-462f-a29e-a2cc6f7b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e...5e4b9873df93525c041c386c06e0ab8fc36b6f33",
            "previous_git_commit": "0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
            "previous_fingerprint": "1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:0c31ab4@sha256:1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
            "previous_trail_name": "0c31ab46a7d8c7d34d2ce0654dc09f8ae4229c7e",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 58766.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
          "template_reference_name": "web",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=da135937-1562-4662-b672-53688f17",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1108468.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=5254e39c-72c5-4946-86ed-08f7b11a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:0c31ab4@sha256:1e03ce9811f7ffaa0d00bb4da3dbc60e939e6d1b3f8e87b88a99121dca481018",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-157",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1108425.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
          "template_reference_name": "web",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd?artifact_id=6edd9e01-0c2e-48b4-98a6-10da27d1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -176974.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1af4cc2636fa44c3867fc792d9285670",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
                    "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
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
      "fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
      "creationTimestamp": [
        1786425173
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "83357f112ef5c10b157cb84732c77965cc8ddc48",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=11539f6a-befb-4b79-9484-fd9f25d3",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/89019f6d8059406e56fa499b2dec2dbf93f4d5c7...83357f112ef5c10b157cb84732c77965cc8ddc48",
        "previous_git_commit": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
        "previous_fingerprint": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
        "previous_trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 660751.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
          "template_reference_name": "creator",
          "git_commit": "83357f112ef5c10b157cb84732c77965cc8ddc48",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
          "git_commit_info": {
            "sha1": "83357f112ef5c10b157cb84732c77965cc8ddc48",
            "message": "Run the linter as the invoking user (#53)\n\nThe rubocop container wrote reports/rubocop/junit.xml as its own user, so on a\n  linux runner the file belongs to someone else. That broke the attestation added\n  in #52: kosli attest copies evidence with PreserveOwner when given more than one\n  path, and a non-root process cannot chown a file to another uid.\n\n    chown /tmp/1800768837/reports/rubocop/junit.xml: operation not permitted\n\n  The single-path form tars in place and never copies, which is why --results-dir\n  alone had been fine and adding --attachments broke it.\n\n  Passing --user makes the container write as whoever ran it. Worth doing on its\n  own account - a container should not leave files you cannot delete in your\n  working tree - and it sidesteps the CLI's behaviour without waiting on it. That\n  behaviour looks like a bug and is written up in\n  ../kosli-cli-preserve-owner-bug.md for an issue against kosli-dev/cli.\n\n  Docker Desktop maps ownership back to the calling user, so this is invisible on a\n  mac and only shows on the runner.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785764422.0,
            "url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=11539f6a-befb-4b79-9484-fd9f25d3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/89019f6d8059406e56fa499b2dec2dbf93f4d5c7...83357f112ef5c10b157cb84732c77965cc8ddc48",
            "previous_git_commit": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
            "previous_fingerprint": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
            "previous_trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 660751.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
          "template_reference_name": "creator",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=6feaf5cb-761e-4f05-8591-1db09ac4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:07ed087@sha256:26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "creator-26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1108222.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=d5412ba4-c8b6-4bf3-8a8f-05f2ed00",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-150",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1108179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
          "template_reference_name": "creator",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b?artifact_id=68c91d43-921c-4024-a9c2-94fb5101",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -177220.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d85a1f3513dd45c788f6341641110bfd",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
                    "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
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
      "fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
      "creationTimestamp": [
        1786425092
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "108cccf9bccf9af5d455db66c250480b53cbecc7",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=50b8cff6-1888-4c76-b31a-fdd7a311",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/10e162d4e1294815375a31121f14d57e13183b34...108cccf9bccf9af5d455db66c250480b53cbecc7",
        "previous_git_commit": "10e162d4e1294815375a31121f14d57e13183b34",
        "previous_fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34",
        "previous_trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 162716.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
          "template_reference_name": "differ",
          "git_commit": "108cccf9bccf9af5d455db66c250480b53cbecc7",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7",
          "git_commit_info": {
            "sha1": "108cccf9bccf9af5d455db66c250480b53cbecc7",
            "message": "Merge pull request #449 from cyber-dojo/fix-exit-non-zero",
            "author": "AlexKantor87 <alex@kosli.com>",
            "branch": "",
            "timestamp": 1786262376.0,
            "url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=50b8cff6-1888-4c76-b31a-fdd7a311",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/10e162d4e1294815375a31121f14d57e13183b34...108cccf9bccf9af5d455db66c250480b53cbecc7",
            "previous_git_commit": "10e162d4e1294815375a31121f14d57e13183b34",
            "previous_fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34",
            "previous_trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 162716.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
          "template_reference_name": "differ",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=33c43d32-ff7c-4f02-8819-c03ff8e0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1108141.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=a1a352b5-d5bb-4420-b064-c0b165d7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-32",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1108098.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
          "template_reference_name": "differ",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac?artifact_id=690b4ddd-ace2-4b7d-9471-12b200ec",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -177301.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/35d500a5dc23412bad3e1fe7459c66fb",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
                    "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
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
      "fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
      "creationTimestamp": [
        1786425086
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=01bf7de8-52fc-4585-a4b6-abf82047",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/595e902fa2f5844d9ce0612a5c9295cd8dab5b97...36f0420f728fe61e44a3ab0043cf9a3d70863cad",
        "previous_git_commit": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
        "previous_fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
        "previous_trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 171420.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
          "template_reference_name": "saver",
          "git_commit": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad",
          "git_commit_info": {
            "sha1": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
            "message": "Make exit_non_zero actually exit (#438)\n\nkill -INT $$ only stops the script while nothing traps INT. Add\n  a cleanup trap on INT - a normal thing for a script to do - and\n  bash runs the handler and resumes at the next statement, so a\n  guard prints its error and the script carries on to exit 0.\n  exit 42 cannot be declined, and the EXIT trap still cleans up.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786253666.0,
            "url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=01bf7de8-52fc-4585-a4b6-abf82047",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/595e902fa2f5844d9ce0612a5c9295cd8dab5b97...36f0420f728fe61e44a3ab0043cf9a3d70863cad",
            "previous_git_commit": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
            "previous_fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
            "previous_trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 171420.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
          "template_reference_name": "saver",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=070b4e9b-f146-43ef-89f9-49b75fa4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1108135.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=b3939e7a-afe0-460c-8da7-f456c2df",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-32",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1108092.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
          "template_reference_name": "saver",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a?artifact_id=3cf28177-22a0-448e-8041-517eb434",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -177307.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d20584d0428f41a3944ac335cea4da5c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
                    "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
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
      "fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
      "creationTimestamp": [
        1786425083
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=a805b555-f25a-4828-89d2-a28881c8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/da7bacefac23b0983d2b9f39d87508e0f85b1167...2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "previous_git_commit": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
        "previous_fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167",
        "previous_trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 660655.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
          "template_reference_name": "dashboard",
          "git_commit": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
          "git_commit_info": {
            "sha1": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
            "message": "Run the linter as the invoking user (#432)\n\nThe rubocop container wrote reports/rubocop/junit.xml as its own user, so on a\n  linux runner the file belongs to someone else. That breaks the attestation as\n  soon as it has more than one path to send: kosli attest copies evidence with\n  PreserveOwner, and a non-root process cannot chown a file to another uid.\n\n    chown /tmp/1800768837/reports/rubocop/junit.xml: operation not permitted\n\n  Attaching .rubocop.yml in #431 is what supplied the second path. With one path\n  the CLI tars in place and never copies, which is why this had been fine.\n\n  Passing --user makes the container write as whoever ran it. Worth doing on its\n  own account - a container should not leave files you cannot delete in your\n  working tree - and it sidesteps the CLI's behaviour without waiting on it. That\n  behaviour looks like a bug and is written up in\n  ../kosli-cli-preserve-owner-bug.md for an issue against kosli-dev/cli.\n\n  Docker Desktop maps ownership back to the calling user, so this is invisible on a\n  mac and only shows on the runner.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785764428.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=a805b555-f25a-4828-89d2-a28881c8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/da7bacefac23b0983d2b9f39d87508e0f85b1167...2b300f450f72006f6a9000aaf9cd04485f1e8095",
            "previous_git_commit": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
            "previous_fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167",
            "previous_trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 660655.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
          "template_reference_name": "dashboard",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=12bfdb5d-1c9b-4420-b2e1-83318c0f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1108132.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=2eff9d42-2240-4f5b-8217-ccc995c3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-153",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1108089.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
          "template_reference_name": "dashboard",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5?artifact_id=57054d48-c200-4d8f-b566-d51d2a3d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -177310.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fb58f1ca5ba94c30b59fe097af55fd5f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
                    "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
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
      "fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
      "creationTimestamp": [
        1786425079
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=4154b9c8-14cc-426f-abc5-05220611",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/6a7f7be81022f7ed3fa8383f016b55af86e2af23...068b3424c7da843a4f2d428d2e4915f33efc4a02",
        "previous_git_commit": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "previous_fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "previous_trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 31476.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
          "template_reference_name": "languages-start-points",
          "git_commit": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02",
          "git_commit_info": {
            "sha1": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
            "message": "Merge pull request #245 from cyber-dojo/update-zig\n\nUpdate zig-test to 0.16.0",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786393603.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=4154b9c8-14cc-426f-abc5-05220611",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/6a7f7be81022f7ed3fa8383f016b55af86e2af23...068b3424c7da843a4f2d428d2e4915f33efc4a02",
            "previous_git_commit": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
            "previous_fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
            "previous_trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 31476.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
          "template_reference_name": "languages-start-points",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=d9e69b41-322d-4dea-8b56-dbd50334",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 1108128.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=ee065d98-ce20-46c7-bc2f-a4502952",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promote-all-31",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 1108085.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
          "template_reference_name": "languages-start-points",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb?artifact_id=8950ac80-e8f9-49b8-b910-00050d53",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -177314.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ed7c6bde626840e6a054cc94cd2c3363",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
                    "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
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
      "fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
      "creationTimestamp": [
        1786425079
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "fb791742054fa28dd89269aac8002ebfd7b3386e",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=b9778ac6-6d83-4954-98ba-a3e60a22",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/5ce2769937a4014a853787d7b3d89ec30b6ac967...fb791742054fa28dd89269aac8002ebfd7b3386e",
        "previous_git_commit": "5ce2769937a4014a853787d7b3d89ec30b6ac967",
        "previous_fingerprint": "7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:5ce2769@sha256:7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/5ce2769937a4014a853787d7b3d89ec30b6ac967",
        "previous_trail_name": "5ce2769937a4014a853787d7b3d89ec30b6ac967",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 412187.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
          "template_reference_name": "nginx",
          "git_commit": "fb791742054fa28dd89269aac8002ebfd7b3386e",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e",
          "git_commit_info": {
            "sha1": "fb791742054fa28dd89269aac8002ebfd7b3386e",
            "message": "Merge pull request #166 from cyber-dojo/drop-old-fork-spellings\n\nStop rate limiting the old fork paths",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1786012892.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=b9778ac6-6d83-4954-98ba-a3e60a22",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/5ce2769937a4014a853787d7b3d89ec30b6ac967...fb791742054fa28dd89269aac8002ebfd7b3386e",
            "previous_git_commit": "5ce2769937a4014a853787d7b3d89ec30b6ac967",
            "previous_fingerprint": "7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:5ce2769@sha256:7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/5ce2769937a4014a853787d7b3d89ec30b6ac967",
            "previous_trail_name": "5ce2769937a4014a853787d7b3d89ec30b6ac967",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 412187.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
          "template_reference_name": "nginx",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=9474b76c-5cd0-42da-b469-c6a26c8c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "nginx-55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1108128.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-33",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=49f9d376-d38a-4540-bbb1-4a739116",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:5ce2769@sha256:7ef0c05ccfbd506e8c72c17f5ff2e6c0c9732c4dd281b7b071e89da900fa0332",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-156",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1108085.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
          "template_reference_name": "nginx",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf?artifact_id=d9ae3fe8-6c0e-43dc-92c5-167a742c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -177314.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/50474795074a4b039a5d59ff411b87e9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
      "fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
      "creationTimestamp": [
        1785241255
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffb671be-6388-4f6a-ae64-8ba95d82",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/804f248d832dc34e564507b009c246dfb4f0c657...258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "previous_git_commit": "804f248d832dc34e564507b009c246dfb4f0c657",
        "previous_fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
        "previous_trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 929108.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
          "template_reference_name": "exercises-start-points",
          "git_commit": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
          "git_commit_info": {
            "sha1": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
            "message": "Merge pull request #146 from cyber-dojo/add-drift-detection\n\nAdd periodic drift-detection workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784312147.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffb671be-6388-4f6a-ae64-8ba95d82",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/804f248d832dc34e564507b009c246dfb4f0c657...258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
            "previous_git_commit": "804f248d832dc34e564507b009c246dfb4f0c657",
            "previous_fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
            "previous_trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 929108.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "exercises-start-points",
          "git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
          "git_commit_info": {
            "sha1": "81c216a55b2cb1787645e699ceaceca868cad253",
            "message": "Add spooler service name to promote_one.yml",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785143054.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=b17578fc-3dc0-42c5-98a7-216ebe8a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 98201.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
          "template_reference_name": "exercises-start-points",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=c5be014c-5c90-4940-9d24-3f1d472a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -75696.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
          "template_reference_name": "exercises-start-points",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=d28229df-bd00-4604-9dbd-c16495e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -1361138.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f248719ae7814027825075c5ea81acff",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-31",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
      "fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
      "creationTimestamp": [
        1785241244
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=653e13a5-2f2a-4a23-be4e-1693fc77",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/d37aace7598ee943ba0bd5e51f224335cbdf0a3e...790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "previous_git_commit": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "previous_fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "previous_trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 929228.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
          "template_reference_name": "custom-start-points",
          "git_commit": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
          "git_commit_info": {
            "sha1": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
            "message": "Merge pull request #140 from cyber-dojo/add-drift-detection\n\nAdd periodic drift-detection workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784312016.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=653e13a5-2f2a-4a23-be4e-1693fc77",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/d37aace7598ee943ba0bd5e51f224335cbdf0a3e...790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
            "previous_git_commit": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
            "previous_fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
            "previous_trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 929228.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "custom-start-points",
          "git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
          "git_commit_info": {
            "sha1": "81c216a55b2cb1787645e699ceaceca868cad253",
            "message": "Add spooler service name to promote_one.yml",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785143054.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=48b388e8-ce61-4668-a0dd-eb163cd4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 98190.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
          "template_reference_name": "custom-start-points",
          "git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
          "git_commit_info": {
            "sha1": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "message": "Drop lone use of = separator on Kosli CLI boolean flag",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1785316951.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=84b30964-e32f-409b-8cae-d4f8b94b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -75707.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
          "template_reference_name": "custom-start-points",
          "git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
          "git_commit_info": {
            "sha1": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "message": "Extract the repeated retrying curl into a composite action\n\n  The retry flags were pasted into six call sites, so tuning them\n  meant six edits with five chances to miss one.\n\n  Two of the three jobs check out the caller's repo, where\n  ./.github/actions does not resolve, so those name the action by\n  its repo path.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1786602393.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=fd2e72e8-e9eb-449f-a9cd-11e9bc6e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -1361149.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/6bf799c87c194e17be0f99fcd811abb6",
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

