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
  "index": 5138,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1785386758.6525679,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5138",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:c81791f@sha256:6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-145",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
      "fingerprint": "6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
      "creationTimestamp": [
        1785310509
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "c81791fd10558a59f83876137fb021abcd89f262",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=28274720-dc6e-4b52-b48e-4418ecaa",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/e4d9d0868e299522b207696e19c07966a09bf08a...c81791fd10558a59f83876137fb021abcd89f262",
        "previous_git_commit": "e4d9d0868e299522b207696e19c07966a09bf08a",
        "previous_fingerprint": "2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:e4d9d08@sha256:2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/e4d9d0868e299522b207696e19c07966a09bf08a",
        "previous_trail_name": "e4d9d0868e299522b207696e19c07966a09bf08a",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 791.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "c81791fd10558a59f83876137fb021abcd89f262",
          "template_reference_name": "spooler",
          "git_commit": "c81791fd10558a59f83876137fb021abcd89f262",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262",
          "git_commit_info": {
            "sha1": "c81791fd10558a59f83876137fb021abcd89f262",
            "message": "Merge pull request #13 from cyber-dojo/unsequenced-writes-no-longer-wedge-drainer\n\nKeep a shard draining when a write has no tab_seq",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785309718.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/c81791fd10558a59f83876137fb021abcd89f262"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=28274720-dc6e-4b52-b48e-4418ecaa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/e4d9d0868e299522b207696e19c07966a09bf08a...c81791fd10558a59f83876137fb021abcd89f262",
            "previous_git_commit": "e4d9d0868e299522b207696e19c07966a09bf08a",
            "previous_fingerprint": "2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:e4d9d08@sha256:2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/e4d9d0868e299522b207696e19c07966a09bf08a",
            "previous_trail_name": "e4d9d0868e299522b207696e19c07966a09bf08a",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 791.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-145",
          "template_reference_name": "spooler",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=6154dd8b-8a89-49c6-be10-9c36fd71",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:e4d9d08@sha256:2d13ace2ba9449bcabeaef32f8cdc9255eff976ddf7a4ce5bd70e46bac11b204",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promotion-one-144",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 167455.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
          "template_reference_name": "spooler",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=0f8ba851-1d60-4993-b9a7-89690ad3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6442.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
          "template_reference_name": "spooler",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=a05351bc-0c56-4d25-a9c6-970995d2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6442.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f33363aadf854b71b715ff4961e94b82",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:6a7f7be@sha256:b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
      "fingerprint": "b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
      "creationTimestamp": [
        1785241263
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=796c3a9f-ee70-45ca-8a69-4be16335",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/c6db342472238a7852b6ff31b04f9a6a6099f5cf...6a7f7be81022f7ed3fa8383f016b55af86e2af23",
        "previous_git_commit": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
        "previous_fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
        "previous_trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 929088.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
          "template_reference_name": "languages-start-points",
          "git_commit": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23",
          "git_commit_info": {
            "sha1": "6a7f7be81022f7ed3fa8383f016b55af86e2af23",
            "message": "Merge pull request #243 from cyber-dojo/add-drift-detection\n\nAdd periodic drift-detection workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784312175.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/6a7f7be81022f7ed3fa8383f016b55af86e2af23"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=796c3a9f-ee70-45ca-8a69-4be16335",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/c6db342472238a7852b6ff31b04f9a6a6099f5cf...6a7f7be81022f7ed3fa8383f016b55af86e2af23",
            "previous_git_commit": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
            "previous_fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
            "previous_trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 929088.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "languages-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=a1ab8675-9b0a-485b-be6a-c153fd4e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 98209.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=87b1ac1b-49ca-4fcf-8c56-e2c3fd03",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -75688.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=2ae63760-e6dc-4062-b27b-2cf67090",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -75688.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/42e358b2bd144b99b7f4b93382dddc90",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
                    "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-137",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
      "fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
      "creationTimestamp": [
        1785138608,
        1785138608,
        1785138609
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "19f873464a01f28ecd588504ffe03529119d6297",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=046fc54c-c295-45b3-bac0-81d40282",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b...19f873464a01f28ecd588504ffe03529119d6297",
        "previous_git_commit": "6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
        "previous_fingerprint": "d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6dac3ae@sha256:d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
        "previous_trail_name": "6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 85840.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
          "template_reference_name": "runner",
          "git_commit": "19f873464a01f28ecd588504ffe03529119d6297",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297",
          "git_commit_info": {
            "sha1": "19f873464a01f28ecd588504ffe03529119d6297",
            "message": "Merge pull request #275 from cyber-dojo/extend-snyk-ignore-expiry-to-2026-08-26\n\nExtend .snyk ignore expiry to 2026-08-26",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785052768.0,
            "url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=046fc54c-c295-45b3-bac0-81d40282",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b...19f873464a01f28ecd588504ffe03529119d6297",
            "previous_git_commit": "6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
            "previous_fingerprint": "d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6dac3ae@sha256:d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
            "previous_trail_name": "6dac3ae5d85ee8e6040d8badd5c2eede44bc8a6b",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 85840.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-137",
          "template_reference_name": "runner",
          "git_commit": "76325d840dc66e1c84743725e17de05a16616419",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
          "git_commit_info": {
            "sha1": "76325d840dc66e1c84743725e17de05a16616419",
            "message": "Add emoji prefix to workflow names",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783852701.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=cceaf70c-da3e-4637-a622-d7091e3c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6dac3ae@sha256:d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-136",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1285907.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=58e670d1-a803-43fe-88b6-2c46fffc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6dac3ae@sha256:d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "runner-d7c56f15abf30e1424444c9de9beb4884f72dd400183da58fa9d8d1092309e7b",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -178343.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=5a04d332-d146-4cce-8967-aaa5b043",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -178343.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ffc316ec94724a67a7775accf9b9232a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:2779354@sha256:af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
                    "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-143",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
      "fingerprint": "af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
      "creationTimestamp": [
        1785243407,
        1785243408,
        1785243412
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/2779354a4fda0eeb90fd43f32211836d99f6bde1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=dc864446-cc9f-43e9-bf70-db7dc03b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f...2779354a4fda0eeb90fd43f32211836d99f6bde1",
        "previous_git_commit": "aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
        "previous_fingerprint": "30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aaf06ae@sha256:30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
        "previous_trail_name": "aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 856.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
          "template_reference_name": "web",
          "git_commit": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/2779354a4fda0eeb90fd43f32211836d99f6bde1",
          "git_commit_info": {
            "sha1": "2779354a4fda0eeb90fd43f32211836d99f6bde1",
            "message": "Add spooler env-vars for deployment (#389)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785242551.0,
            "url": "https://github.com/cyber-dojo/web/commit/2779354a4fda0eeb90fd43f32211836d99f6bde1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=dc864446-cc9f-43e9-bf70-db7dc03b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f...2779354a4fda0eeb90fd43f32211836d99f6bde1",
            "previous_git_commit": "aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
            "previous_fingerprint": "30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aaf06ae@sha256:30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
            "previous_trail_name": "aaf06aec0e096d2de9c58152d1ee8d75c8f2a31f",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 856.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-143",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=11f2828c-83b9-4e8c-bd6a-be37eb17",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aaf06ae@sha256:30658abf51aa2b17e4edfa8636cc14aa9725432c2665ed3fcb2ee99ecae03889",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promotion-one-142",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 100353.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=50be4d35-101d-40bf-9b50-e737a284",
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
          "commit_lead_time": -73544.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=dbbe15a4-98b9-4835-9f88-a6aa4da1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -73544.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4984e4ce7a34424585623c1a67da8c6d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
                    "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
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
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
      "fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
      "creationTimestamp": [
        1785241593
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "1b7ea87a174a1a290600b469dc1029ec4c974320",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=53b144c7-33a3-4d8a-b416-37aea745",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/335ddfa139708c37908dd594a0502bc6d88f8615...1b7ea87a174a1a290600b469dc1029ec4c974320",
        "previous_git_commit": "335ddfa139708c37908dd594a0502bc6d88f8615",
        "previous_fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615",
        "previous_trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 929480.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
          "template_reference_name": "differ",
          "git_commit": "1b7ea87a174a1a290600b469dc1029ec4c974320",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
          "git_commit_info": {
            "sha1": "1b7ea87a174a1a290600b469dc1029ec4c974320",
            "message": "Read deployed image for drift-detection plan (#435)\n\nThe Detect Drift workflow runs a terraform plan with no build behind it,\nbut the ECS deployment requires a container image (TF_VAR_TAGGED_IMAGE).\nThe variable has no default and the task definition tracks it directly,\nso a drift plan either fails with \"no value for required variable\" or, if\ngiven a placeholder, reports permanent false drift on the task definition.\n\nBefore planning, each environment reads the image that is currently\ndeployed straight from its ECS task definition and passes it to the\nreusable drift workflow as TF_VAR_TAGGED_IMAGE. The image lookup is done\nexplicitly in this repository rather than in the shared kosli-dev/tf\nworkflow, so Kosli's own drift detection is unaffected.\n\nThe logic lives in a local reusable workflow, detect-drift-env.yml, which\nis parameterized by AWS account and environment. detect-drift.yml holds\nonly the schedule and a beta/prod matrix that calls it, so there is no\nduplication between environments and adding another is a two-line change.",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1784312113.0,
            "url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=53b144c7-33a3-4d8a-b416-37aea745",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/335ddfa139708c37908dd594a0502bc6d88f8615...1b7ea87a174a1a290600b469dc1029ec4c974320",
            "previous_git_commit": "335ddfa139708c37908dd594a0502bc6d88f8615",
            "previous_fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615",
            "previous_trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 929480.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=43c3d8db-588e-495b-b5ba-097d8eae",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-128",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 98539.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=5526b4ca-0a09-47b2-93f4-989c0ba7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -75358.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12?artifact_id=b872b4c5-e209-49b6-ade4-49d9e968",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -75358.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7cbb5625fe464da7851d6c4509ff0e9c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a2e4638@sha256:c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
                    "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
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
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
      "fingerprint": "c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
      "creationTimestamp": [
        1785241259
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/a2e4638aaa102446b8a6d1d519c5bc007e24f087",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=c8c04d1b-0457-497c-a969-4d9c0b72",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47...a2e4638aaa102446b8a6d1d519c5bc007e24f087",
        "previous_git_commit": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
        "previous_fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
        "previous_trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 929056.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
          "template_reference_name": "nginx",
          "git_commit": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/a2e4638aaa102446b8a6d1d519c5bc007e24f087",
          "git_commit_info": {
            "sha1": "a2e4638aaa102446b8a6d1d519c5bc007e24f087",
            "message": "Merge pull request #160 from cyber-dojo/add-drift-detection\n\nAdd periodic drift-detection workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784312203.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/a2e4638aaa102446b8a6d1d519c5bc007e24f087"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=c8c04d1b-0457-497c-a969-4d9c0b72",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47...a2e4638aaa102446b8a6d1d519c5bc007e24f087",
            "previous_git_commit": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
            "previous_fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
            "previous_trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 929056.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=97e8ce65-bdc4-4dbe-895b-bc45fe65",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-127",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 98205.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=437edea4-88c8-42dc-b447-67da1b6c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -75692.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c4b92203ca7a794dc2a1e30b3f4f611e6ce22d60dfdfb7684e2c0e276cf36053?artifact_id=d9d87576-4965-49c4-aa11-f24aff09",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -75692.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/06bf724dfec9470fa778682d4fdfab94",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0fb0be4@sha256:c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
                    "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
      "fingerprint": "c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
      "creationTimestamp": [
        1785241255
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "0fb0be439480821efb926a5079e39ce5941eaa48",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0fb0be439480821efb926a5079e39ce5941eaa48",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=e55cba1f-ce06-49ff-9701-62eb823d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/5407827a19ff32c8d0e7ff2e8f18665e86e64f01...0fb0be439480821efb926a5079e39ce5941eaa48",
        "previous_git_commit": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
        "previous_fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
        "previous_trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 527719.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "0fb0be439480821efb926a5079e39ce5941eaa48",
          "template_reference_name": "dashboard",
          "git_commit": "0fb0be439480821efb926a5079e39ce5941eaa48",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0fb0be439480821efb926a5079e39ce5941eaa48",
          "git_commit_info": {
            "sha1": "0fb0be439480821efb926a5079e39ce5941eaa48",
            "message": "Carry (laptop_id, tab_seq) on all dashboard saver writes (#418)\n\nThe saver is about to drop the nil defaults on laptop_id/tab_seq for its\n  kata-write endpoints, and no longer accepts the old index arg on writes.\n  Every dashboard code path that writes to the saver relied on those\n  defaults, so each would raise ArgumentError once they are removed.\n\n  Update all of them to send the writer's (laptop_id, tab_seq) idempotency\n  key and stop sending index:\n  - bin/create_cluster_kata.rb, bin/create_group_kata.rb: each avatar is one\n    writer, modelled by a small Writer (a fixed laptop_id plus a monotonic\n    tab_seq). The monotonic tab_seq matters here because an avatar makes many\n    writes on one kata, and the saver dedups on (laptop_id, tab_seq, colour) -\n    a reused seq would silently drop same-colour lights.\n  - test/scripts/external_saver.rb + create_v2_dashboard.rb: bring the old\n    client to the current write API (kata_file_switch -> kata_file_edit).\n\n  Rebake test/data/saver_cluster.v2.tgz through the fixed seeder and re-point\n  the hardcoded cluster/child ids in cluster_tabs_test.rb and\n  active_groups_test.rb (eyxahp -> vntRcc) to match.\n\n  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784713536.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/0fb0be439480821efb926a5079e39ce5941eaa48"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=e55cba1f-ce06-49ff-9701-62eb823d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/5407827a19ff32c8d0e7ff2e8f18665e86e64f01...0fb0be439480821efb926a5079e39ce5941eaa48",
            "previous_git_commit": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
            "previous_fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
            "previous_trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 527719.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-31",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=6f9db8f1-d02e-42f1-a564-1da7f708",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-131",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 98201.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=f25ae17c-30d1-4519-a8c3-66910f45",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -75696.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98?artifact_id=ce608804-cd89-4683-ab0a-873b873f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -75696.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c454b3320b2144ec988e1926eb8538b2",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea",
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
          "flow_name": "snyk-aws-prod-per-artifact",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=3039fc99-8837-43cb-a068-28058dd4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -75696.0,
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=ffade573-7149-4aaf-8696-3ab527bc",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81",
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
          "flow_name": "snyk-aws-prod-per-artifact",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=a320a699-8ce4-460a-a70a-636fc16b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -75707.0,
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=89848b7a-0c9c-4672-92ef-744a827e",
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/6bf799c87c194e17be0f99fcd811abb6",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
                    "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-141",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
      "fingerprint": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
      "creationTimestamp": [
        1785236539
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=1fb48da0-c9b7-4627-8597-827ecccf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/f4bb3412725258648a7cf5ce1a776609b4dade72...c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
        "previous_git_commit": "f4bb3412725258648a7cf5ce1a776609b4dade72",
        "previous_fingerprint": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72",
        "previous_trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 7420.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
          "template_reference_name": "saver",
          "git_commit": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
          "git_commit_info": {
            "sha1": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
            "message": "Spike saver idempotent append (#436)\n\n* Reduce saver's event write to an idempotent append\n\n  Now that the spooler is the single ordered writer per kata (ADR B4,\n  spooler docs/adr-async-writes-via-spooler.md), writes for one kata reach\n  saver one at a time in tab_seq order. The concurrent-write machinery in\n  commit_event therefore has nothing left to resolve, so remove it:\n\n  - the update-ref compare-and-swap retry loop (and COMMIT_EVENT_MAX_RETRIES\n    and the attempts parameter),\n  - the self-lag re-append of a test-family loser,\n  - the loser-rescue that dropped a file-event loser as \"Out of order\".\n\n  file_edit_before_test_event only existed to swallow that \"Out of order\"\n  drop, so it is gone; ran_tests/predicted_right/predicted_wrong now call\n  file_edit directly to capture any pending edit before the test event.\n\n  Kept: the A8 dedup guard (a redelivered (laptop_id, tab_seq, colour) is a\n  no-op), and the update-ref itself with its base_oid precondition - now a\n  cheap integrity guard against the blue-green overlap rather than loser\n  detection. option_set's CAS stays too: options are a non-event write that\n  does not go through the spooler and can still be written concurrently.\n\n  Spike: tests not updated.\n\n* Drop the dead position return from saver's event writes\n\n  The spooler is now the only writer and its drainer forwards by checking\n  only the response status - it never reads the body. Web reads positions\n  from the committed stream itself (A4/A5). So the {next_index, major_index,\n  minor_index} the write methods computed and returned is dead: nothing reads\n  it. Stop computing and returning it.\n\n  - The nine event writes return nothing (an ack): file_create/delete/rename\n    drop result['next_index']; file_edit's no-edit path returns bare; the\n    test-family writes call commit_event directly.\n  - git_commit_tag_sss had nothing left to do but call commit_event with the\n    same args, so it is removed; git_commit_tag (which fills empty\n    stdout/stderr/status for file events) calls commit_event directly.\n  - The top-level major_index helper is now unused (only the write return used\n    it) and is removed. The read side is untouched: events()/kata_events still\n    carry index (stored) and major_index/minor_index (polyfilled per read by\n    poly_filler).\n  - commit_event: the A8 dedup path returns bare, all_events is inlined into\n    the commit block, and the method ends with nil.\n\n* Update saver tests for idempotent-append writes\n\n  The write methods now return nothing (an ack) and B4 removed the CAS\n  retry / self-lag / loser-rescue, so tests that asserted on a returned\n  position or exercised that machinery no longer hold. Re-express them\n  against the committed event stream (kata_events), which still carries\n  index / major_index / minor_index (poly_filler, read side).\n\n  - Drop next_index = write(...), result['next_index'] and\n    response[m]['next_index'] assertions; assert on kata_events(id) instead\n    (size == head+1, events[i]['index'], and the light's colour + major/minor).\n    Covers kata_file_* (+ client mirrors), kata_ran_tests, kata_reverted,\n    kata_checked_out, kata_torn_read, kata_write_index_ignored,\n    kata_write_accepts_{tab_seq,laptop_id}, kata_diff, differ,\n    kata_ran_tests_with_edit, kata_predicted_{right,wrong},\n    kata_ran_tests_with_outage.\n  - Delete tests of removed behavior: kata_ran_tests.rb Sp4DkR/S/T/H plus the\n    racing_git / assert_test_survives_raced_internal_file_edit helpers, and\n    client/kata_concurrent_saves_test.rb (concurrent same-kata CAS-loser retry -\n    the spooler is now the single ordered writer). Refresh the stale\n    Sp4DkC / Sp4DkJ comments (the error propagates now; no rescue).\n  - The *_metrics_limits.rb files (server + client) were regenerated by the\n    test runner to match the new test counts and coverage.\n\n* Update api.md: writes no longer return an index, kata_events documents it\n\n  The event-write methods stopped returning a position (they are an idempotent\n  append now), so their docs were stale.\n\n  - kata_events: its `returns` now describes the three positional indexes each\n    event carries - index (absolute position), major_index (count of traffic-\n    lights, created=0, a light sits at major.0), minor_index (0 on a light,\n    incremented per inter-test file event since the last light) - and notes they\n    are computed on read, not returned by the writes.\n  - kata_file_create/delete/rename/edit: drop the \"returns the next event index\"\n    text and the { \"kata_file_*\": N } response examples, and strip the now-\n    pointless `| jq .` from their request examples (a write returns nothing\n    meaningful - a 200 ack; the event is read back via kata_events).\n  - kata_file_edit: its description no longer claims the next index is returned\n    unchanged when nothing was edited.\n\n* Stamp laptop_id/tab_seq in the differ/kata_diff test helpers\n\n  These two convenience helpers (kata_ran_tests(id, files)) called the\n  model directly without laptop_id/tab_seq, riding the model's nil\n  defaults. Those defaults are being removed, after which the bare calls\n  would raise ArgumentError (missing keyword). Pass default_laptop_id and\n  next_tab_seq (the same convention as test/server/helpers/model.rb) so\n  these helpers survive the removal.\n\n  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>\n\n* Add ADR on proposed timestamp changes",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785229119.0,
            "url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=1fb48da0-c9b7-4627-8597-827ecccf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/f4bb3412725258648a7cf5ce1a776609b4dade72...c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
            "previous_git_commit": "f4bb3412725258648a7cf5ce1a776609b4dade72",
            "previous_fingerprint": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72",
            "previous_trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 7420.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-141",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=0db443cc-b53c-4780-b759-7a8a1bf8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-133",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 93485.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=986c8a72-0c76-4272-98d2-136b2c0b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -80412.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4?artifact_id=1e09b5c8-60fa-4227-8ddb-67fab193",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:55561dc@sha256:b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "saver-b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -80412.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/77b4502f86ca4337a17e8ddfe0e8177b",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:76672a8@sha256:aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
                    "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-132",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
      "fingerprint": "aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
      "creationTimestamp": [
        1784357070
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "76672a8b247049c3ce8c3140852e17be8f47d995",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/76672a8b247049c3ce8c3140852e17be8f47d995",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=3cb9c270-d59b-4b28-b16a-b23d89d2",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/7e00b70f8911edf1c480ba9a8b9c2a280260cb08...76672a8b247049c3ce8c3140852e17be8f47d995",
        "previous_git_commit": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "previous_fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "previous_trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 45219.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "76672a8b247049c3ce8c3140852e17be8f47d995",
          "template_reference_name": "creator",
          "git_commit": "76672a8b247049c3ce8c3140852e17be8f47d995",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/76672a8b247049c3ce8c3140852e17be8f47d995",
          "git_commit_info": {
            "sha1": "76672a8b247049c3ce8c3140852e17be8f47d995",
            "message": "Read deployed image for drift-detection plan (#43)\n\nThe Detect Drift workflow runs a terraform plan with no build behind it,\nbut the ECS deployment requires a container image (TF_VAR_TAGGED_IMAGE).\nThe variable has no default and the task definition tracks it directly,\nso a drift plan either fails with \"no value for required variable\" or, if\ngiven a placeholder, reports permanent false drift on the task definition.\n\nBefore planning, each environment reads the image that is currently\ndeployed straight from its ECS task definition and passes it to the\nreusable drift workflow as TF_VAR_TAGGED_IMAGE. The image lookup is done\nexplicitly in this repository rather than in the shared kosli-dev/tf\nworkflow, so Kosli's own drift detection is unaffected.\n\nThe logic lives in a local reusable workflow, detect-drift-env.yml, which\nis parameterized by AWS account and environment. detect-drift.yml holds\nonly the schedule and a beta/prod matrix that calls it, so there is no\nduplication between environments and adding another is a two-line change.",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1784311851.0,
            "url": "https://github.com/cyber-dojo/creator/commit/76672a8b247049c3ce8c3140852e17be8f47d995"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=3cb9c270-d59b-4b28-b16a-b23d89d2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/7e00b70f8911edf1c480ba9a8b9c2a280260cb08...76672a8b247049c3ce8c3140852e17be8f47d995",
            "previous_git_commit": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
            "previous_fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
            "previous_trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 45219.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-132",
          "template_reference_name": "creator",
          "git_commit": "76325d840dc66e1c84743725e17de05a16616419",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
          "git_commit_info": {
            "sha1": "76325d840dc66e1c84743725e17de05a16616419",
            "message": "Add emoji prefix to workflow names",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783852701.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=ebfdade0-510f-44f8-9b9f-2d4c7d0d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 504369.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=e337ab34-8c68-4b0b-90d3-f961c5ff",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -959881.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=ef39d97b-055b-4e03-b208-72d8c545",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -959881.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2730a627a7a3472b810cacada52f3935",
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

