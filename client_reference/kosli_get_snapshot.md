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
  "index": 5440,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1791532978.4470391,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5440",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2390863@sha256:a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
      "fingerprint": "a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
      "creationTimestamp": [
        1791290238
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
      "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=de08f569-3531-4bc6-8567-47fbbef9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/10ed49777abb7b3c7be0da1bd536c6b44f34533c...239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_git_commit": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c",
        "previous_fingerprint": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 82841.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "template_reference_name": "creator",
          "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
          "git_commit_info": {
            "sha1": "239086385550e2c369fd3aa1f656b56f362db8f7",
            "message": "Give review the edit hotkeys; test what we rushed (#466)\n\nAlt-J/K/O now act on review whenever it shows, on the\nedit page or from a dashboard, and Alt-T/R/A/G do\nnothing there, rather than running hidden tests.\n\nThe last two days moved fast and left behaviour with\nno tests: review tabs, settings row, scrim, dialog\n[X], review predict counts, kata tab scoping and the\nphonetic ID tip. Each new test was seen to fail with\nits code broken on purpose, then pass when restored.\n\nAlso: the review sheet gets the editor 4px top gap,\nand the phonetic word for P is Papa, not Pappa.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791207397.0,
            "url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=de08f569-3531-4bc6-8567-47fbbef9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/10ed49777abb7b3c7be0da1bd536c6b44f34533c...239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_git_commit": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/10ed49777abb7b3c7be0da1bd536c6b44f34533c",
            "previous_fingerprint": "aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:10ed497@sha256:aff5bba4fc23161df346cb853b65d653d94e963c35fe4b0ea0e0e1eeaf8dc32e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "10ed49777abb7b3c7be0da1bd536c6b44f34533c",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 82841.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-40",
          "template_reference_name": "web",
          "git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "git_commit_info": {
            "sha1": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "message": "Merge pull request #17 from cyber-dojo/deploy-each-component-to-its-own-state\n\nGive each component its own Terraform state on promotion",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791289526.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=5d0e32f0-879b-4387-8fa8-2f05e343",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/4b34724777db6edfc8a04174a9926c595f934dd8...8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-39",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 712.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=48e1317f-bcf3-478b-8fcb-bbdd7338",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 531180.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a944be1a68419c9feffe3656541af2bff65b2efbef9421ae18563bb150868beb?artifact_id=04114627-61f4-4f1c-99ea-d8960692",
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
          "commit_lead_time": 531180.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1c64fd954d44464fb5b6fde6f22825d3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
      "fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
      "creationTimestamp": [
        1791287800,
        1791287808,
        1791287842
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
      "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=8c798531-5ed7-4c2d-9c6d-ec444dd8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/5bdfa1df3baee4124759dcc71a617174e11ed51f...239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_git_commit": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f",
        "previous_fingerprint": "cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5bdfa1d@sha256:cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 80403.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "template_reference_name": "web",
          "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
          "git_commit_info": {
            "sha1": "239086385550e2c369fd3aa1f656b56f362db8f7",
            "message": "Give review the edit hotkeys; test what we rushed (#466)\n\nAlt-J/K/O now act on review whenever it shows, on the\nedit page or from a dashboard, and Alt-T/R/A/G do\nnothing there, rather than running hidden tests.\n\nThe last two days moved fast and left behaviour with\nno tests: review tabs, settings row, scrim, dialog\n[X], review predict counts, kata tab scoping and the\nphonetic ID tip. Each new test was seen to fail with\nits code broken on purpose, then pass when restored.\n\nAlso: the review sheet gets the editor 4px top gap,\nand the phonetic word for P is Papa, not Pappa.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791207397.0,
            "url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=8c798531-5ed7-4c2d-9c6d-ec444dd8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/5bdfa1df3baee4124759dcc71a617174e11ed51f...239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_git_commit": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/5bdfa1df3baee4124759dcc71a617174e11ed51f",
            "previous_fingerprint": "cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5bdfa1d@sha256:cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "5bdfa1df3baee4124759dcc71a617174e11ed51f",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 80403.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "web",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=18ed4a5b-a3ec-450d-a246-aca9ea71",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5bdfa1d@sha256:cf8fe609455bb3871bf4bcb67054b9e640e07aaf038046525dc012f2a60dbb01",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-36",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 914.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=805f6793-5eb3-4068-883f-94055f22",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": 528742.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273?artifact_id=fdbbc89c-5637-4d34-89f9-c9db3899",
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
          "commit_lead_time": 528742.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fbc166d74f234767acd85f6dde3e293a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:7a96f63@sha256:57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
                    "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
      "fingerprint": "57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
      "creationTimestamp": [
        1791287461,
        1791287462,
        1791287540
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/7a96f6335ac05b814cfed0947bed40e29fb14c92",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=143f3ad8-2fab-4f18-ae17-88fa64b1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/6131d764b41b449d77e436598c953691d23eaced...7a96f6335ac05b814cfed0947bed40e29fb14c92",
        "previous_git_commit": "6131d764b41b449d77e436598c953691d23eaced",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced",
        "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "6131d764b41b449d77e436598c953691d23eaced",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 191661.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
          "template_reference_name": "runner",
          "git_commit": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/7a96f6335ac05b814cfed0947bed40e29fb14c92",
          "git_commit_info": {
            "sha1": "7a96f6335ac05b814cfed0947bed40e29fb14c92",
            "message": "Dockerfile - Automated base-image update (#318)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791095800.0,
            "url": "https://github.com/cyber-dojo/runner/commit/7a96f6335ac05b814cfed0947bed40e29fb14c92"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=143f3ad8-2fab-4f18-ae17-88fa64b1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/6131d764b41b449d77e436598c953691d23eaced...7a96f6335ac05b814cfed0947bed40e29fb14c92",
            "previous_git_commit": "6131d764b41b449d77e436598c953691d23eaced",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/6131d764b41b449d77e436598c953691d23eaced",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "6131d764b41b449d77e436598c953691d23eaced",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 191661.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "runner",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=c46a419b-b371-4f67-800a-2bf8d151",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-36",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 575.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=998079ed-f906-437e-a111-34302091",
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
          "commit_lead_time": 528403.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/57dbb120326b3c3fabcec03bc1d2bb220a978fd7b5778f182ddb3dfe4906f1b4?artifact_id=78c3b49e-5f82-4106-b0ae-69757e1f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
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
          "commit_lead_time": 528403.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ec45627ec9f743429ca9fa756e5707b4",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d",
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
        "type": "changed",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=4cda5e92-a51b-426f-9b1b-a5c8a543",
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
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2c861510e434ed618b2e296eaed392648aaf18629908b890947733b11aa97e8d?artifact_id=de7d0bfb-f589-461e-bb4b-efe933e3",
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
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3fb02b6@sha256:3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
                    "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
      "fingerprint": "3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
      "creationTimestamp": [
        1791364437
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=9e147c56-48a1-4d72-9a46-6d20397a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/c415496d0e35cbca51c55d0401c141c982a8d711...3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
        "previous_git_commit": "c415496d0e35cbca51c55d0401c141c982a8d711",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c415496d0e35cbca51c55d0401c141c982a8d711",
        "previous_fingerprint": "e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c415496@sha256:e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "c415496d0e35cbca51c55d0401c141c982a8d711",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 902.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
          "template_reference_name": "custom-start-points",
          "git_commit": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
          "git_commit_info": {
            "sha1": "3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
            "message": "Merge pull request #150 from cyber-dojo/run-workflow-172\n\nDeploy new artifact to reset failed drift-detection",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791363535.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=9e147c56-48a1-4d72-9a46-6d20397a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/c415496d0e35cbca51c55d0401c141c982a8d711...3fb02b6f8a2d4e9edfd7a5e36b8df7c503ee1e99",
            "previous_git_commit": "c415496d0e35cbca51c55d0401c141c982a8d711",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/c415496d0e35cbca51c55d0401c141c982a8d711",
            "previous_fingerprint": "e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c415496@sha256:e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "c415496d0e35cbca51c55d0401c141c982a8d711",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 902.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-173",
          "template_reference_name": "custom-start-points",
          "git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "git_commit_info": {
            "sha1": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "message": "Merge pull request #17 from cyber-dojo/deploy-each-component-to-its-own-state\n\nGive each component its own Terraform state on promotion",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791289526.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=6dcdde81-b426-409f-9514-ba4be120",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/4b34724777db6edfc8a04174a9926c595f934dd8...8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_fingerprint": "e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:c415496@sha256:e232125238c2a0344957e75393c37ba8f88d35b114b35a7c048c642d32681828",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-39",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 74911.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/3fb70797c4e8a01bb490bcb7a040bd2c689048d4c0b4a810beee5a5e7cacfb39?artifact_id=63c111b0-b119-40a9-ad39-54e12413",
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
          "commit_lead_time": 605379.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1ba63dad8f7a4c76b98597e028907952",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
                    "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-40",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
      "fingerprint": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
      "creationTimestamp": [
        1791290226
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
      "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=53075f10-16cd-40aa-941c-0e9a14ad",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/41b9d6108dc358821dd12abbc2305e2457aad146...239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_git_commit": "41b9d6108dc358821dd12abbc2305e2457aad146",
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146",
        "previous_fingerprint": "5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:41b9d61@sha256:5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 82829.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "template_reference_name": "dashboard",
          "git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
          "commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
          "git_commit_info": {
            "sha1": "239086385550e2c369fd3aa1f656b56f362db8f7",
            "message": "Give review the edit hotkeys; test what we rushed (#466)\n\nAlt-J/K/O now act on review whenever it shows, on the\nedit page or from a dashboard, and Alt-T/R/A/G do\nnothing there, rather than running hidden tests.\n\nThe last two days moved fast and left behaviour with\nno tests: review tabs, settings row, scrim, dialog\n[X], review predict counts, kata tab scoping and the\nphonetic ID tip. Each new test was seen to fail with\nits code broken on purpose, then pass when restored.\n\nAlso: the review sheet gets the editor 4px top gap,\nand the phonetic word for P is Papa, not Pappa.\n\nCo-authored-by: Claude Opus 5.5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791207397.0,
            "url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=53075f10-16cd-40aa-941c-0e9a14ad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/41b9d6108dc358821dd12abbc2305e2457aad146...239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_git_commit": "41b9d6108dc358821dd12abbc2305e2457aad146",
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/41b9d6108dc358821dd12abbc2305e2457aad146",
            "previous_fingerprint": "5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:41b9d61@sha256:5d8285110f59fd942cce826c7e6dc6c27397b36ce6c2845b0d104ec6814c1f9f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "41b9d6108dc358821dd12abbc2305e2457aad146",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 82829.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-40",
          "template_reference_name": "web",
          "git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
          "git_commit_info": {
            "sha1": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "message": "Merge pull request #17 from cyber-dojo/deploy-each-component-to-its-own-state\n\nGive each component its own Terraform state on promotion",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791289526.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=4c612b45-905f-4e5a-aceb-6938eae1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/4b34724777db6edfc8a04174a9926c595f934dd8...8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-39",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 700.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=23914b17-7e4e-40e9-98c4-7dc0d02b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2390863@sha256:932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "web-932659867f5bf3d46457c66690f4d559edbf494b9bbefc97bb5e225e80287273",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 531168.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45?artifact_id=e8e8dffb-00c2-4d68-ba92-2c0f7a27",
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
          "commit_lead_time": 531168.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/8a4c32e759b24964affa60b493b1d517",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8e32bc0@sha256:efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
                    "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
      "fingerprint": "efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
      "creationTimestamp": [
        1791287798
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/8e32bc009dd16087e5160d309a9ce4303b7d895f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=e033c82e-2b65-400f-8656-ca4fa6cb",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4...8e32bc009dd16087e5160d309a9ce4303b7d895f",
        "previous_git_commit": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
        "previous_fingerprint": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 191992.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
          "template_reference_name": "saver",
          "git_commit": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/8e32bc009dd16087e5160d309a9ce4303b7d895f",
          "git_commit_info": {
            "sha1": "8e32bc009dd16087e5160d309a9ce4303b7d895f",
            "message": "Dockerfile - Automated base-image update (#453)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791095806.0,
            "url": "https://github.com/cyber-dojo/saver/commit/8e32bc009dd16087e5160d309a9ce4303b7d895f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=e033c82e-2b65-400f-8656-ca4fa6cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4...8e32bc009dd16087e5160d309a9ce4303b7d895f",
            "previous_git_commit": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
            "previous_fingerprint": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "1b1ab5ff9bd37774c20dd3e790abb7ecd9d5c0d4",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 191992.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "saver",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=23a4b404-a7a9-448b-81d6-cd134722",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:1b1ab5f@sha256:02f5a01b12f9fe0ee0e88f74a6ebdbe8a35c23bdb076538a6699a403fc366162",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-36",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 912.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=09b23f05-2bb4-4e36-8e59-86e712ee",
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
          "commit_lead_time": 528740.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/efbafb99870cf4c4a838324e8bbc70975c4f3ea2ba5d395433c5344456b60ae4?artifact_id=26c48fa4-512a-40a0-a06d-a2eb2f8a",
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
          "commit_lead_time": 528740.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/000af09d44a741ed957fe1da6c44e3de",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9b49875@sha256:b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
                    "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
      "fingerprint": "b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
      "creationTimestamp": [
        1791287790
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "9b498758459dd636ff7dbca04367de3f547454f0",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/9b498758459dd636ff7dbca04367de3f547454f0",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=0b1dd4aa-371f-41db-9dc9-ca52d3a3",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/8d428aa6c487aacc14f820314ab5749a861f1319...9b498758459dd636ff7dbca04367de3f547454f0",
        "previous_git_commit": "8d428aa6c487aacc14f820314ab5749a861f1319",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319",
        "previous_fingerprint": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 189773.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "9b498758459dd636ff7dbca04367de3f547454f0",
          "template_reference_name": "differ",
          "git_commit": "9b498758459dd636ff7dbca04367de3f547454f0",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/9b498758459dd636ff7dbca04367de3f547454f0",
          "git_commit_info": {
            "sha1": "9b498758459dd636ff7dbca04367de3f547454f0",
            "message": "Merge pull request #493 from cyber-dojo/update-base-image-a44535c\n\nMerge update-base-image into main",
            "author": "AlexKantor87 <alex@kosli.com>",
            "branch": "",
            "timestamp": 1791098017.0,
            "url": "https://github.com/cyber-dojo/differ/commit/9b498758459dd636ff7dbca04367de3f547454f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=0b1dd4aa-371f-41db-9dc9-ca52d3a3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/8d428aa6c487aacc14f820314ab5749a861f1319...9b498758459dd636ff7dbca04367de3f547454f0",
            "previous_git_commit": "8d428aa6c487aacc14f820314ab5749a861f1319",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/8d428aa6c487aacc14f820314ab5749a861f1319",
            "previous_fingerprint": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "8d428aa6c487aacc14f820314ab5749a861f1319",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 189773.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "differ",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=456c7802-2b9f-40bc-acfb-a0c07465",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8d428aa@sha256:26d973fb3af40e2f0e250986194f7089250620ed1a6eb13529a7a19d7ad1b810",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-37",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 904.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=440efe29-17f5-4c65-a716-51453de5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": 528732.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c?artifact_id=f3d6331b-90b0-4966-b8e0-42e5845d",
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
          "commit_lead_time": 528732.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/14515b546b3d44f0be6c78bb9853ecde",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
                    "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
      "fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
      "creationTimestamp": [
        1791287466
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "28636f69be43a7676d61db98b086eaff507d6e9c",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=bf6bf5b8-e617-4938-acac-ced1cc03",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e...28636f69be43a7676d61db98b086eaff507d6e9c",
        "previous_git_commit": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
        "previous_fingerprint": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 191663.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
          "template_reference_name": "spooler",
          "git_commit": "28636f69be43a7676d61db98b086eaff507d6e9c",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
          "git_commit_info": {
            "sha1": "28636f69be43a7676d61db98b086eaff507d6e9c",
            "message": "Merge pull request #23 from cyber-dojo/update-base-image-a44535c\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791095803.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=bf6bf5b8-e617-4938-acac-ced1cc03",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e...28636f69be43a7676d61db98b086eaff507d6e9c",
            "previous_git_commit": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
            "previous_fingerprint": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "cf50c40078daafd2a6897d0a7f7d1a89bfd1d25e",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 191663.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "spooler",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=d3ae22c6-422a-42e5-ace6-b937a53d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:cf50c40@sha256:cc96812a575d10837cb37165ca066862af7763906bb0605fda8e4e3d4cd11cd1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-37",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 580.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=d184d3a7-bd8e-450b-a293-dae171f6",
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
          "commit_lead_time": 528408.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d?artifact_id=7aa59d4b-3f40-46e9-95de-f3c7948b",
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
          "commit_lead_time": 528408.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/3bcfb4c799f54d0a8c068638670846a5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
                    "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
      "fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
      "creationTimestamp": [
        1791287458
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=7bb1f0f7-24cd-4f5c-a6aa-04828949",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/9047099552a4db3aebbf4187ebf88931b8fec5fb...69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
        "previous_git_commit": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb",
        "previous_fingerprint": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 347275.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
          "template_reference_name": "nginx",
          "git_commit": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
          "git_commit_info": {
            "sha1": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
            "message": "Merge pull request #179 from cyber-dojo/cache-images-for-a-day\n\nCache images for a day so changed ones reach browsers",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1790940183.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=7bb1f0f7-24cd-4f5c-a6aa-04828949",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/9047099552a4db3aebbf4187ebf88931b8fec5fb...69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
            "previous_git_commit": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/9047099552a4db3aebbf4187ebf88931b8fec5fb",
            "previous_fingerprint": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "9047099552a4db3aebbf4187ebf88931b8fec5fb",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 347275.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "nginx",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=92a7d198-a861-458a-a21c-e143f443",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9047099@sha256:7979e65da9f1127cc8d8600782fa06048cbf5c4b99da9e1154e0dc7be13e3300",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-37",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 572.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=b5444afd-339a-40a2-a415-c5dbc1e5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
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
          "commit_lead_time": 528400.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d?artifact_id=7fcf56f0-f436-4f31-b217-487e6e2c",
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
          "commit_lead_time": 528400.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/39d0960f1a184600a0adeb65aaa97623",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c5dd4fa@sha256:5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
                    "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
      "fingerprint": "5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
      "creationTimestamp": [
        1791287456
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c5dd4faa2f40a6a85afceae4565a43a6df553845",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=834cb0b3-828e-4fb3-9d65-fb130696",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9635c369db243bfccdd50a0f4abd8cae78c5693a...c5dd4faa2f40a6a85afceae4565a43a6df553845",
        "previous_git_commit": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a",
        "previous_fingerprint": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 268962.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
          "template_reference_name": "languages-start-points",
          "git_commit": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c5dd4faa2f40a6a85afceae4565a43a6df553845",
          "git_commit_info": {
            "sha1": "c5dd4faa2f40a6a85afceae4565a43a6df553845",
            "message": "Merge pull request #287 from cyber-dojo/add-ada-aunit\n\nAdd Ada-AUnit",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791018494.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/c5dd4faa2f40a6a85afceae4565a43a6df553845"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=834cb0b3-828e-4fb3-9d65-fb130696",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9635c369db243bfccdd50a0f4abd8cae78c5693a...c5dd4faa2f40a6a85afceae4565a43a6df553845",
            "previous_git_commit": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9635c369db243bfccdd50a0f4abd8cae78c5693a",
            "previous_fingerprint": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "9635c369db243bfccdd50a0f4abd8cae78c5693a",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 268962.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-39",
          "template_reference_name": "languages-start-points",
          "git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
          "git_commit_info": {
            "sha1": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "message": "Merge pull request #16 from cyber-dojo/promote-across-repo-moves\n\nLet promotion continue when an Artifact moves repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791286886.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=abc252ce-e5a1-470b-87b9-9f01ccc6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/78095bc425078b1de3795c7dc866d8cafbd564ee...4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit": "78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/78095bc425078b1de3795c7dc866d8cafbd564ee",
            "previous_fingerprint": "b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9635c36@sha256:b37a4601aa580c9111a3964d9845d7d148125afd739fe54b04d624bf1316d5b1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-37",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 570.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=a1a95774-e2a5-46fc-94f1-2ae18949",
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
          "commit_lead_time": 528398.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5f565084b081f73bf44aa1e08407d0f022b6edb8b9cb61c29970b00f84104aaa?artifact_id=09363226-fa03-4250-9f72-6d532c34",
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
          "commit_lead_time": 528398.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ed3779b1ac504b538484c213e526a1dc",
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

