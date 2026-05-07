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
|    -h, --help  |  help for snapshot  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy http://proxy-server-ip:proxy-port  |  [optional] The HTTP proxy URL including protocol and port number. e.g. http://proxy-server-ip:proxy-port  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


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
  "index": 4366,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1778128438.445219,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4366",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:a2ffba5@sha256:b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
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
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
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
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
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
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-12",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
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
      "fingerprint": "b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
      "creationTimestamp": [
        1777550805,
        1777550806,
        1777550809
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=fe3ed5e5-0ed1-4cb8-8d5a-57d636d7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/bcf912346ae0a104698da4560e82d5eb277fc0e9...a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
        "previous_git_commit": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
        "previous_fingerprint": "0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bcf9123@sha256:0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bcf912346ae0a104698da4560e82d5eb277fc0e9",
        "previous_trail_name": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 3201.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
          "template_reference_name": "runner",
          "git_commit": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
          "git_commit_info": {
            "sha1": "a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
            "message": "Merge pull request #227 from cyber-dojo/update-base-image-5412310\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777547604.0,
            "url": "https://github.com/cyber-dojo/runner/commit/a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=fe3ed5e5-0ed1-4cb8-8d5a-57d636d7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/bcf912346ae0a104698da4560e82d5eb277fc0e9...a2ffba5a5debbc8f4f199cf5a88e5899c7d6547e",
            "previous_git_commit": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
            "previous_fingerprint": "0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bcf9123@sha256:0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/bcf912346ae0a104698da4560e82d5eb277fc0e9",
            "previous_trail_name": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 3201.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-12",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=a28dcf25-ff8e-40f5-8adc-c24b10ef",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1a3f516ca3da64bb329c5447dddc8c58751ec82b...1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_git_commit": "1a3f516ca3da64bb329c5447dddc8c58751ec82b",
            "previous_fingerprint": "0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bcf9123@sha256:0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1a3f516ca3da64bb329c5447dddc8c58751ec82b",
            "previous_trail_name": "promotion-one-42",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 188812.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
          "template_reference_name": "runner",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=9a789764-d559-46c7-945f-dd414e03",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -64130.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "runner-b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039",
          "template_reference_name": "runner",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/b6df6b1da5f73049085d9e04549f9674f0e54e9f0273467db9d7b46e3e9ad039?artifact_id=038ea0a7-e29d-4f1e-b505-79447d8a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7e307436bf47f2ce550e8e86838f4993b385de5c...117e18e0cb1eab30b9747ece58327eabfc595b90",
            "previous_git_commit": "7e307436bf47f2ce550e8e86838f4993b385de5c",
            "previous_fingerprint": "0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bcf9123@sha256:0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7e307436bf47f2ce550e8e86838f4993b385de5c",
            "previous_trail_name": "runner-0ef17bb0750a014fffa6cc419feb5b69774db08f18a354a39b552a5b1e785f98",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -64130.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/bb5a7256bb4445b9821ff8e6e3cf0a86",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
              "satisfied": true,
              "ignored": false,
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
        "type": "unchanged",
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
          "flow_name": "snyk-vulns-aws-prod",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=7037421b-6bc3-4370-86e5-34d83a36",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": 466202.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=d58e2fcc-a224-47de-8c1b-4fc7bdbb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": 466202.0,
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
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
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
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
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
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
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
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-13",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
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
      "fingerprint": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
      "creationTimestamp": [
        1777842904,
        1777842905,
        1777842905
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "1999d1303424879336b04fa3310256554aa6cfa6",
      "commit_url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=359b4539-989d-48f5-88eb-8a553baf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98...1999d1303424879336b04fa3310256554aa6cfa6",
        "previous_git_commit": "23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
        "previous_fingerprint": "3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:23d6f24@sha256:3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
        "previous_trail_name": "23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 1241.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
          "template_reference_name": "web",
          "git_commit": "1999d1303424879336b04fa3310256554aa6cfa6",
          "commit_url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6",
          "git_commit_info": {
            "sha1": "1999d1303424879336b04fa3310256554aa6cfa6",
            "message": "Enable CSRF token enforcement on POST requests (Phase 2) (#306)\n\nPhase 1 (deployed April 14) set the csrf_token cookie on all responses.\nPhase 2 enables the enforcement check that was left commented out pending\nall users reloading. Adds a global jQuery ajaxSend hook so all POST\nrequests automatically include the token, and updates the controller test\nbase to seed the cookie and merge the token into POST params.\n\nUsers with a kata page open before this deploy will get one 403 on their\nnext test run; reloading the page picks up the new JS and self-heals.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1777841663.0,
            "url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=359b4539-989d-48f5-88eb-8a553baf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98...1999d1303424879336b04fa3310256554aa6cfa6",
            "previous_git_commit": "23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
            "previous_fingerprint": "3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:23d6f24@sha256:3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
            "previous_trail_name": "23d6f24c36ffdf1210e3556a1f4d1d6b35cfdf98",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1241.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-13",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=a34a55d8-2118-49ac-8899-aa2b6306",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:23d6f24@sha256:3302e9aee07946df391e246572cda3ea64de480c92d7f598c3e6ead9cb5e3020",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promote-all-12",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 480911.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=70de9485-fbcc-4d37-a744-546c44ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": 227969.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "web-541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180?artifact_id=d6d28b90-e930-4451-bb36-13e65471",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": 227969.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9560296ee7a54a18afe27e41c76be7c5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:a6ece2b@sha256:3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
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
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
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
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
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
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
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
      "fingerprint": "3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
      "creationTimestamp": [
        1776923862
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=1281066d-38ba-432c-92c2-f3d7003e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/632127a7f162ad1ac02305a2940888264034364b...a6ece2b597888f7ab149759daadda08e3afab0c1",
        "previous_git_commit": "632127a7f162ad1ac02305a2940888264034364b",
        "previous_fingerprint": "a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:632127a@sha256:a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/632127a7f162ad1ac02305a2940888264034364b",
        "previous_trail_name": "632127a7f162ad1ac02305a2940888264034364b",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 2577.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "a6ece2b597888f7ab149759daadda08e3afab0c1",
          "template_reference_name": "dashboard",
          "git_commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1",
          "git_commit_info": {
            "sha1": "a6ece2b597888f7ab149759daadda08e3afab0c1",
            "message": "Remove defaulted aws-rolename from snyk-scanning job (#363)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776921285.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/a6ece2b597888f7ab149759daadda08e3afab0c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=1281066d-38ba-432c-92c2-f3d7003e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/632127a7f162ad1ac02305a2940888264034364b...a6ece2b597888f7ab149759daadda08e3afab0c1",
            "previous_git_commit": "632127a7f162ad1ac02305a2940888264034364b",
            "previous_fingerprint": "a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:632127a@sha256:a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/632127a7f162ad1ac02305a2940888264034364b",
            "previous_trail_name": "632127a7f162ad1ac02305a2940888264034364b",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 2577.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=2acc6089-d810-49af-a10f-ff262a82",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:632127a@sha256:a03cce86f5958febc442665846863ab9701456d766e76ad3816f3f00a971d850",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-10",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 824607.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=5be0f361-8a6d-4e2d-a7d7-d07cf99d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691073.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=7bf8e775-a41e-4128-bcab-cf0a3461",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691073.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/0993e7a4118e4a7699ad6eb9c06a4b47",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:92c0996@sha256:1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
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
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
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
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
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
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
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
      "fingerprint": "1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
      "creationTimestamp": [
        1776923549
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/92c0996cd9ae7642eb0769f928abe6cb6c391751",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=3666aa1b-a19b-4ab5-a625-fa6afa9d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/0b77a6402320cd10c30cf5bbf6486aa1a448443a...92c0996cd9ae7642eb0769f928abe6cb6c391751",
        "previous_git_commit": "0b77a6402320cd10c30cf5bbf6486aa1a448443a",
        "previous_fingerprint": "5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:0b77a64@sha256:5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/0b77a6402320cd10c30cf5bbf6486aa1a448443a",
        "previous_trail_name": "0b77a6402320cd10c30cf5bbf6486aa1a448443a",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 2075.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
          "template_reference_name": "saver",
          "git_commit": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/92c0996cd9ae7642eb0769f928abe6cb6c391751",
          "git_commit_info": {
            "sha1": "92c0996cd9ae7642eb0769f928abe6cb6c391751",
            "message": "Remove defaulted aws-rolename from snyk-scanning job (#364)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776921474.0,
            "url": "https://github.com/cyber-dojo/saver/commit/92c0996cd9ae7642eb0769f928abe6cb6c391751"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=3666aa1b-a19b-4ab5-a625-fa6afa9d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/0b77a6402320cd10c30cf5bbf6486aa1a448443a...92c0996cd9ae7642eb0769f928abe6cb6c391751",
            "previous_git_commit": "0b77a6402320cd10c30cf5bbf6486aa1a448443a",
            "previous_fingerprint": "5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:0b77a64@sha256:5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/0b77a6402320cd10c30cf5bbf6486aa1a448443a",
            "previous_trail_name": "0b77a6402320cd10c30cf5bbf6486aa1a448443a",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 2075.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=572576fd-b54a-4556-b8c6-a456fc62",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:0b77a64@sha256:5b067d99f617888d66b2656537e442d41ab32367758392fb1e55c88f2e1dce7f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promote-all-10",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 824294.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=43ce67db-a640-4ace-a534-eeafc62e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691386.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "saver-1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/1aec038070877c202ebcf960c202fa5dd35b511d36a3d5a9dda5f2dda2300805?artifact_id=236dbc20-a47c-4a90-bc78-f5fc5993",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691386.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9e8d3a77fae14af1b3f5fd22dc8185cf",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
              "satisfied": true,
              "ignored": false,
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
        "type": "unchanged",
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
          "flow_name": "snyk-vulns-aws-prod",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=c6ec6ca6-9900-445e-8986-76bc3e3d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691396.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=fe2b6149-935b-4098-aafe-1afabea3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691396.0,
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
              "satisfied": true,
              "ignored": false,
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
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
          "flow_name": "snyk-vulns-aws-prod",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=4eefbc15-7ea4-4d60-87d8-3a6098cb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691722.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=f295a00f-04cf-4c92-96d2-44181c6a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691722.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ee14a7db1433415dbcbf9b2a5a983c4d",
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
              "satisfied": true,
              "ignored": false,
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
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
        "type": "unchanged",
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
          "flow_name": "snyk-vulns-aws-beta",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=df1b23f7-316f-4d2a-90c1-4ad1b943",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691727.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=9a1e839e-8a7f-4dbc-abd1-5fe36251",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691727.0,
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
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b1ce55b@sha256:69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
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
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "nginx-ci",
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
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
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
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
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
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
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
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
      "fingerprint": "69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
      "creationTimestamp": [
        1776923200
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=8a73edbf-8c34-4371-a0a1-001dffd2",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd...b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
        "previous_git_commit": "c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
        "previous_fingerprint": "818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c6c81a0@sha256:818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
        "previous_trail_name": "c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 164853.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
          "template_reference_name": "nginx",
          "git_commit": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
          "git_commit_info": {
            "sha1": "b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
            "message": "Merge pull request #108 from cyber-dojo/fix-workflow-call-2\n\nFix workflow call",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776758347.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/b1ce55beb190397c80d3ba0536f6b97bb5f468f6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=8a73edbf-8c34-4371-a0a1-001dffd2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd...b1ce55beb190397c80d3ba0536f6b97bb5f468f6",
            "previous_git_commit": "c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
            "previous_fingerprint": "818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c6c81a0@sha256:818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
            "previous_trail_name": "c6c81a0f8b1458a62eee956bb16a8b32a37fd0fd",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 164853.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-11",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=445f9dbc-9f0f-4b04-bf3f-19ad3199",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:c6c81a0@sha256:818b3f15b642c9aa981397310a632d342a68e667224b55bd9a1b1b4ed0547284",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promotion-one-34",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 823945.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=81a19834-31ea-4e89-843c-a98ba49f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -691735.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "nginx-69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/69ac936feb8487b10fe54005660e407fbc2d7cb058c98485b9764db0f12b041d?artifact_id=7b489340-0541-46e9-9be8-7b05f412",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -691735.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/70cb5b4768f343569f6ffc81a51d984d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:65fd2bf@sha256:ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": true,
              "ignored": false,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "creator-ci",
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-archived-at-1776759327",
                    "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-beta",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-vulns-aws-prod",
                    "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
      "fingerprint": "ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
      "creationTimestamp": [
        1776256761
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
      "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=c5d209a3-9139-4f5b-a553-c6351091",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/f89742ee5f0477a7c729bfdeadc84dcbd70492b2...65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
        "previous_git_commit": "f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
        "previous_fingerprint": "fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:f89742e@sha256:fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
        "previous_trail_name": "f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 4517.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
          "template_reference_name": "creator",
          "git_commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
          "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
          "git_commit_info": {
            "sha1": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
            "message": "Merge branch 'fix-multijson-deprecation-warning' into 'main'\n\nBypass MultiJson.encode deprecation warning in Sinatra's json helper\n\nSee merge request cyber-dojo/creator!243",
            "author": "Jon Jagger <jon@jaggersoft.com>",
            "branch": "main",
            "timestamp": 1776252244.0,
            "url": "https://gitlab.com/cyber-dojo/creator/-/commit/65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=c5d209a3-9139-4f5b-a553-c6351091",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/f89742ee5f0477a7c729bfdeadc84dcbd70492b2...65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
            "previous_git_commit": "f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
            "previous_fingerprint": "fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:f89742e@sha256:fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
            "previous_trail_name": "f89742ee5f0477a7c729bfdeadc84dcbd70492b2",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 4517.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-9",
          "template_reference_name": "creator",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=c1a47a75-cdd5-446b-b08e-040067c3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa...87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_git_commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_fingerprint": "fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:f89742e@sha256:fe04c26b299dbb3ae9feb00d3955427d03a929c7f50e531acc243a176e01f16f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
            "previous_trail_name": "promotion-one-28",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 157506.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-archived-at-1776759327",
          "trail_name": "creator-medium-SNYK-ALPINE322-ZLIB-16078399",
          "template_reference_name": "artifact",
          "git_commit": "8440baadcaccb4ceeb8ba26b25579eb16cc447d6",
          "commit_url": "https://github.com/cyber-dojo/live-snyk-scans/commit/8440baadcaccb4ceeb8ba26b25579eb16cc447d6",
          "git_commit_info": {
            "sha1": "8440baadcaccb4ceeb8ba26b25579eb16cc447d6",
            "message": "Remove unnecessary floor() on trail creation timestamp\n\nfloor() was needed for bash integer arithmetic that has since been\nremoved; .created_at is now only used as a JSON number, which supports\nfloats natively.",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1776347865.0,
            "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/8440baadcaccb4ceeb8ba26b25579eb16cc447d6"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-archived-at-1776759327/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=240caf97-910e-4c8b-91dd-ef048d65",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-archived-at-1776759327",
          "deployment_diff": null,
          "commit_lead_time": -91104.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-beta",
          "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=893e3314-fdff-4f62-b899-2f874504",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
          "deployment_diff": null,
          "commit_lead_time": -1358174.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-vulns-aws-prod",
          "trail_name": "creator-ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod/artifacts/ce59db031695ca55deaaacefda233875fe5c32783c69816fcea2bb3642636e4f?artifact_id=12e53641-ee6f-4f38-bd54-97dc25ad",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-prod",
          "deployment_diff": null,
          "commit_lead_time": -1358174.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/712400a03ac04a9fb22935535516a317",
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

