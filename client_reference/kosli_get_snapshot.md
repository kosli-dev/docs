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
  "index": 5309,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1788256325.6192138,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5309",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:d64d2b1@sha256:c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
                    "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
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
      "fingerprint": "c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
      "creationTimestamp": [
        1788256052
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "d64d2b11879179255f11dc991e81fbaf4a040264",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/d64d2b11879179255f11dc991e81fbaf4a040264",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=61384b36-4d32-43f2-8d5d-a72e2e7e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/83357f112ef5c10b157cb84732c77965cc8ddc48...d64d2b11879179255f11dc991e81fbaf4a040264",
        "previous_git_commit": "83357f112ef5c10b157cb84732c77965cc8ddc48",
        "previous_fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
        "previous_trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 420668.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "d64d2b11879179255f11dc991e81fbaf4a040264",
          "template_reference_name": "creator",
          "git_commit": "d64d2b11879179255f11dc991e81fbaf4a040264",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/d64d2b11879179255f11dc991e81fbaf4a040264",
          "git_commit_info": {
            "sha1": "d64d2b11879179255f11dc991e81fbaf4a040264",
            "message": "Merge update-base-image into main (#56)\n\n* Dockerfile - Automated base-image update\n\n* Make the test harness work on the simplecov the new base image carries\n\n  The automated base-image bump brings simplecov 0.21.2 -> 1.1.1, and\n  three things here were written against the older one. Only the first\n  fails the build; the other two announce themselves on stderr every run.\n\n  simplecov_json.rb reopened SimpleCov::Formatter::JSONFormatter to\n  redefine format. In 1.1.1 that class defines format itself, so ruby -w\n  reports the redefinition twice and test_log_warnings goes from 0 to 2.\n  It is now CoverageMetricsFormatter, named for the coverage_metrics.json\n  it writes, which is the same name runner gives the same job. It never\n  needed to be that class: what it produces is per-group totals, not the\n  per-file shape the shipped formatter writes, so it was only borrowing\n  the name to make itself win.\n\n  SimpleCov.add_group is deprecated in favour of group. The block\n  parameter goes from src to path while passing, since it is a source\n  file in both groups and src said otherwise in the test one.\n\n  # :nocov: is deprecated in favour of # simplecov:disable / :enable. The\n  pair wrapping id58_test_base.rb is the only one in the repo.\n\n  Coverage is unchanged: code.lines.total 526, test.lines.total 677,\n  nothing missed in either. coverage.rb already cleared filters, so the\n  test group survived 1.1.1 tightening the default test_frameworks skip\n  to an anchored regex, which is what caught start-points-base out.\n\n---------\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787835384.0,
            "url": "https://github.com/cyber-dojo/creator/commit/d64d2b11879179255f11dc991e81fbaf4a040264"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=61384b36-4d32-43f2-8d5d-a72e2e7e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/83357f112ef5c10b157cb84732c77965cc8ddc48...d64d2b11879179255f11dc991e81fbaf4a040264",
            "previous_git_commit": "83357f112ef5c10b157cb84732c77965cc8ddc48",
            "previous_fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/83357f112ef5c10b157cb84732c77965cc8ddc48",
            "previous_trail_name": "83357f112ef5c10b157cb84732c77965cc8ddc48",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 420668.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
          "template_reference_name": "creator",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=5d73a605-4286-4a94-be8c-e2262a67",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "creator-adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 594065.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=615d01cb-77c4-4429-9531-60460983",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:83357f1@sha256:adb922d738b50876f1cd13f5a998ade341abfd64b3561d0889264399c33c528b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 2939058.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab",
          "template_reference_name": "creator",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c48710e3304e24406c03381a31d01f520ab2f60846aa0b57adbda0a776ebc1ab?artifact_id=d4d51513-4c22-4eb3-b8b3-caa88478",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 594065.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/3497b80bc2ff41e792b5ca4a833882fc",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:27b3504@sha256:1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
                    "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
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
      "fingerprint": "1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
      "creationTimestamp": [
        1788255750
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=9045bb07-ea42-482f-99c3-4fe5b86f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/fb791742054fa28dd89269aac8002ebfd7b3386e...27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
        "previous_git_commit": "fb791742054fa28dd89269aac8002ebfd7b3386e",
        "previous_fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e",
        "previous_trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 1790.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
          "template_reference_name": "nginx",
          "git_commit": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
          "git_commit_info": {
            "sha1": "27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
            "message": "Merge pull request #169 from cyber-dojo/run-workflow-to-pick-up-fixes-to-snyk-vulns\n\nRun workflow to pick up fixes to new snyk vulns",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788253960.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=9045bb07-ea42-482f-99c3-4fe5b86f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/fb791742054fa28dd89269aac8002ebfd7b3386e...27b350410ebcca5ff192f2ca4cdd0e3e49f5ac65",
            "previous_git_commit": "fb791742054fa28dd89269aac8002ebfd7b3386e",
            "previous_fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/fb791742054fa28dd89269aac8002ebfd7b3386e",
            "previous_trail_name": "fb791742054fa28dd89269aac8002ebfd7b3386e",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1790.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
          "template_reference_name": "nginx",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=d14d27b1-2d09-43a9-bf35-f58f3164",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "nginx-b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 593763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=1b78fe0b-61c8-4e00-bc5a-d54ae788",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fb79174@sha256:b70ff1f9493f5d4205e0e95e565b3fc4d909de237b10e490b250671d0d6895cf",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 2938756.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21",
          "template_reference_name": "nginx",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1d1a2f8e2ea649bac20578eea7b18c9f03cda4cad5118cefbf425521a77ead21?artifact_id=c340a947-0136-4de1-acc8-2a89f741",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 593763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/675ca6104c294b369094b918f30ab6b9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:a357ebd@sha256:28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
                    "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
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
      "fingerprint": "28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
      "creationTimestamp": [
        1788255750
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/a357ebd85acdd54968fa0192405aaf2e289d27c9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=8e028a8d-a1f2-4732-8663-47012b29",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/068b3424c7da843a4f2d428d2e4915f33efc4a02...a357ebd85acdd54968fa0192405aaf2e289d27c9",
        "previous_git_commit": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
        "previous_fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02",
        "previous_trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 10038.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
          "template_reference_name": "languages-start-points",
          "git_commit": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/a357ebd85acdd54968fa0192405aaf2e289d27c9",
          "git_commit_info": {
            "sha1": "a357ebd85acdd54968fa0192405aaf2e289d27c9",
            "message": "Merge pull request #252 from cyber-dojo/speed-updates-to-slowest-ltfs\n\nSpeed updates to the slowest LTFs",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788245712.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/a357ebd85acdd54968fa0192405aaf2e289d27c9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=8e028a8d-a1f2-4732-8663-47012b29",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/068b3424c7da843a4f2d428d2e4915f33efc4a02...a357ebd85acdd54968fa0192405aaf2e289d27c9",
            "previous_git_commit": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
            "previous_fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/068b3424c7da843a4f2d428d2e4915f33efc4a02",
            "previous_trail_name": "068b3424c7da843a4f2d428d2e4915f33efc4a02",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 10038.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
          "template_reference_name": "languages-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=8b7fa132-7335-4301-a248-b13e4286",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "languages-start-points-adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 593763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=790a39b3-0c7c-4220-9d6b-63bff0f3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:068b342@sha256:adf2596645ae3fe9b711849a2e9aae3a65173b270963e3214b9c7ea00b03c1cb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2938756.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832",
          "template_reference_name": "languages-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/28bc41a2185a154249b1d06983741c39beb3574ebdce7273963ecde2ae9dd832?artifact_id=400979c3-f9c3-4652-8b12-2204fabb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 593763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/cbb20953281f4b168eb98575717b01e7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:b12a5c9@sha256:34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
                    "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
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
      "fingerprint": "34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
      "creationTimestamp": [
        1788255398
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=2aa23627-9e91-488e-b3ea-e4bf2e22",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/790d86b66f4d86ab47f5c521daf5039dc8aeef4d...b12a5c9b17023462d13e81381a69c7ef05f84dc2",
        "previous_git_commit": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "previous_fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "previous_trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 416881.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
          "template_reference_name": "custom-start-points",
          "git_commit": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2",
          "git_commit_info": {
            "sha1": "b12a5c9b17023462d13e81381a69c7ef05f84dc2",
            "message": "Merge pull request #143 from cyber-dojo/update-base-image-ce45d62\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787838517.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/b12a5c9b17023462d13e81381a69c7ef05f84dc2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=2aa23627-9e91-488e-b3ea-e4bf2e22",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/790d86b66f4d86ab47f5c521daf5039dc8aeef4d...b12a5c9b17023462d13e81381a69c7ef05f84dc2",
            "previous_git_commit": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
            "previous_fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
            "previous_trail_name": "790d86b66f4d86ab47f5c521daf5039dc8aeef4d",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 416881.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
          "template_reference_name": "custom-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=b5dae6e2-12e1-47bc-a361-ead8aa3f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 593411.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=63e61c31-696e-4465-9145-2c51f6d4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:790d86b@sha256:8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promote-all-31",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2938404.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09",
          "template_reference_name": "custom-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/34fd30b5a876821ef7047c3e3af23158705ec2ea1f63fa784854639ccd807b09?artifact_id=ff77dce2-dd84-40ff-b134-d21758f5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 593411.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b7894ad2c80e4774adbeab8165291101",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:84e986a@sha256:06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
                    "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
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
      "fingerprint": "06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
      "creationTimestamp": [
        1788255396
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=a599cb04-5965-46a6-a774-24dc6341",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/36f0420f728fe61e44a3ab0043cf9a3d70863cad...84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
        "previous_git_commit": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
        "previous_fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad",
        "previous_trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 3241.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
          "template_reference_name": "saver",
          "git_commit": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
          "git_commit_info": {
            "sha1": "84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
            "message": "Run workflow to pick up fixes to expat vulns (#443)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788252155.0,
            "url": "https://github.com/cyber-dojo/saver/commit/84e986ad70d32e9be362d5bd9ce7c7af94f6eaab"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=a599cb04-5965-46a6-a774-24dc6341",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/36f0420f728fe61e44a3ab0043cf9a3d70863cad...84e986ad70d32e9be362d5bd9ce7c7af94f6eaab",
            "previous_git_commit": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
            "previous_fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/36f0420f728fe61e44a3ab0043cf9a3d70863cad",
            "previous_trail_name": "36f0420f728fe61e44a3ab0043cf9a3d70863cad",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3241.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
          "template_reference_name": "saver",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=954a634e-bcc4-4aeb-b74a-3228e48f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "saver-2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=ad8076c0-8b7e-47ac-b82a-2f2bb220",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:36f0420@sha256:2ec004d6e7c2668ff407b4384d6b4c62f92d9606ae18447c5fb326211921bc6a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 2938402.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f",
          "template_reference_name": "saver",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/06f85cc53010535e46f13c348a1aaf5c8dfee0c0fea7f81105312b6c87d5d05f?artifact_id=91be21a4-68bf-4710-9f74-0c7a5ac5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/490f2bdcf1a2453db2a23395e26d2392",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f22a30e@sha256:41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
                    "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
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
      "fingerprint": "41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
      "creationTimestamp": [
        1788255396
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=aa4300d4-b690-4d71-9596-6af987e1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/258b6d07d2b28ad5cb2ce6d29934997f72380f1a...f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
        "previous_git_commit": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "previous_fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "previous_trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 416885.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
          "template_reference_name": "exercises-start-points",
          "git_commit": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
          "git_commit_info": {
            "sha1": "f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
            "message": "Merge pull request #149 from cyber-dojo/update-base-image-ce45d62\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787838511.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/f22a30ed7659b05a88c22e9f22dc2388f2deb8c8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=aa4300d4-b690-4d71-9596-6af987e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/258b6d07d2b28ad5cb2ce6d29934997f72380f1a...f22a30ed7659b05a88c22e9f22dc2388f2deb8c8",
            "previous_git_commit": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
            "previous_fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
            "previous_trail_name": "258b6d07d2b28ad5cb2ce6d29934997f72380f1a",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 416885.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
          "template_reference_name": "exercises-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=f0d94332-8b7c-4437-adf8-dc070a8e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=edc896a3-98a0-4cb0-8147-49fd6952",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:258b6d0@sha256:c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promote-all-31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2938402.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6",
          "template_reference_name": "exercises-start-points",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/41aab2a45d074e91162ffde031d094118f0be3bdffa4d769ea24b415f5e8a9d6?artifact_id=601099dd-9069-4756-8c33-35cf65e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ca7755573c354bb191fc03f5496f0e7a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:90c8d98@sha256:6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
                    "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
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
      "fingerprint": "6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
      "creationTimestamp": [
        1788255396
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=6df79438-91a2-4c2b-a945-52fb5218",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb...90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
        "previous_git_commit": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
        "previous_fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
        "previous_trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 352135.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
          "template_reference_name": "spooler",
          "git_commit": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
          "git_commit_info": {
            "sha1": "90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
            "message": "Merge pull request #18 from cyber-dojo/give-each-saver-forward-its-own-connection\n\nGive each saver forward its own http connection",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787903261.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=6df79438-91a2-4c2b-a945-52fb5218",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb...90c8d982d2ff8c4950f7aca4d0a1e9d29ac74e1f",
            "previous_git_commit": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
            "previous_fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
            "previous_trail_name": "dc7dea2d9086fcdfe4629f3ab02501ed92aad1bb",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 352135.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
          "template_reference_name": "spooler",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=83b85760-e1f3-476b-9925-19541dee",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/10203d5d23f93844726f204390cf3d5ca8d5c913...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/10203d5d23f93844726f204390cf3d5ca8d5c913",
            "previous_trail_name": "spooler-ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=fdd39323-ac61-4894-ae67-fc003bac",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:dc7dea2@sha256:ff871c3c8f4b5cfb60012bed1cd7f020b20f17fdabc2db0d8a5c77e75518fce0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 2938402.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd",
          "template_reference_name": "spooler",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6440151a9419255a47d8f9fb0e610f5af3f555ad68fa84a50f950abae8b098fd?artifact_id=24059058-ed02-4061-a4d1-b9a66269",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 593409.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/61175d755bb64c5bba7130b854325414",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff9f292@sha256:2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
                    "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
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
      "fingerprint": "2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
      "creationTimestamp": [
        1788255387
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "ff9f292e809801d35246183988b7812826bc2760",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=aa6c0c1d-2d5d-4c98-9f9d-1160dd2f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/2b300f450f72006f6a9000aaf9cd04485f1e8095...ff9f292e809801d35246183988b7812826bc2760",
        "previous_git_commit": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "previous_fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "previous_trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 413493.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "ff9f292e809801d35246183988b7812826bc2760",
          "template_reference_name": "dashboard",
          "git_commit": "ff9f292e809801d35246183988b7812826bc2760",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760",
          "git_commit_info": {
            "sha1": "ff9f292e809801d35246183988b7812826bc2760",
            "message": "Use the simplecov 1.x spellings (#436)\n\n* Use the simplecov 1.x spellings\n\n  The base image now carries simplecov 1.1.1 where it carried 0.21.2.\n  Four spellings are deprecated there, each announcing itself on stderr on\n  every run:\n\n    add_group  -> group\n    add_filter -> skip\n    # :nocov:  -> # simplecov:disable / # simplecov:enable\n\n  and the formatter reopened SimpleCov::Formatter::JSONFormatter to\n  redefine format, which in 1.1.1 makes ruby -w report the redefinition.\n  It is now CoverageMetricsFormatter, named for the coverage_metrics.json\n  it writes. It never needed to be that class: what it produces is\n  per-group totals, not the per-file shape the shipped formatter writes,\n  so it was only borrowing the name to make itself win.\n\n  The three :nocov: pairs are all in source, guarding the post methods\n  that only the fixture scripts in test/scripts reach. The comment in\n  create_v2_dashboard.rb naming those markers is renamed with them, so it\n  still points at something that exists.\n\n  source/client/Dockerfile was pinned to cyberdojo/sinatra-base:759c4e9 on\n  Docker Hub, while everything else moved to ghcr.io. The automated\n  base-image PR only rewrites the Dockerfile at the repo root, so that pin\n  had gone unbumped long enough to be several ruby versions behind. It now\n  names the same image as the root.\n\n  That bump is unverified. The client tests cannot run: the client asks\n  for hostname 'server' (source/client/code/external_dashboard.rb) and\n  docker-compose.yml calls that service 'dashboard', so its healthcheck\n  never resolves. Nothing noticed because no workflow runs them and the\n  Makefile has no client target. Left as found, since dashboard is due to\n  be merged into web.\n\n  The group block parameter goes from the to path while passing.\n\n  Coverage is unchanged: test.lines.total 644, code.lines.total 460,\n  nothing missed in either.\n\n* Keep the simplecov markers inside the line length, and let rubocop cache\n\n  simplecov:disable is seven characters longer than the :nocov: it\n  replaced, which took three comment lines past 80 and failed the lint the\n  previous commit had no reason to run. The prose those markers carried\n  moves to its own line above them, so the marker line is only a marker\n  and its length no longer depends on what is being explained.\n\n  Separately, rubocop_lint.sh runs the container as the invoking uid,\n  which has no entry in the container's /etc/passwd. HOME falls back to /,\n  rubocop cannot create /.cache, and it says so once per file inspected -\n  35 lines of it here, and enough to bury the offences it is reporting.\n  Naming a writable HOME lets it cache and say nothing.\n\n  Neither changes what is inspected: 35 files, no offences, and the tests\n  still report 50 runs with coverage on its limits at 644 and 460.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787841894.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/ff9f292e809801d35246183988b7812826bc2760"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=aa6c0c1d-2d5d-4c98-9f9d-1160dd2f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/2b300f450f72006f6a9000aaf9cd04485f1e8095...ff9f292e809801d35246183988b7812826bc2760",
            "previous_git_commit": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
            "previous_fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/2b300f450f72006f6a9000aaf9cd04485f1e8095",
            "previous_trail_name": "2b300f450f72006f6a9000aaf9cd04485f1e8095",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 413493.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
          "template_reference_name": "dashboard",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=07236a18-f9e6-440c-8163-89b30638",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "dashboard-1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 593400.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=7d30bba6-9d58-403b-b6d8-efe3ebad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2b300f4@sha256:1342e060fb8af6c34d004e474544d1472b940250eb0084f206c3d7bf9d78e2b5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 2938393.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f",
          "template_reference_name": "dashboard",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2827829889b4acc994c3ffbfca250346d5f1f0ddf21847bcbe4864ae484ebe4f?artifact_id=95ee902d-ed5f-49ac-a772-a1ea0d78",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 593400.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f61e1822d26f4aa0a417417c3436c569",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:cbe481c@sha256:36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
                    "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-161",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
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
      "fingerprint": "36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
      "creationTimestamp": [
        1788074885,
        1788074889,
        1788074889
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
      "commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=41957e62-eaad-48d2-af40-46879efb",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/5e4b9873df93525c041c386c06e0ab8fc36b6f33...cbe481c4b842f897e4e9e411cd78461a3a12a334",
        "previous_git_commit": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
        "previous_fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33",
        "previous_trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 169904.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
          "template_reference_name": "web",
          "git_commit": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
          "commit_url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334",
          "git_commit_info": {
            "sha1": "cbe481c4b842f897e4e9e411cd78461a3a12a334",
            "message": "Match the siblings on test-output buffering and frozen-string comments (#424)\n\nThe tee in the server test run makes ruby block-buffer stdout, so the\n  progress dots only appeared once the whole run had finished. saver sets\n  $stdout.sync in its own -e script for exactly this reason; web now does\n  too.\n\n  Every repo already freezes literals globally via RUBYOPT in up.sh, so a\n  per-file magic comment buys nothing. runner, creator and differ exclude\n  source/ from the cop, while web grandfathered each file in the todo\n  instead, which is why the cop fired on the one newly added file.\n  Excluding source/ matches them and leaves the todo holding only the bin/\n  script that RUBYOPT does not reach.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1787904981.0,
            "url": "https://github.com/cyber-dojo/web/commit/cbe481c4b842f897e4e9e411cd78461a3a12a334"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=41957e62-eaad-48d2-af40-46879efb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/5e4b9873df93525c041c386c06e0ab8fc36b6f33...cbe481c4b842f897e4e9e411cd78461a3a12a334",
            "previous_git_commit": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
            "previous_fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/5e4b9873df93525c041c386c06e0ab8fc36b6f33",
            "previous_trail_name": "5e4b9873df93525c041c386c06e0ab8fc36b6f33",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 169904.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-161",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=3e754e79-8e4c-486a-ad94-0b183d32",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2757891.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
          "template_reference_name": "web",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=14a0333a-7e59-454f-bcfa-f4c2e34b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5e4b987@sha256:6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "web-6f394e0dccb59b852fa52ffa114fde8452280054c84de05b0627b1b0f18657bd",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 412898.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc",
          "template_reference_name": "web",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/36ad0020c6cd8716c1463808a185ca65379ec8151a9619d72549ee597d86accc?artifact_id=d7711381-757a-437c-9c77-55bcfd5f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 412898.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d68ae20a684745c6ba576ab68a51dd25",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ca65b67@sha256:a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
                    "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
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
      "fingerprint": "a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
      "creationTimestamp": [
        1788255749,
        1788255749,
        1788255844
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=3b03ceaf-96a6-4afa-8aa2-179e5fe9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/976b63e8001ec7441ebc7737ca69f620d47e7ffe...ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
        "previous_git_commit": "976b63e8001ec7441ebc7737ca69f620d47e7ffe",
        "previous_fingerprint": "01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:976b63e@sha256:01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/976b63e8001ec7441ebc7737ca69f620d47e7ffe",
        "previous_trail_name": "976b63e8001ec7441ebc7737ca69f620d47e7ffe",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 92169.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
          "template_reference_name": "runner",
          "git_commit": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
          "git_commit_info": {
            "sha1": "ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
            "message": "Keep the containers stderr empty (#306)\n\n* Run rm and truncate only when the walk finds files\n\n  xargs runs its command once even when its input is empty, on GNU\n  findutils and busybox alike. Most katas have no binary files and none\n  over the size limit, so remove_binary_files and truncate_large_files\n  each ran their command with no file operand and it answered with a\n  usage error.\n\n  That noise went to the container's own stderr, which is the daemon's\n  second attach stream. The kata's stderr is a separate thing, arriving\n  as tmp/stderr inside the payload, so nothing in the suite looked at\n  the stream that carried it.\n\n  --no-run-if-empty is the long form of the flag, and both userlands\n  accept it, unlike xargs --null.\n\n* Give tar member names it has nothing to strip\n\n  The payload's member names are relative: tmp/stdout, and sandbox/...\n  for the kata's own files. runner.rb and Sandbox.out read them by those\n  names. tar asked to archive an absolute path makes them relative\n  itself, by stripping the leading /, and writes a warning about it to\n  the container's stderr. Both tar calls in send_tgz() did that, two\n  lines each, four on every test-run.\n\n  --directory / hands tar names that are already relative to it, so it\n  has nothing to strip and nothing to say. The member names are\n  unchanged: GNU tar 1.35 in a language image writes the same list\n  either way, tmp/stdout through sandbox/sub/b.txt.\n\n  c9Gf21 now pins the whole of it, that the container's stderr is empty.\n  That stream is the daemon's second attach stream, and separate from\n  the kata's own stderr, which arrives as tmp/stderr inside the payload.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788163580.0,
            "url": "https://github.com/cyber-dojo/runner/commit/ca65b67c3e311fbdd2435609fdb6f8a5479f66f9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=3b03ceaf-96a6-4afa-8aa2-179e5fe9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/976b63e8001ec7441ebc7737ca69f620d47e7ffe...ca65b67c3e311fbdd2435609fdb6f8a5479f66f9",
            "previous_git_commit": "976b63e8001ec7441ebc7737ca69f620d47e7ffe",
            "previous_fingerprint": "01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:976b63e@sha256:01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/976b63e8001ec7441ebc7737ca69f620d47e7ffe",
            "previous_trail_name": "976b63e8001ec7441ebc7737ca69f620d47e7ffe",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 92169.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
          "template_reference_name": "runner",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=e9d1f562-ed75-4e9a-ac28-18bdf67f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ad256a36cfd9d90f78acbf393e4bff5a2ef45fcf...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "ad256a36cfd9d90f78acbf393e4bff5a2ef45fcf",
            "previous_fingerprint": "fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:d7541d3@sha256:fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ad256a36cfd9d90f78acbf393e4bff5a2ef45fcf",
            "previous_trail_name": "runner-fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 593762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=95170cfc-5215-420d-a2b0-83fee5dc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:976b63e@sha256:01311f8b73bb61f65baabe680aa75ef9c0e6c5d1697ad81cfd89c89812de6fe9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-160",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2938755.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638",
          "template_reference_name": "runner",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a1b8379841b440286b5649db7517419457b8fdb01398a661bae9ae0c92b05638?artifact_id=d21568bf-b02a-4532-a725-6fc824a6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ed3c81d7322bb8058615095f4aab28c147c53933...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_fingerprint": "fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:d7541d3@sha256:fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_trail_name": "runner-fd8c68c615a68bfa49569beea07d071950dcfeac676028543f530dd7193f5631",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 593762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a8c4fce1500343aa9d5dd37759266af8",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:bcac1c1@sha256:03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
                    "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
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
      "fingerprint": "03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
      "creationTimestamp": [
        1788255749
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=11345222-f37a-4f8d-8051-ec26a321",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/108cccf9bccf9af5d455db66c250480b53cbecc7...bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
        "previous_git_commit": "108cccf9bccf9af5d455db66c250480b53cbecc7",
        "previous_fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7",
        "previous_trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 5862.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
          "template_reference_name": "differ",
          "git_commit": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
          "git_commit_info": {
            "sha1": "bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
            "message": "Rerun workflow to see if it fixes sonar flake (#469)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1788249887.0,
            "url": "https://github.com/cyber-dojo/differ/commit/bcac1c18385b2573ef6c6e8eeae0f62ed14a03de"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=11345222-f37a-4f8d-8051-ec26a321",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/108cccf9bccf9af5d455db66c250480b53cbecc7...bcac1c18385b2573ef6c6e8eeae0f62ed14a03de",
            "previous_git_commit": "108cccf9bccf9af5d455db66c250480b53cbecc7",
            "previous_fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/108cccf9bccf9af5d455db66c250480b53cbecc7",
            "previous_trail_name": "108cccf9bccf9af5d455db66c250480b53cbecc7",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 5862.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
          "template_reference_name": "differ",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=c19121c7-2115-4fe0-b472-1d4ea833",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "differ-31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 593762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=868b85f5-e442-42ac-9474-0cbb1ab3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:108cccf@sha256:31a4c3abc3ccef33397ed1d84496a08d94ca9d6f9d0df44b6a72aba9743bc8ac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-33",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 2938755.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab",
          "template_reference_name": "differ",
          "git_commit": "ed3c81d7322bb8058615095f4aab28c147c53933",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933",
          "git_commit_info": {
            "sha1": "ed3c81d7322bb8058615095f4aab28c147c53933",
            "message": "Unpack one pinned commit instead of fetching each file\n\n    a0c005a moved these two jobs' files to RUNNER_TEMP, which kept them out of\n    the caller's checkout but left the prefix repeated at every use. The paths\n    are absolute because the run steps stay in the checkout, where the Kosli\n    CLI reads git commit information from the working directory, so the prefix\n    cannot be dropped. It can only be folded into the definitions, and a\n    literal /tmp folds where runner.temp does not: the runner context is\n    unavailable in workflow- and job-level env blocks. Both jobs are pinned to\n    ubuntu-latest, one fresh VM per job, so /tmp neither collides nor persists.\n\n    The files also arrived as five separate fetches of main, one per file, so a\n    push landing mid-run could pair a rego policy with params from a different\n    commit. find-snyk-vulns already checks this repo out, so it now publishes\n    the SHA it resolved, and the two later jobs unpack that exact commit as a\n    single tarball. One run reads one version.\n\n    An env-var's prefix now says where its file came from: SNYK_SCANNING_ from\n    this repo at the pinned commit, CALLER_ from the repo being scanned, TMP_\n    produced by the run. That split is worth naming because only one of these\n    files is the caller's, and it is the one .snyk that the decision attests\n    against. Two bare filenames survive because an artifact name cannot\n    contain a '/'.\n\n    fetch-url-to-file now has exactly one caller, for that .snyk.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1787661987.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/ed3c81d7322bb8058615095f4aab28c147c53933"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/03e520a0dcb9da3889b23ef3ab7f0fa29e4c4a7a9d42c2ce022b78a053157bab?artifact_id=d014796c-e7b5-4b48-92f7-99ec7f8f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...ed3c81d7322bb8058615095f4aab28c147c53933",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 593762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2e9f021f4b484d48a46dc90a3b172b31",
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

