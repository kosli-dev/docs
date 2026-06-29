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
  "index": 4879,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1782714538.5522528,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4879",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
                    "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
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
      "fingerprint": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
      "creationTimestamp": [
        1782391598
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "6960ff7cc90425329e6def0adae4d5129dca9997",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=3f4df7b6-febd-4caf-8c8d-eef8083e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/3e563eacf76b48caaf2f19f29472544199df8a00...6960ff7cc90425329e6def0adae4d5129dca9997",
        "previous_git_commit": "3e563eacf76b48caaf2f19f29472544199df8a00",
        "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00",
        "previous_trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 3235.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
          "template_reference_name": "differ",
          "git_commit": "6960ff7cc90425329e6def0adae4d5129dca9997",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997",
          "git_commit_info": {
            "sha1": "6960ff7cc90425329e6def0adae4d5129dca9997",
            "message": "Run workflow to pick up provenance attestation update (#415)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782388363.0,
            "url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=3f4df7b6-febd-4caf-8c8d-eef8083e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/3e563eacf76b48caaf2f19f29472544199df8a00...6960ff7cc90425329e6def0adae4d5129dca9997",
            "previous_git_commit": "3e563eacf76b48caaf2f19f29472544199df8a00",
            "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00",
            "previous_trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3235.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "differ",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=6db97e29-0b50-43d7-9a04-30be5611",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 978084.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
          "template_reference_name": "differ",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=19c5980f-2bbf-4587-90ad-6d873a89",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1030.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
          "template_reference_name": "differ",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a?artifact_id=818b5d06-b4ae-4000-beff-8d7df755",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1030.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fb405151010342aab3628e6acf6b5c7b",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:340cd0e@sha256:9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
                    "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
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
      "fingerprint": "9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
      "creationTimestamp": [
        1782391253,
        1782391255,
        1782391257
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "340cd0e960f59711fd21ee7f23d613401c9ee589",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/340cd0e960f59711fd21ee7f23d613401c9ee589",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=0097b3f1-e098-4b77-b5d4-226879d8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/31a8d2291414e8912ea703982ab07b4966740154...340cd0e960f59711fd21ee7f23d613401c9ee589",
        "previous_git_commit": "31a8d2291414e8912ea703982ab07b4966740154",
        "previous_fingerprint": "19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:31a8d22@sha256:19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/31a8d2291414e8912ea703982ab07b4966740154",
        "previous_trail_name": "31a8d2291414e8912ea703982ab07b4966740154",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1504.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "340cd0e960f59711fd21ee7f23d613401c9ee589",
          "template_reference_name": "runner",
          "git_commit": "340cd0e960f59711fd21ee7f23d613401c9ee589",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/340cd0e960f59711fd21ee7f23d613401c9ee589",
          "git_commit_info": {
            "sha1": "340cd0e960f59711fd21ee7f23d613401c9ee589",
            "message": "Merge pull request #257 from cyber-dojo/run-workflow-133\n\nRerun workflow after adding missing attest-decision for provenance in\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782389749.0,
            "url": "https://github.com/cyber-dojo/runner/commit/340cd0e960f59711fd21ee7f23d613401c9ee589"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=0097b3f1-e098-4b77-b5d4-226879d8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/31a8d2291414e8912ea703982ab07b4966740154...340cd0e960f59711fd21ee7f23d613401c9ee589",
            "previous_git_commit": "31a8d2291414e8912ea703982ab07b4966740154",
            "previous_fingerprint": "19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:31a8d22@sha256:19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/31a8d2291414e8912ea703982ab07b4966740154",
            "previous_trail_name": "31a8d2291414e8912ea703982ab07b4966740154",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1504.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "runner",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=51cfccb2-834a-4879-bf45-3d33ad8c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:31a8d22@sha256:19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promotion-one-75",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 977739.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
          "template_reference_name": "runner",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=a618ee24-5add-4824-87b0-7aae888f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 685.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448",
          "template_reference_name": "runner",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9bfb93f2c2ede3fadb635133ce4d268230dfad82278124dd85b5e6c12446a448?artifact_id=999b3766-ac1d-477a-8832-c4c2239f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/977f096d50418bdc9516329a57d32a3ac8a3f536...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "977f096d50418bdc9516329a57d32a3ac8a3f536",
            "previous_fingerprint": "19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:31a8d22@sha256:19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/977f096d50418bdc9516329a57d32a3ac8a3f536",
            "previous_trail_name": "runner-19f8f11835a17a4f45fdca775dfbd7bcb43dcd5d35dd6381492a75b7a53ec6e3",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 685.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/eace4342ec664ea09fcecca3c4882ff9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:5fbd867@sha256:373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
                    "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
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
      "fingerprint": "373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
      "creationTimestamp": [
        1782390814
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=f0403484-7d4c-48b4-be71-9847ddfa",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/a35d09232116daff39d0f939cb133edc5750e2a1...5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
        "previous_git_commit": "a35d09232116daff39d0f939cb133edc5750e2a1",
        "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1",
        "previous_trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 1062.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
          "template_reference_name": "saver",
          "git_commit": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
          "git_commit_info": {
            "sha1": "5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
            "message": "Rerun workflow after adding missing attest-decision for provenance in snyk-scan (#417)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782389752.0,
            "url": "https://github.com/cyber-dojo/saver/commit/5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=f0403484-7d4c-48b4-be71-9847ddfa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/a35d09232116daff39d0f939cb133edc5750e2a1...5fbd867a5a4f07d4c2aa6b93b75ffcbcc896db10",
            "previous_git_commit": "a35d09232116daff39d0f939cb133edc5750e2a1",
            "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1",
            "previous_trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1062.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-77",
          "template_reference_name": "saver",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=3999089e-605b-40d1-83c8-6a376183",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 977300.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
          "template_reference_name": "saver",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=9cbf6533-9091-49db-917a-73c091c4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 246.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786",
          "template_reference_name": "saver",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/373bb9755e71809e02fa3d9092fcab0124996d2121bf399d6063c20db7411786?artifact_id=61aa96a8-f83f-4c99-95d5-5327e09e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 246.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f870cc19e396422e99e70c1692ecff6e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:0635840@sha256:054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
                    "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-89",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
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
      "fingerprint": "054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
      "creationTimestamp": [
        1782629848
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "06358409a6a8b8accb35c5fd07082d359ee4947a",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/06358409a6a8b8accb35c5fd07082d359ee4947a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=fe6f0961-0fb5-43ec-a90f-0b243a39",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/c1815fc4abb602f840a9e1e643692a143094148e...06358409a6a8b8accb35c5fd07082d359ee4947a",
        "previous_git_commit": "c1815fc4abb602f840a9e1e643692a143094148e",
        "previous_fingerprint": "1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c1815fc@sha256:1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/c1815fc4abb602f840a9e1e643692a143094148e",
        "previous_trail_name": "c1815fc4abb602f840a9e1e643692a143094148e",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 752.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "06358409a6a8b8accb35c5fd07082d359ee4947a",
          "template_reference_name": "nginx",
          "git_commit": "06358409a6a8b8accb35c5fd07082d359ee4947a",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/06358409a6a8b8accb35c5fd07082d359ee4947a",
          "git_commit_info": {
            "sha1": "06358409a6a8b8accb35c5fd07082d359ee4947a",
            "message": "Merge pull request #146 from cyber-dojo/force-new-build\n\nForce a build to test the new commit flag",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1782629096.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/06358409a6a8b8accb35c5fd07082d359ee4947a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=fe6f0961-0fb5-43ec-a90f-0b243a39",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/c1815fc4abb602f840a9e1e643692a143094148e...06358409a6a8b8accb35c5fd07082d359ee4947a",
            "previous_git_commit": "c1815fc4abb602f840a9e1e643692a143094148e",
            "previous_fingerprint": "1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c1815fc@sha256:1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/c1815fc4abb602f840a9e1e643692a143094148e",
            "previous_trail_name": "c1815fc4abb602f840a9e1e643692a143094148e",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 752.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-89",
          "template_reference_name": "nginx",
          "git_commit": "7a51019f802dfb95a2834a68af8b7c741cf56c70",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7a51019f802dfb95a2834a68af8b7c741cf56c70",
          "git_commit_info": {
            "sha1": "7a51019f802dfb95a2834a68af8b7c741cf56c70",
            "message": "Merge pull request #8 from cyber-dojo/require-commit-arg\n\nInstruct tf workflows to pass --commit flag",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782629324.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7a51019f802dfb95a2834a68af8b7c741cf56c70"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=1cdc57dd-f4ac-4c7d-964d-789b458a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/67a21da84f846d7184ad561be6e4123a5fa8c1ec...7a51019f802dfb95a2834a68af8b7c741cf56c70",
            "previous_git_commit": "67a21da84f846d7184ad561be6e4123a5fa8c1ec",
            "previous_fingerprint": "1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c1815fc@sha256:1624496345a5c437bd1147b5b28df1c34018558048c5709950539d170027687e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/67a21da84f846d7184ad561be6e4123a5fa8c1ec",
            "previous_trail_name": "promotion-one-88",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 524.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
          "template_reference_name": "nginx",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=e33ff57b-e7b4-4a34-9161-a2583496",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 239280.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004",
          "template_reference_name": "nginx",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/054a618aa2ef0f27376e0fb388545e3160fa18207eee2cd0cf499d8f0b47d004?artifact_id=aa31db06-c39b-4ffa-b9a3-9b100f14",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_fingerprint": "8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:66c0766@sha256:8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_trail_name": "nginx-8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 239280.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4f011c8cb4a4459a90c8c000f84d244d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:bc0f871@sha256:ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
                    "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
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
      "fingerprint": "ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
      "creationTimestamp": [
        1782391613
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=68982b48-8123-417a-a218-dd4b913c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa...bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
        "previous_git_commit": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
        "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
        "previous_trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 2257.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
          "template_reference_name": "dashboard",
          "git_commit": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
          "git_commit_info": {
            "sha1": "bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
            "message": "Add missing attest-decision for provenance (#397)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782389356.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=68982b48-8123-417a-a218-dd4b913c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa...bc0f871e3ec1fef06e7a8f31e3e58c18e92b753a",
            "previous_git_commit": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
            "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
            "previous_trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 2257.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "dashboard",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=f71de064-43f5-40d4-a674-3d672140",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 978099.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
          "template_reference_name": "dashboard",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=649d60de-0b4d-4ebf-a351-8a06f0fb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1045.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5",
          "template_reference_name": "dashboard",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ae9d9af2005dd15ece57acb592592dcd44a96191b7e37795785a9ac2b4ce3ce5?artifact_id=6a4ab8f9-8f0a-4f2c-bb7e-9d016989",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1045.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/330f2ff595264e4fb4197fb17d4978da",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
                    "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
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
      "fingerprint": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
      "creationTimestamp": [
        1782391599
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=675642dc-0cc9-41e0-8dda-e67a6e64",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/75485ee4a18794755de633775a7b56b2b00cd7c9...88239b96c7bb1f0c99af688010f5aed4097ae7b4",
        "previous_git_commit": "75485ee4a18794755de633775a7b56b2b00cd7c9",
        "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9",
        "previous_trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 2066.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
          "template_reference_name": "exercises-start-points",
          "git_commit": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4",
          "git_commit_info": {
            "sha1": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
            "message": "Merge pull request #138 from cyber-dojo/run-workflow-167\n\nRerun workflow after adding missing attest-decision for provenance in\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782389533.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=675642dc-0cc9-41e0-8dda-e67a6e64",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/75485ee4a18794755de633775a7b56b2b00cd7c9...88239b96c7bb1f0c99af688010f5aed4097ae7b4",
            "previous_git_commit": "75485ee4a18794755de633775a7b56b2b00cd7c9",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9",
            "previous_trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2066.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "exercises-start-points",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=92efe301-7260-4057-9c70-7f20f0ef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 978085.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
          "template_reference_name": "exercises-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=cb214519-c200-444f-8afe-1484528b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 1031.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
          "template_reference_name": "exercises-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781?artifact_id=d1100f69-f068-4fdc-b4ba-eccb14ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 1031.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7b64cd7f74284db698eff9c5674caa23",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:23ca301@sha256:8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
                    "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
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
      "fingerprint": "8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
      "creationTimestamp": [
        1782391343
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "23ca301f1baa78b2c2784261991015597319ee94",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/23ca301f1baa78b2c2784261991015597319ee94",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=426b6c00-c2b9-4cf2-864e-6df73e38",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/bb8a712de74f2fe3edf48169ca072d4eff997564...23ca301f1baa78b2c2784261991015597319ee94",
        "previous_git_commit": "bb8a712de74f2fe3edf48169ca072d4eff997564",
        "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564",
        "previous_trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 1211.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "23ca301f1baa78b2c2784261991015597319ee94",
          "template_reference_name": "languages-start-points",
          "git_commit": "23ca301f1baa78b2c2784261991015597319ee94",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/23ca301f1baa78b2c2784261991015597319ee94",
          "git_commit_info": {
            "sha1": "23ca301f1baa78b2c2784261991015597319ee94",
            "message": "Merge pull request #234 from cyber-dojo/run-workflow-199\n\nRerun workflow after adding missing attest-decision for provenance in\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390132.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/23ca301f1baa78b2c2784261991015597319ee94"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=426b6c00-c2b9-4cf2-864e-6df73e38",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/bb8a712de74f2fe3edf48169ca072d4eff997564...23ca301f1baa78b2c2784261991015597319ee94",
            "previous_git_commit": "bb8a712de74f2fe3edf48169ca072d4eff997564",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564",
            "previous_trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 1211.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "languages-start-points",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=2adafa99-4777-45fb-889e-9efbda1a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 977829.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
          "template_reference_name": "languages-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=9a36eb05-d95b-4b73-aad4-e85358ce",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 775.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7",
          "template_reference_name": "languages-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8d14170a5bd0865934614a9c3f073a0f02f08d3ffac304a7df4aa4390874dee7?artifact_id=5731201d-6380-403c-b309-4967447f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 775.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e0a0d5bfa82a4fd68ac872d0ea0c33d4",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:521b7c3@sha256:51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
                    "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
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
      "fingerprint": "51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
      "creationTimestamp": [
        1782391337
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/521b7c30720e903fa909ae36b7ea9b2f962aa63f",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=1a3dbd1b-5cc1-4d75-9fff-2317ce97",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/514f79a280dee08bf889a4a4fdf41c9d2f231348...521b7c30720e903fa909ae36b7ea9b2f962aa63f",
        "previous_git_commit": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
        "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348",
        "previous_trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 848.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
          "template_reference_name": "custom-start-points",
          "git_commit": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/521b7c30720e903fa909ae36b7ea9b2f962aa63f",
          "git_commit_info": {
            "sha1": "521b7c30720e903fa909ae36b7ea9b2f962aa63f",
            "message": "Merge pull request #129 from cyber-dojo/run-workflow-167\n\nRerun workflow after adding missing attest-decision for provenance in\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390489.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/521b7c30720e903fa909ae36b7ea9b2f962aa63f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=1a3dbd1b-5cc1-4d75-9fff-2317ce97",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/514f79a280dee08bf889a4a4fdf41c9d2f231348...521b7c30720e903fa909ae36b7ea9b2f962aa63f",
            "previous_git_commit": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348",
            "previous_trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 848.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "custom-start-points",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=8477baad-5509-496c-9fdf-d6d2e7e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 977823.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
          "template_reference_name": "custom-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=539fea9c-3b77-452a-b13c-de097656",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 769.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e",
          "template_reference_name": "custom-start-points",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/51ea0bf66b6dbc31be2e9e9a6554c65aec44f1fc1dc23d00e4e0898e5519400e?artifact_id=ee1b9abb-84e9-4831-a735-3c4d1ef3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 769.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d85d7aa8931d4eaeadab414dce020e39",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:077d6f5@sha256:e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
                    "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
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
      "fingerprint": "e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
      "creationTimestamp": [
        1782391258,
        1782391258,
        1782391337
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
      "commit_url": "https://github.com/cyber-dojo/web/commit/077d6f50114958e0d62d0f56f8258a4d02a93e02",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=8e4d1ac0-3457-4938-bfab-98373251",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/42ca333501c90d2cf36ce24035aa0a468e287da4...077d6f50114958e0d62d0f56f8258a4d02a93e02",
        "previous_git_commit": "42ca333501c90d2cf36ce24035aa0a468e287da4",
        "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4",
        "previous_trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 1950.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
          "template_reference_name": "web",
          "git_commit": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
          "commit_url": "https://github.com/cyber-dojo/web/commit/077d6f50114958e0d62d0f56f8258a4d02a93e02",
          "git_commit_info": {
            "sha1": "077d6f50114958e0d62d0f56f8258a4d02a93e02",
            "message": "Add missing attest-decision for provenance (#369)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782389308.0,
            "url": "https://github.com/cyber-dojo/web/commit/077d6f50114958e0d62d0f56f8258a4d02a93e02"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=8e4d1ac0-3457-4938-bfab-98373251",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/42ca333501c90d2cf36ce24035aa0a468e287da4...077d6f50114958e0d62d0f56f8258a4d02a93e02",
            "previous_git_commit": "42ca333501c90d2cf36ce24035aa0a468e287da4",
            "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4",
            "previous_trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1950.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "web",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=8bdb7fb0-4046-4ec2-99bf-8b48af32",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 977744.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
          "template_reference_name": "web",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=3a3cedad-5969-445f-81fe-cc95ae2a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 690.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb",
          "template_reference_name": "web",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e08d7cbc02d13317e1325be541cc5aa0b2374fa5a0e82786c75576f9d80c02cb?artifact_id=b29fe431-e111-4c50-a08d-fff81c50",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 690.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/df9654ceaee549a090fd083a9f3f2d86",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 2,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": null,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
                    "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-27",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
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
      "fingerprint": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
      "creationTimestamp": [
        1782391265
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=58bda834-0bae-4c5a-9cd0-7f326e24",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/9034c75cdb2846757cff32d24e1c5e91f40060a8...0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
        "previous_git_commit": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
        "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8",
        "previous_trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 1735.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
          "template_reference_name": "creator",
          "git_commit": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
          "git_commit_info": {
            "sha1": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
            "message": "Merge pull request #29 from cyber-dojo/run-workflow-5\n\nRerun workflow after adding missing attest-decision for provenance in\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782389530.0,
            "url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=58bda834-0bae-4c5a-9cd0-7f326e24",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/9034c75cdb2846757cff32d24e1c5e91f40060a8...0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
            "previous_git_commit": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
            "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8",
            "previous_trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1735.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-27",
          "template_reference_name": "creator",
          "git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
          "git_commit_info": {
            "sha1": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "message": "Update comment and help text",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781413514.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=f80a0b02-95de-408f-82da-d4f7c53e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-25",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 977751.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
          "template_reference_name": "creator",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=c4d98eae-975d-4ffd-bb0b-748e2130",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 697.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
          "template_reference_name": "creator",
          "git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
          "git_commit_info": {
            "sha1": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "message": "Add missing line-continuation chars",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782390568.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b?artifact_id=7dd62115-76b8-4d93-b899-7ca057c5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 697.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ef9c4ff449b04d0e870ee3fc8bfe49ea",
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
      "version": 2,
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
              "if_condition": null,
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

