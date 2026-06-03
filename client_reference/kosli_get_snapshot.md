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
  "index": 4686,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1780474738.6666076,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4686",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:bc8fb51@sha256:9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "runner-ci",
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
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
      "fingerprint": "9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
      "creationTimestamp": [
        1780332947,
        1780332950,
        1780332952
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/bc8fb51346a42e17a4d3669f3ea11908782a43d1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2?artifact_id=d2a4899e-159a-4bbb-b130-40cedef7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db...bc8fb51346a42e17a4d3669f3ea11908782a43d1",
        "previous_git_commit": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
        "previous_fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
        "previous_trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 2644.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
          "template_reference_name": "runner",
          "git_commit": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/bc8fb51346a42e17a4d3669f3ea11908782a43d1",
          "git_commit_info": {
            "sha1": "bc8fb51346a42e17a4d3669f3ea11908782a43d1",
            "message": "Merge pull request #240 from cyber-dojo/update-snyk-docs\n\nAdd .snyk entry for new snyk vuln that is not exploitable",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780330303.0,
            "url": "https://github.com/cyber-dojo/runner/commit/bc8fb51346a42e17a4d3669f3ea11908782a43d1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2?artifact_id=d2a4899e-159a-4bbb-b130-40cedef7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db...bc8fb51346a42e17a4d3669f3ea11908782a43d1",
            "previous_git_commit": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
            "previous_fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
            "previous_trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 2644.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2?artifact_id=730189ec-4942-4cce-8fdd-7b2c433c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-57",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 968523.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
          "template_reference_name": "runner",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2?artifact_id=559995c1-932a-42c5-a8c7-96b2d084",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/822a5831653b0901ce5256c6e16d7eedb63ebc06...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -59594.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2",
          "template_reference_name": "runner",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9db5a9987ba83419bec8ded2cc7bc5c9db814c8f0f275b5fe7228957ceed5ac2?artifact_id=09e50ea3-2e6c-4aa8-beb6-123969e3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59594.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ce186ada694c4ca4939d4a7e3527ee83",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:2036886@sha256:e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
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
      "fingerprint": "e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
      "creationTimestamp": [
        1780389628
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "20368865b1ba0532f99f69641bbb96e6334cb545",
      "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/20368865b1ba0532f99f69641bbb96e6334cb545",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=d5d4dc83-f3c0-4a50-b5cb-fdc4f610",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/3a066186b7fbbcec0130419518c5bb81b50e71db...20368865b1ba0532f99f69641bbb96e6334cb545",
        "previous_git_commit": "3a066186b7fbbcec0130419518c5bb81b50e71db",
        "previous_fingerprint": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db",
        "previous_trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 1333.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "20368865b1ba0532f99f69641bbb96e6334cb545",
          "template_reference_name": "creator",
          "git_commit": "20368865b1ba0532f99f69641bbb96e6334cb545",
          "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/20368865b1ba0532f99f69641bbb96e6334cb545",
          "git_commit_info": {
            "sha1": "20368865b1ba0532f99f69641bbb96e6334cb545",
            "message": "Merge branch 'downtime-notice' into 'main'\n\nAdd downtime notice for pending infrastructure upgrade\n\nSee merge request cyber-dojo/creator!250",
            "author": "Jon Jagger <jon@jaggersoft.com>",
            "branch": "main",
            "timestamp": 1780388295.0,
            "url": "https://gitlab.com/cyber-dojo/creator/-/commit/20368865b1ba0532f99f69641bbb96e6334cb545"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=d5d4dc83-f3c0-4a50-b5cb-fdc4f610",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/3a066186b7fbbcec0130419518c5bb81b50e71db...20368865b1ba0532f99f69641bbb96e6334cb545",
            "previous_git_commit": "3a066186b7fbbcec0130419518c5bb81b50e71db",
            "previous_fingerprint": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db",
            "previous_trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1333.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-62",
          "template_reference_name": "creator",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=97fad3b0-e932-4eb8-a59f-2e4e5901",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-19",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 1025204.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
          "template_reference_name": "creator",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=6fbc711a-0bfa-4ef3-a670-a637066f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -2913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035",
          "template_reference_name": "creator",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/e433c4e99e5191290a2b36c72acdf86806a960381309e11dab902e4db8bfb035?artifact_id=e1f59cbe-ce12-4e41-96bb-ada47172",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -2913.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5c12e0e349eb44aa8049af6e45f4664d",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:f3c6791@sha256:9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "dashboard-ci",
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
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
      "fingerprint": "9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
      "creationTimestamp": [
        1780333321
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "f3c679170776733c60dc485e076b7cb515caa7a4",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=a92f3bf6-3316-405e-aee8-51af645c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0a839a472d41bf860d1d6dc3ded45ff63144018d...f3c679170776733c60dc485e076b7cb515caa7a4",
        "previous_git_commit": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
        "previous_fingerprint": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d",
        "previous_trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 282213.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "f3c679170776733c60dc485e076b7cb515caa7a4",
          "template_reference_name": "dashboard",
          "git_commit": "f3c679170776733c60dc485e076b7cb515caa7a4",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4",
          "git_commit_info": {
            "sha1": "f3c679170776733c60dc485e076b7cb515caa7a4",
            "message": "Improve demo reliability, hovertip UX, file-event display, and dash\u2026 (#386)\n\n* Improve demo reliability, hovertip UX, file-event display, and dashboard layout\n\n  make demo now stops containers on any of our ports before tearing down the\n  compose stack, preventing port-conflict failures when containers from other\n  projects (e.g. test_web_saver) are already bound to the same ports.\n\n  make demo now depends on image_server which depends on assets, so the\n  pre-built JS/CSS are always regenerated before the server image is baked.\n  Previously a stale pre-built-app.js was silently baked in, causing the\n  diff_summary fetch to hit /differ/ instead of /dashboard/.\n\n  Hovertip improvements:\n  - Removed the duplicate traffic-light icon from the summary row\n  - Removed the \"!\" type marker before each filename in the diff table\n  - Diff line-count boxes are always coloured and always show the digit\n    (including zero), matching the web repo's style; removed disabled attr\n    whose [disabled] CSS rule was making digits invisible against the background\n  - Test filenames shown in steel-blue via cd.lib.isTestFile() (ported from web)\n  - Filename gets 6px left padding now the type-marker column is gone\n\n  Inter-test file events (file_edit, file_create etc.) now render as\n  file_test.png or file_code.png based on whether the filename is a test file,\n  rather than the generic coloured icon. The filename is passed through\n  light_json and Event#filename so the JS can make the distinction.\n\n  Avatars with only inter-test file events (no test runs yet) now appear in\n  both the dashboard and the progress dialog. Previously gatherer.rb required\n  at least one light? event; it now uses a separate has_activity flag so the\n  row is included whenever any non-create event exists.\n\n  extra_file_edits in create_group_kata.rb now edits both hiker.sh and\n  test_hiker.sh per loop iteration, giving the hovertip diff table something\n  realistic to show for both file types.\n\n  Dashboard table max-height changed from a fixed 520px to calc(100dvh - 90px)\n  so all avatar rows are visible on typical screens without being clipped.\n\n* Bump test metrics",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780051108.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/f3c679170776733c60dc485e076b7cb515caa7a4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=a92f3bf6-3316-405e-aee8-51af645c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/0a839a472d41bf860d1d6dc3ded45ff63144018d...f3c679170776733c60dc485e076b7cb515caa7a4",
            "previous_git_commit": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
            "previous_fingerprint": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d",
            "previous_trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 282213.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "dashboard",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=61ae32cc-bd72-4d45-b577-00c7ebcc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-60",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 968897.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
          "template_reference_name": "dashboard",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=62436f11-800d-4c82-8310-fea50750",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "dashboard-ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 4129.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349",
          "template_reference_name": "dashboard",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9aa8b29c6163d8d454fdc63f896d1d0d8dec8f74ad364004e47727db3c1d3349?artifact_id=f4a3012a-bb53-47ac-957f-7b0721f9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59220.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/9e212cb69576480b973a361b12389554",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:ebf104f@sha256:df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
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
      "fingerprint": "df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
      "creationTimestamp": [
        1780333308
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62?artifact_id=03aaa94c-9a17-431f-9758-55096787",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/26438788f75a9a39db985b87100b9b32a2d962a2...ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
        "previous_git_commit": "26438788f75a9a39db985b87100b9b32a2d962a2",
        "previous_fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2",
        "previous_trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 2909.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
          "template_reference_name": "nginx",
          "git_commit": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
          "git_commit_info": {
            "sha1": "ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
            "message": "Merge pull request #127 from cyber-dojo/re-run-to-update-image\n\nRerun workflow to pickup new apk-upgrade fixes in Dockerfile",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780330399.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/ebf104fc1c073c7462a6ec381af70f639e4b8ba0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62?artifact_id=03aaa94c-9a17-431f-9758-55096787",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/26438788f75a9a39db985b87100b9b32a2d962a2...ebf104fc1c073c7462a6ec381af70f639e4b8ba0",
            "previous_git_commit": "26438788f75a9a39db985b87100b9b32a2d962a2",
            "previous_fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2",
            "previous_trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 2909.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "nginx",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62?artifact_id=03cb230d-5297-41c4-ade7-35b627bf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-61",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 968884.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
          "template_reference_name": "nginx",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62?artifact_id=c5b685d4-13c2-4044-80c4-3656357f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/822a5831653b0901ce5256c6e16d7eedb63ebc06...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 4116.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62",
          "template_reference_name": "nginx",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/df695792109b605031fbe0c33d89afa13b3fb26b513e7576f5201e991fd95a62?artifact_id=9d7fb466-72a0-468d-b3b7-d3af0df9",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59233.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ba65aa0520b5454e9c53cc8de29673bd",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:d3e5850@sha256:9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
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
      "fingerprint": "9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
      "creationTimestamp": [
        1780333290
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=7c413c73-ba1e-4707-b6d3-ced83312",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/a300e4c15cff321ef952a60bbc3a4729772a2419...d3e5850912655f2b18a68129f5f3a6480fe305ef",
        "previous_git_commit": "a300e4c15cff321ef952a60bbc3a4729772a2419",
        "previous_fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419",
        "previous_trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 376736.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
          "template_reference_name": "custom-start-points",
          "git_commit": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef",
          "git_commit_info": {
            "sha1": "d3e5850912655f2b18a68129f5f3a6480fe305ef",
            "message": "Merge pull request #116 from cyber-dojo/tidy-workflow\n\nTidy workflow using composite actions",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779956554.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/d3e5850912655f2b18a68129f5f3a6480fe305ef"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=7c413c73-ba1e-4707-b6d3-ced83312",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/a300e4c15cff321ef952a60bbc3a4729772a2419...d3e5850912655f2b18a68129f5f3a6480fe305ef",
            "previous_git_commit": "a300e4c15cff321ef952a60bbc3a4729772a2419",
            "previous_fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/a300e4c15cff321ef952a60bbc3a4729772a2419",
            "previous_trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 376736.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "custom-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=48c2d119-e488-4ba6-8c7e-27abb4f5",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 968866.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
          "template_reference_name": "custom-start-points",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=c151610f-8a0c-4ba7-b38d-b9cbd626",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/822a5831653b0901ce5256c6e16d7eedb63ebc06...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_fingerprint": "434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:a300e4c@sha256:434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 4098.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6",
          "template_reference_name": "custom-start-points",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9452c2f85c1d539974227f7e201f734934dce7b7dcbd2e056fcf9678454895e6?artifact_id=c30e87a8-96f1-49d3-acf3-b5e8e79c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59251.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f8dea79e89ef4714a3d069452ce8aea0",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:517657b@sha256:a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "web-ci",
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
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
      "fingerprint": "a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
      "creationTimestamp": [
        1780333030,
        1780333031,
        1780333034
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
      "commit_url": "https://github.com/cyber-dojo/web/commit/517657b9dec6ac7ff431ca5d9b2de72fded5c295",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770?artifact_id=a2ac6e7a-26e3-42a5-b6d1-369c474f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/d9ac74a950cadda60541db9781e9458832ffd6f8...517657b9dec6ac7ff431ca5d9b2de72fded5c295",
        "previous_git_commit": "d9ac74a950cadda60541db9781e9458832ffd6f8",
        "previous_fingerprint": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8",
        "previous_trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 349532.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
          "template_reference_name": "web",
          "git_commit": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
          "commit_url": "https://github.com/cyber-dojo/web/commit/517657b9dec6ac7ff431ca5d9b2de72fded5c295",
          "git_commit_info": {
            "sha1": "517657b9dec6ac7ff431ca5d9b2de72fded5c295",
            "message": "Fix isTestFile, ITE race, hover-tip cleanup, and dialog Enter key (#354)\n\nAdd cd.isTestFile() to identify files whose stem starts or ends with\ntest/tests/spec/steps. Use it to colour filenames steel-blue in the\nreview diff panel and hover-tips, and to simplify inter-test event\nicons to file_test/file_code.\n\nFix a race where clicking a filename fired saveAnyFileChangesITE\nasynchronously, allowing a concurrent create/delete/rename/test to\nuse a stale kata.index. The fix locks all CodeMirror editors and\ngates create/delete/rename/test behind cd.waitForITE(), which polls\nup to 2s for the in-flight ITE to settle.\n\nClean up hover-tips: remove the traffic-light image and type-marker\nglyph column; colour filenames by file type.\n\nFix Enter key in the delete file dialog, where the disabled input\nblocked the keyup handler. Handling moved to dialog-level keydown\nwith event.preventDefault() to suppress browser default submit.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779983498.0,
            "url": "https://github.com/cyber-dojo/web/commit/517657b9dec6ac7ff431ca5d9b2de72fded5c295"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770?artifact_id=a2ac6e7a-26e3-42a5-b6d1-369c474f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/d9ac74a950cadda60541db9781e9458832ffd6f8...517657b9dec6ac7ff431ca5d9b2de72fded5c295",
            "previous_git_commit": "d9ac74a950cadda60541db9781e9458832ffd6f8",
            "previous_fingerprint": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8",
            "previous_trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 349532.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "web",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770?artifact_id=e9e0ec5b-9c93-4500-a50e-94f2fc7d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-59",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 968606.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
          "template_reference_name": "web",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770?artifact_id=ee235d70-235c-43da-90f4-fef923ae",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -59511.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770",
          "template_reference_name": "web",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a416f3378c6bc07f2735aec03e80bc55acefe1c2f55c04930a5a7c5b4181e770?artifact_id=49737ebd-3f43-4e29-b0d8-65c85748",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59511.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/cae937b4afab4fb6ad2882a91a459c2e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9513e77@sha256:31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
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
      "fingerprint": "31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
      "creationTimestamp": [
        1780333031
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "9513e77858d775950f22173d0afd0634b2ac20b9",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=ed68d54a-2549-4822-9dc5-96dad6c1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/16d155bdd120fe5a926504069dd18a98b8275fa8...9513e77858d775950f22173d0afd0634b2ac20b9",
        "previous_git_commit": "16d155bdd120fe5a926504069dd18a98b8275fa8",
        "previous_fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
        "previous_trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 376070.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "9513e77858d775950f22173d0afd0634b2ac20b9",
          "template_reference_name": "languages-start-points",
          "git_commit": "9513e77858d775950f22173d0afd0634b2ac20b9",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9",
          "git_commit_info": {
            "sha1": "9513e77858d775950f22173d0afd0634b2ac20b9",
            "message": "Merge pull request #214 from cyber-dojo/tidy-workflow\n\nTidy workflow using composite actions",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779956961.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/9513e77858d775950f22173d0afd0634b2ac20b9"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=ed68d54a-2549-4822-9dc5-96dad6c1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/16d155bdd120fe5a926504069dd18a98b8275fa8...9513e77858d775950f22173d0afd0634b2ac20b9",
            "previous_git_commit": "16d155bdd120fe5a926504069dd18a98b8275fa8",
            "previous_fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/16d155bdd120fe5a926504069dd18a98b8275fa8",
            "previous_trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 376070.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "languages-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=8ef65f13-3f37-4cfd-8b36-dcf53855",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 968607.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
          "template_reference_name": "languages-start-points",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=f597c1ad-e9f8-4c30-8af7-411b5a0d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/822a5831653b0901ce5256c6e16d7eedb63ebc06...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_fingerprint": "83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:16d155b@sha256:83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 3839.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02",
          "template_reference_name": "languages-start-points",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/31af583cc43761df4e53ffaabeafb6fa378af6af45f92d9cd12d76e48d4ceb02?artifact_id=b5bf115c-d683-4c78-8cd5-24a7bbe3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/60fd5bffe45bc9618e81fabf8dd6793f92d10817...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -59510.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d7d2ece04ce2423aaa9dd7e9c25c1d30",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:68d791f@sha256:5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
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
      "fingerprint": "5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
      "creationTimestamp": [
        1780332962
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=174dfb75-db2f-40b0-901a-8a02499c",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/a11b7588b2d2333e1346f1a2bb100395f11f42d2...68d791f93dc161fd8dba63e49b7fe9f909cbe758",
        "previous_git_commit": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
        "previous_fingerprint": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2",
        "previous_trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 375439.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
          "template_reference_name": "saver",
          "git_commit": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758",
          "git_commit_info": {
            "sha1": "68d791f93dc161fd8dba63e49b7fe9f909cbe758",
            "message": "Tidy workflow using composite actions (#382)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779957523.0,
            "url": "https://github.com/cyber-dojo/saver/commit/68d791f93dc161fd8dba63e49b7fe9f909cbe758"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=174dfb75-db2f-40b0-901a-8a02499c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/a11b7588b2d2333e1346f1a2bb100395f11f42d2...68d791f93dc161fd8dba63e49b7fe9f909cbe758",
            "previous_git_commit": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
            "previous_fingerprint": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2",
            "previous_trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 375439.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "saver",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=5e6ca9ae-d19c-4ed0-8fee-40daa67b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-58",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 968538.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
          "template_reference_name": "saver",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=c56512ee-6696-474c-8581-6fae3179",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:42c8baf@sha256:e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 3770.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9",
          "template_reference_name": "saver",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5ee9f19010bb3ae0bbd97098f83c9f652254eda1d1a488a057adedf02af9fbc9?artifact_id=06d3e2f8-252c-429e-9376-ef557cbf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59579.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/11fcee940f3043768b79125a4a47d51b",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:43d2a72@sha256:d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "differ-ci",
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
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
      "fingerprint": "d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
      "creationTimestamp": [
        1780332956
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=66b5c45a-22d2-4f37-8688-beeeb449",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/f2e8fa718ca3b72527625bd182beb2950bea3a77...43d2a72431124e9fcf47bf866621ba3fd8e7f618",
        "previous_git_commit": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
        "previous_fingerprint": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77",
        "previous_trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 371812.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
          "template_reference_name": "differ",
          "git_commit": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618",
          "git_commit_info": {
            "sha1": "43d2a72431124e9fcf47bf866621ba3fd8e7f618",
            "message": "Tidy workflow by pushing common steps into composite actions (#390)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779961144.0,
            "url": "https://github.com/cyber-dojo/differ/commit/43d2a72431124e9fcf47bf866621ba3fd8e7f618"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=66b5c45a-22d2-4f37-8688-beeeb449",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/f2e8fa718ca3b72527625bd182beb2950bea3a77...43d2a72431124e9fcf47bf866621ba3fd8e7f618",
            "previous_git_commit": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
            "previous_fingerprint": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77",
            "previous_trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 371812.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "differ",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=b07368f4-ee48-449e-9670-dd0317d6",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-20",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 968532.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
          "template_reference_name": "differ",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=b17291e6-63e5-4e77-bd91-ad319705",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:fd71a71@sha256:dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -59585.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9",
          "template_reference_name": "differ",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/d2c30df1412005c8746cef54c3e3a88ddea23fdc0d96085a8ea66d91c61ac6d9?artifact_id=90aa4628-962e-4bee-8820-a97545ea",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -59585.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ad1c0143190c42c3b102659c4481e2b9",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:7635511@sha256:12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-21",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
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
      "fingerprint": "12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
      "creationTimestamp": [
        1780332951
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "76355112651c4ee66d6ee47f67e35459616f0dae",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=f94caaee-8681-4ead-acb2-8ea7c803",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/545cccbc91f4030fb4004421e1076bd7c2abbc93...76355112651c4ee66d6ee47f67e35459616f0dae",
        "previous_git_commit": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
        "previous_fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
        "previous_trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 376587.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "76355112651c4ee66d6ee47f67e35459616f0dae",
          "template_reference_name": "exercises-start-points",
          "git_commit": "76355112651c4ee66d6ee47f67e35459616f0dae",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae",
          "git_commit_info": {
            "sha1": "76355112651c4ee66d6ee47f67e35459616f0dae",
            "message": "Merge pull request #125 from cyber-dojo/delete-dead-code\n\nDelete unused job outputs",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779956364.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/76355112651c4ee66d6ee47f67e35459616f0dae"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=f94caaee-8681-4ead-acb2-8ea7c803",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/545cccbc91f4030fb4004421e1076bd7c2abbc93...76355112651c4ee66d6ee47f67e35459616f0dae",
            "previous_git_commit": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
            "previous_fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/545cccbc91f4030fb4004421e1076bd7c2abbc93",
            "previous_trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 376587.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-21",
          "template_reference_name": "exercises-start-points",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=5ca58609-53a7-4173-a5ca-c2f57006",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 968527.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
          "template_reference_name": "exercises-start-points",
          "git_commit": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
          "git_commit_info": {
            "sha1": "c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "message": "Delete dead step to force a trail to have empty template",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780329192.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=d3a5612c-c22b-46e5-b367-cd2d7f79",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/822a5831653b0901ce5256c6e16d7eedb63ebc06...c96bbe5f1b3c4cf747f77fc9a81210e1fd2c30e4",
            "previous_git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_fingerprint": "a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:545cccb@sha256:a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 3759.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc",
          "template_reference_name": "exercises-start-points",
          "git_commit": "a2a9d429bf3ff9ec375081d05a069717636cac31",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31",
          "git_commit_info": {
            "sha1": "a2a9d429bf3ff9ec375081d05a069717636cac31",
            "message": "Update expiry-response md file",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1780392541.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/a2a9d429bf3ff9ec375081d05a069717636cac31"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/12c8c3b837fc9fef8c25c7c0fc905f8537877f674a93ebd18cf4ff804594a3bc?artifact_id=e9dd24cf-00db-4548-b41a-374b7f0a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...a2a9d429bf3ff9ec375081d05a069717636cac31",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f3cf3ba@sha256:f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -59590.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/2097842cf82f4e7383ee9e950c9bf355",
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

