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
  "index": 4608,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1779364918.4839022,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4608",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-56",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
      "creationTimestamp": [
        1779364862,
        1779364863,
        1779364863
      ],
      "pods": null,
      "annotation": {
        "type": "started-compliant",
        "was": 0,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a?artifact_id=eab81c14-3820-4a0c-a8d3-65562e1e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/eca92b4633994c93802e4f4c36ab50ba787f4c8c...8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
        "previous_git_commit": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
        "previous_fingerprint": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/eca92b4633994c93802e4f4c36ab50ba787f4c8c",
        "previous_trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1400.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
          "template_reference_name": "runner",
          "git_commit": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
          "git_commit_info": {
            "sha1": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
            "message": "Merge pull request #236 from cyber-dojo/update-base-image-fbde77b\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779363462.0,
            "url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a?artifact_id=eab81c14-3820-4a0c-a8d3-65562e1e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/eca92b4633994c93802e4f4c36ab50ba787f4c8c...8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
            "previous_git_commit": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
            "previous_fingerprint": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/eca92b4633994c93802e4f4c36ab50ba787f4c8c",
            "previous_trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1400.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-56",
          "template_reference_name": "runner",
          "git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
          "git_commit_info": {
            "sha1": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "message": "Bump kosli/setup-cli-action to v5, use latest version",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779364424.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a?artifact_id=53b36a85-2a5c-471a-8ed5-651f0f72",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 438.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f83d7cee61ad4f7ab98ec29f344c6640",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
      "creationTimestamp": [
        1779361878
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "a300e4c15cff321ef952a60bbc3a4729772a2419",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=c8203f7c-be6e-49c7-8386-755b1efa",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/3f0c4e5a2578865b68f0486f0284f52013a038f6...a300e4c15cff321ef952a60bbc3a4729772a2419",
        "previous_git_commit": "3f0c4e5a2578865b68f0486f0284f52013a038f6",
        "previous_fingerprint": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/3f0c4e5a2578865b68f0486f0284f52013a038f6",
        "previous_trail_name": "3f0c4e5a2578865b68f0486f0284f52013a038f6",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 81649.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
          "template_reference_name": "custom-start-points",
          "git_commit": "a300e4c15cff321ef952a60bbc3a4729772a2419",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419",
          "git_commit_info": {
            "sha1": "a300e4c15cff321ef952a60bbc3a4729772a2419",
            "message": "Merge pull request #115 from cyber-dojo/update-base-image-4faa754\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779280229.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=c8203f7c-be6e-49c7-8386-755b1efa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/3f0c4e5a2578865b68f0486f0284f52013a038f6...a300e4c15cff321ef952a60bbc3a4729772a2419",
            "previous_git_commit": "3f0c4e5a2578865b68f0486f0284f52013a038f6",
            "previous_fingerprint": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/3f0c4e5a2578865b68f0486f0284f52013a038f6",
            "previous_trail_name": "3f0c4e5a2578865b68f0486f0284f52013a038f6",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 81649.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
          "template_reference_name": "custom-start-points",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=a990c6d0-aecb-4409-90cc-6cd637bd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "custom-start-points-dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 592969.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "custom-start-points",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=d767d31e-0773-4d2a-a56a-5b06adb0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/74d0c8b5741f72064070019ada1dbe4150ca7ebe...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_fingerprint": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_trail_name": "promote-all-17",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 246753.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2fe7c2743a7e4e2b9abccf5f49ee7941",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
      "creationTimestamp": [
        1779361530,
        1779361539,
        1779361600
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
      "commit_url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4?artifact_id=b745e3de-b475-495d-8c9d-f2e2c9d6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/aad3b92b0be2cc2d47af89ec04266ae4a7f4617b...a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
        "previous_git_commit": "aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
        "previous_fingerprint": "24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aad3b92@sha256:24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
        "previous_trail_name": "aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 81858.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
          "template_reference_name": "web",
          "git_commit": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
          "commit_url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
          "git_commit_info": {
            "sha1": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
            "message": "Dockerfile - Automated base-image update (#347)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779279672.0,
            "url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4?artifact_id=b745e3de-b475-495d-8c9d-f2e2c9d6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/aad3b92b0be2cc2d47af89ec04266ae4a7f4617b...a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
            "previous_git_commit": "aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
            "previous_fingerprint": "24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aad3b92@sha256:24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
            "previous_trail_name": "aad3b92b0be2cc2d47af89ec04266ae4a7f4617b",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 81858.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
          "template_reference_name": "web",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4?artifact_id=bbc77b93-daca-4296-ac3a-3cdf0125",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:4e30f2c@sha256:4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 592621.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "web",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4?artifact_id=872adbfe-6f19-481b-aba7-b315d72d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/74d0c8b5741f72064070019ada1dbe4150ca7ebe...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_fingerprint": "24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:aad3b92@sha256:24c87824172df05e224bd81adb42f721e9b84bc3b5565942d6e08780599daeec",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_trail_name": "promote-all-17",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 246405.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f160a139d55e4487b712638c105c8194",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:75e174e@sha256:68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
      "creationTimestamp": [
        1779361531
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d?artifact_id=1393a075-7f06-4128-9661-52a0664a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/09cbd7ae7b5269b4c55c5e53a0b563d938e656ef...75e174eb5045e8dd5c72079d2e2032a1488c51ef",
        "previous_git_commit": "09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
        "previous_fingerprint": "a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:09cbd7a@sha256:a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
        "previous_trail_name": "09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 15543.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
          "template_reference_name": "differ",
          "git_commit": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef",
          "git_commit_info": {
            "sha1": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
            "message": "Fix Docker cleanup, extract slow-tests reporter, set Puma workers to nprocessors (#385)\n\ncontainers_down now force-removes all containers across all projects, so\nports held by containers from other compose projects (e.g. saver from\ncyber-dojo/web) no longer block test runs. run_tests.sh calls\ncontainers_down at startup so 'make test_server' is self-contained.\n\nSlow-test timing extracted into a dedicated SlowTestsReporter class,\nmatching the pattern already used in cyber-dojo/saver.\n\nPuma configured to spawn one worker per CPU core via Etc.nprocessors.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779345988.0,
            "url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d?artifact_id=1393a075-7f06-4128-9661-52a0664a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/09cbd7ae7b5269b4c55c5e53a0b563d938e656ef...75e174eb5045e8dd5c72079d2e2032a1488c51ef",
            "previous_git_commit": "09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
            "previous_fingerprint": "a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:09cbd7a@sha256:a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
            "previous_trail_name": "09cbd7ae7b5269b4c55c5e53a0b563d938e656ef",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 15543.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "differ",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d?artifact_id=ff3b5589-c362-4b1a-a8e3-604d7d5b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/74d0c8b5741f72064070019ada1dbe4150ca7ebe...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_fingerprint": "a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:09cbd7a@sha256:a90ec8fe19017df7d196d235a5e18fc7b42536fce144aaf297a88d39b15a2ab9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_trail_name": "promote-all-17",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 246406.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/583a929a8ea442b8af7bdc9335b3264f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
      "creationTimestamp": [
        1779361527
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=e5eb4b27-0e03-408b-983c-52631c22",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/a644975af4c0f7aa595bea651b4d9846cb747cd1...545cccbc91f4030fb4004421e1076bd7c2abbc93",
        "previous_git_commit": "a644975af4c0f7aa595bea651b4d9846cb747cd1",
        "previous_fingerprint": "80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:a644975@sha256:80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/a644975af4c0f7aa595bea651b4d9846cb747cd1",
        "previous_trail_name": "a644975af4c0f7aa595bea651b4d9846cb747cd1",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 81303.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
          "template_reference_name": "exercises-start-points",
          "git_commit": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
          "git_commit_info": {
            "sha1": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
            "message": "Merge pull request #123 from cyber-dojo/update-base-image-4faa754\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779280224.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=e5eb4b27-0e03-408b-983c-52631c22",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/a644975af4c0f7aa595bea651b4d9846cb747cd1...545cccbc91f4030fb4004421e1076bd7c2abbc93",
            "previous_git_commit": "a644975af4c0f7aa595bea651b4d9846cb747cd1",
            "previous_fingerprint": "80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:a644975@sha256:80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/a644975af4c0f7aa595bea651b4d9846cb747cd1",
            "previous_trail_name": "a644975af4c0f7aa595bea651b4d9846cb747cd1",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 81303.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
          "template_reference_name": "exercises-start-points",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=2738decb-5d4a-4747-a349-2abd7b72",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:49dc284@sha256:3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "exercises-start-points-3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 592618.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "exercises-start-points",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=674d8605-a6ff-4f55-a99e-dc1e10f5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:a644975@sha256:80511ff4acdf84df7ae47831e5be885522274957b46eb323fee7aada95985aa3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promotion-one-53",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 246402.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/8cb257df3f4e4ea1ba94d41abf21e638",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
      "creationTimestamp": [
        1779361526
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534?artifact_id=1ab21e30-b72a-4b81-96f2-2c88ca7c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/39b850a3d527c047dab963bbaa396a14b644ffa1...e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
        "previous_git_commit": "39b850a3d527c047dab963bbaa396a14b644ffa1",
        "previous_fingerprint": "fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:39b850a@sha256:fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/39b850a3d527c047dab963bbaa396a14b644ffa1",
        "previous_trail_name": "39b850a3d527c047dab963bbaa396a14b644ffa1",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 11827.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
          "template_reference_name": "saver",
          "git_commit": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
          "git_commit_info": {
            "sha1": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
            "message": "Avoid per-request flock overhead by detecting concurrent writes at the git layer (#380)\n\nThe OS-level flock in app_base penalised every POST with three filesystem\noperations (mkdir_p, file open, flock) to guard against rare concurrent\nout-of-sync events. The git merge --ff-only in kata_v2 already provides\nthe same protection: only one concurrent write can fast-forward merge. The\nnew rescue in worktree_commit detects the merge failure and raises\n\"Out of order event\" when events.json confirms another write succeeded first.\nSequential stale-index events are still caught by the existing index check\nbefore any git work is done.\n\nAlso extracts worktree_commit from git_commit_tag_sss for clarity, and\nremoves flock-specific tests that no longer have code to cover.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779349699.0,
            "url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534?artifact_id=1ab21e30-b72a-4b81-96f2-2c88ca7c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/39b850a3d527c047dab963bbaa396a14b644ffa1...e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
            "previous_git_commit": "39b850a3d527c047dab963bbaa396a14b644ffa1",
            "previous_fingerprint": "fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:39b850a@sha256:fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/39b850a3d527c047dab963bbaa396a14b644ffa1",
            "previous_trail_name": "39b850a3d527c047dab963bbaa396a14b644ffa1",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 11827.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "saver",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534?artifact_id=f89d4c07-f6c2-48f9-b329-c8544edd",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/74d0c8b5741f72064070019ada1dbe4150ca7ebe...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_fingerprint": "fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:39b850a@sha256:fbaa777ff7fd22760d125775fd682dc6c5afe90839c595f35601f838654e02a9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_trail_name": "promote-all-17",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 246401.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e219532d5e5e47cbaebd512f21ca1838",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
      "creationTimestamp": [
        1779361516
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "16d155bdd120fe5a926504069dd18a98b8275fa8",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=ca3a337f-0625-4fa1-a39e-f5e9fcf1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/02db0daf31f1a59d795a53b8f31c1e33e26e2475...16d155bdd120fe5a926504069dd18a98b8275fa8",
        "previous_git_commit": "02db0daf31f1a59d795a53b8f31c1e33e26e2475",
        "previous_fingerprint": "3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:02db0da@sha256:3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/02db0daf31f1a59d795a53b8f31c1e33e26e2475",
        "previous_trail_name": "02db0daf31f1a59d795a53b8f31c1e33e26e2475",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 81290.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
          "template_reference_name": "languages-start-points",
          "git_commit": "16d155bdd120fe5a926504069dd18a98b8275fa8",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
          "git_commit_info": {
            "sha1": "16d155bdd120fe5a926504069dd18a98b8275fa8",
            "message": "Merge pull request #213 from cyber-dojo/update-base-image-4faa754\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779280226.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=ca3a337f-0625-4fa1-a39e-f5e9fcf1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/02db0daf31f1a59d795a53b8f31c1e33e26e2475...16d155bdd120fe5a926504069dd18a98b8275fa8",
            "previous_git_commit": "02db0daf31f1a59d795a53b8f31c1e33e26e2475",
            "previous_fingerprint": "3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:02db0da@sha256:3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/02db0daf31f1a59d795a53b8f31c1e33e26e2475",
            "previous_trail_name": "02db0daf31f1a59d795a53b8f31c1e33e26e2475",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 81290.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
          "template_reference_name": "languages-start-points",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=46e807c2-8271-446f-b1ff-4ac4c24e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 592607.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "languages-start-points",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=818f6b50-553a-465f-a8ac-b11e5d91",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:02db0da@sha256:3c29b82d698d9f1a395647fdd3e113e760d0b1cf7a49e58f82955cf2f99edc6c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promotion-one-54",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 246391.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/27516a6e0f704dd0a4ccf20e2b5f72cc",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:18fb270@sha256:e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-55",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
      "creationTimestamp": [
        1779309324
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "18fb2702a5109248489b8a562399101f803b3d8d",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78?artifact_id=83608343-1dc4-4c06-905b-65079665",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/9cd9145fb82307891749144f4394b5ae2cde287c...18fb2702a5109248489b8a562399101f803b3d8d",
        "previous_git_commit": "9cd9145fb82307891749144f4394b5ae2cde287c",
        "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/9cd9145fb82307891749144f4394b5ae2cde287c",
        "previous_trail_name": "9cd9145fb82307891749144f4394b5ae2cde287c",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 1073.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
          "template_reference_name": "dashboard",
          "git_commit": "18fb2702a5109248489b8a562399101f803b3d8d",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d",
          "git_commit_info": {
            "sha1": "18fb2702a5109248489b8a562399101f803b3d8d",
            "message": "Restore avatar column to left alignment (#380)\n\nRemoving display:inline-block in #376 meant margin:auto started\ncentering the table horizontally. Dropping margin:auto lets the\ntable sit at the left edge as it did before.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779308251.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78?artifact_id=83608343-1dc4-4c06-905b-65079665",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/9cd9145fb82307891749144f4394b5ae2cde287c...18fb2702a5109248489b8a562399101f803b3d8d",
            "previous_git_commit": "9cd9145fb82307891749144f4394b5ae2cde287c",
            "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/9cd9145fb82307891749144f4394b5ae2cde287c",
            "previous_trail_name": "9cd9145fb82307891749144f4394b5ae2cde287c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 1073.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-55",
          "template_reference_name": "dashboard",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78?artifact_id=4ec47328-b987-4c17-a876-61718b26",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/74d0c8b5741f72064070019ada1dbe4150ca7ebe...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_trail_name": "promote-all-17",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 194199.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
          "template_reference_name": "dashboard",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78?artifact_id=50e75bc9-b13e-4543-8cf3-bdfdeedc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 540415.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
          "template_reference_name": "dashboard",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78?artifact_id=db045ae1-0393-4591-9787-0a6f3cb4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "dashboard-ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 540415.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c0e251c28c9b411babacacd7a6b33599",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:8c3fc7c@sha256:8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-17",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
      "creationTimestamp": [
        1779114165
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3?artifact_id=c1fb3437-795c-4423-b082-339e55a0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/a275152a77724fb46bf388fc717447dcb206ae7a...8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
        "previous_git_commit": "a275152a77724fb46bf388fc717447dcb206ae7a",
        "previous_fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a",
        "previous_trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 21853.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
          "template_reference_name": "nginx",
          "git_commit": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
          "git_commit_info": {
            "sha1": "8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
            "message": "Merge pull request #122 from cyber-dojo/raise-kata-file-edit-rate-limit\n\nRaise kata_file_edit burst limit from 3 to 10",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779092312.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3?artifact_id=c1fb3437-795c-4423-b082-339e55a0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/a275152a77724fb46bf388fc717447dcb206ae7a...8c3fc7c5fd507a5f5af2cd795c8b0a6cd3532f98",
            "previous_git_commit": "a275152a77724fb46bf388fc717447dcb206ae7a",
            "previous_fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a",
            "previous_trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 21853.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-17",
          "template_reference_name": "nginx",
          "git_commit": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe",
          "git_commit_info": {
            "sha1": "74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "message": "Restore accidentally deleted sdlc-control-gate from deployment jobs",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778866079.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/74d0c8b5741f72064070019ada1dbe4150ca7ebe"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3?artifact_id=32172370-58c3-458a-95ce-ac538284",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...74d0c8b5741f72064070019ada1dbe4150ca7ebe",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-16",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 248086.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
          "template_reference_name": "nginx",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3?artifact_id=3e68a75b-88ba-4a07-a9f5-a308a3d0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 345256.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3",
          "template_reference_name": "nginx",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/8af37e66006d491a96f23b5118d30ed933f7f090d873c80618920772096974a3?artifact_id=1018cbc0-dfcc-4b1c-9c9d-3504502a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 345256.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9f01497da0dd42e1b76ede246742c912",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-16",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
      "creationTimestamp": [
        1778762397
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
      "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=cf2e83f9-6605-43d2-9d16-b43e9df6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/b3152a10de1f36b7dbe2818c0918af06fd3aca61...dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
        "previous_git_commit": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "previous_fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "previous_trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 1476.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
          "template_reference_name": "creator",
          "git_commit": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
          "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
          "git_commit_info": {
            "sha1": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
            "message": "Merge branch 'fix-junit-reporting-ruby4' into 'main'\n\nFix JUnit reporting broken by Ruby 4 upgrade; suppress Docker hints\n\nSee merge request cyber-dojo/creator!247",
            "author": "Jon Jagger <jon@jaggersoft.com>",
            "branch": "main",
            "timestamp": 1778760921.0,
            "url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=cf2e83f9-6605-43d2-9d16-b43e9df6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/b3152a10de1f36b7dbe2818c0918af06fd3aca61...dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
            "previous_git_commit": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
            "previous_fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/b3152a10de1f36b7dbe2818c0918af06fd3aca61",
            "previous_trail_name": "b3152a10de1f36b7dbe2818c0918af06fd3aca61",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1476.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=c599f3fb-70e7-40b2-9f73-77accb3f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-14",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 516806.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
          "template_reference_name": "creator",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=62c4d19f-6b81-42ce-addf-9b6e57cc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6512.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
          "template_reference_name": "creator",
          "git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
          "git_commit_info": {
            "sha1": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "message": "Show critical vulnerabilities first in the GitHub step summary\n\nReorder SEVERITY_ORDER from [low, medium, high, critical] to\n[critical, high, medium, low] so the most severe findings appear\nat the top of each environment's step summary table. Update the\nfour stale test fixture files to match the current per-severity\nformat (the fixtures had drifted to a prior per-artifact format).\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778768909.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=f8521f25-1f12-4489-bccf-1c5fa876",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/60fd5bffe45bc9618e81fabf8dd6793f92d10817...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_fingerprint": "4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b3152a1@sha256:4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -6512.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/68464f809bc34a068ab4818bada7117e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:eca92b4@sha256:91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
                  }
                }
              ]
            }
          ],
          "policy_name": "trail-compliance"
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": "COMPLIANT"
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
                  "must_be_compliant": true
                }
              },
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d",
      "creationTimestamp": [
        1779361866,
        1779361871,
        1779361872
      ],
      "pods": null,
      "annotation": {
        "type": "exited",
        "was": 3,
        "now": 0
      },
      "flow_name": "runner-ci",
      "git_commit": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/eca92b4633994c93802e4f4c36ab50ba787f4c8c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d?artifact_id=78130d2f-c749-4273-b6a4-5b81264b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/ff9225b7868a17e9c98f3a714763ebd78bbc9019...eca92b4633994c93802e4f4c36ab50ba787f4c8c",
        "previous_git_commit": "ff9225b7868a17e9c98f3a714763ebd78bbc9019",
        "previous_fingerprint": "1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ff9225b@sha256:1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ff9225b7868a17e9c98f3a714763ebd78bbc9019",
        "previous_trail_name": "ff9225b7868a17e9c98f3a714763ebd78bbc9019",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 1890.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
          "template_reference_name": "runner",
          "git_commit": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/eca92b4633994c93802e4f4c36ab50ba787f4c8c",
          "git_commit_info": {
            "sha1": "eca92b4633994c93802e4f4c36ab50ba787f4c8c",
            "message": "Merge pull request #235 from cyber-dojo/slow-tests-reporter-and-platform-fixes\n\nSlow tests reporter and platform fixes",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779359976.0,
            "url": "https://github.com/cyber-dojo/runner/commit/eca92b4633994c93802e4f4c36ab50ba787f4c8c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d?artifact_id=78130d2f-c749-4273-b6a4-5b81264b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/ff9225b7868a17e9c98f3a714763ebd78bbc9019...eca92b4633994c93802e4f4c36ab50ba787f4c8c",
            "previous_git_commit": "ff9225b7868a17e9c98f3a714763ebd78bbc9019",
            "previous_fingerprint": "1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ff9225b@sha256:1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/ff9225b7868a17e9c98f3a714763ebd78bbc9019",
            "previous_trail_name": "ff9225b7868a17e9c98f3a714763ebd78bbc9019",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 1890.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-18",
          "template_reference_name": "runner",
          "git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
          "git_commit_info": {
            "sha1": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "message": "Restore approve jobs without the deprecated kosli-report-approval step\n\nThe manual GitHub approval gate (environment: name: production) was\naccidentally removed along with the Kosli reporting step. This restores\nthe approve jobs with just the environment gate, and drops setup from\neach job's needs since it no longer references setup's outputs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779115125.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/91cbaa165d3b36fdf251114906b7c8dbc96356334d65851bb5e0c673ad68094d?artifact_id=49d13da0-ad5b-40c5-b7fe-5f713a8a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/cd10b07c778a554edf81b7c04d283858b8651769...5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_git_commit": "cd10b07c778a554edf81b7c04d283858b8651769",
            "previous_fingerprint": "1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ff9225b@sha256:1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/cd10b07c778a554edf81b7c04d283858b8651769",
            "previous_trail_name": "promotion-one-52",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 246741.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f6b8572b2dd74c218464003706c9a78a",
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
              "must_be_compliant": true
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
      "id": "5da6b9e4-a7ca-4e01-b956-f1230198",
      "name": "trail-compliance",
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
              "must_be_compliant": true
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

