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
  "index": 5588,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1794385498.3975194,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5588",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:d8dd8e1@sha256:58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
                    "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
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
      "fingerprint": "58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
      "creationTimestamp": [
        1794043932
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e?artifact_id=d6f1b255-9fa7-4ee3-9438-fb70fdcb",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3...d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
        "previous_git_commit": "aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
        "previous_fingerprint": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 85165.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
          "template_reference_name": "differ",
          "git_commit": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
          "git_commit_info": {
            "sha1": "d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
            "message": "Run workflow to pick up fixes to new expat vulns (#521)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793958767.0,
            "url": "https://github.com/cyber-dojo/differ/commit/d8dd8e1d64e95cdd09a677a95e874b2ed518bf93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e?artifact_id=d6f1b255-9fa7-4ee3-9438-fb70fdcb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3...d8dd8e1d64e95cdd09a677a95e874b2ed518bf93",
            "previous_git_commit": "aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
            "previous_fingerprint": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "aca49ec4abe49fb4abf98e4d7b7af3af6b8239c3",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 85165.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-43",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e?artifact_id=c453d83b-b1d5-4ef8-b194-21d756de",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 2394660.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
          "template_reference_name": "differ",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e?artifact_id=8ecc3bc1-690c-4e0f-8a62-dcb28434",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3284874.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e",
          "template_reference_name": "differ",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/58fa441f593eb0c9b5b5047a1f517fb0d771cb6f42fa34a62ab60aedad7f365e?artifact_id=49136970-46cd-4519-bccd-1f37e005",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:aca49ec@sha256:4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_artifact_compliance_state": "NON-COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-4769761969b2b6af19828321d9471320b6fa671357553b885fe922ff211461de",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3284874.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a47a744f98f54b4b8d953693b6c6bf0a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:fd680a8@sha256:b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
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
      "fingerprint": "b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
      "creationTimestamp": [
        1793179334,
        1793179336,
        1793179343
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=05fa6306-e46c-490f-bda0-8c38d3c0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/83553f52e8de8a9766a64fced8fbfb3cd32318a3...fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "previous_fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 75922.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "template_reference_name": "web",
          "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
          "git_commit_info": {
            "sha1": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "message": "Give creator, web and dashboard the same 15s health wait (#477)\n\nCreator polled 50 times at 0.1s, about 6s in all, and it\nnormally needs about 5s to boot. A slightly slow CI runner\ntipped it over and failed the base-image update (#476)\nwith an empty container log.\n\nWeb waited 60s and dashboard 10s for no stated reason.\nAll three now use docker compose --wait-timeout=15.\nCreator still dumps its container log on timeout.\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793103412.0,
            "url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=05fa6306-e46c-490f-bda0-8c38d3c0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/83553f52e8de8a9766a64fced8fbfb3cd32318a3...fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
            "previous_fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 75922.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=2b84def6-5492-4ad7-84af-dabc7ac6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1530062.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=d5b12951-f0c1-41c2-b8f9-d00697ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2420276.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b849bb4996749a3f8fc03f8dcb3038cf456dd8cc472826c6de20b988c91d61e4?artifact_id=00ec4d4f-f599-49a0-a143-88d78daa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2420276.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fdbeaec14a794d1d88bcc2236ef2bb58",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:4bb52cb@sha256:345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
                    "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
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
      "fingerprint": "345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
      "creationTimestamp": [
        1793178869
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=96424b35-49cc-4dea-9efd-bc7e14c6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5...4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
        "previous_git_commit": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
        "previous_fingerprint": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 77067.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
          "template_reference_name": "spooler",
          "git_commit": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
          "git_commit_info": {
            "sha1": "4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
            "message": "Merge pull request #29 from cyber-dojo/update-base-image-5997b3d\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793101802.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/4bb52cbbdefcd01d973f91b08fd9b5b386570c80"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=96424b35-49cc-4dea-9efd-bc7e14c6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5...4bb52cbbdefcd01d973f91b08fd9b5b386570c80",
            "previous_git_commit": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
            "previous_fingerprint": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 77067.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=b2879b95-4e55-4935-a0d7-9c24be2c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 1529597.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
          "template_reference_name": "spooler",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=269868cf-f223-44b1-98c4-d9dd9d9f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 2419811.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41",
          "template_reference_name": "spooler",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/345743d602e5af11022f409b4451193a7f632b69b90c3a23490201a96c443d41?artifact_id=19fd06ec-66ab-44a2-ad4b-e547470d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 2419811.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/beee4a33544b42e78811dfaf83a7417c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:fd680a8@sha256:0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
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
      "fingerprint": "0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
      "creationTimestamp": [
        1793178783
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=9134bfd2-d550-4c10-93d3-bbd4f6c4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_fingerprint": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 75371.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "template_reference_name": "dashboard",
          "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
          "git_commit_info": {
            "sha1": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "message": "Give creator, web and dashboard the same 15s health wait (#477)\n\nCreator polled 50 times at 0.1s, about 6s in all, and it\nnormally needs about 5s to boot. A slightly slow CI runner\ntipped it over and failed the base-image update (#476)\nwith an empty container log.\n\nWeb waited 60s and dashboard 10s for no stated reason.\nAll three now use docker compose --wait-timeout=15.\nCreator still dumps its container log on timeout.\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793103412.0,
            "url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=9134bfd2-d550-4c10-93d3-bbd4f6c4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_fingerprint": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 75371.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=553972b2-76dd-47c6-a058-f379d2be",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-185",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1529511.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=d330c8c5-4e7c-4daf-8ec7-f0e72bab",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2419725.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/0700dd34e5e360389f948bc6f321258e4dadc07c4d03452ea31a1dd2a8ac69af?artifact_id=bb996c3e-1bb3-4f50-a7a9-a5731f5c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2419725.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/50c09d6d3dc34e76a623145a7e82f1a9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:fd680a8@sha256:000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
                    "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
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
      "fingerprint": "000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
      "creationTimestamp": [
        1793178778
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=0e7140db-7422-4ea7-954b-fa840a0a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
        "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_fingerprint": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 75366.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "template_reference_name": "creator",
          "git_commit": "fd680a809587fa6e4071fe874d63192f65f251c1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1",
          "git_commit_info": {
            "sha1": "fd680a809587fa6e4071fe874d63192f65f251c1",
            "message": "Give creator, web and dashboard the same 15s health wait (#477)\n\nCreator polled 50 times at 0.1s, about 6s in all, and it\nnormally needs about 5s to boot. A slightly slow CI runner\ntipped it over and failed the base-image update (#476)\nwith an empty container log.\n\nWeb waited 60s and dashboard 10s for no stated reason.\nAll three now use docker compose --wait-timeout=15.\nCreator still dumps its container log on timeout.\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793103412.0,
            "url": "https://github.com/cyber-dojo/web/commit/fd680a809587fa6e4071fe874d63192f65f251c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=0e7140db-7422-4ea7-954b-fa840a0a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...fd680a809587fa6e4071fe874d63192f65f251c1",
            "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_fingerprint": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 75366.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=53803fd2-76ca-488d-a7ec-e46cd58d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-185",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1529506.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=86e89528-29fd-48ee-b993-1e4de7b2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2419720.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/000a36f4debb15073c77bc5e9b7a864ebf60c2ce3116fed603ce0ac654bdf568?artifact_id=8897a9dd-66c1-466e-a5c9-dccf9669",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2419720.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ca3e3783c9cc455d9b55b7406f645307",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:6baf182@sha256:f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
                    "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
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
      "fingerprint": "f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
      "creationTimestamp": [
        1794043936
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "6baf18253638f0417e2dc20d71804cc6db5329c5",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b?artifact_id=12ff0d35-c78f-425e-abbb-687bc264",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/573bc849ed628bf0230b94be375122cf51b3f48f...6baf18253638f0417e2dc20d71804cc6db5329c5",
        "previous_git_commit": "573bc849ed628bf0230b94be375122cf51b3f48f",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/573bc849ed628bf0230b94be375122cf51b3f48f",
        "previous_fingerprint": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "573bc849ed628bf0230b94be375122cf51b3f48f",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 85349.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "6baf18253638f0417e2dc20d71804cc6db5329c5",
          "template_reference_name": "saver",
          "git_commit": "6baf18253638f0417e2dc20d71804cc6db5329c5",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5",
          "git_commit_info": {
            "sha1": "6baf18253638f0417e2dc20d71804cc6db5329c5",
            "message": "Run workflow to pick up fixes to new expat vulns (#469)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793958587.0,
            "url": "https://github.com/cyber-dojo/saver/commit/6baf18253638f0417e2dc20d71804cc6db5329c5"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b?artifact_id=12ff0d35-c78f-425e-abbb-687bc264",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/573bc849ed628bf0230b94be375122cf51b3f48f...6baf18253638f0417e2dc20d71804cc6db5329c5",
            "previous_git_commit": "573bc849ed628bf0230b94be375122cf51b3f48f",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/573bc849ed628bf0230b94be375122cf51b3f48f",
            "previous_fingerprint": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "573bc849ed628bf0230b94be375122cf51b3f48f",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 85349.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-43",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b?artifact_id=39b17f73-8f14-4ad5-aa39-02fadc39",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 2394664.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
          "template_reference_name": "saver",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b?artifact_id=00e84981-2592-4942-962b-e2991d15",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3284878.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b",
          "template_reference_name": "saver",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f1a21454d08341c75ceb4e9a8bc95fab3f83c7e1db8c286d9f6ed22651c9210b?artifact_id=eb4b97c4-19b2-4902-b1c9-ecbf4161",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:573bc84@sha256:e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-e16d7a10b27f5946e0c4ab8914f0b9e421b626854592692c5db5592eaebc7203",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3284878.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b3bf6c453f794f66bb9724de53bdc51a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b52ea1f@sha256:b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
                    "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
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
      "fingerprint": "b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
      "creationTimestamp": [
        1794043915
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec?artifact_id=de6cb598-f90e-4732-a96b-40458168",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/38062992c27234fbb3784c9730b0f7229a2dda66...b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
        "previous_git_commit": "38062992c27234fbb3784c9730b0f7229a2dda66",
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/38062992c27234fbb3784c9730b0f7229a2dda66",
        "previous_fingerprint": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "38062992c27234fbb3784c9730b0f7229a2dda66",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 85362.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
          "template_reference_name": "nginx",
          "git_commit": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
          "git_commit_info": {
            "sha1": "b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
            "message": "Merge pull request #189 from cyber-dojo/run-workflow-160\n\nRun workflow to pick up fixes to new expat vulns",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793958553.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/b52ea1fb0b04c2cda0bff8db8887d019a7a81637"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec?artifact_id=de6cb598-f90e-4732-a96b-40458168",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/38062992c27234fbb3784c9730b0f7229a2dda66...b52ea1fb0b04c2cda0bff8db8887d019a7a81637",
            "previous_git_commit": "38062992c27234fbb3784c9730b0f7229a2dda66",
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/38062992c27234fbb3784c9730b0f7229a2dda66",
            "previous_fingerprint": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "38062992c27234fbb3784c9730b0f7229a2dda66",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 85362.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-43",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec?artifact_id=a17237eb-1eca-4733-bb0a-4c3c922d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-42",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 2394643.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
          "template_reference_name": "nginx",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec?artifact_id=4962c63a-8408-4af5-b86e-93c785b6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 3284857.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec",
          "template_reference_name": "nginx",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b83f0ef11a76c864e06243b9c6a94ab946618dd68afd84d6a3ea0892c23219ec?artifact_id=b8e3ee20-11d6-47bb-8cf9-5f3f4b29",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:3806299@sha256:44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_artifact_compliance_state": "NON-COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-44700e827553393dfc4ef9ba9f9948aeb28c1a2f75bd3f2dfa0ecfc3e7eb28df",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 3284857.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/311673519b7346a781f5d70c8dbcd7e5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:190eb03@sha256:a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
                    "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
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
      "fingerprint": "a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
      "creationTimestamp": [
        1793179259
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=f30b0455-6aa8-425e-ba1d-2ae2b497",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/270c3c87aecb0e008e90879be753e67983e692c8...190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
        "previous_git_commit": "270c3c87aecb0e008e90879be753e67983e692c8",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8",
        "previous_fingerprint": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 76651.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
          "template_reference_name": "custom-start-points",
          "git_commit": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
          "git_commit_info": {
            "sha1": "190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
            "message": "Merge pull request #157 from cyber-dojo/update-base-image-2fa325e\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793102608.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/190eb03bc9a6d783dad9d8d74d977c85f1d3f30c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=f30b0455-6aa8-425e-ba1d-2ae2b497",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/270c3c87aecb0e008e90879be753e67983e692c8...190eb03bc9a6d783dad9d8d74d977c85f1d3f30c",
            "previous_git_commit": "270c3c87aecb0e008e90879be753e67983e692c8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8",
            "previous_fingerprint": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 76651.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=78044fbb-8075-480a-bf0a-14fbeb7b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 1529987.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
          "template_reference_name": "custom-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=2383be39-77f9-423f-9ade-cba9f225",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2420201.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb",
          "template_reference_name": "custom-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a9aa686d2bfa307bc715841448326e65a394aa2861d94c4744f797a599fc9edb?artifact_id=58c4bce1-a2a0-4a30-a2c2-d0801465",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c415496@sha256:e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2420201.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/54911a331a454eda99b5c608f03b479c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bbd98e9@sha256:9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
                    "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
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
      "fingerprint": "9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
      "creationTimestamp": [
        1793179127,
        1793179130,
        1793179132
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=f418eb3f-416b-4def-861c-aaebadf6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e...bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
        "previous_git_commit": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
        "previous_fingerprint": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 77252.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
          "template_reference_name": "runner",
          "git_commit": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
          "git_commit_info": {
            "sha1": "bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
            "message": "Dockerfile - Automated base-image update (#330)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793101875.0,
            "url": "https://github.com/cyber-dojo/runner/commit/bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=f418eb3f-416b-4def-861c-aaebadf6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e...bbd98e9edd32f97a4e2490ddb6963d4ed363eb6e",
            "previous_git_commit": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
            "previous_fingerprint": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 77252.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=e564abfe-1845-496c-821a-7edda247",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1529855.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
          "template_reference_name": "runner",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=769c44ac-1174-42bc-ad07-1a38e707",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2420069.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757",
          "template_reference_name": "runner",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9f8ac40adc070f4ded8fa56ca2a168804cbc882c42d94fc4537666d39d8d1757?artifact_id=da83d227-62dc-4c5f-a50e-f017c0d9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2420069.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fd1f0d36db6641058095ba8fc9981816",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9fcbc9e@sha256:7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
                    "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
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
      "fingerprint": "7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
      "creationTimestamp": [
        1793179128
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=9b49ae7a-d0e1-4e04-ba77-ec89b9dd",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8442c1b837d6dca9e349a6c3401437f11e6bd9f0...9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
        "previous_git_commit": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
        "previous_fingerprint": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 73931.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
          "template_reference_name": "languages-start-points",
          "git_commit": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
          "git_commit_info": {
            "sha1": "9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
            "message": "Merge pull request #305 from cyber-dojo/update-readme-2\n\nUpdate readme screenshot to match readme text",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793105197.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/9fcbc9ef1306b6fed965cecfd4ff778582015fa3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=9b49ae7a-d0e1-4e04-ba77-ec89b9dd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8442c1b837d6dca9e349a6c3401437f11e6bd9f0...9fcbc9ef1306b6fed965cecfd4ff778582015fa3",
            "previous_git_commit": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
            "previous_fingerprint": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 73931.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=d16ca28a-e85e-4367-87f2-ec3ea9ac",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 1529856.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
          "template_reference_name": "languages-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=d36cdd1e-27ba-4913-a3ba-703db682",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2420070.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024",
          "template_reference_name": "languages-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7d318c34350a409ba26020f301a298ee8aa30979c8ec4854743911401d229024?artifact_id=2ee9623f-3fac-41bc-b3e8-dd272cc6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c5dd4fa@sha256:5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2420070.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a5768b257e86419786f131e31ec1ba1a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:9f2aa63@sha256:30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
                    "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-42",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
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
      "fingerprint": "30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
      "creationTimestamp": [
        1793178791
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=4369d9e0-a55a-40ac-aab6-01719a95",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/68636bed4906a15df27ee99e2afddd4377d3867e...9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
        "previous_git_commit": "68636bed4906a15df27ee99e2afddd4377d3867e",
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e",
        "previous_fingerprint": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 76180.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
          "template_reference_name": "exercises-start-points",
          "git_commit": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
          "git_commit_info": {
            "sha1": "9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
            "message": "Merge pull request #160 from cyber-dojo/update-base-image-2fa325e\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1793102611.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/9f2aa63fc77d01f4796ad05965a1b7d706d47bb6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=4369d9e0-a55a-40ac-aab6-01719a95",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/68636bed4906a15df27ee99e2afddd4377d3867e...9f2aa63fc77d01f4796ad05965a1b7d706d47bb6",
            "previous_git_commit": "68636bed4906a15df27ee99e2afddd4377d3867e",
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e",
            "previous_fingerprint": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 76180.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-42",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=d0272b0b-9b01-45a4-95f8-924f3794",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 1529519.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
          "template_reference_name": "exercises-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=cefaa13b-2218-4462-b8ad-9e122195",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2419733.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509",
          "template_reference_name": "exercises-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/30dbd3457ff111148a139daae9dd77d8d725629037bb59bd4eb450964e6a3509?artifact_id=e784c7ce-0e40-472a-bf88-5e1228bd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2419733.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/963d5df329324b95b125fc539ee4790c",
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

