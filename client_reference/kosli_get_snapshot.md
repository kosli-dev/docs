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
  "index": 5069,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1784790118.4310617,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5069",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:2e200e4@sha256:919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
                    "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-134",
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
      "fingerprint": "919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067",
      "creationTimestamp": [
        1784790028,
        1784790030,
        1784790031
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/2e200e4e3ee5b6dc4968bac67c27431e46be992c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067?artifact_id=ac186b3c-a669-4002-86ad-432aeedd",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/88b7eeacb488a5117ac568408363ac59a146f41a...2e200e4e3ee5b6dc4968bac67c27431e46be992c",
        "previous_git_commit": "88b7eeacb488a5117ac568408363ac59a146f41a",
        "previous_fingerprint": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a",
        "previous_trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1758.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
          "template_reference_name": "runner",
          "git_commit": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/2e200e4e3ee5b6dc4968bac67c27431e46be992c",
          "git_commit_info": {
            "sha1": "2e200e4e3ee5b6dc4968bac67c27431e46be992c",
            "message": "Merge pull request #268 from cyber-dojo/ignore-grpc-transport-vuln-18172578\n\nIgnore non-exploitable gRPC-Go transport vuln 18172578",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784788270.0,
            "url": "https://github.com/cyber-dojo/runner/commit/2e200e4e3ee5b6dc4968bac67c27431e46be992c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067?artifact_id=ac186b3c-a669-4002-86ad-432aeedd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/88b7eeacb488a5117ac568408363ac59a146f41a...2e200e4e3ee5b6dc4968bac67c27431e46be992c",
            "previous_git_commit": "88b7eeacb488a5117ac568408363ac59a146f41a",
            "previous_fingerprint": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a",
            "previous_trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1758.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-134",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/919ef9b551049248ad99cf2a292992e34df407578068be9dbb59fa60ab04d067?artifact_id=fe49d75f-2d97-4e1b-96ea-94d91aff",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-120",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 937327.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b7e1677259124d8ba844f72a08d8cb2f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:f4bb341@sha256:fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
                    "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-133",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
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
      "fingerprint": "fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
      "creationTimestamp": [
        1784443888
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "f4bb3412725258648a7cf5ce1a776609b4dade72",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
        "previous_git_commit": "55561dc8a8d25313f5318038f26892cdee5e90f7",
        "previous_fingerprint": "b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:55561dc@sha256:b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/55561dc8a8d25313f5318038f26892cdee5e90f7",
        "previous_trail_name": "55561dc8a8d25313f5318038f26892cdee5e90f7",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 3678.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "f4bb3412725258648a7cf5ce1a776609b4dade72",
          "template_reference_name": "saver",
          "git_commit": "f4bb3412725258648a7cf5ce1a776609b4dade72",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72",
          "git_commit_info": {
            "sha1": "f4bb3412725258648a7cf5ce1a776609b4dade72",
            "message": "Docs api tab seq and restructure (#435)\n\n* Document tab_seq and restructure the API reference\n\n  The saver now dedups kata writes on (laptop_id, tab_seq), so tab_seq\n  needs documenting alongside laptop_id on the nine write methods, and\n  the read-event examples need it shown on committed events.\n\n  While there, make the API reference easier to scan and navigate:\n  - headings and links use bare method names (params moved below)\n  - each section lists its methods in a Verb/Method/Description table\n  - Cluster/Group/Kata/ID/Diff/Probe each gain a one-line blurb\n  - each method leads with a description item; parameters become a\n    Name/Type/Description table\n  - kata_events/kata_event examples refreshed to the v2 event shape\n\n  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>\n\n* Add client-side tab_seq to the kata write methods\n\n  The saver dedups kata writes on (laptop_id, tab_seq), but the client\n  library only forwarded laptop_id and had no tab_seq coverage, so a\n  redelivered write could not be exercised end-to-end from the client.\n\n  Make tab_seq a required arg on the five client write methods (forwarded\n  in the POST body like laptop_id), have the test-base forwarders default\n  it via a per-test next_tab_seq counter, and add kata_tab_seq_test:\n  tab_seq is stored and read back, a redelivered (laptop_id, tab_seq) is a\n  no-op, and distinct tab_seqs both commit. Same-laptop concurrent writes\n  now pass a distinct tab_seq per racing thread so they are not deduped.\n\n  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784440210.0,
            "url": "https://github.com/cyber-dojo/saver/commit/f4bb3412725258648a7cf5ce1a776609b4dade72"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=e3c009b8-349c-4f4e-8730-f45dfccf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/55561dc8a8d25313f5318038f26892cdee5e90f7...f4bb3412725258648a7cf5ce1a776609b4dade72",
            "previous_git_commit": "55561dc8a8d25313f5318038f26892cdee5e90f7",
            "previous_fingerprint": "b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:55561dc@sha256:b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/55561dc8a8d25313f5318038f26892cdee5e90f7",
            "previous_trail_name": "55561dc8a8d25313f5318038f26892cdee5e90f7",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3678.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-133",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=4863df5d-e4e4-4239-ba51-0c76d3e8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:55561dc@sha256:b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-129",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 591187.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
          "template_reference_name": "saver",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=4aa077cf-8d66-4f9c-8aa4-9e4e13f3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 592914.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97",
          "template_reference_name": "saver",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/fcfc73775b49f8b8414c720e820b38258c6d18cb9d25b7ac76ff2d528a7add97?artifact_id=6040043c-d039-4721-b0b6-ee022576",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_fingerprint": "b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:55561dc@sha256:b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_trail_name": "saver-b0c07ba3f67f16c2a1b6f0096f1474df6600ed3556e0e82b78d24acabc9b2bab",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 592914.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a63d8644d8fc4fa8b527fabd8e6cec3a",
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
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=9cb9b0f1-bae9-4e1b-903e-ae9dfe7e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 506096.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6",
          "template_reference_name": "creator",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/aaf68b01cfe75f9012155d59cc7421dac140457ea7f5eb1e508e12b7f1e58aa6?artifact_id=ff64caf2-05e1-4e62-99a8-7c20edd8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 506096.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2730a627a7a3472b810cacada52f3935",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:5407827@sha256:d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
                    "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-131",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
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
      "fingerprint": "d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
      "creationTimestamp": [
        1784355921
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=53e5b750-6f87-43db-a8a3-e1f5b1db",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/e4757683b74df7033c95aa544a7824b395c2f8bb...5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
        "previous_git_commit": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "previous_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "previous_trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 43879.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
          "template_reference_name": "dashboard",
          "git_commit": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
          "git_commit_info": {
            "sha1": "5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
            "message": "Read deployed image for drift-detection plan (#417)\n\nThe Detect Drift workflow runs a terraform plan with no build behind it,\nbut the ECS deployment requires a container image (TF_VAR_TAGGED_IMAGE).\nThe variable has no default and the task definition tracks it directly,\nso a drift plan either fails with \"no value for required variable\" or, if\ngiven a placeholder, reports permanent false drift on the task definition.\n\nBefore planning, each environment reads the image that is currently\ndeployed straight from its ECS task definition and passes it to the\nreusable drift workflow as TF_VAR_TAGGED_IMAGE. The image lookup is done\nexplicitly in this repository rather than in the shared kosli-dev/tf\nworkflow, so Kosli's own drift detection is unaffected.\n\nThe logic lives in a local reusable workflow, detect-drift-env.yml, which\nis parameterized by AWS account and environment. detect-drift.yml holds\nonly the schedule and a beta/prod matrix that calls it, so there is no\nduplication between environments and adding another is a two-line change.",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1784312042.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/5407827a19ff32c8d0e7ff2e8f18665e86e64f01"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=53e5b750-6f87-43db-a8a3-e1f5b1db",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/e4757683b74df7033c95aa544a7824b395c2f8bb...5407827a19ff32c8d0e7ff2e8f18665e86e64f01",
            "previous_git_commit": "e4757683b74df7033c95aa544a7824b395c2f8bb",
            "previous_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
            "previous_trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 43879.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-131",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=4485997e-f05e-4e02-a192-8e7ccff7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 503220.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
          "template_reference_name": "dashboard",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=0562cdd9-17c8-47ae-84ab-86991475",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 504947.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e",
          "template_reference_name": "dashboard",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/d5e2c2da34f74c61721f620d410e6ae9299f15e1f928aeb903cefdd72a1e815e?artifact_id=6c980c24-01d3-4dd3-a111-329308e2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 504947.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fb1ca8ead3c2436e83ca34d72d275313",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3f0b997@sha256:0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
                    "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-130",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
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
      "fingerprint": "0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
      "creationTimestamp": [
        1784352887,
        1784352892,
        1784352892
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
      "commit_url": "https://github.com/cyber-dojo/web/commit/3f0b9975f96b7f4e4aae0b4409cebda3209be164",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=0f00c8a9-1489-416c-b64f-5819890f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/bdf01beca687a34db9689499bd805cfc752a1747...3f0b9975f96b7f4e4aae0b4409cebda3209be164",
        "previous_git_commit": "bdf01beca687a34db9689499bd805cfc752a1747",
        "previous_fingerprint": "64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bdf01be@sha256:64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/bdf01beca687a34db9689499bd805cfc752a1747",
        "previous_trail_name": "bdf01beca687a34db9689499bd805cfc752a1747",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 56258.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
          "template_reference_name": "web",
          "git_commit": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
          "commit_url": "https://github.com/cyber-dojo/web/commit/3f0b9975f96b7f4e4aae0b4409cebda3209be164",
          "git_commit_info": {
            "sha1": "3f0b9975f96b7f4e4aae0b4409cebda3209be164",
            "message": "Merge pull request #385 from cyber-dojo/add-drift-detection\n\nRead deployed image for drift-detection plan",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1784296629.0,
            "url": "https://github.com/cyber-dojo/web/commit/3f0b9975f96b7f4e4aae0b4409cebda3209be164"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=0f00c8a9-1489-416c-b64f-5819890f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/bdf01beca687a34db9689499bd805cfc752a1747...3f0b9975f96b7f4e4aae0b4409cebda3209be164",
            "previous_git_commit": "bdf01beca687a34db9689499bd805cfc752a1747",
            "previous_fingerprint": "64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bdf01be@sha256:64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/bdf01beca687a34db9689499bd805cfc752a1747",
            "previous_trail_name": "bdf01beca687a34db9689499bd805cfc752a1747",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 56258.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
          "template_reference_name": "web",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=7a70a8fa-ae6d-40c2-9aea-532dfae2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "web-929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 501913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-130",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=ef4ad7ac-354a-4541-beb1-9d1e1ac7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/76325d840dc66e1c84743725e17de05a16616419...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "76325d840dc66e1c84743725e17de05a16616419",
            "previous_fingerprint": "64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:bdf01be@sha256:64c1342f34dfbf19a5da21b0b027ac20abdbc1be6e1c763ff90a83ae207f9920",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/76325d840dc66e1c84743725e17de05a16616419",
            "previous_trail_name": "promotion-one-125",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 500186.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972",
          "template_reference_name": "web",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0eaa303537220d95ba656b829c1d9c85e2865c986c4736962b85f4df5adb8972?artifact_id=bf651877-3dd3-4001-820b-df04f225",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 501913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ef2471a4418645c1ae25de259e1ac91f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:335ddfa@sha256:c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
                    "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-128",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
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
      "fingerprint": "c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
      "creationTimestamp": [
        1784184597
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "335ddfa139708c37908dd594a0502bc6d88f8615",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=5f3d2a2e-acdb-4414-a1e7-ebca7c32",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/8beff9901ac67acb7afcab3408106208571a1124...335ddfa139708c37908dd594a0502bc6d88f8615",
        "previous_git_commit": "8beff9901ac67acb7afcab3408106208571a1124",
        "previous_fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
        "previous_trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 423508.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "335ddfa139708c37908dd594a0502bc6d88f8615",
          "template_reference_name": "differ",
          "git_commit": "335ddfa139708c37908dd594a0502bc6d88f8615",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615",
          "git_commit_info": {
            "sha1": "335ddfa139708c37908dd594a0502bc6d88f8615",
            "message": "Run workflow so image has updated git to fix new cares snyk vuln (#431)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783761089.0,
            "url": "https://github.com/cyber-dojo/differ/commit/335ddfa139708c37908dd594a0502bc6d88f8615"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=5f3d2a2e-acdb-4414-a1e7-ebca7c32",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/8beff9901ac67acb7afcab3408106208571a1124...335ddfa139708c37908dd594a0502bc6d88f8615",
            "previous_git_commit": "8beff9901ac67acb7afcab3408106208571a1124",
            "previous_fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
            "previous_trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 423508.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-128",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=c445f15d-1957-4d94-9123-d67ad0b8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 331896.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
          "template_reference_name": "differ",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=dd1d108b-6d0a-47fb-8d6e-046c2862",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 333623.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f",
          "template_reference_name": "differ",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/c2a404127f3114a7b82a8c0633f85bad599dd54d9c97cf1bc872ae9eab2bbe5f?artifact_id=f745a495-4a20-4dd8-80d2-b61ab6a0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 333623.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/28557ef6830842138dd4db99a13c5d4a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7ba8029@sha256:3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
                    "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-127",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
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
      "fingerprint": "3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
      "creationTimestamp": [
        1784183551
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=5c293d3e-84a1-42dd-8215-6abd8d8d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/9b711df71c76a1f293c2525ace65778036591baf...7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
        "previous_git_commit": "9b711df71c76a1f293c2525ace65778036591baf",
        "previous_fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
        "previous_trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 1377.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
          "template_reference_name": "nginx",
          "git_commit": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
          "git_commit_info": {
            "sha1": "7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
            "message": "Merge pull request #159 from cyber-dojo/remove-curl-fix-snyk-alpine323-curl-17970543\n\nRemove curl to clear recurring Alpine libcurl CVEs",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784182174.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=5c293d3e-84a1-42dd-8215-6abd8d8d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/9b711df71c76a1f293c2525ace65778036591baf...7ba8029e0cb5d4c8fa51360f59b5cb8714a60d47",
            "previous_git_commit": "9b711df71c76a1f293c2525ace65778036591baf",
            "previous_fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
            "previous_trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 1377.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-127",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=70dad200-6f93-430c-a06d-e1479d48",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 330850.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
          "template_reference_name": "nginx",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=39abaccd-2adc-48e5-992d-8804e957",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_fingerprint": "8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:66c0766@sha256:8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_trail_name": "nginx-8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 332577.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5",
          "template_reference_name": "nginx",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/3fe0f4dede834e7315a340526c9719446a7537a4e4e42c6802c3c5ac86db3ec5?artifact_id=dd50eb8f-6a1c-44ca-a377-51e9a110",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 332577.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/950b7815820f45dd82a7dec0a382128a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c6db342@sha256:f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
      "fingerprint": "f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
      "creationTimestamp": [
        1783618209
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=ed104a44-8358-4883-beeb-ac3c8bb7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/04e0e14bb8874ab521d35c97d6040133f0d2143a...c6db342472238a7852b6ff31b04f9a6a6099f5cf",
        "previous_git_commit": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
        "previous_fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
        "previous_trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 81654.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
          "template_reference_name": "languages-start-points",
          "git_commit": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf",
          "git_commit_info": {
            "sha1": "c6db342472238a7852b6ff31b04f9a6a6099f5cf",
            "message": "Merge pull request #242 from cyber-dojo/declare-sbom-and-provenance-facts-attestations\n\nDeclare sbom and provenance facts+decision attestations in the trail \u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783536555.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/c6db342472238a7852b6ff31b04f9a6a6099f5cf"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=ed104a44-8358-4883-beeb-ac3c8bb7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/04e0e14bb8874ab521d35c97d6040133f0d2143a...c6db342472238a7852b6ff31b04f9a6a6099f5cf",
            "previous_git_commit": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
            "previous_fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/04e0e14bb8874ab521d35c97d6040133f0d2143a",
            "previous_trail_name": "04e0e14bb8874ab521d35c97d6040133f0d2143a",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 81654.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
          "template_reference_name": "languages-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=a9535090-47a2-4ea2-8827-c368a63e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:04e0e14@sha256:a89642efb4e686ea38d597e20c2c3f256649d8bca02e2d923767844a6897667c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 711101.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
          "template_reference_name": "languages-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=b08301eb-028d-4fa4-8256-d1be128c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -232765.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
          "template_reference_name": "languages-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=89037be6-c695-4b0e-adad-87a83502",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -232765.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e0989e55de644314bd7c0db5f877729c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d37aace@sha256:1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
      "fingerprint": "1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
      "creationTimestamp": [
        1783618204
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
        "previous_git_commit": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
        "previous_fingerprint": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659",
        "previous_trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 4272.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
          "template_reference_name": "custom-start-points",
          "git_commit": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
          "git_commit_info": {
            "sha1": "d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
            "message": "Merge pull request #139 from cyber-dojo/run-workflow-171\n\nRun main workflow to check updates to secure-build sub workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783613932.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/d37aace7598ee943ba0bd5e51f224335cbdf0a3e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=e434f9eb-be9c-4851-ab99-187f1a26",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/fc6b09be0518fbf8ab76815cb85b1745631e3659...d37aace7598ee943ba0bd5e51f224335cbdf0a3e",
            "previous_git_commit": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
            "previous_fingerprint": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/fc6b09be0518fbf8ab76815cb85b1745631e3659",
            "previous_trail_name": "fc6b09be0518fbf8ab76815cb85b1745631e3659",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 4272.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
          "template_reference_name": "custom-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=f63f0700-2e41-44a7-ab00-31da5193",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:fc6b09b@sha256:1dbac604d2f08378e085032c135be4f4910559a7d7723c26372724d6fb8010d1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 711096.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
          "template_reference_name": "custom-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=947aceb0-d3d2-4dc6-857f-48489d35",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -232770.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
          "template_reference_name": "custom-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=acf7a61b-1150-48ad-896b-d88a4715",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -232770.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5333f9f522e74ab797a3893465e348d9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:804f248@sha256:a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-30",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
      "fingerprint": "a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
      "creationTimestamp": [
        1783618126
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "804f248d832dc34e564507b009c246dfb4f0c657",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=0e55e1be-fab1-475b-8aaa-b45ca6e2",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/80b913e9f88902428a3567f75165d8b9d73b561a...804f248d832dc34e564507b009c246dfb4f0c657",
        "previous_git_commit": "80b913e9f88902428a3567f75165d8b9d73b561a",
        "previous_fingerprint": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a",
        "previous_trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 81944.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "804f248d832dc34e564507b009c246dfb4f0c657",
          "template_reference_name": "exercises-start-points",
          "git_commit": "804f248d832dc34e564507b009c246dfb4f0c657",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657",
          "git_commit_info": {
            "sha1": "804f248d832dc34e564507b009c246dfb4f0c657",
            "message": "Merge pull request #145 from cyber-dojo/declare-sbom-and-provenance-facts-attestations\n\nDeclare sbom and provenance facts+decision attestations in the trail \u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783536182.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/804f248d832dc34e564507b009c246dfb4f0c657"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=0e55e1be-fab1-475b-8aaa-b45ca6e2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/80b913e9f88902428a3567f75165d8b9d73b561a...804f248d832dc34e564507b009c246dfb4f0c657",
            "previous_git_commit": "80b913e9f88902428a3567f75165d8b9d73b561a",
            "previous_fingerprint": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/80b913e9f88902428a3567f75165d8b9d73b561a",
            "previous_trail_name": "80b913e9f88902428a3567f75165d8b9d73b561a",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 81944.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
          "template_reference_name": "exercises-start-points",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=729eea0c-e715-4d68-8a0a-b25a7202",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:80b913e@sha256:748c413e0f6e45c3652fa4ee47ff2d7371da0bade41c027711296216b53db39b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 711018.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
          "template_reference_name": "exercises-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=d2f09480-2fe9-4995-9f0b-5b24b3b8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -232848.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
          "template_reference_name": "exercises-start-points",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=35476f3a-e0c2-43d9-bf69-80a4e599",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -232848.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c2a918fa550f40d6a4f2b35f023d40f1",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:88b7eea@sha256:cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
                    "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-120",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
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
      "fingerprint": "cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
      "creationTimestamp": [
        1783757709,
        1783757715,
        1783757716
      ],
      "pods": null,
      "annotation": {
        "type": "exited",
        "was": 3,
        "now": 0
      },
      "flow_name": "runner-ci",
      "git_commit": "88b7eeacb488a5117ac568408363ac59a146f41a",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
        "previous_git_commit": "627315ab66d5250fec7ec574b073f1095879a8a4",
        "previous_fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/627315ab66d5250fec7ec574b073f1095879a8a4",
        "previous_trail_name": "627315ab66d5250fec7ec574b073f1095879a8a4",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1776.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "88b7eeacb488a5117ac568408363ac59a146f41a",
          "template_reference_name": "runner",
          "git_commit": "88b7eeacb488a5117ac568408363ac59a146f41a",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a",
          "git_commit_info": {
            "sha1": "88b7eeacb488a5117ac568408363ac59a146f41a",
            "message": "Merge pull request #266 from cyber-dojo/update-snyk-policy\n\nUpdate .snyk policy file for new vulns that are not exploitable",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783755933.0,
            "url": "https://github.com/cyber-dojo/runner/commit/88b7eeacb488a5117ac568408363ac59a146f41a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=34ecf062-b48d-4c41-8714-e432768c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/627315ab66d5250fec7ec574b073f1095879a8a4...88b7eeacb488a5117ac568408363ac59a146f41a",
            "previous_git_commit": "627315ab66d5250fec7ec574b073f1095879a8a4",
            "previous_fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/627315ab66d5250fec7ec574b073f1095879a8a4",
            "previous_trail_name": "627315ab66d5250fec7ec574b073f1095879a8a4",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1776.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-120",
          "template_reference_name": "runner",
          "git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
          "git_commit_info": {
            "sha1": "d7e31ce0207b766140ae689f38625da4374acf87",
            "message": "Merge pull request #15 from cyber-dojo/delete-dead-comments\n\nDelete dead comments",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782907108.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=5951a303-b159-46bf-b22b-ab2c6f1e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 850601.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
          "template_reference_name": "runner",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=ca67618d-6290-404e-b19d-404bd891",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:627315a@sha256:b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "runner-b65f224d822ea1b3702a1154c1bd088f27906393755b73c570aefa054ef4211b",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -93265.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf",
          "template_reference_name": "runner",
          "git_commit": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
          "git_commit_info": {
            "sha1": "35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "message": "Add emoji prefixes to workflow names\n\n  Match the visual convention already used in the kosli-demo/stochastic-committer\n  repo, where the Actions sidebar distinguishes workflow roles at a glance.\n\n  The two aws-* files are the top-level entry points, triggered by dispatch and\n  schedule, so they get the play emoji. The three reusable workflow_call\n  sub-workflows get the package emoji to mark them as callable building blocks.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1783850974.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/35a09b2d283bafd6bbc12c29eba3306d5b36a5f7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=95ed58aa-f8ca-49ce-b328-1e13f52b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -93265.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/605ef5f5a475499bb0b6dd215978e96e",
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

