---
title: "kosli get snapshot"
beta: false
deprecated: false
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
  "index": 4781,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1781596438.4966626,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4781",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
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
                    "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
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
      "fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
      "creationTimestamp": [
        1781590488,
        1781590574,
        1781590577
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=73a8e588-a383-4eb5-a88c-a1db6160",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/bc5fbc14361ce7a6281b6110049d90a03f69d786...9cc2a80e1306376b88039715dfdcfc161a0e3904",
        "previous_git_commit": "bc5fbc14361ce7a6281b6110049d90a03f69d786",
        "previous_fingerprint": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bc5fbc14361ce7a6281b6110049d90a03f69d786",
        "previous_trail_name": "bc5fbc14361ce7a6281b6110049d90a03f69d786",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 8211.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
          "template_reference_name": "runner",
          "git_commit": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904",
          "git_commit_info": {
            "sha1": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
            "message": "Merge pull request #244 from cyber-dojo/force-ci-run-129\n\nRun ci workflow to pickup new --annotation in secure-docker-build.yml",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781417039.0,
            "url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=73a8e588-a383-4eb5-a88c-a1db6160",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/bc5fbc14361ce7a6281b6110049d90a03f69d786...9cc2a80e1306376b88039715dfdcfc161a0e3904",
            "previous_git_commit": "bc5fbc14361ce7a6281b6110049d90a03f69d786",
            "previous_fingerprint": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bc5fbc14361ce7a6281b6110049d90a03f69d786",
            "previous_trail_name": "bc5fbc14361ce7a6281b6110049d90a03f69d786",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 8211.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=de0528f8-6f6a-437c-801c-0f6a5302",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc5fbc1@sha256:bdc8eb7fd4717d25b74f5bae58316e66c24283f17a03ce0256ea04fe7eee72b1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-63",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 11736.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
          "template_reference_name": "runner",
          "git_commit": "09e584191c69ab283e35869dcdaa474414b03e45",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/09e584191c69ab283e35869dcdaa474414b03e45",
          "git_commit_info": {
            "sha1": "09e584191c69ab283e35869dcdaa474414b03e45",
            "message": "Detect build flows by the type=build annotation, not a hardcoded list\n\n  The hardcoded BUILD_FLOWS list had to be hand-edited per service, and a\n  new build flow missing from it was silently skipped, leaving its artifact\n  unscanned (the unsafe direction). Detect build flows from the per-artifact\n  type=build annotation instead.\n\n  - artifacts.py: is_build_flow reads the (flow, fingerprint) annotation via an\n    injected fetcher; derive repo_name from the commit_url rather than stripping\n    a -ci suffix.\n  - Fail loud on missing KOSLI_HOST/ORG/API_TOKEN, and run kosli with a\n    PATH-only environment.\n  - Replace the shell artifacts test with pytest using a fake fetcher (no live\n    kosli calls).\n  - Bring the docs into line with the current code.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781535543.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/09e584191c69ab283e35869dcdaa474414b03e45"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=81df1aad-7d4f-4376-ae57-29400c8c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/604111f4822bbc01169317b26fd0f794f5ee7cbf...09e584191c69ab283e35869dcdaa474414b03e45",
            "previous_git_commit": "604111f4822bbc01169317b26fd0f794f5ee7cbf",
            "previous_fingerprint": "9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc8fb51@sha256:9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
            "previous_artifact_compliance_state": "NON-COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/604111f4822bbc01169317b26fd0f794f5ee7cbf",
            "previous_trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -110293.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
          "template_reference_name": "runner",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06?artifact_id=70e23416-e30e-4783-abff-a1dd3ed4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169690.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c5d9f7159999424d8bffd557e2e421da",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
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
                    "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
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
      "fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
      "creationTimestamp": [
        1781590462
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=954d759d-077a-4359-b51f-54c7f182",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/d3e5850912655f2b18a68129f5f3a6480fe305ef...6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
        "previous_git_commit": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "previous_fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "previous_trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 7979.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
          "template_reference_name": "custom-start-points",
          "git_commit": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
          "git_commit_info": {
            "sha1": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
            "message": "Merge pull request #119 from cyber-dojo/annotate-build-attestation\n\nAdd --annotate type=build to kosli-attest-artifact",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781417184.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=954d759d-077a-4359-b51f-54c7f182",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/d3e5850912655f2b18a68129f5f3a6480fe305ef...6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
            "previous_git_commit": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
            "previous_fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
            "previous_trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 7979.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
          "template_reference_name": "custom-start-points",
          "git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
          "git_commit_info": {
            "sha1": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "message": "Add notes on proposed refactoring to detecting a build flow [ci skip]",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781416288.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=b86568eb-1f60-4797-b74f-dd18f8d0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 8875.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=1db97c2c-1e00-400b-a712-bde4fce3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 11649.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
          "template_reference_name": "custom-start-points",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928?artifact_id=50f19ded-0e89-4099-ac88-2cacc4ad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169777.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/79e01ca7846446399eb4a8a0e4a5f508",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:34f14b6@sha256:f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
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
                    "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-69",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
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
      "fingerprint": "f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
      "creationTimestamp": [
        1781592148
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=bafbb0d0-e794-4acf-bdf5-81262268",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/a288de54e3751244517d5e04fc73622e5363257d...34f14b6fc5d87ff95426046716ec8a09141c13a7",
        "previous_git_commit": "a288de54e3751244517d5e04fc73622e5363257d",
        "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/a288de54e3751244517d5e04fc73622e5363257d",
        "previous_trail_name": "a288de54e3751244517d5e04fc73622e5363257d",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 849.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
          "template_reference_name": "creator",
          "git_commit": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7",
          "git_commit_info": {
            "sha1": "34f14b6fc5d87ff95426046716ec8a09141c13a7",
            "message": "Merge pull request #23 from cyber-dojo/remove-infra-upgrade-notice\n\nRemove infrastructure upgrade notice",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781591299.0,
            "url": "https://github.com/cyber-dojo/creator/commit/34f14b6fc5d87ff95426046716ec8a09141c13a7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=bafbb0d0-e794-4acf-bdf5-81262268",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/a288de54e3751244517d5e04fc73622e5363257d...34f14b6fc5d87ff95426046716ec8a09141c13a7",
            "previous_git_commit": "a288de54e3751244517d5e04fc73622e5363257d",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/a288de54e3751244517d5e04fc73622e5363257d",
            "previous_trail_name": "a288de54e3751244517d5e04fc73622e5363257d",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 849.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-69",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=9c9caf33-c2d0-4732-b203-7de62808",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promotion-one-68",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 178634.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
          "template_reference_name": "creator",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=7fbd1cd0-0a21-4eba-afb9-361d314f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -2792.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43",
          "template_reference_name": "creator",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=cad967ea-3ba5-498a-b93c-9c16e7a5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -2792.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fe497fd2bf964fa5b33898a96aff2883",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
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
                    "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
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
      "fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
      "creationTimestamp": [
        1781590487,
        1781590572,
        1781590572
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
      "commit_url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=ed664433-201f-41ac-938b-5931b5f4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/8863c10c2c93d3539672e0bf75bd9925f8778564...f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
        "previous_git_commit": "8863c10c2c93d3539672e0bf75bd9925f8778564",
        "previous_fingerprint": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/8863c10c2c93d3539672e0bf75bd9925f8778564",
        "previous_trail_name": "8863c10c2c93d3539672e0bf75bd9925f8778564",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 3595.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
          "template_reference_name": "web",
          "git_commit": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
          "commit_url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
          "git_commit_info": {
            "sha1": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
            "message": "Unify with fork options on home page (#360)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781421562.0,
            "url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=ed664433-201f-41ac-938b-5931b5f4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/8863c10c2c93d3539672e0bf75bd9925f8778564...f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
            "previous_git_commit": "8863c10c2c93d3539672e0bf75bd9925f8778564",
            "previous_fingerprint": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/8863c10c2c93d3539672e0bf75bd9925f8778564",
            "previous_trail_name": "8863c10c2c93d3539672e0bf75bd9925f8778564",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 3595.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=f3c729dc-26db-4c43-961c-1dd0d4d0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8d5d7b8b19d97204eb0701a813fe53c68c21ccd0...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "8d5d7b8b19d97204eb0701a813fe53c68c21ccd0",
            "previous_fingerprint": "443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8863c10@sha256:443fe71ccfa84a1b7eb1ebe4cf8931c43371843201f540e5f6a8c55154fdb735",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8d5d7b8b19d97204eb0701a813fe53c68c21ccd0",
            "previous_trail_name": "promotion-one-65",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 11643.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
          "template_reference_name": "web",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4?artifact_id=60a2f8f5-0eb8-414a-8f17-e0516412",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169783.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f08f2c3460d64049a886ec5a8d334a95",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
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
                    "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
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
      "fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
      "creationTimestamp": [
        1781590483
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=bf5cf82a-8413-437c-97b0-1977ba2c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/68d791f93dc161fd8dba63e49b7fe9f909cbe758...8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
        "previous_git_commit": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
        "previous_fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758",
        "previous_trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 10730.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
          "template_reference_name": "saver",
          "git_commit": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
          "git_commit_info": {
            "sha1": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
            "message": "Force ci run to pick up changes in secure-docker-build workflow (#404)\n\nThe secure-docker-build now annotates the artifact with type=build\nand the intention is to use this annotation to improve the snyk\nscanning workflows determination of which flow among many in a\nenvironment snapshot is the build flow.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781414517.0,
            "url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=bf5cf82a-8413-437c-97b0-1977ba2c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/68d791f93dc161fd8dba63e49b7fe9f909cbe758...8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
            "previous_git_commit": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
            "previous_fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758",
            "previous_trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 10730.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
          "template_reference_name": "saver",
          "git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
          "git_commit_info": {
            "sha1": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "message": "Add notes on proposed refactoring to detecting a build flow [ci skip]",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781416288.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=d2a65e4e-2cc7-4f40-9a76-cc369677",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 8959.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=e1457e4c-5b88-4bc6-930e-5d84b1c0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 11733.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
          "template_reference_name": "saver",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=4e422cd5-c6ed-4986-b4c4-514ff1ee",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169693.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/8d72a550952c4512b8b9bd5b74565dfd",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
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
                    "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
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
      "fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
      "creationTimestamp": [
        1781590480
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "7e86fede3e42d573de92fed483559b8317ce2dda",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=8f51b5c2-8561-491c-a91e-248d6452",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9513e77858d775950f22173d0afd0634b2ac20b9...7e86fede3e42d573de92fed483559b8317ce2dda",
        "previous_git_commit": "9513e77858d775950f22173d0afd0634b2ac20b9",
        "previous_fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
        "previous_trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 7951.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
          "template_reference_name": "languages-start-points",
          "git_commit": "7e86fede3e42d573de92fed483559b8317ce2dda",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda",
          "git_commit_info": {
            "sha1": "7e86fede3e42d573de92fed483559b8317ce2dda",
            "message": "Merge pull request #217 from cyber-dojo/annotate-build-attestation\n\nAdd --annotate type=build to kosli-attest-artifact",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781417546.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=8f51b5c2-8561-491c-a91e-248d6452",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9513e77858d775950f22173d0afd0634b2ac20b9...7e86fede3e42d573de92fed483559b8317ce2dda",
            "previous_git_commit": "9513e77858d775950f22173d0afd0634b2ac20b9",
            "previous_fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
            "previous_trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 7951.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
          "template_reference_name": "languages-start-points",
          "git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
          "git_commit_info": {
            "sha1": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "message": "Add notes on proposed refactoring to detecting a build flow [ci skip]",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781416288.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=1358dc7a-956e-42d9-94f0-f80d43f4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 9209.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=829046f2-8834-4970-b5e0-eeb47e59",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 11983.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
          "template_reference_name": "languages-start-points",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676?artifact_id=ff36b479-e375-4c03-8a1e-66d35e93",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/60fd5bffe45bc9618e81fabf8dd6793f92d10817...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -169443.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a1f4adbbf9094ef88e2e8f7a05e50a65",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
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
                    "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
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
      "fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
      "creationTimestamp": [
        1781590473
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "706526874659341458da5bb21903a6423c0a5a29",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/706526874659341458da5bb21903a6423c0a5a29",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=0438395b-a9b0-4ee5-9b30-8cd146d9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/cdaac807f3282bd0bba056d906d5536074297a04...706526874659341458da5bb21903a6423c0a5a29",
        "previous_git_commit": "cdaac807f3282bd0bba056d906d5536074297a04",
        "previous_fingerprint": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/cdaac807f3282bd0bba056d906d5536074297a04",
        "previous_trail_name": "cdaac807f3282bd0bba056d906d5536074297a04",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 8575.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "706526874659341458da5bb21903a6423c0a5a29",
          "template_reference_name": "nginx",
          "git_commit": "706526874659341458da5bb21903a6423c0a5a29",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/706526874659341458da5bb21903a6423c0a5a29",
          "git_commit_info": {
            "sha1": "706526874659341458da5bb21903a6423c0a5a29",
            "message": "Merge pull request #132 from cyber-dojo/force-ci-run-34\n\nRun ci workflow to pickup new --annotation in secure-docker-build.yml",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781416577.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/706526874659341458da5bb21903a6423c0a5a29"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=0438395b-a9b0-4ee5-9b30-8cd146d9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/cdaac807f3282bd0bba056d906d5536074297a04...706526874659341458da5bb21903a6423c0a5a29",
            "previous_git_commit": "cdaac807f3282bd0bba056d906d5536074297a04",
            "previous_fingerprint": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/cdaac807f3282bd0bba056d906d5536074297a04",
            "previous_trail_name": "cdaac807f3282bd0bba056d906d5536074297a04",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 8575.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=3c4dd232-3468-4345-a062-0bc37fd1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8d5d7b8b19d97204eb0701a813fe53c68c21ccd0...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "8d5d7b8b19d97204eb0701a813fe53c68c21ccd0",
            "previous_fingerprint": "da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cdaac80@sha256:da15b4868e6a3d31647edb8be04f3ef47878315068bd5f15ea78c8da09eba2b4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8d5d7b8b19d97204eb0701a813fe53c68c21ccd0",
            "previous_trail_name": "promotion-one-64",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 11638.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
          "template_reference_name": "nginx",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=12da50dd-c783-4045-af67-71a8b222",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:ebf104f@sha256:df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -169788.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
          "template_reference_name": "nginx",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=655894cf-1a00-46fb-a6e9-5b538d4f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169788.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f28f3838890949eb9661023a6ac67c44",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
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
                    "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
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
      "fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
      "creationTimestamp": [
        1781590471
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=bd23bb89-f867-46b2-9139-1f7fc8b3",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f3c679170776733c60dc485e076b7cb515caa7a4...87f560f87fb2bc242ee5c58d74d0e209d71cd338",
        "previous_git_commit": "f3c679170776733c60dc485e076b7cb515caa7a4",
        "previous_fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4",
        "previous_trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 8302.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
          "template_reference_name": "dashboard",
          "git_commit": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338",
          "git_commit_info": {
            "sha1": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
            "message": "Run ci workflow to pickup new --annotation in secure-docker-build.yml (#390)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781417198.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=bd23bb89-f867-46b2-9139-1f7fc8b3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f3c679170776733c60dc485e076b7cb515caa7a4...87f560f87fb2bc242ee5c58d74d0e209d71cd338",
            "previous_git_commit": "f3c679170776733c60dc485e076b7cb515caa7a4",
            "previous_fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4",
            "previous_trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 8302.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
          "template_reference_name": "dashboard",
          "git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
          "git_commit_info": {
            "sha1": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "message": "Add notes on proposed refactoring to detecting a build flow [ci skip]",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781416288.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=79a051e4-4e90-4286-a0db-b9ea21b7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 9212.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=009a5042-4d7f-45e4-86e6-fc4fa29c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 11986.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
          "template_reference_name": "dashboard",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c?artifact_id=6a20b693-7b8d-449d-9275-2956bd48",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169440.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/eebdec81e47f486cbe1c50abf06472ce",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
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
                    "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
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
      "fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
      "creationTimestamp": [
        1781590465
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=4d62c06d-f9a2-4bfb-a8aa-a8d36ab8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/76355112651c4ee66d6ee47f67e35459616f0dae...b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
        "previous_git_commit": "76355112651c4ee66d6ee47f67e35459616f0dae",
        "previous_fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
        "previous_trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 7905.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
          "template_reference_name": "exercises-start-points",
          "git_commit": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
          "git_commit_info": {
            "sha1": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
            "message": "Merge pull request #128 from cyber-dojo/annotate-build-attestation\n\nAdd --annotate type=build to kosli-attest-artifact",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781417251.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=4d62c06d-f9a2-4bfb-a8aa-a8d36ab8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/76355112651c4ee66d6ee47f67e35459616f0dae...b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
            "previous_git_commit": "76355112651c4ee66d6ee47f67e35459616f0dae",
            "previous_fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
            "previous_trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 7905.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
          "template_reference_name": "exercises-start-points",
          "git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
          "git_commit_info": {
            "sha1": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "message": "Add notes on proposed refactoring to detecting a build flow [ci skip]",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781416288.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=880ae39c-9b28-48f1-8e1d-58d9722f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4...7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 8868.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=4ea0353c-31ad-4235-a5e9-362c5bd2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 11642.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
          "template_reference_name": "exercises-start-points",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8?artifact_id=3164998a-5527-40ba-8712-4fe7988d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f3cf3ba@sha256:f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -169784.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d3d45fdbeeb14a9bb070d4dd19887138",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "provenance"
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 1,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": false,
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
                    "artifact_status": "COMPLIANT"
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
                  "type": "generic",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
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
                    "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-23",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
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
      "fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
      "creationTimestamp": [
        1781590460
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=03312679-db2a-4f55-a323-7cdb2c89",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/43d2a72431124e9fcf47bf866621ba3fd8e7f618...981dcfc34f584d46afb46b217b47ce68f2f14a08",
        "previous_git_commit": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
        "previous_fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618",
        "previous_trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 5387.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
          "template_reference_name": "differ",
          "git_commit": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08",
          "git_commit_info": {
            "sha1": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
            "message": "Run ci workflow to pickup new --annotation in secure-docker-build.yml (#403)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781420097.0,
            "url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=03312679-db2a-4f55-a323-7cdb2c89",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/43d2a72431124e9fcf47bf866621ba3fd8e7f618...981dcfc34f584d46afb46b217b47ce68f2f14a08",
            "previous_git_commit": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
            "previous_fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618",
            "previous_trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 5387.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-23",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=5105b3dd-9a43-47c6-b724-375ecf8c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-21",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 11970.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
          "template_reference_name": "differ",
          "git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
          "git_commit_info": {
            "sha1": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "message": "Shorten the per-vuln attestation name to a 10-char fingerprint\n\n  The per-vuln attestation was named snyk-<full-fingerprint>. A full\n  SHA-256 fingerprint is 64 hex chars, which renders badly on the\n  snyk-<env>-per-vuln flow page. The fingerprint is only there to keep two\n  builds of the same artifact in one deploy snapshot from clobbering each\n  other on the shared per-vuln trail, and the first 10 hex chars (40 bits)\n  are far more than enough to keep distinct builds apart.\n\n  GitHub Actions expressions have no substring function, so the name can\n  no longer be built inline in the job-level env. Compute it in a shell\n  step that truncates the fingerprint and exports VULN_ATTESTATION_NAME to\n  $GITHUB_ENV, ahead of every step that reads it.\n\n  Note: per-vuln trails that already carry a snyk-<full-fingerprint>\n  attestation will, on their next run, also gain a snyk-<10-char> one,\n  since Kosli keys attestations by name. Only trails created after this\n  change will have the short name alone.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781594940.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b?artifact_id=c3ced9a1-6a7a-4708-a10d-de37693a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -169456.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1163f1ac7b424e038fca08fee39f5c4c",
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
                "text": "flow.name == \"snyk-aws-prod-per-artifact\""
              },
              "name": "snyk-container-scan",
              "type": "generic",
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
      "version": 1,
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
              "type": "generic",
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

