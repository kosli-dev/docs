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
  "index": 4434,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1778647258.809749,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4434",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-15",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
      "creationTimestamp": [
        1778592064,
        1778592065,
        1778592065
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "59d0a20b8494a667e2eefff618395523a1bae4c6",
      "commit_url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705?artifact_id=6d01039a-91d3-480a-acee-a0ac8cc7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/c175db1be81803bc9587ccb3175723d450468ab0...59d0a20b8494a667e2eefff618395523a1bae4c6",
        "previous_git_commit": "c175db1be81803bc9587ccb3175723d450468ab0",
        "previous_fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0",
        "previous_trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 81204.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
          "template_reference_name": "web",
          "git_commit": "59d0a20b8494a667e2eefff618395523a1bae4c6",
          "commit_url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6",
          "git_commit_info": {
            "sha1": "59d0a20b8494a667e2eefff618395523a1bae4c6",
            "message": "Make email addresses in feedback and sponsorship dialogs clickable (#330)\n\nConvert plain-text email addresses to mailto: links so users can click\nto open their email client directly from the dialogs.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778510860.0,
            "url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705?artifact_id=6d01039a-91d3-480a-acee-a0ac8cc7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/c175db1be81803bc9587ccb3175723d450468ab0...59d0a20b8494a667e2eefff618395523a1bae4c6",
            "previous_git_commit": "c175db1be81803bc9587ccb3175723d450468ab0",
            "previous_fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0",
            "previous_trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 81204.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
          "template_reference_name": "web",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705?artifact_id=696b76a8-d703-4589-a97a-371c5fbe",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/b073fd2bc7c8c8cb94b0b1d06509ef38eb9900b6...badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_git_commit": "b073fd2bc7c8c8cb94b0b1d06509ef38eb9900b6",
            "previous_fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/b073fd2bc7c8c8cb94b0b1d06509ef38eb9900b6",
            "previous_trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 18832.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-15",
          "template_reference_name": "web",
          "git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "git_commit_info": {
            "sha1": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "message": "Upgrade kosli-dev/setup-cli-action to move past node deprecation warnings",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245591.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705?artifact_id=ac09fcdf-e333-4040-a7e6-ad06e6aa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-14",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 346473.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
          "template_reference_name": "web",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705?artifact_id=b2ec6bd4-6480-404b-81e2-54684c57",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -20252.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f88ea409440942afae2e419c244f68fb",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
      "creationTimestamp": [
        1778502825
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=a745299f-f8f0-4b68-89b3-173aafe8",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/a6ece2b597888f7ab149759daadda08e3afab0c1...89b113a1531ed1a88cd466d67a8e107ee88672d4",
        "previous_git_commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
        "previous_fingerprint": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1",
        "previous_trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 174793.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
          "template_reference_name": "dashboard",
          "git_commit": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4",
          "git_commit_info": {
            "sha1": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
            "message": "Revert differ proxy routes (#366)\n\n* Revert differ/saver proxy routes; call nginx differ/ directly\n\nThe proxy routes (/diff_summary, /group_manifest) added to the dashboard\ncontroller are no longer needed now that GET routes for differ/ have been\nrestored to nginx. Remove ExternalDiffer and its wiring, and update the\nfetch() calls to hit /differ/diff_summary and /saver/group_manifest\ndirectly, extracting json.diff_summary and json.group_manifest from the\nwrapped nginx responses.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Update test metrics\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778328032.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=a745299f-f8f0-4b68-89b3-173aafe8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/a6ece2b597888f7ab149759daadda08e3afab0c1...89b113a1531ed1a88cd466d67a8e107ee88672d4",
            "previous_git_commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
            "previous_fingerprint": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1",
            "previous_trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 174793.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-14",
          "template_reference_name": "dashboard",
          "git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "git_commit_info": {
            "sha1": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "message": "Upgrade kosli-dev/setup-cli-action to move past node deprecation warnings",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245591.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=d310fe4e-9ad2-4d7e-a4ca-ece936aa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-11",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 257234.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
          "template_reference_name": "dashboard",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=5fcdff8f-004f-4e55-b17d-e9602a40",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -70407.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
          "template_reference_name": "dashboard",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=ee172b69-812b-40d5-ac62-0fc9b9e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109491.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/534b56a827ba4aa4967841abfa41f667",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
      "creationTimestamp": [
        1778502501
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "af7241f29969110655505267dc8ce7f9644fbf6a",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=dfd55d86-8f32-4b13-94a9-99033f50",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/cfb0d52610ab73011f325c4bb5bf0b54fb51031c...af7241f29969110655505267dc8ce7f9644fbf6a",
        "previous_git_commit": "cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
        "previous_fingerprint": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
        "previous_trail_name": "cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 74212.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
          "template_reference_name": "saver",
          "git_commit": "af7241f29969110655505267dc8ce7f9644fbf6a",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a",
          "git_commit_info": {
            "sha1": "af7241f29969110655505267dc8ce7f9644fbf6a",
            "message": "Manifest reads persisted options (#368)\n\n* manifest(id) now returns actual persisted option values\n\npolyfill_manifest_defaults used ||= to apply defaults, so options that\nhad been changed via option_set were never reflected in the manifest\nresponse -- the stored option files were never read. Fix reads each\noption via option_get after polyfilling, so callers always see the\nreal persisted value.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Update coverage and test-count metric limits\n\nTwo new lines of production code (manifest reads options) and one new\ntest push the limits up by the exact amounts needed.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778428289.0,
            "url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=dfd55d86-8f32-4b13-94a9-99033f50",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/cfb0d52610ab73011f325c4bb5bf0b54fb51031c...af7241f29969110655505267dc8ce7f9644fbf6a",
            "previous_git_commit": "cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
            "previous_fingerprint": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
            "previous_trail_name": "cfb0d52610ab73011f325c4bb5bf0b54fb51031c",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 74212.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-14",
          "template_reference_name": "saver",
          "git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "git_commit_info": {
            "sha1": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "message": "Upgrade kosli-dev/setup-cli-action to move past node deprecation warnings",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245591.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=7458425e-2a2e-427b-b3f0-69963dcb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:cfb0d52@sha256:a91ad5b7e510c364402342b6eea631e1f1b1b2166f1dac2c3dd28d007f95c3ed",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promotion-one-46",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 256910.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
          "template_reference_name": "saver",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=f281c60b-199e-4fbd-9ebd-aaf1f88f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -70731.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
          "template_reference_name": "saver",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=76a26ce4-f35c-4ae4-845e-d6a50617",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109815.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/39f21a43bc564548b396bd0db3000938",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
      "creationTimestamp": [
        1778502489
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
      "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=36be2954-6f6d-4a7b-b705-fc3e7466",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c...b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "previous_git_commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
        "previous_fingerprint": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
        "previous_trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 619994.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
          "template_reference_name": "creator",
          "git_commit": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
          "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
          "git_commit_info": {
            "sha1": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
            "message": "Merge branch 'remove-ga-tracking' into 'main'\n\nGoogle shut down Universal Analytics in July 2023\n\nSee merge request cyber-dojo/creator!244",
            "author": "Jon Jagger <jon@jaggersoft.com>",
            "branch": "main",
            "timestamp": 1777882495.0,
            "url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=36be2954-6f6d-4a7b-b705-fc3e7466",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c...b3152a10de1f36b7dbe2818c0918af06fd3aca61",
            "previous_git_commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
            "previous_fingerprint": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
            "previous_trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 619994.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
          "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
          "template_reference_name": "creator",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=b9129448-20c9-4dce-bf9d-eb7b5aa2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930",
          "deployment_diff": null,
          "commit_lead_time": 887554.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
          "template_reference_name": "creator",
          "git_commit": "e50b0406a64efc36fb236afd464e75b31877f623",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623",
          "git_commit_info": {
            "sha1": "e50b0406a64efc36fb236afd464e75b31877f623",
            "message": "Split snyk Kosli flows to separate per-vuln and per-artifact trails\n\nsnyk-vulns-{env} mixed two trail naming patterns: {repo}-{severity}-{CVE}\nfor individual vulnerabilities, and {repo}-{fingerprint} for aggregate\nartifact scan results. snyk-{env}-per-vuln and snyk-{env}-per-artifact\nmake each flow's purpose explicit and the Kosli UI easier to navigate.\n\nAlso removes temporary debug logging from the fingerprint step.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778153406.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=87bc38a8-23db-438a-8c76-2998432c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": 349083.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-14",
          "template_reference_name": "creator",
          "git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "git_commit_info": {
            "sha1": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "message": "Upgrade kosli-dev/setup-cli-action to move past node deprecation warnings",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245591.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=2b48efcd-4725-4afc-a131-61ba781b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-9",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 256898.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
          "template_reference_name": "creator",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=74140e68-b3e7-4a3b-9285-51be26b1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109827.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
          "template_reference_name": "creator",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=2f81e52d-48ac-40a7-be52-e99e0909",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109827.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9f700f8dcf58425cb6ce574fac656b8a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-48",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
      "creationTimestamp": [
        1778245547,
        1778245548,
        1778245549
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=6d4a3808-b45b-4283-9bd8-73bc1197",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/8768460dc1c91de5f6485a7d3e36870b683edfc3...81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
        "previous_git_commit": "8768460dc1c91de5f6485a7d3e36870b683edfc3",
        "previous_fingerprint": "2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8768460@sha256:2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/8768460dc1c91de5f6485a7d3e36870b683edfc3",
        "previous_trail_name": "8768460dc1c91de5f6485a7d3e36870b683edfc3",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 2126.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
          "template_reference_name": "runner",
          "git_commit": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
          "git_commit_info": {
            "sha1": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
            "message": "Merge pull request #231 from cyber-dojo/annotate-new-snyk-http2-entry\n\n.snyk: ignore SNYK-GOLANG-GOLANGORGXNETHTTP2-16535157 pending upstrea\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778243421.0,
            "url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=6d4a3808-b45b-4283-9bd8-73bc1197",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/8768460dc1c91de5f6485a7d3e36870b683edfc3...81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
            "previous_git_commit": "8768460dc1c91de5f6485a7d3e36870b683edfc3",
            "previous_fingerprint": "2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8768460@sha256:2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/8768460dc1c91de5f6485a7d3e36870b683edfc3",
            "previous_trail_name": "8768460dc1c91de5f6485a7d3e36870b683edfc3",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2126.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-48",
          "template_reference_name": "runner",
          "git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
          "git_commit_info": {
            "sha1": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "message": "Add Snyk scan to promote-all, scoped to aws-prod compliance only\n\nMirrors the change made to promote-one: inserts a snyk-scan job\n(before sdlc-control-gate) that scans each artifact against the\naws-prod environment policy. Removes KOSLI_AWS_BETA env var and\nthe aws-beta assert and attest steps.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777361993.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=bc1384dc-8f47-4916-8569-0180d9d5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8768460@sha256:2509ca654e1f09c19c59813aea76d45e787f487c9c18b3216e0a6d407e6b05e3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promotion-one-47",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 883554.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
          "template_reference_name": "runner",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=12a057ae-6dcb-4aa2-ab57-0925b3ab",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -366769.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
          "template_reference_name": "runner",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=69d04aee-743d-4e2b-963a-05e3a958",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -366769.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/8e8004a503584b378e411f9e150ac07d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:db53382@sha256:f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-45",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
      "creationTimestamp": [
        1778081137
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "db53382650db8b7b3f216d0055009b0d77685677",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=cc5da9c3-89bd-4ac1-a5ed-8885517d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/1a191ad636b6d1d2215e3726ad307f48f58843b6...db53382650db8b7b3f216d0055009b0d77685677",
        "previous_git_commit": "1a191ad636b6d1d2215e3726ad307f48f58843b6",
        "previous_fingerprint": "808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a191ad@sha256:808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/1a191ad636b6d1d2215e3726ad307f48f58843b6",
        "previous_trail_name": "1a191ad636b6d1d2215e3726ad307f48f58843b6",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 846.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
          "template_reference_name": "languages-start-points",
          "git_commit": "db53382650db8b7b3f216d0055009b0d77685677",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677",
          "git_commit_info": {
            "sha1": "db53382650db8b7b3f216d0055009b0d77685677",
            "message": "Merge pull request #206 from cyber-dojo/update-csharp-nunit2\n\nUpdate csharp-nunit",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778080291.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=cc5da9c3-89bd-4ac1-a5ed-8885517d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/1a191ad636b6d1d2215e3726ad307f48f58843b6...db53382650db8b7b3f216d0055009b0d77685677",
            "previous_git_commit": "1a191ad636b6d1d2215e3726ad307f48f58843b6",
            "previous_fingerprint": "808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a191ad@sha256:808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/1a191ad636b6d1d2215e3726ad307f48f58843b6",
            "previous_trail_name": "1a191ad636b6d1d2215e3726ad307f48f58843b6",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 846.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-45",
          "template_reference_name": "languages-start-points",
          "git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
          "git_commit_info": {
            "sha1": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "message": "Add Snyk scan to promote-all, scoped to aws-prod compliance only\n\nMirrors the change made to promote-one: inserts a snyk-scan job\n(before sdlc-control-gate) that scans each artifact against the\naws-prod environment policy. Removes KOSLI_AWS_BETA env var and\nthe aws-beta assert and attest steps.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777361993.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=88d4f5e5-448f-4b7c-b8a6-e21c5cfc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:1a191ad@sha256:808640967968ed09d2719d88e77e77a617030e5335d408a077d98cfbbeb49cf4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promotion-one-44",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 719144.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=7037421b-6bc3-4370-86e5-34d83a36",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947",
          "deployment_diff": null,
          "commit_lead_time": 466202.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=d58e2fcc-a224-47de-8c1b-4fc7bdbb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930",
          "deployment_diff": null,
          "commit_lead_time": 466202.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "e50b0406a64efc36fb236afd464e75b31877f623",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623",
          "git_commit_info": {
            "sha1": "e50b0406a64efc36fb236afd464e75b31877f623",
            "message": "Split snyk Kosli flows to separate per-vuln and per-artifact trails\n\nsnyk-vulns-{env} mixed two trail naming patterns: {repo}-{severity}-{CVE}\nfor individual vulnerabilities, and {repo}-{fingerprint} for aggregate\nartifact scan results. snyk-{env}-per-vuln and snyk-{env}-per-artifact\nmake each flow's purpose explicit and the Kosli UI easier to navigate.\n\nAlso removes temporary debug logging from the fingerprint step.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778153406.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=ebdd640f-262f-44d5-ac49-0c708fe2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": -72269.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=8423f705-5b80-4a74-b676-17487db8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -492095.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=818fc60e-1886-4306-96d1-fa582cad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -531179.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4c27d625895a4234a4e8a819817e4289",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
      "creationTimestamp": [
        1776923539
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=f1d404d2-81f9-4f7a-9a01-9742e3e2",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/8adb92a471e3f5caf65481155d45121a865b67a7...9dd6c657bc443c45c19e81165ff99286e237cfe3",
        "previous_git_commit": "8adb92a471e3f5caf65481155d45121a865b67a7",
        "previous_fingerprint": "db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:8adb92a@sha256:db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/8adb92a471e3f5caf65481155d45121a865b67a7",
        "previous_trail_name": "8adb92a471e3f5caf65481155d45121a865b67a7",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 2530.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
          "template_reference_name": "custom-start-points",
          "git_commit": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3",
          "git_commit_info": {
            "sha1": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
            "message": "Merge pull request #110 from cyber-dojo/remove-defaulted-aws-rolename\n\nRemove defaulted aws-rolename from snyk-scanning job",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776921009.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=f1d404d2-81f9-4f7a-9a01-9742e3e2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/8adb92a471e3f5caf65481155d45121a865b67a7...9dd6c657bc443c45c19e81165ff99286e237cfe3",
            "previous_git_commit": "8adb92a471e3f5caf65481155d45121a865b67a7",
            "previous_fingerprint": "db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:8adb92a@sha256:db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/8adb92a471e3f5caf65481155d45121a865b67a7",
            "previous_trail_name": "8adb92a471e3f5caf65481155d45121a865b67a7",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2530.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "custom-start-points",
          "git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "git_commit_info": {
            "sha1": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "message": "Revert WEB_SECRET_KEY_BASE changes - SECRET_KEY_BASE now fetched from AWS SSM in web's Terraform\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776099255.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=604eb5a4-324d-4140-a976-19265352",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:8adb92a@sha256:db4ebea9fe973c7f195668be3706cd6049c07ed693de1b6e7a2a090f00498497",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-10",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 824284.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=c6ec6ca6-9900-445e-8986-76bc3e3d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947",
          "deployment_diff": null,
          "commit_lead_time": -691396.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=fe2b6149-935b-4098-aafe-1afabea3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930",
          "deployment_diff": null,
          "commit_lead_time": -691396.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "e50b0406a64efc36fb236afd464e75b31877f623",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623",
          "git_commit_info": {
            "sha1": "e50b0406a64efc36fb236afd464e75b31877f623",
            "message": "Split snyk Kosli flows to separate per-vuln and per-artifact trails\n\nsnyk-vulns-{env} mixed two trail naming patterns: {repo}-{severity}-{CVE}\nfor individual vulnerabilities, and {repo}-{fingerprint} for aggregate\nartifact scan results. snyk-{env}-per-vuln and snyk-{env}-per-artifact\nmake each flow's purpose explicit and the Kosli UI easier to navigate.\n\nAlso removes temporary debug logging from the fingerprint step.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778153406.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=95af50be-66db-486f-8278-24a0ead0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": -1229867.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=caaa287b-e9f3-47cd-86b7-e76a1b58",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1649693.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=a2f4aeb3-5dce-4ef8-89ca-3b962782",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1688777.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f009873b96764616a63037619de83dd3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
      "creationTimestamp": [
        1776923208
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "447231c2018bc0690735b4ee110ca46431162fd5",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=98831c77-04a8-4427-9cf8-03950550",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/83ea563b423559eaf750dd680fc2329e59f60e3b...447231c2018bc0690735b4ee110ca46431162fd5",
        "previous_git_commit": "83ea563b423559eaf750dd680fc2329e59f60e3b",
        "previous_fingerprint": "597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:83ea563@sha256:597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/83ea563b423559eaf750dd680fc2329e59f60e3b",
        "previous_trail_name": "83ea563b423559eaf750dd680fc2329e59f60e3b",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 2123.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
          "template_reference_name": "exercises-start-points",
          "git_commit": "447231c2018bc0690735b4ee110ca46431162fd5",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5",
          "git_commit_info": {
            "sha1": "447231c2018bc0690735b4ee110ca46431162fd5",
            "message": "Merge pull request #117 from cyber-dojo/remove-defaulted-aws-rolename\n\nRemove defaulted aws-rolename from snyk-scanning job",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776921085.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=98831c77-04a8-4427-9cf8-03950550",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/83ea563b423559eaf750dd680fc2329e59f60e3b...447231c2018bc0690735b4ee110ca46431162fd5",
            "previous_git_commit": "83ea563b423559eaf750dd680fc2329e59f60e3b",
            "previous_fingerprint": "597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:83ea563@sha256:597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/83ea563b423559eaf750dd680fc2329e59f60e3b",
            "previous_trail_name": "83ea563b423559eaf750dd680fc2329e59f60e3b",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2123.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "exercises-start-points",
          "git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "git_commit_info": {
            "sha1": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "message": "Revert WEB_SECRET_KEY_BASE changes - SECRET_KEY_BASE now fetched from AWS SSM in web's Terraform\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776099255.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=82549870-9631-4bf3-90f7-13e64e6f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:83ea563@sha256:597d104edc7247a48d3a0339dd240d965a3176d0c1ce6531a1e2b5b8a9250846",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-10",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 823953.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=df1b23f7-316f-4d2a-90c1-4ad1b943",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930",
          "deployment_diff": null,
          "commit_lead_time": -691727.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=9a1e839e-8a7f-4dbc-abd1-5fe36251",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947",
          "deployment_diff": null,
          "commit_lead_time": -691727.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "e50b0406a64efc36fb236afd464e75b31877f623",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623",
          "git_commit_info": {
            "sha1": "e50b0406a64efc36fb236afd464e75b31877f623",
            "message": "Split snyk Kosli flows to separate per-vuln and per-artifact trails\n\nsnyk-vulns-{env} mixed two trail naming patterns: {repo}-{severity}-{CVE}\nfor individual vulnerabilities, and {repo}-{fingerprint} for aggregate\nartifact scan results. snyk-{env}-per-vuln and snyk-{env}-per-artifact\nmake each flow's purpose explicit and the Kosli UI easier to navigate.\n\nAlso removes temporary debug logging from the fingerprint step.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778153406.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=87b188e8-ada1-4090-8fce-dd25c3c1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": -1230198.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=27a1cec0-a6f0-4732-97e6-56a3a69b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1650024.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=a099ed90-59e0-4730-9630-5d7df684",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1689108.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a86d9e772a4b43e0b855e0e9d43163ca",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-14",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
      "creationTimestamp": [
        1778502485
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=6d83c4b2-39dd-4eba-9f37-dcdda1d9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/b1ce55beb190397c80d3ba0536f6b97bb5f468f6...498bf29ef05ecc0986874ca8a8949fd2a39ad269",
        "previous_git_commit": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
        "previous_fingerprint": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
        "previous_trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 78041.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
          "template_reference_name": "nginx",
          "git_commit": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269",
          "git_commit_info": {
            "sha1": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
            "message": "Merge pull request #117 from cyber-dojo/ci-test-job-and-expand-adr\n\nAdd CI test job, Harden Runner steps, and expand rate-limiting ADR",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778424444.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=6d83c4b2-39dd-4eba-9f37-dcdda1d9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/b1ce55beb190397c80d3ba0536f6b97bb5f468f6...498bf29ef05ecc0986874ca8a8949fd2a39ad269",
            "previous_git_commit": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
            "previous_fingerprint": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
            "previous_trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 78041.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-14",
          "template_reference_name": "nginx",
          "git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
          "git_commit_info": {
            "sha1": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "message": "Upgrade kosli-dev/setup-cli-action to move past node deprecation warnings",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245591.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=f5467047-77a7-42f8-a733-03548e75",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-11",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 256894.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
          "template_reference_name": "nginx",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=81802a3f-8765-4512-bb1a-d19038f7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109831.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
          "template_reference_name": "nginx",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=f672bab6-0945-4f7a-8f70-5f0f0581",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -109831.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7b99ba7056144cf7bc04d773dc1c61d7",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "attestation",
                "definition": {
                  "if": {
                    "text": "flow.name == \"snyk-vulns-aws-prod\""
                  },
                  "name": "snyk-container-scan",
                  "type": "generic",
                  "must_be_compliant": true
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "snyk-scan-aws-prod"
        },
        {
          "policy_version": 6,
          "status": "COMPLIANT",
          "rule_evaluations": [
            {
              "rule": {
                "type": "provenance",
                "definition": {
                  "required": true,
                  "exceptions": [
                    {
                      "if": {
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
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
                        "text": "flow.tags.kind != \"build\""
                      }
                    }
                  ]
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-11",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
      "creationTimestamp": [
        1776923213
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "30dffd09c3f896a322c65029247abcea3019c43a",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=046919b1-42dd-47f8-8569-912d0259",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/c9bbaa1eceb4b8bdffa065ea7034de23d3364919...30dffd09c3f896a322c65029247abcea3019c43a",
        "previous_git_commit": "c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
        "previous_fingerprint": "480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:c9bbaa1@sha256:480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
        "previous_trail_name": "c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 1092.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
          "template_reference_name": "differ",
          "git_commit": "30dffd09c3f896a322c65029247abcea3019c43a",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a",
          "git_commit_info": {
            "sha1": "30dffd09c3f896a322c65029247abcea3019c43a",
            "message": "Remove defaulted aws-rolename from snyk-scanning job (#373)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776922121.0,
            "url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=046919b1-42dd-47f8-8569-912d0259",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/c9bbaa1eceb4b8bdffa065ea7034de23d3364919...30dffd09c3f896a322c65029247abcea3019c43a",
            "previous_git_commit": "c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
            "previous_fingerprint": "480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:c9bbaa1@sha256:480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
            "previous_trail_name": "c9bbaa1eceb4b8bdffa065ea7034de23d3364919",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1092.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "differ",
          "git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
          "git_commit_info": {
            "sha1": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "message": "Revert WEB_SECRET_KEY_BASE changes - SECRET_KEY_BASE now fetched from AWS SSM in web's Terraform\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776099255.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=a5169b25-0d5c-491c-991e-2c1d389b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:c9bbaa1@sha256:480f4443a28b5057b956b1bcce13475b41bd2c1343563f18337ac0e7bf6e65ea",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-10",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 823958.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod-archived-at-1778595947",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=4eefbc15-7ea4-4d60-87d8-3a6098cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod-archived-at-1778595947",
          "deployment_diff": null,
          "commit_lead_time": -691722.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta-archived-at-1778595930",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "117e18e0cb1eab30b9747ece58327eabfc595b90",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90",
          "git_commit_info": {
            "sha1": "117e18e0cb1eab30b9747ece58327eabfc595b90",
            "message": "Add debug commands for kosli-fingerprint",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777614935.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/117e18e0cb1eab30b9747ece58327eabfc595b90"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=f295a00f-04cf-4c92-96d2-44181c6a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta-archived-at-1778595930",
          "deployment_diff": null,
          "commit_lead_time": -691722.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "e50b0406a64efc36fb236afd464e75b31877f623",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623",
          "git_commit_info": {
            "sha1": "e50b0406a64efc36fb236afd464e75b31877f623",
            "message": "Split snyk Kosli flows to separate per-vuln and per-artifact trails\n\nsnyk-vulns-{env} mixed two trail naming patterns: {repo}-{severity}-{CVE}\nfor individual vulnerabilities, and {repo}-{fingerprint} for aggregate\nartifact scan results. snyk-{env}-per-vuln and snyk-{env}-per-artifact\nmake each flow's purpose explicit and the Kosli UI easier to navigate.\n\nAlso removes temporary debug logging from the fingerprint step.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778153406.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/e50b0406a64efc36fb236afd464e75b31877f623"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=274a4692-c2f3-48eb-b9d9-6cbbedad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": -1230193.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
          "git_commit_info": {
            "sha1": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "message": "Swap \"See\" and \"Response guide\" lines in Slack expiry notification\n\nMove \"Response guide\" from the SLACK_MESSAGE jq output into the Send\nSlack step, after the \"See\" run URL line, so the action link appears\nbefore the docs link.\n\nAlso extract the two inline jq conditionals (day/days and rego/.snyk)\ninto named variables to shorten the long interpolated string.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778573232.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=1ef3d0fc-f3ea-4363-9f13-8eef3051",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1650019.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
          "git_commit_info": {
            "sha1": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "message": "Readme update",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778612316.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=5f14c5f2-2373-43fc-bab7-e8680377",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1689103.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ee14a7db1433415dbcbf9b2a5a983c4d",
        "cluster_name": null,
        "service_name": null
      }
    }
  ],
  "applied_policies": [
    {
      "id": "93d8505f-bce5-4c7c-a2c8-f98236c8",
      "name": "snyk-scan-aws-prod",
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
                "text": "flow.name == \"snyk-vulns-aws-prod\""
              },
              "name": "snyk-container-scan",
              "type": "generic",
              "must_be_compliant": true
            }
          ]
        }
      },
      "failing_artifacts": []
    },
    {
      "id": "e398f263-0770-42d3-bca1-b417aba0",
      "name": "build-process",
      "version": 6,
      "policy_dump": {
        "schema_version": "1",
        "artifacts": {
          "provenance": {
            "required": true,
            "exceptions": [
              {
                "if_condition": {
                  "text": "flow.tags.kind != \"build\""
                }
              }
            ]
          },
          "trail_compliance": {
            "required": true,
            "exceptions": [
              {
                "if_condition": {
                  "text": "flow.tags.kind != \"build\""
                }
              }
            ]
          },
          "attestations": [
            {
              "if_condition": {
                "text": "flow.tags.kind == \"build\""
              },
              "name": "*",
              "type": "pull_request",
              "must_be_compliant": true
            }
          ]
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

