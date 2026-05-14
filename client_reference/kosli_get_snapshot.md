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
  "index": 4522,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1778779378.493324,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4522",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
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
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
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
      "fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
      "creationTimestamp": [
        1778779325
      ],
      "pods": null,
      "annotation": {
        "type": "started-compliant",
        "was": 0,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
        "previous_git_commit": "db53382650db8b7b3f216d0055009b0d77685677",
        "previous_fingerprint": "f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:db53382@sha256:f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677",
        "previous_trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 162785.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
          "template_reference_name": "languages-start-points",
          "git_commit": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
          "git_commit_info": {
            "sha1": "20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
            "message": "Merge pull request #207 from cyber-dojo/update-base-image-449676e\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778599614.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/20ff3f9f64b0d16c605ac58fa2d2d899545444aa"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=f06f3260-846f-4c9c-91f2-3947ba85",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/db53382650db8b7b3f216d0055009b0d77685677...20ff3f9f64b0d16c605ac58fa2d2d899545444aa",
            "previous_git_commit": "db53382650db8b7b3f216d0055009b0d77685677",
            "previous_fingerprint": "f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:db53382@sha256:f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/db53382650db8b7b3f216d0055009b0d77685677",
            "previous_trail_name": "db53382650db8b7b3f216d0055009b0d77685677",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 162785.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
          "template_reference_name": "languages-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=aaf907bf-5fae-4110-9bf9-9194bb65",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:db53382@sha256:f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promotion-one-45",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 516808.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
          "template_reference_name": "languages-start-points",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=a7566b5c-cb5f-47df-a6c5-4bcf08ed",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108169.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7?artifact_id=b1e0fdc0-3862-4af1-baea-299a8ce6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6510.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/03cda4ab5d474279b936452ca0dbd1f6",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ebab7f1@sha256:f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
                    "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
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
      "fingerprint": "f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
      "creationTimestamp": [
        1778762498,
        1778762500,
        1778762599
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b?artifact_id=d0649f4c-70a6-46f2-bfe3-0ce4d95c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e...ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
        "previous_git_commit": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
        "previous_fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
        "previous_trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 17174.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
          "template_reference_name": "runner",
          "git_commit": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
          "git_commit_info": {
            "sha1": "ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
            "message": "Merge pull request #232 from cyber-dojo/update-base-image-122de61\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778745324.0,
            "url": "https://github.com/cyber-dojo/runner/commit/ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b?artifact_id=d0649f4c-70a6-46f2-bfe3-0ce4d95c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e...ebab7f1d30aebb6cb5ad2f2905ac966c31f6ffef",
            "previous_git_commit": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
            "previous_fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
            "previous_trail_name": "81cfb0d451a3b4bcbf6d948d3f140ae016f5ab5e",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 17174.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
          "template_reference_name": "runner",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b?artifact_id=69b95d18-6d74-4932-95f7-2d4db3b5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/60fd5bffe45bc9618e81fabf8dd6793f92d10817...60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 108268.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
          "template_reference_name": "runner",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b?artifact_id=5f69b0d3-f8b8-4a76-9ad7-00c5219d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:81cfb0d@sha256:98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promotion-one-48",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 516907.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b",
          "template_reference_name": "runner",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f9082ed3b49b9b6fc2d2fae43a3cb04615db2275e26880ba7bf7b827120dc27b?artifact_id=81094a6c-cef6-4dc1-a145-1a35dea9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108268.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e5ce7ff262684944ae4e4067cf7242e4",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:4e30f2c@sha256:4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
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
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
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
      "fingerprint": "4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
      "creationTimestamp": [
        1778762483,
        1778762487,
        1778762571
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "4e30f2c13e5aedc4814360186742a689aba65f64",
      "commit_url": "https://github.com/cyber-dojo/web/commit/4e30f2c13e5aedc4814360186742a689aba65f64",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0?artifact_id=94db5f95-81ca-428d-bf02-16a3f3c6",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/59d0a20b8494a667e2eefff618395523a1bae4c6...4e30f2c13e5aedc4814360186742a689aba65f64",
        "previous_git_commit": "59d0a20b8494a667e2eefff618395523a1bae4c6",
        "previous_fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6",
        "previous_trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 88981.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "4e30f2c13e5aedc4814360186742a689aba65f64",
          "template_reference_name": "web",
          "git_commit": "4e30f2c13e5aedc4814360186742a689aba65f64",
          "commit_url": "https://github.com/cyber-dojo/web/commit/4e30f2c13e5aedc4814360186742a689aba65f64",
          "git_commit_info": {
            "sha1": "4e30f2c13e5aedc4814360186742a689aba65f64",
            "message": "Load CodeMirror 5.65.18 from CDN instead of bundling v5.21.0 (#339)\n\n* Load CodeMirror 5.65.18 from CDN instead of bundling v5.21.0\n\nRemoves ~18k lines of vendored JS and CSS; only the custom\ncyber-dojo output mode stays bundled. The makefile mode was\ndropped from CodeMirror in newer versions, so Makefile files\nnow use cmake syntax highlighting instead. The rust mode\nrequires addon/mode/simple, which is also loaded from CDN.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Delete dead docs/ file\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778673502.0,
            "url": "https://github.com/cyber-dojo/web/commit/4e30f2c13e5aedc4814360186742a689aba65f64"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0?artifact_id=94db5f95-81ca-428d-bf02-16a3f3c6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/59d0a20b8494a667e2eefff618395523a1bae4c6...4e30f2c13e5aedc4814360186742a689aba65f64",
            "previous_git_commit": "59d0a20b8494a667e2eefff618395523a1bae4c6",
            "previous_fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/59d0a20b8494a667e2eefff618395523a1bae4c6",
            "previous_trail_name": "59d0a20b8494a667e2eefff618395523a1bae4c6",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 88981.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0?artifact_id=4deb71ec-fe52-45e6-b817-3f435723",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-15",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 516892.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
          "template_reference_name": "web",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0?artifact_id=6f1f7593-f138-4c45-bd14-1613914b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108253.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4ec587aee0bbe5a491af075c545686f34c4efa5101dac087be0a8a5e8b2436d0?artifact_id=855be8b9-4caa-4568-bf59-0b6b968b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/badc2f94f69941514e5abeea74c9bc62f9207d49...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_fingerprint": "3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:59d0a20@sha256:3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_trail_name": "web-3304ad9c2912bf2b9228fc5051f2e21fd4635d2c6de409b9928d414f8bbe0705",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -6426.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d3d669b0d2c74293970dc7a1992ea773",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:fd71a71@sha256:dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
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
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
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
      "fingerprint": "dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
      "creationTimestamp": [
        1778762570
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b?artifact_id=4b01e92f-73e2-421d-9ab8-973ada3e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/30dffd09c3f896a322c65029247abcea3019c43a...fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
        "previous_git_commit": "30dffd09c3f896a322c65029247abcea3019c43a",
        "previous_fingerprint": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a",
        "previous_trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 161414.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
          "template_reference_name": "differ",
          "git_commit": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
          "git_commit_info": {
            "sha1": "fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
            "message": "Fix new empty file misclassified as renamed when another empty file e\u2026 (#376)\n\n* Fix new empty file misclassified as renamed when another empty file exists\n\ngit diff --find-copies-harder considers unmodified files as copy sources.\nSince all empty files share blob hash e69de29, adding a new empty file\nalongside an existing one causes git to emit copy from/to headers rather\nthan new file mode. The parser had no copy header handling, so it fell\nthrough to the old != new filename branch and returned :renamed.\n\nFix: replace --find-copies-harder with --find-renames in the git diff\ncommand (preserving rename detection, dropping copy detection), and add\na copy-header guard in parse_old_new_filenames as defence in depth.\n\n* Bump test metrics",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778601156.0,
            "url": "https://github.com/cyber-dojo/differ/commit/fd71a71146c5f8d0f83f2599b6acc4cd2664753c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b?artifact_id=4b01e92f-73e2-421d-9ab8-973ada3e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/30dffd09c3f896a322c65029247abcea3019c43a...fd71a71146c5f8d0f83f2599b6acc4cd2664753c",
            "previous_git_commit": "30dffd09c3f896a322c65029247abcea3019c43a",
            "previous_fingerprint": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/30dffd09c3f896a322c65029247abcea3019c43a",
            "previous_trail_name": "30dffd09c3f896a322c65029247abcea3019c43a",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 161414.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b?artifact_id=b1a92274-bae0-4b77-86ba-4cd507d4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:30dffd0@sha256:becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-11",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 516979.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
          "template_reference_name": "differ",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b?artifact_id=f073a97f-83a9-41a8-b93e-129217a8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108340.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b?artifact_id=b50533df-effc-46f5-8020-3ca89179",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6339.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f77e43ffb2e84fd78d67beeb7940d1df",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:42c8baf@sha256:e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
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
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
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
      "fingerprint": "e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
      "creationTimestamp": [
        1778762482
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/42c8bafd9e5f939070a775e87e86466f6e7497a8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a?artifact_id=bafb554f-b3a9-4789-8a68-e1fe74c0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/af7241f29969110655505267dc8ce7f9644fbf6a...42c8bafd9e5f939070a775e87e86466f6e7497a8",
        "previous_git_commit": "af7241f29969110655505267dc8ce7f9644fbf6a",
        "previous_fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a",
        "previous_trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 163533.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
          "template_reference_name": "saver",
          "git_commit": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/42c8bafd9e5f939070a775e87e86466f6e7497a8",
          "git_commit_info": {
            "sha1": "42c8bafd9e5f939070a775e87e86466f6e7497a8",
            "message": "Merge update-base-image into main (#369)\n\n* Dockerfile - Automated base-image update\n\n* Update test expected message after base image update\n\n* Bump test metrics after base image update\n\n---------\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778598949.0,
            "url": "https://github.com/cyber-dojo/saver/commit/42c8bafd9e5f939070a775e87e86466f6e7497a8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a?artifact_id=bafb554f-b3a9-4789-8a68-e1fe74c0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/af7241f29969110655505267dc8ce7f9644fbf6a...42c8bafd9e5f939070a775e87e86466f6e7497a8",
            "previous_git_commit": "af7241f29969110655505267dc8ce7f9644fbf6a",
            "previous_fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/af7241f29969110655505267dc8ce7f9644fbf6a",
            "previous_trail_name": "af7241f29969110655505267dc8ce7f9644fbf6a",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 163533.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a?artifact_id=42d7c06d-6b5e-4b41-9e0b-1f7564ef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-14",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 516891.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
          "template_reference_name": "saver",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a?artifact_id=2b954a95-a10c-48f0-9d73-7359c3a5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108252.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a?artifact_id=879f4816-ecf3-4559-82a9-78b86ad0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/badc2f94f69941514e5abeea74c9bc62f9207d49...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_fingerprint": "510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:af7241f@sha256:510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -6427.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/1a0da42cbb9b413fa8bf06fa4d166982",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f3cf3ba@sha256:f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
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
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
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
      "fingerprint": "f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
      "creationTimestamp": [
        1778762407
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4?artifact_id=0adb46ff-150c-40c8-bb65-2b088361",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/447231c2018bc0690735b4ee110ca46431162fd5...f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
        "previous_git_commit": "447231c2018bc0690735b4ee110ca46431162fd5",
        "previous_fingerprint": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5",
        "previous_trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 162797.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
          "template_reference_name": "exercises-start-points",
          "git_commit": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
          "git_commit_info": {
            "sha1": "f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
            "message": "Merge pull request #118 from cyber-dojo/update-base-image-449676e\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778599610.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4?artifact_id=0adb46ff-150c-40c8-bb65-2b088361",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/447231c2018bc0690735b4ee110ca46431162fd5...f3cf3ba6cc2630fc3cec74980db40abbb18bdfc6",
            "previous_git_commit": "447231c2018bc0690735b4ee110ca46431162fd5",
            "previous_fingerprint": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/447231c2018bc0690735b4ee110ca46431162fd5",
            "previous_trail_name": "447231c2018bc0690735b4ee110ca46431162fd5",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 162797.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
          "template_reference_name": "exercises-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4?artifact_id=3e1c03d5-75bf-4862-8ff7-9137bf18",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:447231c@sha256:691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-11",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 516816.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
          "template_reference_name": "exercises-start-points",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4?artifact_id=1d9c4d55-87d4-4c75-8279-37da88c7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108177.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4?artifact_id=4ace9edf-44fa-4406-b0c6-de3d9584",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6502.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e4f087ffa0bd4c00bb725292d3c79629",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:82ae3ae@sha256:08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
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
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
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
      "fingerprint": "08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
      "creationTimestamp": [
        1778762402
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408?artifact_id=0cc8202f-ee45-47a9-9676-d79408e4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/9dd6c657bc443c45c19e81165ff99286e237cfe3...82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
        "previous_git_commit": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
        "previous_fingerprint": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3",
        "previous_trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 162790.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
          "template_reference_name": "custom-start-points",
          "git_commit": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
          "git_commit_info": {
            "sha1": "82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
            "message": "Merge pull request #111 from cyber-dojo/update-base-image-449676e\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778599612.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/82ae3aee8f6b6c145cf50f6565815f1b125fbc6a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408?artifact_id=0cc8202f-ee45-47a9-9676-d79408e4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/9dd6c657bc443c45c19e81165ff99286e237cfe3...82ae3aee8f6b6c145cf50f6565815f1b125fbc6a",
            "previous_git_commit": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
            "previous_fingerprint": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/9dd6c657bc443c45c19e81165ff99286e237cfe3",
            "previous_trail_name": "9dd6c657bc443c45c19e81165ff99286e237cfe3",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 162790.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
          "template_reference_name": "custom-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408?artifact_id=7c2fbff4-1bb2-4690-ad87-04e68bf9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:9dd6c65@sha256:cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-11",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 516811.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
          "template_reference_name": "custom-start-points",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408?artifact_id=71cacde1-715e-4219-910a-1690c091",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108172.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/08bfc9f8c035a2a31de21aa11ca85a325e9b78afd0ab330a71f5a36e87bf3408?artifact_id=269faaca-9578-4295-93cc-5a708e41",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -6507.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/4570c79106df4e2ebb7efb45fe61acfe",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f5630da@sha256:6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
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
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
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
      "fingerprint": "6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
      "creationTimestamp": [
        1778762401
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f5630dab81ccd7e1a06cecdef60d903669964d3b",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8?artifact_id=9ff0d77b-f52e-4648-ac8b-b44f152a",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/89b113a1531ed1a88cd466d67a8e107ee88672d4...f5630dab81ccd7e1a06cecdef60d903669964d3b",
        "previous_git_commit": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
        "previous_fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4",
        "previous_trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 163447.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
          "template_reference_name": "dashboard",
          "git_commit": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f5630dab81ccd7e1a06cecdef60d903669964d3b",
          "git_commit_info": {
            "sha1": "f5630dab81ccd7e1a06cecdef60d903669964d3b",
            "message": "Dockerfile - Automated base-image update (#367)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778598954.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/f5630dab81ccd7e1a06cecdef60d903669964d3b"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8?artifact_id=9ff0d77b-f52e-4648-ac8b-b44f152a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/89b113a1531ed1a88cd466d67a8e107ee88672d4...f5630dab81ccd7e1a06cecdef60d903669964d3b",
            "previous_git_commit": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
            "previous_fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/89b113a1531ed1a88cd466d67a8e107ee88672d4",
            "previous_trail_name": "89b113a1531ed1a88cd466d67a8e107ee88672d4",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 163447.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8?artifact_id=3a55a12f-e6f4-42a1-9af2-d5044bf6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-14",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 516810.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
          "template_reference_name": "dashboard",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8?artifact_id=dfaade21-4b19-4d98-9d52-78a28b5d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108171.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6ee5825c950c4aa23f79f3b40c3f2b27e3c0717326910a0107bae256fd1b4af8?artifact_id=4c8ea330-5f34-46b6-a417-f77e0643",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/badc2f94f69941514e5abeea74c9bc62f9207d49...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_fingerprint": "ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:89b113a@sha256:ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/badc2f94f69941514e5abeea74c9bc62f9207d49",
            "previous_trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -6508.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a7dd4d86660d480da19e966bdc5c2742",
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
          "policy_name": "build-process"
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
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=d512c86e-fe78-49c4-a1c4-17ed3d34",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108167.0,
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41?artifact_id=48b062d0-b64b-46c5-89f6-9cf5627e",
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
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
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
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
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
      "fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
      "creationTimestamp": [
        1778762392
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "a275152a77724fb46bf388fc717447dcb206ae7a",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0?artifact_id=98d72c43-d90c-4d1a-992b-d3d03217",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/498bf29ef05ecc0986874ca8a8949fd2a39ad269...a275152a77724fb46bf388fc717447dcb206ae7a",
        "previous_git_commit": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
        "previous_fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269",
        "previous_trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 87659.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "a275152a77724fb46bf388fc717447dcb206ae7a",
          "template_reference_name": "nginx",
          "git_commit": "a275152a77724fb46bf388fc717447dcb206ae7a",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a",
          "git_commit_info": {
            "sha1": "a275152a77724fb46bf388fc717447dcb206ae7a",
            "message": "Merge pull request #118 from cyber-dojo/increase-kata-option-set-burst\n\nIncrease kata/option_set rate-limit burst from 3 to 4",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778674733.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/a275152a77724fb46bf388fc717447dcb206ae7a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0?artifact_id=98d72c43-d90c-4d1a-992b-d3d03217",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/498bf29ef05ecc0986874ca8a8949fd2a39ad269...a275152a77724fb46bf388fc717447dcb206ae7a",
            "previous_git_commit": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
            "previous_fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/498bf29ef05ecc0986874ca8a8949fd2a39ad269",
            "previous_trail_name": "498bf29ef05ecc0986874ca8a8949fd2a39ad269",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 87659.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-16",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0?artifact_id=fa3bbe88-4b8c-4fa0-96a6-32a4e2bb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-14",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 516801.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
          "template_reference_name": "nginx",
          "git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
          "git_commit_info": {
            "sha1": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "message": "Use workflow cronjob time that is not on the hour",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778654230.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0?artifact_id=cb829297-508f-4244-bfef-113e146e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 108162.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0?artifact_id=10aefee2-ea97-4ed7-9865-62af9c05",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/814567c5d116ba754a099604f0c8b8d93c735a10...4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_git_commit": "814567c5d116ba754a099604f0c8b8d93c735a10",
            "previous_fingerprint": "342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:498bf29@sha256:342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/814567c5d116ba754a099604f0c8b8d93c735a10",
            "previous_trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -6517.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/03b9e062a25345a9870d036d43e3ac28",
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

