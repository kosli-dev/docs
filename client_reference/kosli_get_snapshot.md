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
|        --debug  |  [optional] Print debug logs to stdout.  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |
|    -q, --quiet  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both --quiet and --debug are set, --debug wins.  |


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
  "index": 4404,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1778502898.4686973,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4404",
  "artifacts": [
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
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
        "type": "unchanged",
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
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3",
          "template_reference_name": "dashboard",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/ca8bd0b1073a1be8cd7b82f8ef9e5977c3b19b84187cdb86e41cd5ed3b12f5f3?artifact_id=29d3f828-dc04-41f9-ab93-edc337a8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 1970.0,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
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
        "type": "unchanged",
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
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694",
          "template_reference_name": "saver",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/510d5503851868af22fbfe32379b12811ac32bcfc54d01e8939190ea71270694?artifact_id=202e5a12-27ac-4937-bb62-027df5be",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 1646.0,
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/39f21a43bc564548b396bd0db3000938",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:c175db1@sha256:5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                    "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
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
                }
              ]
            }
          ],
          "policy_name": "build-process"
        }
      ],
      "reasons_for_incompliance": [],
      "fingerprint": "5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
      "creationTimestamp": [
        1778502481,
        1778502488,
        1778502490
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "c175db1be81803bc9587ccb3175723d450468ab0",
      "commit_url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6?artifact_id=088ed687-0522-4341-9042-0bd99b1f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/1999d1303424879336b04fa3310256554aa6cfa6...c175db1be81803bc9587ccb3175723d450468ab0",
        "previous_git_commit": "1999d1303424879336b04fa3310256554aa6cfa6",
        "previous_fingerprint": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6",
        "previous_trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 67361.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "c175db1be81803bc9587ccb3175723d450468ab0",
          "template_reference_name": "web",
          "git_commit": "c175db1be81803bc9587ccb3175723d450468ab0",
          "commit_url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0",
          "git_commit_info": {
            "sha1": "c175db1be81803bc9587ccb3175723d450468ab0",
            "message": "Fix 403 on checkout and revert by migrating to fetch() (#329)\n\n* Fix 403 on checkout and revert by migrating to fetch()\n\nThe commit that deleted cyber-dojo_csrf.js (the global jQuery ajaxSend\nCSRF hook) missed two $.post() calls: /kata/checkout in\n_checkout_button.erb and /kata/revert in run_tests.js.erb. Without the\nhook, those requests reach Sinatra without a CSRF token and are rejected\nwith 403. Migrate both to fetch() with explicit X-CSRF-Token and\nX-Requested-With headers, matching the pattern used elsewhere.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Tweak fork dialog button text\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778435120.0,
            "url": "https://github.com/cyber-dojo/web/commit/c175db1be81803bc9587ccb3175723d450468ab0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6?artifact_id=088ed687-0522-4341-9042-0bd99b1f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/1999d1303424879336b04fa3310256554aa6cfa6...c175db1be81803bc9587ccb3175723d450468ab0",
            "previous_git_commit": "1999d1303424879336b04fa3310256554aa6cfa6",
            "previous_fingerprint": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/1999d1303424879336b04fa3310256554aa6cfa6",
            "previous_trail_name": "1999d1303424879336b04fa3310256554aa6cfa6",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 67361.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6",
          "template_reference_name": "web",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6?artifact_id=eea8ea5b-816d-42b1-8e95-d036899c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 1626.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-14",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5ee3e7eec6b56da0b03840edddc643e49e9c0d8571d5e7a359b9309a6c65f9d6?artifact_id=542eedd6-71f5-49e5-89ba-745ed5db",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/1085da6ce837c6ebc77dda1e23b5de4e3c33380f...010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_git_commit": "1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_fingerprint": "541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:1999d13@sha256:541b7d4c1b129eb894ce1dd1713f72ae268e07cf49d178aeda684bbef2bfc180",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/1085da6ce837c6ebc77dda1e23b5de4e3c33380f",
            "previous_trail_name": "promote-all-13",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 256890.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f9bd72daa2064bbd93b123ef4f3e28ec",
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
                    "flow_name": "snyk-vulns-aws-beta",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
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
        "type": "unchanged",
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
          "flow_name": "snyk-vulns-aws-beta",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=b9129448-20c9-4dce-bf9d-eb7b5aa2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-vulns-aws-beta",
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
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3",
          "template_reference_name": "creator",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/4db0e95a793aa0539250f9998bc4fbe10b5d96a339730c20a25b9e763a8a5ff3?artifact_id=359d9477-6cc7-4449-ba40-9b989474",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 1634.0,
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9f700f8dcf58425cb6ce574fac656b8a",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
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
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099",
          "template_reference_name": "nginx",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/342cf442ebf26b4f1ec676b9ce1a3093eb1c5dcab1576b78b819b7048592a099?artifact_id=30574453-4fa7-4a98-a7cf-d1b02d10",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": 1630.0,
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/7b99ba7056144cf7bc04d773dc1c61d7",
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
        "type": "unchanged",
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
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=40015803-b4af-4f89-bd60-c43cfae3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -255308.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9",
          "template_reference_name": "runner",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/98b678856849684467bd8a25f7bc1cdd47f609b6b008b19bfe7f81a2a9b9c5c9?artifact_id=e5e3acd6-1a0b-40ce-aafe-5ec1c6d0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -255308.0,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=61ec148f-260b-4f7c-ba5e-4b6e6db7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -419718.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98",
          "template_reference_name": "languages-start-points",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f66cfbbc69bcb75bd3d2df7227d168335a8adbc27a0b59695db259ddde320a98?artifact_id=5c723ccb-8453-4235-8af0-cf9f0860",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -419718.0,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
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
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=aa74a05c-6026-4ac8-b0f9-b20bcfc4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577316.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1",
          "template_reference_name": "custom-start-points",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cdf80bb23fc22020b7a7eb8278540fc85345f1130eea182c5bf4ad5d8a20a7d1?artifact_id=30b226ba-4a5d-4dde-ab49-a54f141c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577316.0,
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
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=4be7df8a-0505-4c49-bf03-866889ea",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577642.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355",
          "template_reference_name": "differ",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/becf55d8a2ed6e43bdd4d26c82dc0e3a69204b92738858ad9cd25329fa513355?artifact_id=8f72594c-39df-4600-a201-46f5e334",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577642.0,
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
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=d0c489e2-0a3e-43c3-ab6a-d532ea24",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577647.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac",
          "template_reference_name": "exercises-start-points",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/691a6f0bcd1ce71af0a2175f1c4295e627f3e5ea93cb78264a2042d8ed2aa9ac?artifact_id=2ded1f66-a8c7-4df8-a72c-d68444b2",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1577647.0,
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
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
        "type": "exited",
        "was": 1,
        "now": 0
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
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact-archived-at-1778154285",
          "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=87660fcc-9088-4b68-ad78-e3d873aa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact-archived-at-1778154285",
          "deployment_diff": null,
          "commit_lead_time": -1229544.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
          "template_reference_name": "dashboard",
          "git_commit": "7e436ab66bcfceb524d65b3957dac6c2797b2a46",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7e436ab66bcfceb524d65b3957dac6c2797b2a46",
          "git_commit_info": {
            "sha1": "7e436ab66bcfceb524d65b3957dac6c2797b2a46",
            "message": "Make all env-level step summary headings self-explanatory\n\nThe headings previously showed just the env name (or \"Count=0\" for the\nall-clear case), giving no context about what was being counted or why.\nThe new label \"Snyk vulns nearing expiry: Count=N\" makes every\nenv-level heading readable at a glance.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778245944.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/7e436ab66bcfceb524d65b3957dac6c2797b2a46"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=76cf141d-e95a-47c6-a427-30c974ae",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1322082.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e",
          "template_reference_name": "dashboard",
          "git_commit": "c81f982df631e41eb6d4552165753924674b23d9",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9",
          "git_commit_info": {
            "sha1": "c81f982df631e41eb6d4552165753924674b23d9",
            "message": "Drop WARNING_DAYS; always show closest vuln in Slack\n\nWARNING_DAYS (7) was larger than all rego limits (max 6 days), so no\nvuln could ever reach the next_up phase before becoming non-compliant.\nThe three-stage journey (next_up -> expiring -> non-compliant) was\nunreachable for rego_limit vulns.\n\nReplace with a single unconditional Slack message: the closest upcoming\nnon-compliance event, or all-clear if none. The GitHub step summary\nshows all currently-tracked vulns grouped by artifact and severity.\n\nRestore RESPONSE_GUIDE_URL in the Slack message for non-empty cases.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1778500855.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c81f982df631e41eb6d4552165753924674b23d9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/3f419f93e3cdd7a3a2b358fdee8ee925dc233b5b2fe0eff20d8bce17f7473c8e?artifact_id=3c593714-b799-4dc8-8ce9-7beec686",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -1576993.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/0993e7a4118e4a7699ad6eb9c06a4b47",
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

