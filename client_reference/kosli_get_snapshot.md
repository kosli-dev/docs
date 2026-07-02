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
  "index": 4932,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1782973678.4485867,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4932",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9d18877@sha256:7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "differ-ci",
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
                    "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-115",
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
      "fingerprint": "7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb",
      "creationTimestamp": [
        1782973596
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb?artifact_id=2253016a-6669-4742-a9ac-19e2c25a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/5812bb564e572c9e33aef2789d2687f1a999a687...9d1887776497e501bc8dcd46e508488bf5c8b0c8",
        "previous_git_commit": "5812bb564e572c9e33aef2789d2687f1a999a687",
        "previous_fingerprint": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/5812bb564e572c9e33aef2789d2687f1a999a687",
        "previous_trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 1729.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
          "template_reference_name": "differ",
          "git_commit": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8",
          "git_commit_info": {
            "sha1": "9d1887776497e501bc8dcd46e508488bf5c8b0c8",
            "message": "Force ci-run to allow creation of terraform differ-drift file on aws-prod (#420)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782971867.0,
            "url": "https://github.com/cyber-dojo/differ/commit/9d1887776497e501bc8dcd46e508488bf5c8b0c8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb?artifact_id=2253016a-6669-4742-a9ac-19e2c25a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/5812bb564e572c9e33aef2789d2687f1a999a687...9d1887776497e501bc8dcd46e508488bf5c8b0c8",
            "previous_git_commit": "5812bb564e572c9e33aef2789d2687f1a999a687",
            "previous_fingerprint": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/5812bb564e572c9e33aef2789d2687f1a999a687",
            "previous_trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1729.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-115",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7be2ef9d49b95f256b734987619068484fde1dbe123bd9c814947d573b6638cb?artifact_id=61527ef0-824c-4ce0-a20a-5306d41f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_fingerprint": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_trail_name": "promotion-one-102",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 66488.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/30b9891184444c3cb7656cf2215a7bdf",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:df9af0c@sha256:157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
                    "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-113",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
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
      "fingerprint": "157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
      "creationTimestamp": [
        1782969676
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/df9af0c9a2a81ed7bfc429979121b8310bbe7138",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=149f3e12-210d-48b5-af42-01085ab2",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f62bce8337416d4f785ca825999e3045382b5e5d...df9af0c9a2a81ed7bfc429979121b8310bbe7138",
        "previous_git_commit": "f62bce8337416d4f785ca825999e3045382b5e5d",
        "previous_fingerprint": "eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f62bce8@sha256:eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f62bce8337416d4f785ca825999e3045382b5e5d",
        "previous_trail_name": "f62bce8337416d4f785ca825999e3045382b5e5d",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 1357.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
          "template_reference_name": "dashboard",
          "git_commit": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/df9af0c9a2a81ed7bfc429979121b8310bbe7138",
          "git_commit_info": {
            "sha1": "df9af0c9a2a81ed7bfc429979121b8310bbe7138",
            "message": "Force ci run to create terraform dashboard-drift file on aws-prod (#407)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782968319.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/df9af0c9a2a81ed7bfc429979121b8310bbe7138"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=149f3e12-210d-48b5-af42-01085ab2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/f62bce8337416d4f785ca825999e3045382b5e5d...df9af0c9a2a81ed7bfc429979121b8310bbe7138",
            "previous_git_commit": "f62bce8337416d4f785ca825999e3045382b5e5d",
            "previous_fingerprint": "eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f62bce8@sha256:eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/f62bce8337416d4f785ca825999e3045382b5e5d",
            "previous_trail_name": "f62bce8337416d4f785ca825999e3045382b5e5d",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1357.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-113",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=ee85bf2e-bc97-4d0b-8084-c990ebd5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c1b1e0c943de88d31a15ba62466f4e9c6bd45259...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_fingerprint": "eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f62bce8@sha256:eb7487a1d5c579d3eca8bda22d5e71667e515efb2d20ae4ef8b1a91bf4cb072b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_trail_name": "promotion-one-98",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 62568.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
          "template_reference_name": "dashboard",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=d72c5b89-4699-495a-ab81-97725b1c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 170373.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1",
          "template_reference_name": "dashboard",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/157aa8681858c1be91d5a4ecda1674d0e40b6e0cde1a22027b80c51c7a2eb1b1?artifact_id=f9964800-44f6-4ab5-a4ec-4ac77369",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0e0b4c1@sha256:76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "dashboard-76898630b521e22b13e4bbec9e14ada885b5571f7ef64d721369198a3b77480f",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 170373.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/406f3babd3d1460cbf42ba999c8a8015",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:139dc6d@sha256:45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
                    "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-111",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
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
      "fingerprint": "45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
      "creationTimestamp": [
        1782966801
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=03592b11-2821-4d18-b7cb-7e4442a7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/670c9632fe81e69d2cf48aa1dc21347b562fb042...139dc6d316a5e4b66755fecc926f2e25cd5c8208",
        "previous_git_commit": "670c9632fe81e69d2cf48aa1dc21347b562fb042",
        "previous_fingerprint": "e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:670c963@sha256:e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/670c9632fe81e69d2cf48aa1dc21347b562fb042",
        "previous_trail_name": "670c9632fe81e69d2cf48aa1dc21347b562fb042",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 1693.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
          "template_reference_name": "saver",
          "git_commit": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208",
          "git_commit_info": {
            "sha1": "139dc6d316a5e4b66755fecc926f2e25cd5c8208",
            "message": "Disable dead workflows (#419)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782965108.0,
            "url": "https://github.com/cyber-dojo/saver/commit/139dc6d316a5e4b66755fecc926f2e25cd5c8208"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=03592b11-2821-4d18-b7cb-7e4442a7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/670c9632fe81e69d2cf48aa1dc21347b562fb042...139dc6d316a5e4b66755fecc926f2e25cd5c8208",
            "previous_git_commit": "670c9632fe81e69d2cf48aa1dc21347b562fb042",
            "previous_fingerprint": "e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:670c963@sha256:e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/670c9632fe81e69d2cf48aa1dc21347b562fb042",
            "previous_trail_name": "670c9632fe81e69d2cf48aa1dc21347b562fb042",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1693.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-111",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=12d9e7c1-4458-49cc-90f9-65e7d617",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c1b1e0c943de88d31a15ba62466f4e9c6bd45259...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_fingerprint": "e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:670c963@sha256:e60133ad9dfe473b76853173204f15c0a307fd81b561be2531f197efb99e8499",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_trail_name": "promotion-one-91",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 59693.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
          "template_reference_name": "saver",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=de3fc417-9922-45d4-a5f5-a6ff932c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 167498.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd",
          "template_reference_name": "saver",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/45aed88b436d6e57bca837e366ee5c8fe2baaca3715d6fa2a15da8a9fe6f23bd?artifact_id=e3318c41-a758-45bb-a068-34d16d05",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a35d092@sha256:5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "saver-5153955367bbc753a61648d385a73f0e391d2a7410e3d55e095da7d69b418b7e",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 167498.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/8b0f830462714c0cb4b3b81654b602eb",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:027b85e@sha256:38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
                    "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-112",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
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
      "fingerprint": "38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
      "creationTimestamp": [
        1782966793,
        1782966799,
        1782966800
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
      "commit_url": "https://github.com/cyber-dojo/web/commit/027b85ebccec65b35b0ba0e4da196b7738d4ba82",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=df97a2c6-d2eb-4465-b276-084bd7a7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a...027b85ebccec65b35b0ba0e4da196b7738d4ba82",
        "previous_git_commit": "44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
        "previous_fingerprint": "11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:44e3ad9@sha256:11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
        "previous_trail_name": "44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 1026.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
          "template_reference_name": "web",
          "git_commit": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
          "commit_url": "https://github.com/cyber-dojo/web/commit/027b85ebccec65b35b0ba0e4da196b7738d4ba82",
          "git_commit_info": {
            "sha1": "027b85ebccec65b35b0ba0e4da196b7738d4ba82",
            "message": "Force ci-run to create terraform web-drift file for aws-prod (#372)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782965767.0,
            "url": "https://github.com/cyber-dojo/web/commit/027b85ebccec65b35b0ba0e4da196b7738d4ba82"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=df97a2c6-d2eb-4465-b276-084bd7a7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a...027b85ebccec65b35b0ba0e4da196b7738d4ba82",
            "previous_git_commit": "44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
            "previous_fingerprint": "11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:44e3ad9@sha256:11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
            "previous_trail_name": "44e3ad96800ba2ccd41a3aec3ba4e728d40e9e4a",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1026.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-112",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=d8014b09-34a8-4fff-89a2-07786149",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c1b1e0c943de88d31a15ba62466f4e9c6bd45259...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_fingerprint": "11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:44e3ad9@sha256:11ea3e527a5d5d6c8a54cd098dc6f78bdf6368b78c22a024fc046cf8be4124fe",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_trail_name": "promotion-one-94",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 59685.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
          "template_reference_name": "web",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=3b1ccdd3-5b97-4b00-9b4d-39c34b68",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "web-29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 167490.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac",
          "template_reference_name": "web",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/38f8dcef0a01f88341d5e0b051a462c34622877c880a48b1ba40635a20ee1dac?artifact_id=da0dc1f1-2d47-4d1f-b6e5-96374b32",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:42ca333@sha256:d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "web-d7112bc0d70f56933b10c90b29e3d47abeaff64b9c95f2b53882f7d3ec819685",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 167490.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f0cdd7720c464eddb42fef9802d5c04a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:ae0c2f0@sha256:fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
                    "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-110",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
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
      "fingerprint": "fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
      "creationTimestamp": [
        1782966159
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=23d32989-6594-441a-8baa-ba54c633",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/2b7b7759d2f5f8246a5d0e9ea99def087a7e2817...ae0c2f039480061d958cc007bc4c78e5b0f36a83",
        "previous_git_commit": "2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
        "previous_fingerprint": "7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:2b7b775@sha256:7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
        "previous_trail_name": "2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 1076.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
          "template_reference_name": "custom-start-points",
          "git_commit": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83",
          "git_commit_info": {
            "sha1": "ae0c2f039480061d958cc007bc4c78e5b0f36a83",
            "message": "Merge pull request #131 from cyber-dojo/force-ci-run-169\n\nRun ci workflow to create terraform drift file on aws-prod",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782965083.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/ae0c2f039480061d958cc007bc4c78e5b0f36a83"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=23d32989-6594-441a-8baa-ba54c633",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/2b7b7759d2f5f8246a5d0e9ea99def087a7e2817...ae0c2f039480061d958cc007bc4c78e5b0f36a83",
            "previous_git_commit": "2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
            "previous_fingerprint": "7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:2b7b775@sha256:7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
            "previous_trail_name": "2b7b7759d2f5f8246a5d0e9ea99def087a7e2817",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 1076.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-110",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=c8be4dd9-1e66-497d-b4ff-acbf6ef0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c1b1e0c943de88d31a15ba62466f4e9c6bd45259...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_fingerprint": "7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:2b7b775@sha256:7f297e8a0ed0459b7251fd024042e5bcbd24b654934de2a7963db8d1416859a3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_trail_name": "promotion-one-97",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 59051.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
          "template_reference_name": "custom-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=95c90ad9-a395-40cc-a9b4-6b044a2a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "custom-start-points-b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 166856.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3",
          "template_reference_name": "custom-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/fc0f6172590f996051b97a84551748cbb02f3ee4812f824ffe5b9ff17f69a8b3?artifact_id=6d3f6435-b913-4693-a6b8-f386b85f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:514f79a@sha256:311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "custom-start-points-311da8e95c74716bf3953de67a6dc3fe514c88d805a08a55ab17c677d75cf797",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 166856.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ad075a2ed76047bfadfc827e5102f274",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:552f300@sha256:7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
                    "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-109",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
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
      "fingerprint": "7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
      "creationTimestamp": [
        1782963924,
        1782963926,
        1782963931
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "552f300213a65ee0c8c773474d75b26b2d723575",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=3136a438-a076-4242-8e2f-d6595cfe",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/84d9fee0524e602c1d7529bf18279fc78486bdb0...552f300213a65ee0c8c773474d75b26b2d723575",
        "previous_git_commit": "84d9fee0524e602c1d7529bf18279fc78486bdb0",
        "previous_fingerprint": "3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:84d9fee@sha256:3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/84d9fee0524e602c1d7529bf18279fc78486bdb0",
        "previous_trail_name": "84d9fee0524e602c1d7529bf18279fc78486bdb0",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1262.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "552f300213a65ee0c8c773474d75b26b2d723575",
          "template_reference_name": "runner",
          "git_commit": "552f300213a65ee0c8c773474d75b26b2d723575",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575",
          "git_commit_info": {
            "sha1": "552f300213a65ee0c8c773474d75b26b2d723575",
            "message": "Merge pull request #260 from cyber-dojo/force-ci-run-134\n\nRun CI workflow to see if terraform runner-drift is created on aws-prod",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782962662.0,
            "url": "https://github.com/cyber-dojo/runner/commit/552f300213a65ee0c8c773474d75b26b2d723575"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=3136a438-a076-4242-8e2f-d6595cfe",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/84d9fee0524e602c1d7529bf18279fc78486bdb0...552f300213a65ee0c8c773474d75b26b2d723575",
            "previous_git_commit": "84d9fee0524e602c1d7529bf18279fc78486bdb0",
            "previous_fingerprint": "3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:84d9fee@sha256:3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/84d9fee0524e602c1d7529bf18279fc78486bdb0",
            "previous_trail_name": "84d9fee0524e602c1d7529bf18279fc78486bdb0",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1262.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-109",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=07a1ca37-ffef-4540-9fd9-372060d2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_fingerprint": "3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:84d9fee@sha256:3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_trail_name": "promotion-one-103",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 56816.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
          "template_reference_name": "runner",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=5a2885a8-1056-4277-887d-723eecec",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 164621.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073",
          "template_reference_name": "runner",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7bd902d1b29b1e30e88671422320ad4842bde74c6a7aea38d24d5c72954b2073?artifact_id=aa506591-16f1-425d-85ba-ea1bc1ef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:84d9fee@sha256:3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "runner-3f1c9f2a39bd7fa31e3cb453e5937e0c0e1cf43ba58e66423e459dfec74aa966",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 164621.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a1523927ec1b420f92580ca726371f54",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:665d6dd@sha256:961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
                    "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-108",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
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
      "fingerprint": "961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
      "creationTimestamp": [
        1782907144
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=5869dda9-7c8d-456f-a512-95c79667",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/a6e433a6fd3eb29c499b75310756420864b6c346...665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
        "previous_git_commit": "a6e433a6fd3eb29c499b75310756420864b6c346",
        "previous_fingerprint": "94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a6e433a@sha256:94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/a6e433a6fd3eb29c499b75310756420864b6c346",
        "previous_trail_name": "a6e433a6fd3eb29c499b75310756420864b6c346",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 924.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
          "template_reference_name": "nginx",
          "git_commit": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
          "git_commit_info": {
            "sha1": "665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
            "message": "Merge pull request #150 from cyber-dojo/run-workflow-146\n\nRun workflow to test changes to deployment pipeline",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1782906220.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/665d6dde5f736dbb33b5a0592fe49b5e577f4ecf"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=5869dda9-7c8d-456f-a512-95c79667",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/a6e433a6fd3eb29c499b75310756420864b6c346...665d6dde5f736dbb33b5a0592fe49b5e577f4ecf",
            "previous_git_commit": "a6e433a6fd3eb29c499b75310756420864b6c346",
            "previous_fingerprint": "94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a6e433a@sha256:94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/a6e433a6fd3eb29c499b75310756420864b6c346",
            "previous_trail_name": "a6e433a6fd3eb29c499b75310756420864b6c346",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 924.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-108",
          "template_reference_name": "nginx",
          "git_commit": "c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
          "git_commit_info": {
            "sha1": "c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
            "message": "Merge pull request #14 from cyber-dojo/add-back-checkout\n\nkosli-attest-decision requires a git repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782906897.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c03b1c05559f7bf6e23c890bcbddd6262f008ae9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=c3a0c40d-c27a-4195-a823-1e3e0db3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/935669068568593a9658781a56bb6cab5686e136...c03b1c05559f7bf6e23c890bcbddd6262f008ae9",
            "previous_git_commit": "935669068568593a9658781a56bb6cab5686e136",
            "previous_fingerprint": "94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a6e433a@sha256:94e9462c088ceb7baaf95799dc935277ad0c50b2a5d99f0d489bb7329dddf8c4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/935669068568593a9658781a56bb6cab5686e136",
            "previous_trail_name": "promotion-one-105",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 247.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
          "template_reference_name": "nginx",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=4d80a948-3f93-4c31-ae6f-727a684b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:7065268@sha256:b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "nginx-b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 107841.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098",
          "template_reference_name": "nginx",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/961d0b116ee6b2bc292e221c6a40d70a17383b9c315843dbb7ee9d2818d50098?artifact_id=0c896953-219d-45b0-886e-585ae595",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_fingerprint": "8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:66c0766@sha256:8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/d07d841723e4e524e4ea4d7dc8a7e60f0fc3349e",
            "previous_trail_name": "nginx-8bc44a90894de99aa76cd931ea42e2544b0727c5e3842ea57e4f08cace175ca9",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 107841.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/759ae63934ad4579ab7690f7133f68a2",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:ca386e0@sha256:133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
                    "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-106",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
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
      "fingerprint": "133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
      "creationTimestamp": [
        1782900828
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e5dd9397-3db0-4786-b854-e938e315",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/0867cd49ecfb556eb662e1942c500f0d4fc50bf4...ca386e022a6857ad4ea8cfcc765a574452555ac7",
        "previous_git_commit": "0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
        "previous_fingerprint": "edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:0867cd4@sha256:edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
        "previous_trail_name": "0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 2062.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
          "template_reference_name": "languages-start-points",
          "git_commit": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7",
          "git_commit_info": {
            "sha1": "ca386e022a6857ad4ea8cfcc765a574452555ac7",
            "message": "Merge pull request #236 from cyber-dojo/force-ci\n\nOne more force CI build",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782898766.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/ca386e022a6857ad4ea8cfcc765a574452555ac7"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e5dd9397-3db0-4786-b854-e938e315",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/0867cd49ecfb556eb662e1942c500f0d4fc50bf4...ca386e022a6857ad4ea8cfcc765a574452555ac7",
            "previous_git_commit": "0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
            "previous_fingerprint": "edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:0867cd4@sha256:edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
            "previous_trail_name": "0867cd49ecfb556eb662e1942c500f0d4fc50bf4",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2062.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-106",
          "template_reference_name": "languages-start-points",
          "git_commit": "935669068568593a9658781a56bb6cab5686e136",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/935669068568593a9658781a56bb6cab5686e136",
          "git_commit_info": {
            "sha1": "935669068568593a9658781a56bb6cab5686e136",
            "message": "Merge pull request #12 from cyber-dojo/put-template-back-to-generic\n\nPut template back to attestation of type generic",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782898702.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/935669068568593a9658781a56bb6cab5686e136"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=8180d5e2-b1e8-4aa8-ba83-c6f42c81",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/c1b1e0c943de88d31a15ba62466f4e9c6bd45259...935669068568593a9658781a56bb6cab5686e136",
            "previous_git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_fingerprint": "edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:0867cd4@sha256:edb1b94727eb135859997161077febbc2e6c9face4d82c4aeb43642f07e9480d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_trail_name": "promotion-one-100",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 2126.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
          "template_reference_name": "languages-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=8fca0a17-a7e4-4fd3-956c-4f8e5a2e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "languages-start-points-b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 101525.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e",
          "template_reference_name": "languages-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/133c8d845b2fc30950b720e0a308bf623c543c072727ebdce54876995a2cff1e?artifact_id=e9632a5f-0053-40a1-8c7d-248b552f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:bb8a712@sha256:5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "languages-start-points-5bc686a6794d6a180f3a70f815348627578982e951f16e7462b1b6f533a97f38",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 101525.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5dc5a4d24e0446afa8a6d3db69f459d3",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:17f61f8@sha256:edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
                    "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-101",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
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
      "fingerprint": "edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
      "creationTimestamp": [
        1782833760
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "17f61f83683a52ec1b9040127da582affb70e997",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=1157cd4a-b91c-4788-b572-22996ccd",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/88239b96c7bb1f0c99af688010f5aed4097ae7b4...17f61f83683a52ec1b9040127da582affb70e997",
        "previous_git_commit": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
        "previous_fingerprint": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4",
        "previous_trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 5700.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "17f61f83683a52ec1b9040127da582affb70e997",
          "template_reference_name": "exercises-start-points",
          "git_commit": "17f61f83683a52ec1b9040127da582affb70e997",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997",
          "git_commit_info": {
            "sha1": "17f61f83683a52ec1b9040127da582affb70e997",
            "message": "Merge pull request #139 from cyber-dojo/force-ci\n\nForce a CI run",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782828060.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/17f61f83683a52ec1b9040127da582affb70e997"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=1157cd4a-b91c-4788-b572-22996ccd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/88239b96c7bb1f0c99af688010f5aed4097ae7b4...17f61f83683a52ec1b9040127da582affb70e997",
            "previous_git_commit": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
            "previous_fingerprint": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/88239b96c7bb1f0c99af688010f5aed4097ae7b4",
            "previous_trail_name": "88239b96c7bb1f0c99af688010f5aed4097ae7b4",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 5700.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-101",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
          "git_commit_info": {
            "sha1": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "message": "Merge pull request #10 from cyber-dojo/deploy-differ-with-tf\n\nDeploy differ with the Kosli \"tf\" tooling",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782832173.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=2287a0a2-f493-497b-a77d-b7ac3fe7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:88239b9@sha256:34e5f0ce1ddbc2131d1142512871eebc5422ac74c4e36d56f4c0f7370f102781",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-27",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 1587.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=c170de5a-fd29-41dd-83cf-58f4dba5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "exercises-start-points-f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 34457.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/edb41a34c32f887de0e62aa5f7dc111f4efc1400d03f5bccc52f16533f51794e?artifact_id=660c6d60-6ce4-42a3-a4ed-44f76bf9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:75485ee@sha256:fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "exercises-start-points-fe536dd19b159d9cb43aaa09236d26c916906bd915c648991aa824fb2f69af58",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 34457.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a7e980a11b7c49f6afbabdf91fd46c2f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2a3119f@sha256:eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
                    "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-99",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
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
      "fingerprint": "eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
      "creationTimestamp": [
        1782831972
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/2a3119f72fa7bf62bbc83a3d48266120085d03ab",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33?artifact_id=08189ccd-6f3a-439e-99ca-e5abe3ee",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/0053b2e10ecb42e515c78b5d8b926c70ef3908b9...2a3119f72fa7bf62bbc83a3d48266120085d03ab",
        "previous_git_commit": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
        "previous_fingerprint": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
        "previous_trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 3937.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
          "template_reference_name": "creator",
          "git_commit": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/2a3119f72fa7bf62bbc83a3d48266120085d03ab",
          "git_commit_info": {
            "sha1": "2a3119f72fa7bf62bbc83a3d48266120085d03ab",
            "message": "Merge pull request #30 from cyber-dojo/force-ci\n\nForce a CI run",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1782828035.0,
            "url": "https://github.com/cyber-dojo/creator/commit/2a3119f72fa7bf62bbc83a3d48266120085d03ab"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33?artifact_id=08189ccd-6f3a-439e-99ca-e5abe3ee",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/0053b2e10ecb42e515c78b5d8b926c70ef3908b9...2a3119f72fa7bf62bbc83a3d48266120085d03ab",
            "previous_git_commit": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
            "previous_fingerprint": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
            "previous_trail_name": "0053b2e10ecb42e515c78b5d8b926c70ef3908b9",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 3937.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-99",
          "template_reference_name": "creator",
          "git_commit": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
          "git_commit_info": {
            "sha1": "c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "message": "Merge pull request #9 from cyber-dojo/deploy-saver-with-tf\n\nDeploy saver with the Kosli \"tf\" tooling",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782814107.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/c1b1e0c943de88d31a15ba62466f4e9c6bd45259"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33?artifact_id=a5ad20a0-26f2-4bab-bbea-25fd6659",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...c1b1e0c943de88d31a15ba62466f4e9c6bd45259",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:0053b2e@sha256:9514e7ca0904b3f585ac20163e34d53839262d7d3d44dac353c1ed1e7d7cb15b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-27",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 17865.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
          "template_reference_name": "creator",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33?artifact_id=270109e4-c54f-4467-9271-a8e81eef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:9034c75@sha256:4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "creator-4aaeb948517477d75c3077d5749e5c470e787b94f583b2cf95c22eb676c2fce6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 32669.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33",
          "template_reference_name": "creator",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/eff1499216faedf137034f80e4027afb552b37a681e83d9a556254bf65db9b33?artifact_id=5ea1c8b1-24e8-4cdf-a3bd-bbb8a1c6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:a288de5@sha256:e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "creator-e8b5e25c5550658cdbd2b8339684b18bce86aaf6538611124ff62f2582c2e5b6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 32669.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7ab9a6dcbbac4e78ac32c9cc3b55a944",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:5812bb5@sha256:e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
                    "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-102",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
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
      "fingerprint": "e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
      "creationTimestamp": [
        1782835716
      ],
      "pods": null,
      "annotation": {
        "type": "exited",
        "was": 1,
        "now": 0
      },
      "flow_name": "differ-ci",
      "git_commit": "5812bb564e572c9e33aef2789d2687f1a999a687",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/5812bb564e572c9e33aef2789d2687f1a999a687",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=b0c5a0c3-e982-43a4-b906-de850bf4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/6960ff7cc90425329e6def0adae4d5129dca9997...5812bb564e572c9e33aef2789d2687f1a999a687",
        "previous_git_commit": "6960ff7cc90425329e6def0adae4d5129dca9997",
        "previous_fingerprint": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997",
        "previous_trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 5231.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "5812bb564e572c9e33aef2789d2687f1a999a687",
          "template_reference_name": "differ",
          "git_commit": "5812bb564e572c9e33aef2789d2687f1a999a687",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/5812bb564e572c9e33aef2789d2687f1a999a687",
          "git_commit_info": {
            "sha1": "5812bb564e572c9e33aef2789d2687f1a999a687",
            "message": "Merge pull request #418 from cyber-dojo/adopt-tf\n\nSwitch deploys to kosli-dev/tf for drift detection",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "",
            "timestamp": 1782830485.0,
            "url": "https://github.com/cyber-dojo/differ/commit/5812bb564e572c9e33aef2789d2687f1a999a687"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=b0c5a0c3-e982-43a4-b906-de850bf4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/6960ff7cc90425329e6def0adae4d5129dca9997...5812bb564e572c9e33aef2789d2687f1a999a687",
            "previous_git_commit": "6960ff7cc90425329e6def0adae4d5129dca9997",
            "previous_fingerprint": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/6960ff7cc90425329e6def0adae4d5129dca9997",
            "previous_trail_name": "6960ff7cc90425329e6def0adae4d5129dca9997",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 5231.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-102",
          "template_reference_name": "differ",
          "git_commit": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
          "git_commit_info": {
            "sha1": "a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "message": "Merge pull request #10 from cyber-dojo/deploy-differ-with-tf\n\nDeploy differ with the Kosli \"tf\" tooling",
            "author": "Graham Savage <gsavage@users.noreply.github.com>",
            "branch": "main",
            "timestamp": 1782832173.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=7efcbd11-af63-4532-82b7-b9028200",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...a464ba86b9bfc5989075d85e6e3dc69e8cc3f16e",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:6960ff7@sha256:f3679107eb4cbe7a6a17b4c9b2b3d5f939f80c7fdc395e85755c10b2aee15f2a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-27",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 3543.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
          "template_reference_name": "differ",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=e9a0eb1d-506a-40fc-99ab-8efd2440",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/00c479764cb9eca038fdaaaef108672d0bb0ed26...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_trail_name": "differ-902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 36413.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1",
          "template_reference_name": "differ",
          "git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
          "git_commit_info": {
            "sha1": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "message": "Remove unneeded provenance decision attestation - this is not a build flow",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1782799303.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e0b800ffec04cd448529032a71423eaaecd86b2078b889df8eb7389fa8bebda1?artifact_id=e87fcb63-08b2-427f-8859-790c4307",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/c17bb3ed8862de03c1a491dfe790fd8734fc7071...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_fingerprint": "ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3e563ea@sha256:ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c17bb3ed8862de03c1a491dfe790fd8734fc7071",
            "previous_trail_name": "differ-ff893d25180aa091de68a42598a76286843ff8ff590c28dfbb62fd76cb0fcd38",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 36413.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/88ff9a0698874e6ca10c73065c9600d0",
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

