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
  "index": 5007,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1784014258.5595071,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5007",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:5195398@sha256:f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "web-ci",
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
                    "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-122",
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
      "fingerprint": "f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459",
      "creationTimestamp": [
        1784014182,
        1784014183,
        1784014184
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
      "commit_url": "https://github.com/cyber-dojo/web/commit/51953982aab0dae2f7ff684ebb4a76e5c132e777",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459?artifact_id=231d4126-b8bb-4db6-80e9-77922477",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/8d345854efbb1063d7546ef988dd771ed5445116...51953982aab0dae2f7ff684ebb4a76e5c132e777",
        "previous_git_commit": "8d345854efbb1063d7546ef988dd771ed5445116",
        "previous_fingerprint": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116",
        "previous_trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 1243.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
          "template_reference_name": "web",
          "git_commit": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
          "commit_url": "https://github.com/cyber-dojo/web/commit/51953982aab0dae2f7ff684ebb4a76e5c132e777",
          "git_commit_info": {
            "sha1": "51953982aab0dae2f7ff684ebb4a76e5c132e777",
            "message": "Fix false \"mobbing?\" dialog for a solo user on an unshared kata (#381)\n\nThe \"mobbing?\" dialog is meant to fire only when two or more laptops\n  share a kata-id and their [test] submissions interfere. But a single\n  user working alone could trigger it too.\n\n  Cause: an inter-test file event (create/delete/rename/edit) posts at the\n  browser's current index and advances it only from the response. Its fetch\n  aborted after 2s, so a slow-but-successful save committed on the server\n  while the browser never applied the returned index. The browser's index\n  was now behind the committed head, and the next [test] sent that stale\n  index, which the saver rejects as an \"Out of order event\" and the browser\n  renders as \"mobbing?\". nginx rate-limiting was ruled out: a 429 is\n  rejected before it reaches the saver, so it never commits and never\n  desyncs the index.\n\n  Fix (web only; saver and the index contract are unchanged):\n  - Add GET /kata/next_index/:id returning last_committed_index + 1, the\n    authoritative index a browser resyncs to.\n  - On a lost/failed inter-test response, resync the browser index from\n    that endpoint instead of silently leaving it stale (and drop the\n    misleading \"rate-limited\" log). Degrades safely if the endpoint is\n    absent (eg an older web instance mid-deploy): it 404s, resync no-ops,\n    index unchanged.\n  - Hold the in-progress flag for every inter-test event, not just\n    file_edit, so a following [test] waits behind an in-flight file op.\n  - Raise the inter-test abort 2s -> 30s (matching [test]); the 2s was not\n    guarding any rate limiter and was the main trigger for abandoning a\n    commit that actually landed.\n\n  The additive route and graceful client fallback keep a mid-session deploy\n  safe: every old/new browser-vs-server combination is either fixed or the\n  prior behavior, never worse.\n\n  Adds a dedicated endpoint test and a lost-event recovery test.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1784012939.0,
            "url": "https://github.com/cyber-dojo/web/commit/51953982aab0dae2f7ff684ebb4a76e5c132e777"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459?artifact_id=231d4126-b8bb-4db6-80e9-77922477",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/8d345854efbb1063d7546ef988dd771ed5445116...51953982aab0dae2f7ff684ebb4a76e5c132e777",
            "previous_git_commit": "8d345854efbb1063d7546ef988dd771ed5445116",
            "previous_fingerprint": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116",
            "previous_trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1243.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-122",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/f1b2a1723fee8d534e5a50f2ec83854b23e770aa57dea0479870dc308a948459?artifact_id=9e0d50c1-0d9b-4b26-8c48-b9f72d24",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 161481.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/eae2542c20df45a68733ec5cf1e2125a",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e59370c@sha256:48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
                    "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-121",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
      "fingerprint": "48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
      "creationTimestamp": [
        1783853016
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=be95fb64-f609-4b67-b5cb-e0efe36e",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/b8e6c03975a5701e3e8d198549f463989f1a00f4...e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
        "previous_git_commit": "b8e6c03975a5701e3e8d198549f463989f1a00f4",
        "previous_fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/b8e6c03975a5701e3e8d198549f463989f1a00f4",
        "previous_trail_name": "b8e6c03975a5701e3e8d198549f463989f1a00f4",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 11792.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
          "template_reference_name": "saver",
          "git_commit": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
          "git_commit_info": {
            "sha1": "e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
            "message": "Ignore Snyk c-ares CVE-2026-33630 until Alpine v3.24 backports the fix (#424)\n\nSnyk reports SNYK-ALPINE324-CARES-17896522 (CVE-2026-33630, a remote DoS\n  in c-ares, fixed in 1.34.8-r0) against the saver image. The fixed package\n  is not yet published to the Alpine v3.24 repo, so a rebuild or base-image\n  bump cannot remediate it, and git is needed at runtime so the dependency\n  (git -> libcurl -> c-ares) cannot be dropped.\n\n  c-ares is not exercised by saver: its only git use is local (clone from\n  \".\", remote remove, update-ref), which does no DNS resolution. The ignore\n  is time-boxed (expires 2026-08-11) so it re-surfaces; once Alpine backports\n  1.34.8-r0 a routine rebuild removes it and this entry should be deleted.\n\n  Document the assessment under docs/vulns/, following the pattern used by\n  the runner repo.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783841224.0,
            "url": "https://github.com/cyber-dojo/saver/commit/e59370cc9a235dec909ef1f8467d4cd6fb923ae8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=be95fb64-f609-4b67-b5cb-e0efe36e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/b8e6c03975a5701e3e8d198549f463989f1a00f4...e59370cc9a235dec909ef1f8467d4cd6fb923ae8",
            "previous_git_commit": "b8e6c03975a5701e3e8d198549f463989f1a00f4",
            "previous_fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/b8e6c03975a5701e3e8d198549f463989f1a00f4",
            "previous_trail_name": "b8e6c03975a5701e3e8d198549f463989f1a00f4",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 11792.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-121",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=da608fde-692a-43d4-bb49-f9865d77",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...76325d840dc66e1c84743725e17de05a16616419",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-30",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 315.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=b856980b-075b-491a-acc8-2cc325c9",
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
          "commit_lead_time": 2042.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/48f4e8dcbb47c68acb1ed199ab915f69fa81d8dc052b04eae26617e9a9b1599c?artifact_id=035499a3-d5cc-4f3c-8946-c2a19694",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...35a09b2d283bafd6bbc12c29eba3306d5b36a5f7",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b8e6c03@sha256:e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "saver-e930c316594afc43877740e30d7ac95cdadcf753a2b8a51935652c9531def452",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 2042.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/384f0dfe9f834a75ab534d0393c32cd9",
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
        "type": "unchanged",
        "was": 3,
        "now": 3
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=55813f39-7624-4502-bc05-18072121",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/cf3f94bb0d1130ca799b94450614109a917d8c53ea99fc20bd04c51141873fcf?artifact_id=418b1f5f-bdda-4cb4-95cf-4fccb515",
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
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:7e00b70@sha256:0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
                    "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
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
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
      "fingerprint": "0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
      "creationTimestamp": [
        1783618467
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
      "commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=aeec9b85-1a23-4579-b4a8-dbc98a05",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/creator/compare/6ff6b4c71ab218d39065654bef32839b9226d21f...7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
        "previous_git_commit": "6ff6b4c71ab218d39065654bef32839b9226d21f",
        "previous_fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
        "previous_trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 79786.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
          "template_reference_name": "creator",
          "git_commit": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
          "commit_url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
          "git_commit_info": {
            "sha1": "7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
            "message": "Update kosli template with provenance facts+decision (#41)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783538681.0,
            "url": "https://github.com/cyber-dojo/creator/commit/7e00b70f8911edf1c480ba9a8b9c2a280260cb08"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=aeec9b85-1a23-4579-b4a8-dbc98a05",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/creator/compare/6ff6b4c71ab218d39065654bef32839b9226d21f...7e00b70f8911edf1c480ba9a8b9c2a280260cb08",
            "previous_git_commit": "6ff6b4c71ab218d39065654bef32839b9226d21f",
            "previous_fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/creator/commit/6ff6b4c71ab218d39065654bef32839b9226d21f",
            "previous_trail_name": "6ff6b4c71ab218d39065654bef32839b9226d21f",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 79786.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
          "template_reference_name": "creator",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=38e3d0b8-7897-4f0c-8b4b-72fa4745",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 711359.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=57b05a37-659f-4f41-801b-1a441ba0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:6ff6b4c@sha256:a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "creator-a523828dc47cd4f31aecf2d5ef1dea569944a1abcd214e4b2cda50676b2c4dc8",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 819164.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0744a611723cb72a3f24b33c2d56fcbb1bfbedf0637a962f259fada8e3dbbe50?artifact_id=6ac99a6e-fe18-4880-9c37-b2781448",
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
          "commit_lead_time": -232507.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/aabbbdeadb0b4fe4a415ddcc8030db24",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:9b711df@sha256:0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
                    "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
      "fingerprint": "0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
      "creationTimestamp": [
        1783618458
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "9b711df71c76a1f293c2525ace65778036591baf",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=0d448ff6-ac85-47bb-8d86-9dfab222",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/cbf0063e279351ffb201b39296e9bfe892dc772f...9b711df71c76a1f293c2525ace65778036591baf",
        "previous_git_commit": "cbf0063e279351ffb201b39296e9bfe892dc772f",
        "previous_fingerprint": "c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cbf0063@sha256:c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f",
        "previous_trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 12638.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "9b711df71c76a1f293c2525ace65778036591baf",
          "template_reference_name": "nginx",
          "git_commit": "9b711df71c76a1f293c2525ace65778036591baf",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf",
          "git_commit_info": {
            "sha1": "9b711df71c76a1f293c2525ace65778036591baf",
            "message": "Merge pull request #158 from cyber-dojo/run-workflow-152\n\nRun main workflow to check updates to secure-docker-build sub workflow",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783605820.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/9b711df71c76a1f293c2525ace65778036591baf"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=0d448ff6-ac85-47bb-8d86-9dfab222",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/cbf0063e279351ffb201b39296e9bfe892dc772f...9b711df71c76a1f293c2525ace65778036591baf",
            "previous_git_commit": "cbf0063e279351ffb201b39296e9bfe892dc772f",
            "previous_fingerprint": "c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cbf0063@sha256:c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/cbf0063e279351ffb201b39296e9bfe892dc772f",
            "previous_trail_name": "cbf0063e279351ffb201b39296e9bfe892dc772f",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 12638.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=389fea12-1169-476e-b156-27970ac8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:cbf0063@sha256:c2ec29a9c6cce9948227159bc97dbb689cdc5803e77c4cff5573a6f257c8182c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promotion-one-118",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 711350.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=3ebc7928-e96e-465b-a205-6f9ed1fc",
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
          "commit_lead_time": -232516.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/0a858af40ca7a862ac1ba6a895e75c9030097f5890e9cc37c828e4adc55940e7?artifact_id=e96930e3-5ed2-4174-bb6a-f09901cd",
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
          "commit_lead_time": -232516.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e229983953cd42e5a38849ac1cf5b41f",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=15c2cd90-9acb-472f-bd2a-93299448",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/f4ed92af30318fe8230648a2fc1f482970ad0ef821eeaaeac76759cd8fe03418?artifact_id=c03b0261-dfb5-4626-9b43-e3bfc66c",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=289e3f72-1142-4bb3-a33e-42bfc205",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/1ed61f19b66b82f7f122b7b88522360de73abb3536fab5d0f8eadb9b987f9400?artifact_id=a7aecd18-7c13-495d-bf39-cc8b3fd8",
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5333f9f522e74ab797a3893465e348d9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768@sha256:54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                    "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
      "fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "creationTimestamp": [
        1783618197
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "e4757683b74df7033c95aa544a7824b395c2f8bb",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=cc7c618f-d22e-4d95-b6f1-cea4fded",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/6d203a85ffda1513db4d86d4e48b1f969bd2f510...e4757683b74df7033c95aa544a7824b395c2f8bb",
        "previous_git_commit": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
        "previous_fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510",
        "previous_trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 79687.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
          "template_reference_name": "dashboard",
          "git_commit": "e4757683b74df7033c95aa544a7824b395c2f8bb",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
          "git_commit_info": {
            "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
            "message": "Update kosli template with provenance facts+decision (#414)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783538510.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=cc7c618f-d22e-4d95-b6f1-cea4fded",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/6d203a85ffda1513db4d86d4e48b1f969bd2f510...e4757683b74df7033c95aa544a7824b395c2f8bb",
            "previous_git_commit": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
            "previous_fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/6d203a85ffda1513db4d86d4e48b1f969bd2f510",
            "previous_trail_name": "6d203a85ffda1513db4d86d4e48b1f969bd2f510",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 79687.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=345df2c2-785f-4d79-a5fa-0e576d45",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "dashboard-4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 818894.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=58819de1-c255-4e0c-a08d-e5807021",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:6d203a8@sha256:4d1ba1622515a86443d2ec4b76df41daa7b98daabeb557a134607f6e200e8ebc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 711089.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb?artifact_id=b5910c68-49fe-49b8-b1ca-c2814ee1",
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
          "commit_lead_time": -232777.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/fca9ca08541544e0bba91f462605371e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:8beff99@sha256:7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
                    "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
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
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
      "fingerprint": "7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
      "creationTimestamp": [
        1783618126
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "8beff9901ac67acb7afcab3408106208571a1124",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=ece4f8ca-6c19-4ca5-a482-dd4af708",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/26dcd06257a4bb00d594dbb5de05eefbb7b20379...8beff9901ac67acb7afcab3408106208571a1124",
        "previous_git_commit": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
        "previous_fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379",
        "previous_trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 77967.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "8beff9901ac67acb7afcab3408106208571a1124",
          "template_reference_name": "differ",
          "git_commit": "8beff9901ac67acb7afcab3408106208571a1124",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124",
          "git_commit_info": {
            "sha1": "8beff9901ac67acb7afcab3408106208571a1124",
            "message": "Update kosli template with provenance facts+decision (#428)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783540159.0,
            "url": "https://github.com/cyber-dojo/differ/commit/8beff9901ac67acb7afcab3408106208571a1124"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=ece4f8ca-6c19-4ca5-a482-dd4af708",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/26dcd06257a4bb00d594dbb5de05eefbb7b20379...8beff9901ac67acb7afcab3408106208571a1124",
            "previous_git_commit": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
            "previous_fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/26dcd06257a4bb00d594dbb5de05eefbb7b20379",
            "previous_trail_name": "26dcd06257a4bb00d594dbb5de05eefbb7b20379",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 77967.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=d70bdb3a-6d3f-4ff4-9cce-651590a5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 711018.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=0df2564f-0d3c-4379-bd18-d16e40a8",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/a517304f4e9013e2e9ea67e90c7342f7e56653f0...a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_git_commit": "a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_fingerprint": "8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:26dcd06@sha256:8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a517304f4e9013e2e9ea67e90c7342f7e56653f0",
            "previous_trail_name": "differ-8f01c6f92f1226465177b079c360d26898315356b172042f8dedb593c95d2dd7",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 818823.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/7e2d411aedcf779dc4be7da47957f698696df954a7f557688d0052e9a18218fc?artifact_id=cc856081-7c14-4a5b-9020-35165c8b",
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
          "commit_lead_time": -232848.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/10e2c5d7013342098a15699c13707b71",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=6f626279-b0ca-41dd-931a-9c235a4e",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a07b93ce0975df90f08f0dc171105a4f6e61e5b91aaf5ca9874d372084e1b613?artifact_id=3aae3348-407f-4de1-9241-4d61c88b",
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
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c2a918fa550f40d6a4f2b35f023d40f1",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:8d34585@sha256:99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
                    "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
      "fingerprint": "99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
      "creationTimestamp": [
        1783618129,
        1783618201,
        1783618209
      ],
      "pods": null,
      "annotation": {
        "type": "exited",
        "was": 3,
        "now": 0
      },
      "flow_name": "web-ci",
      "git_commit": "8d345854efbb1063d7546ef988dd771ed5445116",
      "commit_url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f?artifact_id=022a327b-df37-4f2c-94f2-2f7c3fd0",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/97ebee56e01ca3af95bfcae0c7c328eee8c56865...8d345854efbb1063d7546ef988dd771ed5445116",
        "previous_git_commit": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
        "previous_fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865",
        "previous_trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 1293.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "8d345854efbb1063d7546ef988dd771ed5445116",
          "template_reference_name": "web",
          "git_commit": "8d345854efbb1063d7546ef988dd771ed5445116",
          "commit_url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116",
          "git_commit_info": {
            "sha1": "8d345854efbb1063d7546ef988dd771ed5445116",
            "message": "When kata is in a cluster make [dashboard] open in cluster view (#379)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1783616836.0,
            "url": "https://github.com/cyber-dojo/web/commit/8d345854efbb1063d7546ef988dd771ed5445116"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f?artifact_id=022a327b-df37-4f2c-94f2-2f7c3fd0",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/97ebee56e01ca3af95bfcae0c7c328eee8c56865...8d345854efbb1063d7546ef988dd771ed5445116",
            "previous_git_commit": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
            "previous_fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/97ebee56e01ca3af95bfcae0c7c328eee8c56865",
            "previous_trail_name": "97ebee56e01ca3af95bfcae0c7c328eee8c56865",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1293.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-30",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f?artifact_id=980ad392-95f2-486b-ae9e-5f073c4d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/d7e31ce0207b766140ae689f38625da4374acf87...d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_git_commit": "d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_fingerprint": "929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:97ebee5@sha256:929748bb88b31863da9cd8d62a5039c274ff3c669f2ef05bc025e6989d2c1eab",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/d7e31ce0207b766140ae689f38625da4374acf87",
            "previous_trail_name": "promote-all-29",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 711021.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/99da6bff005f90bf23d728dc2c7cfd65f0e251772b246766955fd3dc209dbb6f?artifact_id=be9da614-3eeb-462d-be85-f38bf8c4",
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
          "commit_lead_time": -232845.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e5637d1722824c84878a645cd36e9639",
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

