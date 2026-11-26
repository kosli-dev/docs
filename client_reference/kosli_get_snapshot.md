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


## JSON output

With `--output json`, this command prints the response of the [Get snapshot](/api-reference/snapshots/get-snapshot) API operation as the server returned it. The shape follows the server's published API spec, not the CLI version.

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
  "index": 5646,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1795687438.5866702,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5646",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:0191adf@sha256:f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
                    "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
      "fingerprint": "f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
      "creationTimestamp": [
        1795105649
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=11cf8b7e-ae89-4065-ac14-29fca4fa",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/6b3ef8b0e2436e882515c3a7310b84dee24bde2f...0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
        "previous_git_commit": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "previous_fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 5874.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
          "template_reference_name": "differ",
          "git_commit": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
          "git_commit_info": {
            "sha1": "0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
            "message": "Dockerfile - Automated base-image update (#530)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099775.0,
            "url": "https://github.com/cyber-dojo/differ/commit/0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=11cf8b7e-ae89-4065-ac14-29fca4fa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/6b3ef8b0e2436e882515c3a7310b84dee24bde2f...0191adf5ea7d0698482162d4eaa8b41d2c5aa7c6",
            "previous_git_commit": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
            "previous_fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "6b3ef8b0e2436e882515c3a7310b84dee24bde2f",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 5874.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=6f9bc265-5469-47e5-a0e2-32c55b47",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3456377.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=a83d9ca2-a3e5-41df-a3fa-31e0e5f0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6b3ef8b@sha256:165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-165d478330693da4c5cc398cde8fbafd12991cf9b360c48d7afb600d179b59ea",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 120144.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f57e0b5b04ad524bea3a61f54fa718d4694ca0d5535457a745ca944d2142810b?artifact_id=85bb8556-b6f7-4b1f-b527-954df9a3",
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
          "commit_lead_time": 120144.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f605629e86ec4fe59fecb7712082fb32",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bcb5902@sha256:97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
                    "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
      "fingerprint": "97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
      "creationTimestamp": [
        1795105518,
        1795105519,
        1795105524
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
      "commit_url": "https://github.com/cyber-dojo/web/commit/bcb5902178a74126ae2593f6c3189cacb9d049fb",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=66d77503-6993-4ecd-8da5-edab1814",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...bcb5902178a74126ae2593f6c3189cacb9d049fb",
        "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 2659.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
          "template_reference_name": "web",
          "git_commit": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
          "commit_url": "https://github.com/cyber-dojo/web/commit/bcb5902178a74126ae2593f6c3189cacb9d049fb",
          "git_commit_info": {
            "sha1": "bcb5902178a74126ae2593f6c3189cacb9d049fb",
            "message": "Name the metrics decisions without the web. prefix (#481)\n\nkosli attest takes artifact.name in --name to aim\nat an artifact. kosli evaluate policy does not:\nits --name must match ^[a-zA-Z0-9-_,]+$ and the\nartifact is named by --fingerprint. The server\nrejected web.test-decision with HTTP 400. The\nbare names match the web artifact template in\napp-web/.kosli.yml.\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795102859.0,
            "url": "https://github.com/cyber-dojo/web/commit/bcb5902178a74126ae2593f6c3189cacb9d049fb"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=66d77503-6993-4ecd-8da5-edab1814",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...bcb5902178a74126ae2593f6c3189cacb9d049fb",
            "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_fingerprint": "36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:049c9e0@sha256:36f7cb3aeab9b546d1ffc3b567638eb43c57acb3adaf10f8844d7db8a0089642",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2659.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=0999b590-4504-4478-aa2a-198f6089",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2bf3642@sha256:626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-45",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3456246.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=669410bf-065b-4a8c-9803-a7cd1c16",
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
          "commit_lead_time": 120013.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/97119d390de442ea20818f83d061bd7e137a8d4cedcbf98b94b1bc5d4810a59f?artifact_id=e6436033-28ed-41ad-bbec-cf325b2f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 120013.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/bed9f2185ea54c28be59193e0cc5adc3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2bf3642@sha256:626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
      "fingerprint": "626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
      "creationTimestamp": [
        1795105418
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "2bf36429ac734ade22e72033fa3d663080b53b82",
      "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=d5b49703-6e49-4c2b-a26e-09f227c9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
        "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 6330.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
          "template_reference_name": "creator",
          "git_commit": "2bf36429ac734ade22e72033fa3d663080b53b82",
          "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
          "git_commit_info": {
            "sha1": "2bf36429ac734ade22e72033fa3d663080b53b82",
            "message": "Dockerfile - Automated base-image update (#479)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099088.0,
            "url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=d5b49703-6e49-4c2b-a26e-09f227c9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
            "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 6330.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=eac67adc-1861-491c-a5d7-fe8a98fb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3456146.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=c27d377b-f3dc-4053-8192-3a867acb",
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
          "commit_lead_time": 119913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/626373460d5c228796dd299476fcb39bab1d92a8ec72d17b904e0825fe9edd3f?artifact_id=286b5a72-ba1d-4927-ad61-e5132fef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 119913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/6fa0a3799f7e466bbf11a92bd91c2303",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2bf3642@sha256:82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
                    "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
      "fingerprint": "82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
      "creationTimestamp": [
        1795105417
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "2bf36429ac734ade22e72033fa3d663080b53b82",
      "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=a56a9821-03d8-46d8-a58d-c0f189c9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
        "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 6329.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "2bf36429ac734ade22e72033fa3d663080b53b82",
          "template_reference_name": "dashboard",
          "git_commit": "2bf36429ac734ade22e72033fa3d663080b53b82",
          "commit_url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82",
          "git_commit_info": {
            "sha1": "2bf36429ac734ade22e72033fa3d663080b53b82",
            "message": "Dockerfile - Automated base-image update (#479)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099088.0,
            "url": "https://github.com/cyber-dojo/web/commit/2bf36429ac734ade22e72033fa3d663080b53b82"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=a56a9821-03d8-46d8-a58d-c0f189c9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/049c9e06227ba3262b91b585ae6594c1d0f79666...2bf36429ac734ade22e72033fa3d663080b53b82",
            "previous_git_commit": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_fingerprint": "20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:049c9e0@sha256:20e49172ceb0c2e228e1b395a3ca439747f67fb0f309a6da5781a0edba446858",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "049c9e06227ba3262b91b585ae6594c1d0f79666",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 6329.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=7e814149-0b3b-45a0-837f-fead435a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3456145.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=f4e45a31-d240-4faa-aa6e-52cf2939",
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
          "commit_lead_time": 119912.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/82183707e4f953b1cc3db650f5effb79dc755ec024e84feb59dcb4ac9195fe3c?artifact_id=13baeda3-2e11-47ac-95de-96ade952",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:049c9e0@sha256:8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-8e6cf6d68a282eda6fc172398ea45a81cff03414bce74e1eedc530b4556bf55a",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 119912.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/93710993833c42f5ad5d932839cc4d8f",
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
        "type": "updated-provenance",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=bd4e131d-9439-4143-b0b6-ceabe6b5",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7acc042e14f2b5d32bffdf245459315adcc54a913c861b18826f76b4d07fa329?artifact_id=1807c493-253e-4927-aa98-b07516a1",
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
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:cfb37e8@sha256:f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
                    "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
      "fingerprint": "f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
      "creationTimestamp": [
        1795105743
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "cfb37e8c1a1634799f4518186603ce6da97d0958",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/cfb37e8c1a1634799f4518186603ce6da97d0958",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=f6712d86-2289-4ed3-81fc-83c3d50a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/530926abbebc41a1201839ccc5d8a4b1062315eb...cfb37e8c1a1634799f4518186603ce6da97d0958",
        "previous_git_commit": "530926abbebc41a1201839ccc5d8a4b1062315eb",
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
        "previous_fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 6149.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "cfb37e8c1a1634799f4518186603ce6da97d0958",
          "template_reference_name": "exercises-start-points",
          "git_commit": "cfb37e8c1a1634799f4518186603ce6da97d0958",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/cfb37e8c1a1634799f4518186603ce6da97d0958",
          "git_commit_info": {
            "sha1": "cfb37e8c1a1634799f4518186603ce6da97d0958",
            "message": "Merge pull request #162 from cyber-dojo/update-base-image-3b5b5fc\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099594.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/cfb37e8c1a1634799f4518186603ce6da97d0958"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=f6712d86-2289-4ed3-81fc-83c3d50a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/530926abbebc41a1201839ccc5d8a4b1062315eb...cfb37e8c1a1634799f4518186603ce6da97d0958",
            "previous_git_commit": "530926abbebc41a1201839ccc5d8a4b1062315eb",
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/530926abbebc41a1201839ccc5d8a4b1062315eb",
            "previous_fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "530926abbebc41a1201839ccc5d8a4b1062315eb",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 6149.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=6cc75d4c-116a-42cf-a5ec-18688760",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 3456471.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=dc2b83c9-65ac-4a48-97b0-48291979",
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
          "commit_lead_time": 120238.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f704b506936a4f135ab63a61eb01930e6c420eef6f2d6c8074426bace2a52235?artifact_id=9db92460-f0fc-444e-8c19-52735b69",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:530926a@sha256:93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-93747ec121d5e2dfde7c3528cae4a90bea44818c16184ad382c9e7ad8fed1bc9",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 120238.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/274a431464b14ecfa3ae4251eb356fc9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:aad1254@sha256:aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
                    "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
      "fingerprint": "aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
      "creationTimestamp": [
        1795105651
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "aad12541eaefc579b91f77059df895b032eba259",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/aad12541eaefc579b91f77059df895b032eba259",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=e0ba195d-c8fd-47f4-a19d-77568fe4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/4726aeaf7f611b7e4c2c5be6140a6423055d1db9...aad12541eaefc579b91f77059df895b032eba259",
        "previous_git_commit": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
        "previous_fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 6079.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "aad12541eaefc579b91f77059df895b032eba259",
          "template_reference_name": "custom-start-points",
          "git_commit": "aad12541eaefc579b91f77059df895b032eba259",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/aad12541eaefc579b91f77059df895b032eba259",
          "git_commit_info": {
            "sha1": "aad12541eaefc579b91f77059df895b032eba259",
            "message": "Merge pull request #159 from cyber-dojo/update-base-image-3b5b5fc\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099572.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/aad12541eaefc579b91f77059df895b032eba259"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=e0ba195d-c8fd-47f4-a19d-77568fe4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/4726aeaf7f611b7e4c2c5be6140a6423055d1db9...aad12541eaefc579b91f77059df895b032eba259",
            "previous_git_commit": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
            "previous_fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "4726aeaf7f611b7e4c2c5be6140a6423055d1db9",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 6079.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=ec3d679c-7582-4ad3-8268-bb22d2e4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 3456379.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=f73cad80-b084-4114-aec0-eb2bef38",
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
          "commit_lead_time": 120146.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aeaf9f6ae23e6b8cc7534d7efbef0e79cdec5e4b2fb27576dabd24cd746a7e97?artifact_id=dc760a4d-1791-4c04-8ea5-7de0e675",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:4726aea@sha256:78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-78753c1204076896b06cf85e8ae42fab94d4e07bc41cbf7be0b95756d3c6dd68",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 120146.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/72c07d37676840f79e56a6a936533ed5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:a0ffbb8@sha256:4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
                    "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
      "fingerprint": "4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
      "creationTimestamp": [
        1795105409,
        1795105410,
        1795105415
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=462ca1fd-0679-480b-a21d-3d199429",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/799f82f087a0029f9b4c3a9d85db930752190e09...a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
        "previous_git_commit": "799f82f087a0029f9b4c3a9d85db930752190e09",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
        "previous_fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1538.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
          "template_reference_name": "runner",
          "git_commit": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
          "git_commit_info": {
            "sha1": "a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
            "message": "Remove the snyk debug harness (#333)\n\ndebug/ probed a staging flow, snyk-vulns-build,\nwith kosli evaluate trails, which the CLI now\ndeprecates in favour of kosli evaluate policy.\nNothing in CI, the Makefile or the scripts runs\nit, so it is removed rather than migrated.\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795103871.0,
            "url": "https://github.com/cyber-dojo/runner/commit/a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=462ca1fd-0679-480b-a21d-3d199429",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/799f82f087a0029f9b4c3a9d85db930752190e09...a0ffbb8fbf36be8100c9aa11a00cadfe9231c81d",
            "previous_git_commit": "799f82f087a0029f9b4c3a9d85db930752190e09",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/799f82f087a0029f9b4c3a9d85db930752190e09",
            "previous_fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "799f82f087a0029f9b4c3a9d85db930752190e09",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1538.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=002b674c-db0e-4162-96ed-58a1e1cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 3456137.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=46521508-02c9-4af8-859a-ae0f5a91",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:799f82f@sha256:184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-184231596338774ed6f2bb342bc141fe3d3ea93e7d52246884402cced9274a17",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 119904.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4984d39ca8dcf8dd09fb336a32bc0e9e587bf495aca7266b2effa37b69e32e57?artifact_id=7243b071-f732-4192-8625-e3fb6f2f",
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
          "commit_lead_time": 119904.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b517fe2e5e87494085a5d5da29dee333",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a1b031@sha256:0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
                    "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
      "fingerprint": "0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
      "creationTimestamp": [
        1795105188
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "1a1b031d793c474599506ec12faac073df5b6647",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/1a1b031d793c474599506ec12faac073df5b6647",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=048a5579-4e40-45e2-8465-a2e72e55",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/bd40ecfc45d8682a287d9200389b0a45b4d10e73...1a1b031d793c474599506ec12faac073df5b6647",
        "previous_git_commit": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "previous_fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 5642.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "1a1b031d793c474599506ec12faac073df5b6647",
          "template_reference_name": "languages-start-points",
          "git_commit": "1a1b031d793c474599506ec12faac073df5b6647",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/1a1b031d793c474599506ec12faac073df5b6647",
          "git_commit_info": {
            "sha1": "1a1b031d793c474599506ec12faac073df5b6647",
            "message": "Merge pull request #307 from cyber-dojo/update-base-image-3b5b5fc\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099546.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/1a1b031d793c474599506ec12faac073df5b6647"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=048a5579-4e40-45e2-8465-a2e72e55",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/bd40ecfc45d8682a287d9200389b0a45b4d10e73...1a1b031d793c474599506ec12faac073df5b6647",
            "previous_git_commit": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bd40ecfc45d8682a287d9200389b0a45b4d10e73",
            "previous_fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "bd40ecfc45d8682a287d9200389b0a45b4d10e73",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 5642.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=fb02be6c-390a-4418-ba27-54ef85b0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 3455916.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=c0478039-9606-4a62-8d6c-2c228740",
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
          "commit_lead_time": 119683.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/0b8d1d9b46fdd826adc06566da4443bbb41bb1f8912a83e459d21b0d1ff33412?artifact_id=71535b6e-1d0c-4dd0-9ab0-3defbaf6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bd40ecf@sha256:7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-7f5eef62f660c37096ee5dbf47f4da141c4a0777d7297ed060ecc12e401c30e0",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 119683.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/26675c8012f54106a84cbbfe2a420624",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b3940c2@sha256:48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
                    "trail_name": "b3940c267183bbcee441756523576162575f8e01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
      "fingerprint": "48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
      "creationTimestamp": [
        1795105186
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "b3940c267183bbcee441756523576162575f8e01",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/b3940c267183bbcee441756523576162575f8e01",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=43b1823b-0ade-4eba-8849-f1b7a0f4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/787de90aa159f24ec115fd42b3ddfbe44996171f...b3940c267183bbcee441756523576162575f8e01",
        "previous_git_commit": "787de90aa159f24ec115fd42b3ddfbe44996171f",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
        "previous_fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 6078.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "b3940c267183bbcee441756523576162575f8e01",
          "template_reference_name": "saver",
          "git_commit": "b3940c267183bbcee441756523576162575f8e01",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/b3940c267183bbcee441756523576162575f8e01",
          "git_commit_info": {
            "sha1": "b3940c267183bbcee441756523576162575f8e01",
            "message": "Dockerfile - Automated base-image update (#471)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099108.0,
            "url": "https://github.com/cyber-dojo/saver/commit/b3940c267183bbcee441756523576162575f8e01"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=43b1823b-0ade-4eba-8849-f1b7a0f4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/787de90aa159f24ec115fd42b3ddfbe44996171f...b3940c267183bbcee441756523576162575f8e01",
            "previous_git_commit": "787de90aa159f24ec115fd42b3ddfbe44996171f",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/787de90aa159f24ec115fd42b3ddfbe44996171f",
            "previous_fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "787de90aa159f24ec115fd42b3ddfbe44996171f",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 6078.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=11348453-961e-4b78-8c37-bf3e80a4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3455914.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=04cf6583-9629-4d44-8c2a-4dd2a01d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:787de90@sha256:bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-bf2ba4d3c86d36c8b8be1a651a04c4824efa68e2be3df0386ce57f37e537c31f",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 119681.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/48a49b8d15af9f645a487aff64baa2b2b2202dad0a4f057d4ef267aa87f71c5a?artifact_id=b2ed028f-2dcd-4b0e-ae1b-0fe45c8c",
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
          "commit_lead_time": 119681.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5bf956185f2f40f7942c39a7cb88a694",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c15feb2@sha256:1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
                    "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
      "fingerprint": "1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
      "creationTimestamp": [
        1795105183
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/c15feb2710922b82ec50d2cf131da532e09e7dc9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=4dc14438-0e15-40e3-bd64-5754a198",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213...c15feb2710922b82ec50d2cf131da532e09e7dc9",
        "previous_git_commit": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "previous_fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 6119.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
          "template_reference_name": "spooler",
          "git_commit": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/c15feb2710922b82ec50d2cf131da532e09e7dc9",
          "git_commit_info": {
            "sha1": "c15feb2710922b82ec50d2cf131da532e09e7dc9",
            "message": "Merge pull request #31 from cyber-dojo/update-base-image-4d448af\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "timestamp": 1795099064.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/c15feb2710922b82ec50d2cf131da532e09e7dc9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=4dc14438-0e15-40e3-bd64-5754a198",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213...c15feb2710922b82ec50d2cf131da532e09e7dc9",
            "previous_git_commit": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
            "previous_fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "56e2a91cdc7ffcfaef89e77e8031cea2e44dc213",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 6119.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-45",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=fa205b92-c087-45b9-b8eb-0232c84d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-44",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 3455911.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=6d5795b7-1131-4a8f-8c1f-9e7316cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/66785384faab54e612390a18cc8d96fc529ee6f6...66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit": "66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/66785384faab54e612390a18cc8d96fc529ee6f6",
            "previous_fingerprint": "84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:56e2a91@sha256:84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-84e72f5e570c0c2f42a47c492c5cf8d212ba6c5e78a5152258c9e5f5e81563f7",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 119678.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1ec1b2b1fa44d268eeba008cf68d06a7d82eb5938140bf6611c929241703cdd7?artifact_id=f136490a-32ee-4a06-9558-f1329961",
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
          "commit_lead_time": 119678.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/07f283c9d0c14a58a3476f45ef24c960",
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

