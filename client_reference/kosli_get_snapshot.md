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
  "index": 4833,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1782295018.5650613,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4833",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:05fa6c1@sha256:5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
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
                    "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
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
      "fingerprint": "5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
      "creationTimestamp": [
        1782291397,
        1782291402,
        1782291406
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=6d9685ea-4831-42e9-a40c-e91cafcf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/c248c8e2175307f6906e4a016d09b21d177923bd...05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
        "previous_git_commit": "c248c8e2175307f6906e4a016d09b21d177923bd",
        "previous_fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
        "previous_trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 2592.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
          "template_reference_name": "runner",
          "git_commit": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
          "git_commit_info": {
            "sha1": "05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
            "message": "Merge pull request #251 from cyber-dojo/document-containerd-v2client-vuln-CVE-2026-53488\n\nDocument containerd v2/client vuln CVE-2026-53488 as not exploitable",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782288805.0,
            "url": "https://github.com/cyber-dojo/runner/commit/05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=6d9685ea-4831-42e9-a40c-e91cafcf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/c248c8e2175307f6906e4a016d09b21d177923bd...05fa6c14db21fa6a6f61c0e8ce08e929a28d13cd",
            "previous_git_commit": "c248c8e2175307f6906e4a016d09b21d177923bd",
            "previous_fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
            "previous_trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2592.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=9531a26e-b495-4f00-96f6-3a2747f2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 877883.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
          "template_reference_name": "runner",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=f1f0c7d1-50ba-40fa-999b-c298b15f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 63837.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f",
          "template_reference_name": "runner",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5d093e9ba47c05046427ca26f9eb579f593c98c713695c00ff5206e88e44523f?artifact_id=e6e00418-1fb2-45e3-8663-5455c990",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 63837.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/bc010ab6597c4e85a06a23dcc5ca5e6d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
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
                    "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
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
      "fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
      "creationTimestamp": [
        1782291377
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=5bbbda58-e526-4b64-9f80-6adcda47",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/ff89dd9bd1bfc5441854450adcf25d5aad9508f4...0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
        "previous_git_commit": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "previous_fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "previous_trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 63585.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
          "template_reference_name": "dashboard",
          "git_commit": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
          "git_commit_info": {
            "sha1": "0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
            "message": "Replace attest-generic with attest-decision for snyk (#393)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782227792.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=5bbbda58-e526-4b64-9f80-6adcda47",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/ff89dd9bd1bfc5441854450adcf25d5aad9508f4...0e0b4c1c45ffb25251bbd2b27d892c2e3f810efa",
            "previous_git_commit": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
            "previous_fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
            "previous_trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 63585.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=98e56fce-86a4-400d-894c-e6e26a6e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 877863.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
          "template_reference_name": "dashboard",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=504677d7-c88f-4589-8b3e-41b1fc3c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 63817.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
          "template_reference_name": "dashboard",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f?artifact_id=9f2a3338-95db-442b-8074-757825b4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 63817.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7b24838e05874fa7af957d4fcd7d5dfe",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
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
                    "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
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
      "fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
      "creationTimestamp": [
        1782291366
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "75485ee4a18794755de633775a7b56b2b00cd7c9",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=0289c6f2-2ff3-466b-8b94-12e7c2b0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1...75485ee4a18794755de633775a7b56b2b00cd7c9",
        "previous_git_commit": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
        "previous_fingerprint": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
        "previous_trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 61395.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "75485ee4a18794755de633775a7b56b2b00cd7c9",
          "template_reference_name": "exercises-start-points",
          "git_commit": "75485ee4a18794755de633775a7b56b2b00cd7c9",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9",
          "git_commit_info": {
            "sha1": "75485ee4a18794755de633775a7b56b2b00cd7c9",
            "message": "Merge pull request #133 from cyber-dojo/replace-attest-generic-with-attest-decision\n\nReplace attest-generic with attest-decision for snyk",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782229971.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/75485ee4a18794755de633775a7b56b2b00cd7c9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=0289c6f2-2ff3-466b-8b94-12e7c2b0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1...75485ee4a18794755de633775a7b56b2b00cd7c9",
            "previous_git_commit": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
            "previous_fingerprint": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
            "previous_trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 61395.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=a7db7c48-106b-4f74-91ea-9363192e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 877852.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
          "template_reference_name": "exercises-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=e8793bba-63ed-41b9-b7a3-d9b8fd60",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 63806.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
          "template_reference_name": "exercises-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58?artifact_id=c3b01365-40c6-48f5-80cb-e238da1e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 63806.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/0e2583c0f1dd43cba941fe7ceebcf0bd",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
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
                    "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
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
      "fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
      "creationTimestamp": [
        1782291138
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=e8a01a2b-b310-4700-bd41-33c1c4f0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/34f14b6fc5d87ff95426046716ec8a09141c13a7...9034c75cdb2846757cff32d24e1c5e91f40060a8",
        "previous_git_commit": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
        "previous_fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
        "previous_trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 65705.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
          "template_reference_name": "creator",
          "git_commit": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8",
          "git_commit_info": {
            "sha1": "9034c75cdb2846757cff32d24e1c5e91f40060a8",
            "message": "Merge pull request #25 from cyber-dojo/run-ci-workflow\n\nRun ci workflow to check attest-decision in snyk-scanning action",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782225433.0,
            "url": "https://github.com/cyber-dojo/creator/commit/9034c75cdb2846757cff32d24e1c5e91f40060a8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=e8a01a2b-b310-4700-bd41-33c1c4f0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/34f14b6fc5d87ff95426046716ec8a09141c13a7...9034c75cdb2846757cff32d24e1c5e91f40060a8",
            "previous_git_commit": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
            "previous_fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
            "previous_trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 65705.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=46e767c8-465c-4124-8925-742b71fb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promotion-one-69",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 877624.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
          "template_reference_name": "creator",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=eebfab9d-9ede-4b06-a3ed-58648ada",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 63578.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
          "template_reference_name": "creator",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6?artifact_id=5bc1d3d5-7f4a-45ef-b35a-592b86e6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 63578.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/14846a44ca68486da3530516d8b3842d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:33b1b15@sha256:c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
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
                    "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
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
      "fingerprint": "c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
      "creationTimestamp": [
        1782291127
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "33b1b15247724eee83ab795f3d586b4eac93b456",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/33b1b15247724eee83ab795f3d586b4eac93b456",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=a6329b0b-72c5-43cd-a27a-e2f52c79",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/635027125d65a253a9c98bfd97d22cb3abbefa5a...33b1b15247724eee83ab795f3d586b4eac93b456",
        "previous_git_commit": "635027125d65a253a9c98bfd97d22cb3abbefa5a",
        "previous_fingerprint": "d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:6350271@sha256:d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/635027125d65a253a9c98bfd97d22cb3abbefa5a",
        "previous_trail_name": "635027125d65a253a9c98bfd97d22cb3abbefa5a",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 61533.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "33b1b15247724eee83ab795f3d586b4eac93b456",
          "template_reference_name": "nginx",
          "git_commit": "33b1b15247724eee83ab795f3d586b4eac93b456",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/33b1b15247724eee83ab795f3d586b4eac93b456",
          "git_commit_info": {
            "sha1": "33b1b15247724eee83ab795f3d586b4eac93b456",
            "message": "Merge pull request #134 from cyber-dojo/replace-attest-generic-with-attest-decision\n\nReplace attest-generic with attest-decision for snyk",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782229594.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/33b1b15247724eee83ab795f3d586b4eac93b456"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=a6329b0b-72c5-43cd-a27a-e2f52c79",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/635027125d65a253a9c98bfd97d22cb3abbefa5a...33b1b15247724eee83ab795f3d586b4eac93b456",
            "previous_git_commit": "635027125d65a253a9c98bfd97d22cb3abbefa5a",
            "previous_fingerprint": "d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:6350271@sha256:d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/635027125d65a253a9c98bfd97d22cb3abbefa5a",
            "previous_trail_name": "635027125d65a253a9c98bfd97d22cb3abbefa5a",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 61533.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=99ca1415-f539-4183-a2fe-fb88ed6a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:6350271@sha256:d89025511c4f629e8a99d2764f9abc8666eb3353e877f3844d56481e0137cefb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promotion-one-70",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 877613.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
          "template_reference_name": "nginx",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=57fb8717-1db8-4b14-bf91-6982c478",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 63567.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3",
          "template_reference_name": "nginx",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c0101e646536ba14826d25c3ae7f16e2aef596f6bbc60dd97405fdbd930ddfb3?artifact_id=b0ac2637-bc49-4ead-8cdd-dba828b2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 63567.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/52f3b55614024e678d09d466e8285e04",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
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
                    "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
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
      "fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
      "creationTimestamp": [
        1782291119
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "bb8a712de74f2fe3edf48169ca072d4eff997564",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=531ae2f0-0b5f-44b9-8253-159ba612",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/7eeaac4c57e26887e4d027aa3c815bc2f214f934...bb8a712de74f2fe3edf48169ca072d4eff997564",
        "previous_git_commit": "7eeaac4c57e26887e4d027aa3c815bc2f214f934",
        "previous_fingerprint": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7eeaac4c57e26887e4d027aa3c815bc2f214f934",
        "previous_trail_name": "7eeaac4c57e26887e4d027aa3c815bc2f214f934",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 61026.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "bb8a712de74f2fe3edf48169ca072d4eff997564",
          "template_reference_name": "languages-start-points",
          "git_commit": "bb8a712de74f2fe3edf48169ca072d4eff997564",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564",
          "git_commit_info": {
            "sha1": "bb8a712de74f2fe3edf48169ca072d4eff997564",
            "message": "Merge pull request #227 from cyber-dojo/replace-attest-generic-with-attest-decision\n\nReplace attest-generic with attest-decision for snyk",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782230093.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/bb8a712de74f2fe3edf48169ca072d4eff997564"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=531ae2f0-0b5f-44b9-8253-159ba612",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/7eeaac4c57e26887e4d027aa3c815bc2f214f934...bb8a712de74f2fe3edf48169ca072d4eff997564",
            "previous_git_commit": "7eeaac4c57e26887e4d027aa3c815bc2f214f934",
            "previous_fingerprint": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7eeaac4c57e26887e4d027aa3c815bc2f214f934",
            "previous_trail_name": "7eeaac4c57e26887e4d027aa3c815bc2f214f934",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 61026.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=c391c24e-576b-467a-a2cf-470614f7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promotion-one-73",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 877605.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
          "template_reference_name": "languages-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=847032ad-ebf4-4b4b-9df7-23f03a92",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7eeaac4@sha256:7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-7f24a41aacf7c218e09b85fc3ce76512fe891cebe5aa6c88719e70096d0afc0f",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 63559.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
          "template_reference_name": "languages-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38?artifact_id=32be2251-bb7b-41f2-8045-7630c4cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 63559.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5b89008a421147b3ac8d2b1638a027b8",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
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
                    "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
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
      "fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
      "creationTimestamp": [
        1782291046
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "a35d09232116daff39d0f939cb133edc5750e2a1",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=85ae3f6e-d663-406b-9d5a-fcf95308",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/fbae360261d949b25a66a927921e757d4d064543...a35d09232116daff39d0f939cb133edc5750e2a1",
        "previous_git_commit": "fbae360261d949b25a66a927921e757d4d064543",
        "previous_fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543",
        "previous_trail_name": "fbae360261d949b25a66a927921e757d4d064543",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 61099.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "a35d09232116daff39d0f939cb133edc5750e2a1",
          "template_reference_name": "saver",
          "git_commit": "a35d09232116daff39d0f939cb133edc5750e2a1",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1",
          "git_commit_info": {
            "sha1": "a35d09232116daff39d0f939cb133edc5750e2a1",
            "message": "Replace attest-generic with attest-decision for snyk (#410)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782229947.0,
            "url": "https://github.com/cyber-dojo/saver/commit/a35d09232116daff39d0f939cb133edc5750e2a1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=85ae3f6e-d663-406b-9d5a-fcf95308",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/fbae360261d949b25a66a927921e757d4d064543...a35d09232116daff39d0f939cb133edc5750e2a1",
            "previous_git_commit": "fbae360261d949b25a66a927921e757d4d064543",
            "previous_fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543",
            "previous_trail_name": "fbae360261d949b25a66a927921e757d4d064543",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 61099.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=97544b21-370c-4344-b9a5-fee39d18",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 877532.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
          "template_reference_name": "saver",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=b09eef2d-c142-48f4-b0b1-d12989f8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 63486.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
          "template_reference_name": "saver",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e?artifact_id=423a8e12-5f18-44d1-a23e-97a5924b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 63486.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5b99926988d2488f92d72c4bb61fa0d7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
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
                    "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
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
      "fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
      "creationTimestamp": [
        1782291043
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "3e563eacf76b48caaf2f19f29472544199df8a00",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=68ef150a-fe86-4b14-845b-7bcb814f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1...3e563eacf76b48caaf2f19f29472544199df8a00",
        "previous_git_commit": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "previous_fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "previous_trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 62471.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "3e563eacf76b48caaf2f19f29472544199df8a00",
          "template_reference_name": "differ",
          "git_commit": "3e563eacf76b48caaf2f19f29472544199df8a00",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00",
          "git_commit_info": {
            "sha1": "3e563eacf76b48caaf2f19f29472544199df8a00",
            "message": "Replace attest-generic with attest-decision for snyk (#412)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782228572.0,
            "url": "https://github.com/cyber-dojo/differ/commit/3e563eacf76b48caaf2f19f29472544199df8a00"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=68ef150a-fe86-4b14-845b-7bcb814f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1...3e563eacf76b48caaf2f19f29472544199df8a00",
            "previous_git_commit": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
            "previous_fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
            "previous_trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 62471.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=5451f41c-0226-41f0-aa15-c9fe0967",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 877529.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
          "template_reference_name": "differ",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=70da620d-1f41-4406-98dc-5431b5f8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 63483.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
          "template_reference_name": "differ",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38?artifact_id=21ae6d19-921e-4fb2-aabb-8de8dd52",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 63483.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9088edc0949e4d2aa29466f2008b7e04",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
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
                    "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
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
      "fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
      "creationTimestamp": [
        1782291042
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=b20812a6-ee26-4984-97e9-87c4be75",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/843d6556ec718da1a1f51ce906c8c5bd6366d691...514f79a280dee08bf889a4a4fdf41c9d2f231348",
        "previous_git_commit": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
        "previous_fingerprint": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691",
        "previous_trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 61181.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
          "template_reference_name": "custom-start-points",
          "git_commit": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348",
          "git_commit_info": {
            "sha1": "514f79a280dee08bf889a4a4fdf41c9d2f231348",
            "message": "Merge pull request #124 from cyber-dojo/replace-attest-generic-with-attest-decision\n\nReplace attest-generic with attest-decision for snyk",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782229861.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/514f79a280dee08bf889a4a4fdf41c9d2f231348"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=b20812a6-ee26-4984-97e9-87c4be75",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/843d6556ec718da1a1f51ce906c8c5bd6366d691...514f79a280dee08bf889a4a4fdf41c9d2f231348",
            "previous_git_commit": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
            "previous_fingerprint": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691",
            "previous_trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 61181.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=64f6a22f-070b-4514-b0ce-8d21d90f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 877528.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
          "template_reference_name": "custom-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=881d0041-1375-4033-8161-4081756c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 63482.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
          "template_reference_name": "custom-start-points",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797?artifact_id=2aed2133-b816-44c2-a3e8-c8dd56cc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 63482.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/cce78d00505a412f94e50d1376b58c4d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
        },
        {
          "policy_version": 1,
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
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
                    "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-25",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
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
      "fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
      "creationTimestamp": [
        1782291035,
        1782291036,
        1782291036
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "42ca333501c90d2cf36ce24035aa0a468e287da4",
      "commit_url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=ad37f417-d1a3-4744-a7b9-f2dec951",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1...42ca333501c90d2cf36ce24035aa0a468e287da4",
        "previous_git_commit": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "previous_fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "previous_trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 61115.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "42ca333501c90d2cf36ce24035aa0a468e287da4",
          "template_reference_name": "web",
          "git_commit": "42ca333501c90d2cf36ce24035aa0a468e287da4",
          "commit_url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4",
          "git_commit_info": {
            "sha1": "42ca333501c90d2cf36ce24035aa0a468e287da4",
            "message": "Replace attest-generic with attest-decision for snyk (#365)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782229920.0,
            "url": "https://github.com/cyber-dojo/web/commit/42ca333501c90d2cf36ce24035aa0a468e287da4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=ad37f417-d1a3-4744-a7b9-f2dec951",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1...42ca333501c90d2cf36ce24035aa0a468e287da4",
            "previous_git_commit": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
            "previous_fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
            "previous_trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 61115.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-25",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=a1ef7991-492d-4e61-889e-bf6f9f98",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-24",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 877521.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
          "template_reference_name": "web",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=4f730427-cb10-4153-bf6f-9f9117d8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 63475.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
          "template_reference_name": "web",
          "git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
          "git_commit_info": {
            "sha1": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "message": "Replace attest-generic with attest-decision",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782227560.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685?artifact_id=b9671c71-23bf-45cc-99c1-eebc1680",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 63475.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b3d139f82a754ee286ae50b33859f6e6",
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
      "version": 1,
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
          "attestations": []
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "93d8505f-bce5-4c7c-a2c8-f98236c8",
      "name": "snyk-scan-aws-prod",
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
                "text": "flow.name == \"snyk-aws-prod-per-artifact\""
              },
              "name": "snyk-container-scan",
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

