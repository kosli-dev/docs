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
  "index": 4798,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1781862838.595731,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4798",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:fbae360@sha256:b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "saver-ci",
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
      "creationTimestamp": [
        1781862763
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "fbae360261d949b25a66a927921e757d4d064543",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=6df95847-0740-4e9e-8795-c960e47b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600...fbae360261d949b25a66a927921e757d4d064543",
        "previous_git_commit": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
        "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
        "previous_trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 65594.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "fbae360261d949b25a66a927921e757d4d064543",
          "template_reference_name": "saver",
          "git_commit": "fbae360261d949b25a66a927921e757d4d064543",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543",
          "git_commit_info": {
            "sha1": "fbae360261d949b25a66a927921e757d4d064543",
            "message": "Return 400, not 500, for well-formed but non-existent ids (#407)\n\nAPI endpoints that resolve an id raised a generic RuntimeError from the\n  manifest read when the id was well-formed but referenced nothing on disk\n  (eg kata_events for a non-existent kata-id). The global error handler maps\n  that to HTTP 500, telling the client the server broke when in fact the\n  request named something that does not exist.\n\n  Wrap each resolver (kata_version, group, cluster_manifest) so a missing\n  entity surfaces as a RequestError (HTTP 400), while genuine failures on an\n  entity that does exist are re-raised unchanged rather than masked as\n  \"does not exist\". cluster_hierarchy likewise now raises for an id matching\n  no kata, group or cluster instead of returning an empty hierarchy.\n\n  Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781797169.0,
            "url": "https://github.com/cyber-dojo/saver/commit/fbae360261d949b25a66a927921e757d4d064543"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=6df95847-0740-4e9e-8795-c960e47b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600...fbae360261d949b25a66a927921e757d4d064543",
            "previous_git_commit": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
            "previous_trail_name": "8c84facc7fd6a663fe7d40a6b4aff8f13a94d600",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 65594.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=66dcf0c8-08c4-4f4f-ac7e-26ab9830",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "saver-f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 267823.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b0ac80b4b90e684564fdda70932166d1ccf8033640242bae23aee17e1a5fed6e?artifact_id=bab84b72-7c27-435a-ad77-4f90c22e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:8c84fac@sha256:f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 449249.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b24c7b8c777b453392bc921a6cc21139",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:c248c8e@sha256:a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "runner-ci",
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
      "creationTimestamp": [
        1781862524,
        1781862527,
        1781862576
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "c248c8e2175307f6906e4a016d09b21d177923bd",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=2596689f-18f2-4c1b-b176-64e8b46f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/9cc2a80e1306376b88039715dfdcfc161a0e3904...c248c8e2175307f6906e4a016d09b21d177923bd",
        "previous_git_commit": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
        "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904",
        "previous_trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 265707.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "c248c8e2175307f6906e4a016d09b21d177923bd",
          "template_reference_name": "runner",
          "git_commit": "c248c8e2175307f6906e4a016d09b21d177923bd",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd",
          "git_commit_info": {
            "sha1": "c248c8e2175307f6906e4a016d09b21d177923bd",
            "message": "Merge pull request #247 from cyber-dojo/remove-go-jose-vuln-and-bump-snyk-expiry\n\nDrop go-jose v4 snyk ignores now that the CVE is fixed; refresh expir\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781596817.0,
            "url": "https://github.com/cyber-dojo/runner/commit/c248c8e2175307f6906e4a016d09b21d177923bd"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=2596689f-18f2-4c1b-b176-64e8b46f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/9cc2a80e1306376b88039715dfdcfc161a0e3904...c248c8e2175307f6906e4a016d09b21d177923bd",
            "previous_git_commit": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/9cc2a80e1306376b88039715dfdcfc161a0e3904",
            "previous_trail_name": "9cc2a80e1306376b88039715dfdcfc161a0e3904",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 265707.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=fe0b93ed-ad27-4b6e-9d10-a4bed0ed",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/09e584191c69ab283e35869dcdaa474414b03e45...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "09e584191c69ab283e35869dcdaa474414b03e45",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/09e584191c69ab283e35869dcdaa474414b03e45",
            "previous_trail_name": "runner-414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 267584.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a08f777df1038d7f01a1ea13420b40be242eda069dc2e23316aa5be5096d20fc?artifact_id=7c54ea3e-6632-4187-b3c6-26b9e6f0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:9cc2a80@sha256:414a07a72fbd04444ba4d2e19b6c7102095d5aeb469211f99166538626c08d06",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 449010.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d0cc8b328fa047f68fd080671dac3ea1",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:11fb356@sha256:df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443",
      "creationTimestamp": [
        1781862518
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443?artifact_id=6e7dfa64-c5c1-4a47-98f2-5e61c7b4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d...11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
        "previous_git_commit": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
        "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
        "previous_trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 914.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
          "template_reference_name": "exercises-start-points",
          "git_commit": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
          "git_commit_info": {
            "sha1": "11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
            "message": "Merge pull request #130 from cyber-dojo/update-base-image-53f1afd\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781861604.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/11fb35642d6c79603c1979f01d4fae7c1f7f0ce1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443?artifact_id=6e7dfa64-c5c1-4a47-98f2-5e61c7b4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d...11fb35642d6c79603c1979f01d4fae7c1f7f0ce1",
            "previous_git_commit": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
            "previous_trail_name": "b8e5cbf56e7fc03becdeee6a1d493c0231fa2d0d",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 914.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/df3c3018338b58650f75291ce06fa18e054b88be2a19520e87208dcfc00e1443?artifact_id=574003bb-90c9-4dcf-9e2f-52f891f8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:b8e5cbf@sha256:f00aa234bebafb1980dced29626750f84a6fe6c9c50f6a90167e4d8e6511a8a8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 449004.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a0d43249cd4f46a89427d9bcb84227ef",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:ff89dd9@sha256:c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "dashboard-ci",
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
      "creationTimestamp": [
        1781862505
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ff697a42-4717-4727-b9de-e3d77870",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/87f560f87fb2bc242ee5c58d74d0e209d71cd338...ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
        "previous_git_commit": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
        "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338",
        "previous_trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 426682.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
          "template_reference_name": "dashboard",
          "git_commit": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
          "git_commit_info": {
            "sha1": "ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
            "message": "Dockerfile - Automated base-image update (#391)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781435823.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/ff89dd9bd1bfc5441854450adcf25d5aad9508f4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ff697a42-4717-4727-b9de-e3d77870",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/87f560f87fb2bc242ee5c58d74d0e209d71cd338...ff89dd9bd1bfc5441854450adcf25d5aad9508f4",
            "previous_git_commit": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/87f560f87fb2bc242ee5c58d74d0e209d71cd338",
            "previous_trail_name": "87f560f87fb2bc242ee5c58d74d0e209d71cd338",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 426682.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=ba658957-8b40-4c67-b78e-de8d3293",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/7172cc22125f480a9f12127edb481a4d84aabea3...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/7172cc22125f480a9f12127edb481a4d84aabea3",
            "previous_trail_name": "dashboard-45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 267565.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c3e10b6879caa50792774c8d5eccf54ce23cbd730bee922846abf28fa534d5db?artifact_id=3407e8f9-e4f6-4c87-aed0-f2016d77",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:87f560f@sha256:45513c642ba191052bde056d56eeba8b06b0346eb444ec0008bd59bc0581bb8c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 448991.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f52f52698da74760bc5c8f5590180956",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:843d655@sha256:58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b",
      "creationTimestamp": [
        1781862431
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b?artifact_id=a467f7de-b8f1-45fe-a7aa-3479ee90",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/6b5c1598cc13c388a0fec71852e6b03bf0696e0b...843d6556ec718da1a1f51ce906c8c5bd6366d691",
        "previous_git_commit": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
        "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
        "previous_trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 832.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
          "template_reference_name": "custom-start-points",
          "git_commit": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691",
          "git_commit_info": {
            "sha1": "843d6556ec718da1a1f51ce906c8c5bd6366d691",
            "message": "Merge pull request #121 from cyber-dojo/update-base-image-53f1afd\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781861599.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/843d6556ec718da1a1f51ce906c8c5bd6366d691"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b?artifact_id=a467f7de-b8f1-45fe-a7aa-3479ee90",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/6b5c1598cc13c388a0fec71852e6b03bf0696e0b...843d6556ec718da1a1f51ce906c8c5bd6366d691",
            "previous_git_commit": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
            "previous_trail_name": "6b5c1598cc13c388a0fec71852e6b03bf0696e0b",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 832.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/58af6b791d447d089f43c716ef61fe81521af92cd982435968fe4c47ce800c7b?artifact_id=d85f5a12-124a-4777-b2d2-8c196161",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:6b5c159@sha256:b4448ca68a0926e4a7a800f5b101b63e9c2f38e1caaebb7e929d992763570928",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 448917.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5d521351a25845d4abb94577184aba6c",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:c1cd97e@sha256:c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe",
      "creationTimestamp": [
        1781862429
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c1cd97e11606d0a705df6619424c9ad8b07a57ca",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe?artifact_id=8064d7d2-d257-43e9-a609-0eb172f5",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/7e86fede3e42d573de92fed483559b8317ce2dda...c1cd97e11606d0a705df6619424c9ad8b07a57ca",
        "previous_git_commit": "7e86fede3e42d573de92fed483559b8317ce2dda",
        "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda",
        "previous_trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 827.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
          "template_reference_name": "languages-start-points",
          "git_commit": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/c1cd97e11606d0a705df6619424c9ad8b07a57ca",
          "git_commit_info": {
            "sha1": "c1cd97e11606d0a705df6619424c9ad8b07a57ca",
            "message": "Merge pull request #219 from cyber-dojo/update-base-image-53f1afd\n\nMerge update-base-image into main",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1781861602.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/c1cd97e11606d0a705df6619424c9ad8b07a57ca"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe?artifact_id=8064d7d2-d257-43e9-a609-0eb172f5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/7e86fede3e42d573de92fed483559b8317ce2dda...c1cd97e11606d0a705df6619424c9ad8b07a57ca",
            "previous_git_commit": "7e86fede3e42d573de92fed483559b8317ce2dda",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/7e86fede3e42d573de92fed483559b8317ce2dda",
            "previous_trail_name": "7e86fede3e42d573de92fed483559b8317ce2dda",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 827.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c76269bea7882b92f84938ca73220090b2b958c6cf468141aac49f54aeacecbe?artifact_id=e3e8b293-9e2d-48ee-a146-0724344e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:7e86fed@sha256:b2f51324efc1528e4dda57d235bdbc68d966e1ea23722d5d296f98eefbfc2676",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 448915.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f6459002a13f436295361080ca6a89f8",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:47ef6ca@sha256:82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "web-ci",
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
      "creationTimestamp": [
        1781862425,
        1781862427,
        1781862427
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=87b6ce7f-f34c-485b-8d6f-15a460ab",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c...47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
        "previous_git_commit": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
        "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
        "previous_trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 426625.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
          "template_reference_name": "web",
          "git_commit": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
          "git_commit_info": {
            "sha1": "47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
            "message": "Dockerfile - Automated base-image update (#362)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781435800.0,
            "url": "https://github.com/cyber-dojo/web/commit/47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=87b6ce7f-f34c-485b-8d6f-15a460ab",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c...47ef6ca4f22445ca7138a4818f8fe3a8b69b81f1",
            "previous_git_commit": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
            "previous_trail_name": "f66cc5c51fcc19b04b36e0542b36b6cc52515d3c",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 426625.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=f68b413b-90b4-4341-835b-57ad0b8b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74",
            "previous_fingerprint": "a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:517657b@sha256:a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74",
            "previous_trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 267485.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/82bd54f6d6cce8a290b0dbb106177c731ace68e6d1829c91e969de8d841d125f?artifact_id=4aae0d64-3134-42e5-bff9-3f722a8b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:f66cc5c@sha256:29c69c2f30f261a26fff4793fd8ae44b9081def1d4bcaaa27b0fef0501d949e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 448911.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/abca63ccf84346a5a39c68f735d50815",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:3ab1ef8@sha256:c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "differ-ci",
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
                    "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-24",
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
      "fingerprint": "c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
      "creationTimestamp": [
        1781862426
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=c25bc6ba-cbfd-4ad5-b5ab-d4bca4e9",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/981dcfc34f584d46afb46b217b47ce68f2f14a08...3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
        "previous_git_commit": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
        "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08",
        "previous_trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 422046.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
          "template_reference_name": "differ",
          "git_commit": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
          "git_commit_info": {
            "sha1": "3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
            "message": "Dockerfile - Automated base-image update (#405)\n\nCo-authored-by: JonJagger <JonJagger@users.noreply.github.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1781440380.0,
            "url": "https://github.com/cyber-dojo/differ/commit/3ab1ef84cb2243f184502ddb7f491e24d4ced1c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=c25bc6ba-cbfd-4ad5-b5ab-d4bca4e9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/981dcfc34f584d46afb46b217b47ce68f2f14a08...3ab1ef84cb2243f184502ddb7f491e24d4ced1c1",
            "previous_git_commit": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/981dcfc34f584d46afb46b217b47ce68f2f14a08",
            "previous_trail_name": "981dcfc34f584d46afb46b217b47ce68f2f14a08",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 422046.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=cc1db022-c674-4d4b-94d2-40b64e6b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74...00c479764cb9eca038fdaaaef108672d0bb0ed26",
            "previous_git_commit": "ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74",
            "previous_fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/ee081fb7be2ac7e2094bb4d02f3effdb9f73dd74",
            "previous_trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 267486.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-24",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/c012ad13f83df1701223f5e5d3a88e76cae4e3fd3662255f2b48ed444eea65cd?artifact_id=cf9f2757-e21d-48ea-89d8-3c0ea720",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/01dd4c6406d6655898ef2236875ec9f67091c792...01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_git_commit": "01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_fingerprint": "902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:981dcfc@sha256:902ec7af03407049ac6e5ef713146d518bbffd9d99cd28715fa0df973e809b7b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/01dd4c6406d6655898ef2236875ec9f67091c792",
            "previous_trail_name": "promote-all-23",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 448912.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/188f5f0511504893942a417bd1807175",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=ee1a78f9-85e5-41e6-b8c3-66d5d8fd",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f221996be414b7698b15bfe68d143c90896dc70431099bd42ecc594127087c43?artifact_id=5e4a1e8e-3675-46e0-b1fb-fe306f67",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=3b3fccd4-a0a5-4c65-8212-d599b670",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b7ff2cf22c934716a4280f0450ae52fe822cda7fce7fc5488bf62853860cddc8?artifact_id=dcb8881b-0f62-439c-8036-c9dbc6a6",
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
        "type": "exited",
        "was": 1,
        "now": 0
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f5909cc8dd53b2105953d1a72cd5d6181367d3588964aa01a04c056205a5d419?artifact_id=c47b8a1c-771d-41a8-8181-b0217289",
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

