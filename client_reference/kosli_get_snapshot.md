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
  "index": 5177,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1785832018.4991596,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5177",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:48bb369@sha256:8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
                    "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-154",
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
      "fingerprint": "8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392",
      "creationTimestamp": [
        1785831942,
        1785831943,
        1785831945
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392?artifact_id=21473a84-3307-44f6-9fbe-fe200ddb",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/19f873464a01f28ecd588504ffe03529119d6297...48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
        "previous_git_commit": "19f873464a01f28ecd588504ffe03529119d6297",
        "previous_fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297",
        "previous_trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1250.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
          "template_reference_name": "runner",
          "git_commit": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
          "git_commit_info": {
            "sha1": "48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
            "message": "Merge pull request #276 from cyber-dojo/ignore-sigstore-go-pkg-verify-vuln-18508018\n\nIgnore non-exploitable sigstore-go expired-key vuln 18508018",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785830692.0,
            "url": "https://github.com/cyber-dojo/runner/commit/48bb36950ae12b98bdcaf39d77225a3ca7b1dda3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392?artifact_id=21473a84-3307-44f6-9fbe-fe200ddb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/19f873464a01f28ecd588504ffe03529119d6297...48bb36950ae12b98bdcaf39d77225a3ca7b1dda3",
            "previous_git_commit": "19f873464a01f28ecd588504ffe03529119d6297",
            "previous_fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/19f873464a01f28ecd588504ffe03529119d6297",
            "previous_trail_name": "19f873464a01f28ecd588504ffe03529119d6297",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1250.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-154",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8cd50be384864573324f1edd08dbd2b7d00448e12c400db8bf84fbcf0da5d392?artifact_id=3289e6b7-69b9-421e-bc5c-b80beb60",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:19f8734@sha256:8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-137",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 514948.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/692753f7d523432eb54d98204385e34a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:da7bace@sha256:8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
                    "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-153",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
      "fingerprint": "8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
      "creationTimestamp": [
        1785755094
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=04894b11-8736-4651-9824-7e882b54",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0e39ff79ccab8804f4bfdff993b5df786bf47426...da7bacefac23b0983d2b9f39d87508e0f85b1167",
        "previous_git_commit": "0e39ff79ccab8804f4bfdff993b5df786bf47426",
        "previous_fingerprint": "778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e39ff7@sha256:778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e39ff79ccab8804f4bfdff993b5df786bf47426",
        "previous_trail_name": "0e39ff79ccab8804f4bfdff993b5df786bf47426",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 86983.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
          "template_reference_name": "dashboard",
          "git_commit": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167",
          "git_commit_info": {
            "sha1": "da7bacefac23b0983d2b9f39d87508e0f85b1167",
            "message": "Build URLs from the mount point instead of writing /dashboard (#427)\n\nSeven places spelled the prefix into URLs the app emits - a redirect target,\n  two asset links and four fetch calls - because the app had no way to know\n  where it was mounted. It does now: rack sets SCRIPT_NAME, so path_to()\n  prepends it for ruby and cd.mountPath carries it to the JavaScript.\n\n  App.mounted is the one place that knows the prefix, and config.ru and the\n  test base both call it. That closes a gap that had the tests driving the app\n  at the root while production served it under /dashboard, so URL assertions\n  had to encode whichever shape the harness happened to produce.\n\n  The four fetch calls also shared a duplicated headers literal, now\n  cd.lib.jsonHeaders.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785668111.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/da7bacefac23b0983d2b9f39d87508e0f85b1167"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=04894b11-8736-4651-9824-7e882b54",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0e39ff79ccab8804f4bfdff993b5df786bf47426...da7bacefac23b0983d2b9f39d87508e0f85b1167",
            "previous_git_commit": "0e39ff79ccab8804f4bfdff993b5df786bf47426",
            "previous_fingerprint": "778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e39ff7@sha256:778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0e39ff79ccab8804f4bfdff993b5df786bf47426",
            "previous_trail_name": "0e39ff79ccab8804f4bfdff993b5df786bf47426",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 86983.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=71cbe6e6-7819-4d3b-a3ba-773139b6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0fb0be4@sha256:c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "dashboard-c7481eac72e01e25aa4f1dda5e8fa1f8c89215d32c32891762e3fc0b99fbfe98",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 438143.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-153",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=d16ab1fc-fcc7-4e29-8ef9-5e01760e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e39ff7@sha256:778f16c37db1079972a0d51fb97d4cd468a2f838a1e75b40bd51ca5f8d44a54c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-149",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 438100.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8a89de34c6d8102bc376b6a238015b1dd768a81f16a741b28dbd8c8af3deefd6?artifact_id=96b440e9-6ecd-401c-a93a-866a0c15",
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
          "commit_lead_time": 438143.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4fdad7d44d2e41ce9c96957d2baeeba9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c221bb1@sha256:d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
                    "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-152",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
      "fingerprint": "d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
      "creationTimestamp": [
        1785744284
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "c221bb1cdea95e14bc2df052e894756a9d96c378",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/c221bb1cdea95e14bc2df052e894756a9d96c378",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355?artifact_id=071c9aea-36bf-4284-9394-80b05793",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/bc3fd56aa1076613dc6631f817fb336424824506...c221bb1cdea95e14bc2df052e894756a9d96c378",
        "previous_git_commit": "bc3fd56aa1076613dc6631f817fb336424824506",
        "previous_fingerprint": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/bc3fd56aa1076613dc6631f817fb336424824506",
        "previous_trail_name": "bc3fd56aa1076613dc6631f817fb336424824506",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 7763.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "c221bb1cdea95e14bc2df052e894756a9d96c378",
          "template_reference_name": "nginx",
          "git_commit": "c221bb1cdea95e14bc2df052e894756a9d96c378",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/c221bb1cdea95e14bc2df052e894756a9d96c378",
          "git_commit_info": {
            "sha1": "c221bb1cdea95e14bc2df052e894756a9d96c378",
            "message": "Merge pull request #163 from cyber-dojo/rate-limits-configurable-by-env\n\nLet a test run turn a rate limit up without leaving this image",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785736521.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/c221bb1cdea95e14bc2df052e894756a9d96c378"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355?artifact_id=071c9aea-36bf-4284-9394-80b05793",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/bc3fd56aa1076613dc6631f817fb336424824506...c221bb1cdea95e14bc2df052e894756a9d96c378",
            "previous_git_commit": "bc3fd56aa1076613dc6631f817fb336424824506",
            "previous_fingerprint": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/bc3fd56aa1076613dc6631f817fb336424824506",
            "previous_trail_name": "bc3fd56aa1076613dc6631f817fb336424824506",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 7763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-152",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355?artifact_id=42308372-38b1-4d1c-afa4-f1c848a3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bc3fd56@sha256:55335a374bd7c02fb204ad62ec94b060e5fef14b83c2ba879ade094db04f8744",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promotion-one-151",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 427290.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/d801a758e959a9e30ddeb9f82df9ff6eb4515eb9e6bb6a7d2b57500d0e665355?artifact_id=be88b797-2a2c-4785-8e48-ea834df7",
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
          "commit_lead_time": 427333.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d6b0e6a626cb48009981aa152c8b4562",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:89019f6@sha256:aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
                    "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-150",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
      "fingerprint": "aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
      "creationTimestamp": [
        1785681913
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=e6a23489-6ea9-44f6-b4de-577edc06",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/07ed087071878b405ac1cf7fe77e5d8c70ce3a4b...89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
        "previous_git_commit": "07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
        "previous_fingerprint": "26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:07ed087@sha256:26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
        "previous_trail_name": "07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 12924.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
          "template_reference_name": "creator",
          "git_commit": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
          "git_commit_info": {
            "sha1": "89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
            "message": "Serve /creator/... in the app, not just after nginx strips it (#48)\n\nnginx rewrites /creator/... down to /... before proxying, so the app has never\n  seen its own prefix. That is why roughly twenty places - a redirect, the asset\n  links in layout.erb, and the JS in eight views - spell /creator into the URLs\n  they emit.\n\n  config.ru now mounts the app at both / and /creator. Nothing changes in\n  production: the rewrite still lands requests on the / mount. Deleting the\n  rewrite, in the real nginx and in nginx_stub, makes the /creator mount serve\n  them; the / mount goes last, so nginx and the app never release together.\n\n  The new test is the only one that loads config.ru - the rest of the suite\n  drives App directly, so nothing else would notice a mount going missing.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785668989.0,
            "url": "https://github.com/cyber-dojo/creator/commit/89019f6d8059406e56fa499b2dec2dbf93f4d5c7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=e6a23489-6ea9-44f6-b4de-577edc06",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/07ed087071878b405ac1cf7fe77e5d8c70ce3a4b...89019f6d8059406e56fa499b2dec2dbf93f4d5c7",
            "previous_git_commit": "07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
            "previous_fingerprint": "26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:07ed087@sha256:26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
            "previous_trail_name": "07ed087071878b405ac1cf7fe77e5d8c70ce3a4b",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 12924.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-150",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=13699012-56b9-4bf4-a484-7cf92f71",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_fingerprint": "26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:07ed087@sha256:26a4c8a14ccf71978ec75fe01edad50d892d7f9054f95fc41d6922fb42995d59",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_trail_name": "promote-all-32",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 364919.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=8613d5d9-8518-43f0-ba81-eae5aa75",
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
          "commit_lead_time": 364962.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aa64db9bd0519d00fba81faf620d0bb1aae3d13839b585ed2ec8179d5e035a34?artifact_id=c0f25582-0724-45c7-af32-9e7d888d",
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
          "commit_lead_time": 364962.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/dec03f30b98f4ecc8d490fa0b85bf421",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:10e162d@sha256:f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
                    "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
      "fingerprint": "f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
      "creationTimestamp": [
        1785559134
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "10e162d4e1294815375a31121f14d57e13183b34",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=7e8c883e-f5ed-4df1-81d0-6b2959ee",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/1b7ea87a174a1a290600b469dc1029ec4c974320...10e162d4e1294815375a31121f14d57e13183b34",
        "previous_git_commit": "1b7ea87a174a1a290600b469dc1029ec4c974320",
        "previous_fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
        "previous_trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 137546.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "10e162d4e1294815375a31121f14d57e13183b34",
          "template_reference_name": "differ",
          "git_commit": "10e162d4e1294815375a31121f14d57e13183b34",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34",
          "git_commit_info": {
            "sha1": "10e162d4e1294815375a31121f14d57e13183b34",
            "message": "Remove dead differ-state-reporter stack and its workflow (#442)\n\nThe nested environment-reporter stack deployed a lambda, differ-state-reporter,\nintended to report differ's Terraform state file to a Kosli environment named\nterraform-state-differ-<env> every minute. It had been broken since ~2025-04:\nevery invocation crashed at init with Runtime.InvalidEntrypoint, so it never\nreported anything, and its target Kosli environments were never created. It was\nsuperseded by the consolidated terraform-statefile-paths-reporter, which covers\nevery service at once.\n\nThe live AWS resources have now been destroyed by hand in both accounts (beta\n244531986313 and prod 274425519734), 16 resources each, so removing the\nconfiguration no longer risks orphaning them. Delete the directory and the\nworkflow together: the workflow triggers on pushes under the stack's path with\ntf_apply set, so removing the directory alone would fire a run against a\nworking_directory that no longer exists.\n\nCo-authored-by: Claude Opus 5 (1M context) <noreply@anthropic.com>",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1785421588.0,
            "url": "https://github.com/cyber-dojo/differ/commit/10e162d4e1294815375a31121f14d57e13183b34"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=7e8c883e-f5ed-4df1-81d0-6b2959ee",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/1b7ea87a174a1a290600b469dc1029ec4c974320...10e162d4e1294815375a31121f14d57e13183b34",
            "previous_git_commit": "1b7ea87a174a1a290600b469dc1029ec4c974320",
            "previous_fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/1b7ea87a174a1a290600b469dc1029ec4c974320",
            "previous_trail_name": "1b7ea87a174a1a290600b469dc1029ec4c974320",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 137546.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-32",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=a6f543ea-34ce-4226-bdf8-e75cd599",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promote-all-31",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 242140.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=8d06fcb7-9ef4-4775-8591-0d64062e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c0666c020044ac5b5181999ec153db1e7f6cd303...c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_git_commit": "c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_fingerprint": "c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:1b7ea87@sha256:c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c0666c020044ac5b5181999ec153db1e7f6cd303",
            "previous_trail_name": "differ-c6c87ec582111b0e0da745ca18867d57fd042c4ce961c8494e4d6a89b4543d12",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 242183.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f68c19b4ca97267fb5be505ec33eb6b89a5297e9ed7ee40d0a3e88fb4082a6e4?artifact_id=cb3e7ff6-5e46-478f-980a-b5ed92c5",
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
          "commit_lead_time": 242183.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/aa5bd18948f84e6fb152029e6f6b8d68",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:595e902@sha256:a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
                    "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-32",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
      "fingerprint": "a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
      "creationTimestamp": [
        1785559130
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=8cfcfa9a-8b26-401b-8c06-945fff4f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e...595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
        "previous_git_commit": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
        "previous_fingerprint": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
        "previous_trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 166899.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
          "template_reference_name": "saver",
          "git_commit": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
          "git_commit_info": {
            "sha1": "595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
            "message": "Delete dead code (#437)\n\n* Delete dead code\n\n* Retire client-test premises the wire can no longer produce\n\n  Every client now sends laptop_id and tab_seq on the kata-write POSTs and\n  sends no index, so a test describing a \"stale-index write\" describes an\n  input that cannot arrive. La7C03 asserted only that two ordinary writes\n  append and that the second laptop_id is stamped. La7C01 already covers the\n  client round-trip and La3F06 covers the two-laptop case more strictly\n  (it asserts both events), so La7C03 goes rather than being reworded.\n\n  La7C02 keeps its coverage but loses its reasoning: a nil laptop_id is not a\n  transitional default waiting for web to catch up, it is a browser with no\n  laptop_id cookie. That path is deliberate, and it is what keeps\n  valid_laptop_id? a live guard rather than dead code.\n\n  The laptop_id focus tests now pass laptop_id explicitly and let the helper\n  supply tab_seq, so the incidental argument stops appearing in tests that\n  are not about it. Deleting La7C03 orphaned the client's another_laptop_id,\n  so that goes too; the server's is still used by kata_torn_read.\n\n  Server-side, LAPTOP_A/B/C duplicated values test_base already exposes as\n  default_laptop_id and another_laptop_id, and uppercase shouts \"important\"\n  for values whose specific bytes do not matter.\n\n  Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1785392231.0,
            "url": "https://github.com/cyber-dojo/saver/commit/595e902fa2f5844d9ce0612a5c9295cd8dab5b97"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=8cfcfa9a-8b26-401b-8c06-945fff4f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e...595e902fa2f5844d9ce0612a5c9295cd8dab5b97",
            "previous_git_commit": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
            "previous_fingerprint": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
            "previous_trail_name": "c29db2ce6d16a9ace09a8548b0cc39fd608abd2e",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 166899.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-32",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=f2818542-8908-44af-aa9d-4d0e6216",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/81c216a55b2cb1787645e699ceaceca868cad253...7494758f8bbc4e66cb5df90ef4cd6b72d75ca584",
            "previous_git_commit": "81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_fingerprint": "680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:c29db2c@sha256:680e9bb851165e8a6e3bc52c1be106286fa910b57c17d844ee052fd3e104e9b4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/81c216a55b2cb1787645e699ceaceca868cad253",
            "previous_trail_name": "promotion-one-141",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 242136.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=ade5596e-b26a-45be-8b91-7e776528",
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
          "commit_lead_time": 242179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a5b224c24732c48daaf6ea495e57345bc4b9fde34b37bf4b7c758b6ee778bee3?artifact_id=e7f2ccee-98d2-4f2e-835d-14a5d894",
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
          "commit_lead_time": 242179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/3c29b1e7fd044e8aad9f803d178a0dee",
        "cluster_name": null,
        "service_name": null
      }
    },
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "spooler-6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac",
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
        "type": "unchanged",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=c911384e-7786-4e3d-99c2-ab107cc4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6442.0,
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6ca8f8d96e1fe8c360fce64b81c330c4ac05d3f128461be4034d36b37147eeac?artifact_id=1099abca-59d5-429d-8b87-f3a6b6e8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=a4dc9877-3cec-4721-b1ef-5b4abcca",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/af5870236f643273d1f26a7f842fd2b616b0f766cc2ac177c6d8f9882b90851e?artifact_id=9e83e1c3-66dd-4567-ace2-a78ccda1",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b",
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
        "type": "unchanged",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=62b559ea-8bf7-4f5c-a33f-784a1708",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b1ee961719fe5dabc18f85450c26719c67a4f9ac3959ba836465ceb14bc67e7b?artifact_id=c6540af7-12d9-4d1a-b047-1207dd1d",
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/42e358b2bd144b99b7f4b93382dddc90",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=140baa5d-f15f-4394-b19f-531979b5",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c7b7fd69d904329f9264e111bd3dc63cf98724cce567bae719e79a171e6925ea?artifact_id=669c0bf2-5f20-4c4e-a0d2-6c5e574f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=f5359561-6cc0-4040-977c-1812f923",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8e965dda26af2d2e68032c25d68e792c85e0c7bd9814862de231bc4c6e935b81?artifact_id=9cd41157-5e0a-49c8-841c-7ada78f4",
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/6bf799c87c194e17be0f99fcd811abb6",
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
        "type": "exited",
        "was": 3,
        "now": 0
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=aa71de9f-9571-41f1-ae0f-680aeeb9",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8c604f9f203a21ad88bd4c9610ef323242874410f0ce796ccdc884d101117b67?artifact_id=73f0bd42-508a-4e5f-a924-9f36ae55",
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

