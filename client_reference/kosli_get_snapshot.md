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
  "index": 5409,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1790759338.4899325,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5409",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
                    "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
      "fingerprint": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
      "creationTimestamp": [
        1790419525
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=0faef22c-d2e1-4199-b115-f97f2dce",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca...9635c369db243bfccdd50a0f4abd8cae78c5693a",
        "previous_git_commit": "8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
        "previous_fingerprint": "031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8a5da3b@sha256:031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 2098.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
          "template_reference_name": "languages-start-points",
          "git_commit": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a",
          "git_commit_info": {
            "sha1": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
            "message": "Merge pull request #284 from cyber-dojo/rename-terraform-dir\n\nRename terraform dir",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417427.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=0faef22c-d2e1-4199-b115-f97f2dce",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca...9635c369db243bfccdd50a0f4abd8cae78c5693a",
            "previous_git_commit": "8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
            "previous_fingerprint": "031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8a5da3b@sha256:031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "8a5da3b0cf05ad43b5b4f80f6c8077c84c0d2dca",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2098.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "languages-start-points",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=4afc7176-4a7f-4652-8a72-b5d90467",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8a5da3b@sha256:031858e5ff2bc45ebbb79d5c80e21f47f8e68e50ec1f3528b6c1ec9e42892453",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-167",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 85704.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
          "template_reference_name": "languages-start-points",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=441e2de7-585a-4a98-a192-738cc7cd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -338191.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1?artifact_id=d68e6623-80d4-4b1a-9b80-07768e45",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": -339533.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/395ce9851c47487a826b4d5ed5cc61d5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
                    "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
      "fingerprint": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
      "creationTimestamp": [
        1790419878
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=a06d8591-02de-464b-ba15-2e7e7158",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/1455947f91ae9264f6cd078ef8fe3f3a0204603a...9047099552a4db3aebbf4187ebf88931b8fec5fb",
        "previous_git_commit": "1455947f91ae9264f6cd078ef8fe3f3a0204603a",
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/1455947f91ae9264f6cd078ef8fe3f3a0204603a",
        "previous_fingerprint": "4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:1455947@sha256:4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "1455947f91ae9264f6cd078ef8fe3f3a0204603a",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 2443.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
          "template_reference_name": "nginx",
          "git_commit": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb",
          "git_commit_info": {
            "sha1": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
            "message": "Merge pull request #174 from cyber-dojo/rename-terraform-dir\n\nRename terraform dir",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417435.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=a06d8591-02de-464b-ba15-2e7e7158",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/1455947f91ae9264f6cd078ef8fe3f3a0204603a...9047099552a4db3aebbf4187ebf88931b8fec5fb",
            "previous_git_commit": "1455947f91ae9264f6cd078ef8fe3f3a0204603a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/1455947f91ae9264f6cd078ef8fe3f3a0204603a",
            "previous_fingerprint": "4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:1455947@sha256:4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "1455947f91ae9264f6cd078ef8fe3f3a0204603a",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 2443.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "nginx",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=e3b90a18-e249-41e6-a44a-220868e0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:1455947@sha256:4aba71112e0756a3a428ec8453d9dc9f18d8e3eb992bb05860d4ed79a996ff98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-169",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 86057.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=24c4977c-f98c-42e1-88b6-ca625183",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1474223.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
          "template_reference_name": "nginx",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300?artifact_id=e55a98e3-6334-43f6-bba5-456a29a1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -337838.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/bf227c0361b544f59762f8f5bf13a270",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
                    "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
      "fingerprint": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
      "creationTimestamp": [
        1790419856
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=1e1ed13b-f217-41b2-9957-9b3eee58",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a...cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
        "previous_git_commit": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
        "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 2426.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
          "template_reference_name": "spooler",
          "git_commit": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
          "git_commit_info": {
            "sha1": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
            "message": "Merge pull request #22 from cyber-dojo/rename-terraform-dir\n\nRename terraform dir",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417430.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=1e1ed13b-f217-41b2-9957-9b3eee58",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a...cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
            "previous_git_commit": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "5e4740c1146988f2e90cd2eb2fc6de0f8603e20a",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 2426.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "spooler",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=7310606e-2060-4a46-a65d-cc375ef5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 86035.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
          "template_reference_name": "spooler",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=644d7cdd-1e45-4731-8e2a-ad5d1cc4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": -337860.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1?artifact_id=f01d9dc2-d9a3-48d3-8e39-c175f160",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": -339202.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f639692403714ef0aa9ff952c3325eb9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:41b9d61@sha256:5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
                    "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
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
      "fingerprint": "5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
      "creationTimestamp": [
        1790419855
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "41b9d6108dc358821dd12abbc2305e2457aad146",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f?artifact_id=3a766a44-342a-42bb-8cdb-c782b4d4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/6b20a423d5ce05139d4480e9ce67f40e3eda2e07...41b9d6108dc358821dd12abbc2305e2457aad146",
        "previous_git_commit": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
        "previous_fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 2422.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
          "template_reference_name": "dashboard",
          "git_commit": "41b9d6108dc358821dd12abbc2305e2457aad146",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146",
          "git_commit_info": {
            "sha1": "41b9d6108dc358821dd12abbc2305e2457aad146",
            "message": "Rename terraform dir (#440)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417433.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f?artifact_id=3a766a44-342a-42bb-8cdb-c782b4d4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/6b20a423d5ce05139d4480e9ce67f40e3eda2e07...41b9d6108dc358821dd12abbc2305e2457aad146",
            "previous_git_commit": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
            "previous_fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "6b20a423d5ce05139d4480e9ce67f40e3eda2e07",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 2422.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "dashboard",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f?artifact_id=23483c3d-bb76-4094-8250-6d343ff2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 86034.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
          "template_reference_name": "dashboard",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f?artifact_id=db3af3ec-5bac-4aa8-a732-7fd2d83f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6b20a42@sha256:4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "dashboard-4889ce921333abe3acc52880342a6ceb27cd66482e4f8fc93e20d5a91d972d29",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -337861.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b384d2ae39444576bb50456ebca06000",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:e302b99@sha256:2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
      "fingerprint": "2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
      "creationTimestamp": [
        1790419522
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/e302b99e045f21adf33ac13c793616cc2fb2ba00",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=5da69929-83e9-451a-981e-a9b9c9db",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/d01bb39495a1356eabe934bef84b92cc964a26f1...e302b99e045f21adf33ac13c793616cc2fb2ba00",
        "previous_git_commit": "d01bb39495a1356eabe934bef84b92cc964a26f1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1",
        "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 2102.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
          "template_reference_name": "exercises-start-points",
          "git_commit": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/e302b99e045f21adf33ac13c793616cc2fb2ba00",
          "git_commit_info": {
            "sha1": "e302b99e045f21adf33ac13c793616cc2fb2ba00",
            "message": "Merge pull request #153 from cyber-dojo/rename-terraform-dir\n\nRename terraform dir",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417420.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/e302b99e045f21adf33ac13c793616cc2fb2ba00"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=5da69929-83e9-451a-981e-a9b9c9db",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/d01bb39495a1356eabe934bef84b92cc964a26f1...e302b99e045f21adf33ac13c793616cc2fb2ba00",
            "previous_git_commit": "d01bb39495a1356eabe934bef84b92cc964a26f1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/d01bb39495a1356eabe934bef84b92cc964a26f1",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "d01bb39495a1356eabe934bef84b92cc964a26f1",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2102.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "exercises-start-points",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=e65a837b-716b-4a02-8dac-d6804342",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 85701.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
          "template_reference_name": "exercises-start-points",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=701d2cbd-cee9-49cc-bc69-d2040515",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -338194.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=684c5624-3d8d-4ee6-98ff-dd0381d5",
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
          "commit_lead_time": -339536.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d80474aeb77e47e995c5dc27aeab7abc",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
                    "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
      "fingerprint": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
      "creationTimestamp": [
        1790419522
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=c204e0b1-78db-4898-a6eb-1c6e77e1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/99d7b74f39e311d492902ad48dbe97da63f2c687...10ed49777abb7b3c7be0da1bd536c6b44f34533c",
        "previous_git_commit": "99d7b74f39e311d492902ad48dbe97da63f2c687",
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687",
        "previous_fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 2071.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
          "template_reference_name": "creator",
          "git_commit": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c",
          "git_commit_info": {
            "sha1": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
            "message": "Rename terraform dir (#61)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417451.0,
            "url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=c204e0b1-78db-4898-a6eb-1c6e77e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/99d7b74f39e311d492902ad48dbe97da63f2c687...10ed49777abb7b3c7be0da1bd536c6b44f34533c",
            "previous_git_commit": "99d7b74f39e311d492902ad48dbe97da63f2c687",
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687",
            "previous_fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "99d7b74f39e311d492902ad48dbe97da63f2c687",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 2071.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "creator",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=fde76598-6573-4fb2-b0c7-69aeb555",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-165",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 85701.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=4164f239-2a9d-4286-a18d-975ae465",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "creator-a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1473867.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
          "template_reference_name": "creator",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e?artifact_id=34b78c85-2d57-40ee-8c0b-232b0caa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613@sha256:ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "creator-ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -338194.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b1eed907137242fc8add39c2ff7e4c09",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
                    "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
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
      "fingerprint": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
      "creationTimestamp": [
        1790419520
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "8d428aa6c487aacc14f820314ab5749a861f1319",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810?artifact_id=d206f015-1370-48df-9fed-00570e74",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/a1af9ed1e38cdf8e447bd9d7de6b97e994876505...8d428aa6c487aacc14f820314ab5749a861f1319",
        "previous_git_commit": "a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
        "previous_fingerprint": "39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:a1af9ed@sha256:39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 1281.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
          "template_reference_name": "differ",
          "git_commit": "8d428aa6c487aacc14f820314ab5749a861f1319",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319",
          "git_commit_info": {
            "sha1": "8d428aa6c487aacc14f820314ab5749a861f1319",
            "message": "Rename terraform dir to allow monorepo style (#486)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790418239.0,
            "url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810?artifact_id=d206f015-1370-48df-9fed-00570e74",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/a1af9ed1e38cdf8e447bd9d7de6b97e994876505...8d428aa6c487aacc14f820314ab5749a861f1319",
            "previous_git_commit": "a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
            "previous_fingerprint": "39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:a1af9ed@sha256:39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "a1af9ed1e38cdf8e447bd9d7de6b97e994876505",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1281.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "differ",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810?artifact_id=c9e6d5eb-f7fc-4994-8edc-d40a441a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:a1af9ed@sha256:39612552204cf3f5ece4e9c0a52982cb9d7ece6e0bf4ff92bcdb0d1d5a645fb2",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-168",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 85699.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
          "template_reference_name": "differ",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810?artifact_id=45afe1fa-fa9b-47d4-a49a-ae5c4e8b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -338196.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4f73fbf73513449baff72766e1719e12",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c267890@sha256:68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
                    "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-37",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
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
      "fingerprint": "68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
      "creationTimestamp": [
        1790419509
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "c267890b689f43e24679bfe9006ddc390447e7e7",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c267890b689f43e24679bfe9006ddc390447e7e7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a?artifact_id=4c117940-9594-43bf-b575-42a1cb69",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/86c839ee588f393d84a6b9c036478d10bb6f2a2d...c267890b689f43e24679bfe9006ddc390447e7e7",
        "previous_git_commit": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d",
        "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 2086.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "c267890b689f43e24679bfe9006ddc390447e7e7",
          "template_reference_name": "custom-start-points",
          "git_commit": "c267890b689f43e24679bfe9006ddc390447e7e7",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c267890b689f43e24679bfe9006ddc390447e7e7",
          "git_commit_info": {
            "sha1": "c267890b689f43e24679bfe9006ddc390447e7e7",
            "message": "Merge pull request #147 from cyber-dojo/rename-terraform-dir\n\nRename terraform dir",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790417423.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/c267890b689f43e24679bfe9006ddc390447e7e7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a?artifact_id=4c117940-9594-43bf-b575-42a1cb69",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/86c839ee588f393d84a6b9c036478d10bb6f2a2d...c267890b689f43e24679bfe9006ddc390447e7e7",
            "previous_git_commit": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/86c839ee588f393d84a6b9c036478d10bb6f2a2d",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "86c839ee588f393d84a6b9c036478d10bb6f2a2d",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2086.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-37",
          "template_reference_name": "custom-start-points",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a?artifact_id=efdf388f-e010-49f3-bab0-d5c63695",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 85688.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a",
          "template_reference_name": "custom-start-points",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/68f35f91b77dad37faa40efc2ab738a18330ae032e5d0b901a3489aff8dd873a?artifact_id=6e4b61ee-c3bb-4796-a321-2a753912",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -338207.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c60c8ebe0c824adb92155e83debfd4d3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
                    "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
      "fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
      "creationTimestamp": [
        1790416576,
        1790416647,
        1790416655
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "6131d764b41b449d77e436598c953691d23eaced",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=f11c519e-c14e-41ca-b67a-a45c4c64",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/4b2bfc038576e2a7648090c4c1289fbc9ebfc481...6131d764b41b449d77e436598c953691d23eaced",
        "previous_git_commit": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
        "previous_fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 8092.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "6131d764b41b449d77e436598c953691d23eaced",
          "template_reference_name": "runner",
          "git_commit": "6131d764b41b449d77e436598c953691d23eaced",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced",
          "git_commit_info": {
            "sha1": "6131d764b41b449d77e436598c953691d23eaced",
            "message": "Accept an untagged or :latest image_name (#317)\n\nSelf-hosted servers use start-points whose\nmanifest image_name has no tag. Runner refused\nevery [test] for them with a 400. Pinning suits\ncyber-dojo.org but is too strict for others.\n\nAn untagged name now means :latest, as it does\nto docker. Malformed names are still refused.\nforget now tags its name as pull does, since\nthe belief it drops is held under :latest.\nWithout that, a missing untagged image would\nnever be pulled again.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790408484.0,
            "url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=f11c519e-c14e-41ca-b67a-a45c4c64",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/4b2bfc038576e2a7648090c4c1289fbc9ebfc481...6131d764b41b449d77e436598c953691d23eaced",
            "previous_git_commit": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
            "previous_fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "4b2bfc038576e2a7648090c4c1289fbc9ebfc481",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 8092.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-36",
          "template_reference_name": "runner",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=34f23e16-6d96-4f4b-b2bb-ac83b2b3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 82755.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
          "template_reference_name": "runner",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=93943447-fedc-4c58-90c0-71f4f186",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -341140.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845?artifact_id=c0b7638a-f928-4330-b70b-8e38cb0b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:4b2bfc0@sha256:8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-8e36719b74e24f93433b2fa52107beec253f7f5dc2fcefc4aad60befe31db65f",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -342482.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/99ca0f5913dc448a8e03667a89f26d9f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5bdfa1d@sha256:cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
                    "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
      "fingerprint": "cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
      "creationTimestamp": [
        1790416570,
        1790416571,
        1790416571
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
      "commit_url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01?artifact_id=b7881f37-2d27-4a47-8e14-1c323d6e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/1fe7246b3c578fa0d594cdd6176615964a461920...5bdfa1df3baee4124759dcc71a617174e11ed51f",
        "previous_git_commit": "1fe7246b3c578fa0d594cdd6176615964a461920",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/1fe7246b3c578fa0d594cdd6176615964a461920",
        "previous_fingerprint": "19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1fe7246@sha256:19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "1fe7246b3c578fa0d594cdd6176615964a461920",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 10897.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
          "template_reference_name": "web",
          "git_commit": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
          "commit_url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f",
          "git_commit_info": {
            "sha1": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
            "message": "Show the runner error in the [test] dialog (#430)\n\nA start-point whose manifest has an untagged\nimage_name makes runner refuse every [test].\nThe dialog showed only \"Status=500\", so the\nkata owner had no clue why.\n\nThe run_tests route now answers a runner\nerror with its message as the body, and the\ndialog shows that body after the status.\nThe message is runner exception JSON minus\nits body field, which holds every kata file.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790405673.0,
            "url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01?artifact_id=b7881f37-2d27-4a47-8e14-1c323d6e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/1fe7246b3c578fa0d594cdd6176615964a461920...5bdfa1df3baee4124759dcc71a617174e11ed51f",
            "previous_git_commit": "1fe7246b3c578fa0d594cdd6176615964a461920",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/1fe7246b3c578fa0d594cdd6176615964a461920",
            "previous_fingerprint": "19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1fe7246@sha256:19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "1fe7246b3c578fa0d594cdd6176615964a461920",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 10897.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-36",
          "template_reference_name": "web",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01?artifact_id=be23ad20-90e5-47e5-a020-3c2a30e2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1fe7246@sha256:19a3ccda7554cbcd85f22f341c65dbd83db95c8bcdf9fbd1876a0402967f7654",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-171",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 82749.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01?artifact_id=a4b3584b-a720-49c4-b176-dcafe939",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1470915.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
          "template_reference_name": "web",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01?artifact_id=88113b31-2ad0-4133-80e9-c1a0129f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -341146.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/710a92566d904f3090ea11a1a8589eaf",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
                    "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-36",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
      "fingerprint": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
      "creationTimestamp": [
        1790416559
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=cba86481-c5e6-4b47-a242-dcbfa57d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/7c4708f675a7717376529273ec32d08cd93f5c26...1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
        "previous_git_commit": "7c4708f675a7717376529273ec32d08cd93f5c26",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26",
        "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 1251.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
          "template_reference_name": "saver",
          "git_commit": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
          "git_commit_info": {
            "sha1": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
            "message": "Rerun workflow to pick up fix for expat (#449)\n\nSnyk reports SNYK-ALPINE324-EXPAT-20066735 in the\nimage on cyber-dojo.org. expat comes in via the\nunpinned apk add git in the Dockerfile, and the\nfixed apk is already out (differ #484), so a\nrebuild picks it up.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790415308.0,
            "url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=cba86481-c5e6-4b47-a242-dcbfa57d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/7c4708f675a7717376529273ec32d08cd93f5c26...1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
            "previous_git_commit": "7c4708f675a7717376529273ec32d08cd93f5c26",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/7c4708f675a7717376529273ec32d08cd93f5c26",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "7c4708f675a7717376529273ec32d08cd93f5c26",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1251.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-36",
          "template_reference_name": "saver",
          "git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
          "git_commit_info": {
            "sha1": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "message": "Fix terraform deployment dir ready for merging web,dashboard,creator",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790333821.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=75565cea-97b1-45d3-969b-3ae4e7e4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-35",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 82738.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
          "template_reference_name": "saver",
          "git_commit": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4",
          "git_commit_info": {
            "sha1": "9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "message": "Merge pull request #5 from cyber-dojo/expiry-report-reads-deadlines-from-the-rego\n\nTake expiry deadlines from the rego, not a python copy",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790757716.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/9dd50c00dae4241dd83b463999f666a4ec604dd4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=600edb2c-95ef-4647-a94a-3b811f1b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...9dd50c00dae4241dd83b463999f666a4ec604dd4",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -341157.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162?artifact_id=62a23664-dc32-4dca-a124-f28e8383",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": -342499.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1ddc3276de22469b9c5dec6ec71ef565",
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

