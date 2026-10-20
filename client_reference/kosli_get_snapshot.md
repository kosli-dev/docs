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
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for snapshot |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


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
  "index": 5502,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 11,
    "false": 0,
    "null": 0
  },
  "timestamp": 1792486738.3284767,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/5502",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:edb38e8@sha256:daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
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
                    "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-187",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
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
      "fingerprint": "daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
      "creationTimestamp": [
        1792486374
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a?artifact_id=6e81efc1-5e0d-43b3-8ff5-2814b1b7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/b543342fa06b0ef415950745fddfff5a85f9d80d...edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
        "previous_git_commit": "b543342fa06b0ef415950745fddfff5a85f9d80d",
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/b543342fa06b0ef415950745fddfff5a85f9d80d",
        "previous_fingerprint": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "b543342fa06b0ef415950745fddfff5a85f9d80d",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 1067.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
          "template_reference_name": "saver",
          "git_commit": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
          "git_commit_info": {
            "sha1": "edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
            "message": "Run workflow to fix new snyk vuln in libexpat (#465)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1792485307.0,
            "url": "https://github.com/cyber-dojo/saver/commit/edb38e8b2a233345645ee339cdc9ed7b3b74fcd2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a?artifact_id=6e81efc1-5e0d-43b3-8ff5-2814b1b7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/b543342fa06b0ef415950745fddfff5a85f9d80d...edb38e8b2a233345645ee339cdc9ed7b3b74fcd2",
            "previous_git_commit": "b543342fa06b0ef415950745fddfff5a85f9d80d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/b543342fa06b0ef415950745fddfff5a85f9d80d",
            "previous_fingerprint": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "b543342fa06b0ef415950745fddfff5a85f9d80d",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1067.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-187",
          "template_reference_name": "saver",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a?artifact_id=d98f72b1-818f-4053-b631-9006ff56",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/f1f6cd6bce0e887649f077657215b50f9cf47d93...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_fingerprint": "2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:b543342@sha256:2bb4255d1477046c8042e9973482a02e0d66b35ce31d86287a58342e990c0efa",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-184",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 837102.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a",
          "template_reference_name": "saver",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/daaa83990b31397a2892ef521dedd06f4d7fd0c19ace1be73da7cf06d6a4734a?artifact_id=d8527b54-7967-46f6-b27e-30ec074b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:7c4708f@sha256:9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "saver-9cfef3281fc531a3c5a5a00ed8a67256e1b954b5271b03936808623960afebfc",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1727316.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/42319575108d4077b44054a6c2d6a943",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:ce9bf5f@sha256:08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
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
                    "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-186",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
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
      "fingerprint": "08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
      "creationTimestamp": [
        1792485660
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff?artifact_id=a80fab87-944a-4e6e-a972-847a95aa",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/842bdad4a2fc94d0acfe996d059972b50037b304...ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
        "previous_git_commit": "842bdad4a2fc94d0acfe996d059972b50037b304",
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/842bdad4a2fc94d0acfe996d059972b50037b304",
        "previous_fingerprint": "807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:842bdad@sha256:807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "842bdad4a2fc94d0acfe996d059972b50037b304",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 5444.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
          "template_reference_name": "differ",
          "git_commit": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
          "git_commit_info": {
            "sha1": "ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
            "message": "Run workflow to pick up new snyk vuln fix (#508)",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1792480216.0,
            "url": "https://github.com/cyber-dojo/differ/commit/ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff?artifact_id=a80fab87-944a-4e6e-a972-847a95aa",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/842bdad4a2fc94d0acfe996d059972b50037b304...ce9bf5fdfb6e10b5d2de1b324fd03483e8b67173",
            "previous_git_commit": "842bdad4a2fc94d0acfe996d059972b50037b304",
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/842bdad4a2fc94d0acfe996d059972b50037b304",
            "previous_fingerprint": "807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:842bdad@sha256:807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "842bdad4a2fc94d0acfe996d059972b50037b304",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 5444.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
          "template_reference_name": "differ",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff?artifact_id=0ef4e0f3-d385-45d0-a1ee-4fbf0488",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:9b49875@sha256:b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-b268bc93ea9aac4a2db861f98c67c21b8a8165091c3f937b8f7ba129e81f665c",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1726602.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-186",
          "template_reference_name": "differ",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff?artifact_id=eda90f94-ac70-4894-94b3-771da86a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:842bdad@sha256:807d0a7538fb9c739beab0b9f2793fe24c0a8bf079ef731ec2a2c2fe6464c463",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 836388.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff",
          "template_reference_name": "differ",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/08830cb438e6e0da0b5b12192695bd16cdfa6fe58e1316bb041492cb7dfabdff?artifact_id=0f4921b5-1f0f-45be-b26e-06e89742",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:2e9bd96@sha256:f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "differ-f61d363b12c540302c97e4f694c76edc6fcb594852e2dcdb8ce92d2d22521409",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 1726602.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/99235f292e76466195f23c7102735fa2",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:83553f5@sha256:da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
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
                    "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-185",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
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
      "fingerprint": "da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
      "creationTimestamp": [
        1791806438,
        1791806440,
        1791806445
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
      "commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=bb10f025-89b9-463a-9857-0a4a205b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...83553f52e8de8a9766a64fced8fbfb3cd32318a3",
        "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_fingerprint": "b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3e6678b@sha256:b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 2820.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
          "template_reference_name": "web",
          "git_commit": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
          "commit_url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3",
          "git_commit_info": {
            "sha1": "83553f52e8de8a9766a64fced8fbfb3cd32318a3",
            "message": "Let a review fork a new avatar into the same group (#475)\n\nForking a light from a kata in a group could only start a\n  new solo kata or a new group, so a mob member who fell\n  behind had no way back into their own group's dashboard.\n  The fork dialog now offers an avatar option that joins the\n  same group and opens the new kata straight in the edit page.\n\n  It relies on saver's avatar_fork, which the current\n  versioner now provides. Saver answers null when the group\n  is full, so the option is disabled for a full group, and a\n  group that fills after the dialog opens shows the same\n  \"sorry, it's full\" dialog the creator does.\n\n  A pulling, timed_out or faulty light is not a test result,\n  so the fork button is now disabled on one.\n\n  The client suite brings containers down first, so the two\n  almost-full (63 avatar) test groups load fresh each run.",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791803618.0,
            "url": "https://github.com/cyber-dojo/web/commit/83553f52e8de8a9766a64fced8fbfb3cd32318a3"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=bb10f025-89b9-463a-9857-0a4a205b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1...83553f52e8de8a9766a64fced8fbfb3cd32318a3",
            "previous_git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_fingerprint": "b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3e6678b@sha256:b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 2820.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-185",
          "template_reference_name": "web",
          "git_commit": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93",
          "git_commit_info": {
            "sha1": "f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "message": "Merge pull request #19 from cyber-dojo/cap-parallel-prod-applies\n\nCap promote-all prod applies at three at a time",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791649272.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/f1f6cd6bce0e887649f077657215b50f9cf47d93"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=318894c2-9470-4ec0-a282-1a903061",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...f1f6cd6bce0e887649f077657215b50f9cf47d93",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:3e6678b@sha256:b2c1ecdf766f6f687057bc95139e1c4f2cf9d086b81586f1b1e9096a279316fd",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 157166.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=2e6f228a-e915-4358-aa65-3b29baba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1047380.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/da7984414ab096232877f301d3d7cea1daf3cdd3fdb72157f530fe186cba3d78?artifact_id=34c1fcde-7d49-41ff-8046-201f864f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 1047380.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ae6431361d3b4a9ea10f22ec6a4d7642",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:68636be@sha256:2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
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
                    "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
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
      "fingerprint": "2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
      "creationTimestamp": [
        1791648622
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "exercises-start-points-ci",
      "git_commit": "68636bed4906a15df27ee99e2afddd4377d3867e",
      "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8?artifact_id=3a46596a-b98c-4c2f-a72a-d8452f32",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/009779d876c8b977e993fcf9ed1187e9c3bcdcc8...68636bed4906a15df27ee99e2afddd4377d3867e",
        "previous_git_commit": "009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
        "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
        "previous_fingerprint": "b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:009779d@sha256:b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
        "previous_template_reference_name": "exercises-start-points"
      },
      "commit_lead_time": 2134.0,
      "flows": [
        {
          "flow_name": "exercises-start-points-ci",
          "trail_name": "68636bed4906a15df27ee99e2afddd4377d3867e",
          "template_reference_name": "exercises-start-points",
          "git_commit": "68636bed4906a15df27ee99e2afddd4377d3867e",
          "commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e",
          "git_commit_info": {
            "sha1": "68636bed4906a15df27ee99e2afddd4377d3867e",
            "message": "Merge pull request #157 from cyber-dojo/multi-arch-start-point\n\nBuild the start-point image for amd64 and arm64",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791646488.0,
            "url": "https://github.com/cyber-dojo/exercises-start-points/commit/68636bed4906a15df27ee99e2afddd4377d3867e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci/artifacts/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8?artifact_id=3a46596a-b98c-4c2f-a72a-d8452f32",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/exercises-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/exercises-start-points/compare/009779d876c8b977e993fcf9ed1187e9c3bcdcc8...68636bed4906a15df27ee99e2afddd4377d3867e",
            "previous_git_commit": "009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/exercises-start-points/commit/009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
            "previous_fingerprint": "b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:009779d@sha256:b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "009779d876c8b977e993fcf9ed1187e9c3bcdcc8",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 2134.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "exercises-start-points",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8?artifact_id=1d6f3ca7-ce34-4cfc-b5f0-6c998408",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_fingerprint": "b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:009779d@sha256:b2cc2492bec7b295c6e33a4992af9fbe9e55f2332c29f1feb9f9ed453fad43c9",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-180",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 8106.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8",
          "template_reference_name": "exercises-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2dffee94d09db0d3e291cef0fc416f007271ab578adcba8b35f359fda5f2a8a8?artifact_id=2a2d6353-8694-44bd-bb5a-dde9128c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:d01bb39@sha256:bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "exercises-start-points-bc1dae4e8ce742e027a6dc6b68e44c65361cd48e588483d3fd9f6d6911a84c31",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": 889564.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/a56b0b31ecdf4a978746c67594ee418f",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:270c3c8@sha256:6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
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
                    "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
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
      "fingerprint": "6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
      "creationTimestamp": [
        1791648621
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "custom-start-points-ci",
      "git_commit": "270c3c87aecb0e008e90879be753e67983e692c8",
      "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93?artifact_id=93be9d1e-6eff-4ff5-a077-ed2baf30",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2...270c3c87aecb0e008e90879be753e67983e692c8",
        "previous_git_commit": "12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
        "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
        "previous_fingerprint": "72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:12bbf7b@sha256:72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
        "previous_template_reference_name": "custom-start-points"
      },
      "commit_lead_time": 2571.0,
      "flows": [
        {
          "flow_name": "custom-start-points-ci",
          "trail_name": "270c3c87aecb0e008e90879be753e67983e692c8",
          "template_reference_name": "custom-start-points",
          "git_commit": "270c3c87aecb0e008e90879be753e67983e692c8",
          "commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8",
          "git_commit_info": {
            "sha1": "270c3c87aecb0e008e90879be753e67983e692c8",
            "message": "Merge pull request #154 from cyber-dojo/multi-arch-start-point\n\nBuild the start-point image for amd64 and arm64",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791646050.0,
            "url": "https://github.com/cyber-dojo/custom-start-points/commit/270c3c87aecb0e008e90879be753e67983e692c8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci/artifacts/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93?artifact_id=93be9d1e-6eff-4ff5-a077-ed2baf30",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/custom-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/custom-start-points/compare/12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2...270c3c87aecb0e008e90879be753e67983e692c8",
            "previous_git_commit": "12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
            "previous_git_commit_url": "https://github.com/cyber-dojo/custom-start-points/commit/12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
            "previous_fingerprint": "72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:12bbf7b@sha256:72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "12bbf7bcb4553b0b0e24741d7bfc76d9972a7dd2",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 2571.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "custom-start-points",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93?artifact_id=94089d91-ec7f-46a8-ade1-2b93b563",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_fingerprint": "72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:12bbf7b@sha256:72c50c09d16309e07d241e0100e4acccff549f92cdf6de712a59f54fddb5c477",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-182",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 8105.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93",
          "template_reference_name": "custom-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6726c2fe6436edca6caaeed069531e326f7bfdceeac41feed28bef90a036cc93?artifact_id=3349fc20-7f93-4bf1-9e18-ab3b7d4e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:86c839e@sha256:ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "custom-start-points-ed0b8b8cc04f951bc7224d792c9c68010388f9ebf3c45d9a5d375be3a68d0b2e",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": 889563.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/215ffdb9e276401e8e3a12a333e06afd",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:3e6678b@sha256:5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
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
      "fingerprint": "5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
      "creationTimestamp": [
        1791648357
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=6923c594-deee-4b7c-83e9-3165a9ed",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/239086385550e2c369fd3aa1f656b56f362db8f7...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_fingerprint": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 15159.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "template_reference_name": "dashboard",
          "git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "git_commit_info": {
            "sha1": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "message": "Web multi platform and dockerhub (#468)\n\n* Build web, creator, dashboard for amd64 + arm64\n\nThe three images were amd64-only, and reached\nDocker Hub only via versioner copying from ECR.\nEach workflow now builds both platforms and\npasses Docker Hub credentials, so the same build\nis pushed to both, with the digest Kosli attests.\n\nasset_builder is amd64-only, but its output is\nCSS/JS text, so the asset stages run on the\nbuild platform and both targets copy the result.\n\nCo-Authored-By: Claude Opus 5.5\n  <noreply@anthropic.com>\n\n* Run the local runner with 16 spares\n\nPre-started spare containers spare test runs the\ncontainer start, so local runs reflect the\nrunner as it is deployed with spares.\n\n---------\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791633198.0,
            "url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=6923c594-deee-4b7c-83e9-3165a9ed",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/239086385550e2c369fd3aa1f656b56f362db8f7...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_git_commit": "239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_fingerprint": "b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:2390863@sha256:b0d1d69124bb75a316f7436a630bf2c5483d6a26e02c9ec709ec9bd3b132fa45",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "239086385550e2c369fd3aa1f656b56f362db8f7",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 15159.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "web",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=89aad915-ff61-4fc0-8352-09d54068",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/54306f735c51413c972b38398da4d0a5fc86d47a...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_fingerprint": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": true,
            "previous_trail_name": "promote-all-41",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 7841.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/5f70df2163e8918675c92251f398bc1a88d0d7a9ce1eef39d1f603525de077b6?artifact_id=25a937bf-2a46-46d2-a6f0-4d125c9d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 889299.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/ee4c2f3bca0b492dbc7024a8db163a70",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3e6678b@sha256:ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
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
                    "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
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
      "fingerprint": "ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
      "creationTimestamp": [
        1791648284
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
      "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=349ebdb8-fe2c-41fb-a05d-49675a91",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/3b4ef042cde981a0668dec70ed3137041a51cbe6...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
        "previous_git_commit": "3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "3b4ef042cde981a0668dec70ed3137041a51cbe6",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 15086.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "template_reference_name": "creator",
          "git_commit": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "commit_url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
          "git_commit_info": {
            "sha1": "3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "message": "Web multi platform and dockerhub (#468)\n\n* Build web, creator, dashboard for amd64 + arm64\n\nThe three images were amd64-only, and reached\nDocker Hub only via versioner copying from ECR.\nEach workflow now builds both platforms and\npasses Docker Hub credentials, so the same build\nis pushed to both, with the digest Kosli attests.\n\nasset_builder is amd64-only, but its output is\nCSS/JS text, so the asset stages run on the\nbuild platform and both targets copy the result.\n\nCo-Authored-By: Claude Opus 5.5\n  <noreply@anthropic.com>\n\n* Run the local runner with 16 spares\n\nPre-started spare containers spare test runs the\ncontainer start, so local runs reflect the\nrunner as it is deployed with spares.\n\n---------\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791633198.0,
            "url": "https://github.com/cyber-dojo/web/commit/3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=349ebdb8-fe2c-41fb-a05d-49675a91",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/3b4ef042cde981a0668dec70ed3137041a51cbe6...3e6678b80d51d7ec4c89d88f46dcee93f27fd6c1",
            "previous_git_commit": "3b4ef042cde981a0668dec70ed3137041a51cbe6",
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/3b4ef042cde981a0668dec70ed3137041a51cbe6",
            "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "3b4ef042cde981a0668dec70ed3137041a51cbe6",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 15086.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "web",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=4bb1dbd0-0ea2-40ee-aae1-a4bbe612",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_fingerprint": "299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3b4ef04@sha256:299aafbad77b4604fd2260ada0659e3f64a770f3411010827087cda34b52dc9e",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-178",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 7768.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb",
          "template_reference_name": "web",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/ee739c0183759b660a740afe28fbbdb20b4c3b434faa48dab975aa8576173efb?artifact_id=8d1e21e9-4f43-465a-8d55-13d4261c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:236898f@sha256:e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "web-e24bd03714d2e583a2196c0eaf82b2aad8eeecf73f29aec58875994b82f0f418",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 889226.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/b0901864b2ba4e5fae7b124fa29c2bd1",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:8442c1b@sha256:b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
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
                    "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
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
      "fingerprint": "b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
      "creationTimestamp": [
        1791648278
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "languages-start-points-ci",
      "git_commit": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
      "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a?artifact_id=87445ff6-7ec9-4337-bf43-0e9b796b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9c8c9cdb74d9aeeda67bae0f4063089bebc99efe...8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
        "previous_git_commit": "9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
        "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
        "previous_fingerprint": "a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9c8c9cd@sha256:a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
        "previous_template_reference_name": "languages-start-points"
      },
      "commit_lead_time": 1154.0,
      "flows": [
        {
          "flow_name": "languages-start-points-ci",
          "trail_name": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
          "template_reference_name": "languages-start-points",
          "git_commit": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
          "commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
          "git_commit_info": {
            "sha1": "8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
            "message": "Merge pull request #295 from cyber-dojo/multi-arch-start-point\n\nBuild the start-point image for amd64 and arm64",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791647124.0,
            "url": "https://github.com/cyber-dojo/languages-start-points/commit/8442c1b837d6dca9e349a6c3401437f11e6bd9f0"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci/artifacts/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a?artifact_id=87445ff6-7ec9-4337-bf43-0e9b796b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/languages-start-points-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/languages-start-points/compare/9c8c9cdb74d9aeeda67bae0f4063089bebc99efe...8442c1b837d6dca9e349a6c3401437f11e6bd9f0",
            "previous_git_commit": "9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
            "previous_git_commit_url": "https://github.com/cyber-dojo/languages-start-points/commit/9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
            "previous_fingerprint": "a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9c8c9cd@sha256:a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "9c8c9cdb74d9aeeda67bae0f4063089bebc99efe",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 1154.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "languages-start-points",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a?artifact_id=d19d8368-9910-475f-93ee-69cf1671",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_fingerprint": "a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:9c8c9cd@sha256:a402a3b392cfc375a6939c822b5d00645e35bbed048a20eb2020ad9904820bda",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-181",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 7762.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a",
          "template_reference_name": "languages-start-points",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b4f37af37368717581502192e3dfc9a55526c528d2f0dd927ff562c856c1a81a?artifact_id=00cfa2f9-4368-4d7d-bba4-43969f59",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:5d1d4b6@sha256:040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "languages-start-points-040bd44819d9e92728fb3b338f6582d4345cd69df769c59e94c61ac0336ad909",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": 889220.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d6e440b28918420bb0710351d9527770",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:b17fe49@sha256:896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
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
                    "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
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
      "fingerprint": "896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
      "creationTimestamp": [
        1791648263
      ],
      "pods": null,
      "annotation": {
        "type": "changed",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f?artifact_id=7b471a07-4b64-4ba5-a309-633e3281",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/69e4ccffb7596125f4bb09886437ca3dee4ac0cf...b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
        "previous_git_commit": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
        "previous_fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 12420.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
          "template_reference_name": "nginx",
          "git_commit": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
          "git_commit_info": {
            "sha1": "b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
            "message": "Merge pull request #184 from cyber-dojo/run-workflow-157\n\nRun workflow to test reusable-actions-workflow called by main which n\u2026",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791635843.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/b17fe49939a63ae7b3996c4bf4f80e2362d537a2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f?artifact_id=7b471a07-4b64-4ba5-a309-633e3281",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/69e4ccffb7596125f4bb09886437ca3dee4ac0cf...b17fe49939a63ae7b3996c4bf4f80e2362d537a2",
            "previous_git_commit": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
            "previous_fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "69e4ccffb7596125f4bb09886437ca3dee4ac0cf",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 12420.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "nginx",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f?artifact_id=30f306f4-9fdf-4b02-87ec-c8a0b6a3",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/4b34724777db6edfc8a04174a9926c595f934dd8...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_fingerprint": "f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:69e4ccf@sha256:f4430327f644e75c547f98d43a148da029760006c572b28d3f957e175bb2352d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-39",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 7747.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f",
          "template_reference_name": "nginx",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/896a2cd49408db95a29b752857d17c6b68df23d8a27b75e70f2e55aa0c3d367f?artifact_id=ab33bace-014e-4b22-b715-5cd5017b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:bd3938c@sha256:aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "nginx-aa63057d266fea8e2336b5d046a85889dd2ec37023cb81a465f6fff6c999c2c5",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 889205.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c504d73fba9b4e3b93940db0f41717a5",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ef6768e@sha256:9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
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
                    "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
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
      "fingerprint": "9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
      "creationTimestamp": [
        1791648700,
        1791648702,
        1791648776
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b?artifact_id=c0267819-47af-42c9-bb43-4470c04f",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/376f811ff50beefefbfda03047b45ba8b62fccc0...ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
        "previous_git_commit": "376f811ff50beefefbfda03047b45ba8b62fccc0",
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/376f811ff50beefefbfda03047b45ba8b62fccc0",
        "previous_fingerprint": "68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:376f811@sha256:68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "376f811ff50beefefbfda03047b45ba8b62fccc0",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 16199.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
          "template_reference_name": "runner",
          "git_commit": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
          "git_commit_info": {
            "sha1": "ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
            "message": "Build runner for amd64 and arm64, push to Hub (#325)\n\nThe runner image was amd64-only, so it could not\nrun natively on arm64 hosts, and reached Docker\nHub only via versioner copying it from ECR.\n\nsecure-docker-build now builds both platforms\nand, given Docker Hub credentials, pushes\ncyberdojo/runner:<tag> from the same build as\nECR, so both hold the digest Kosli attests.\n\nCo-Authored-By: Claude Opus 5.5\n  <noreply@anthropic.com>\n\nCo-authored-by: Claude Opus 5.5 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791632501.0,
            "url": "https://github.com/cyber-dojo/runner/commit/ef6768eefe96ec54dacc1b8cabac1dde2d2f636e"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b?artifact_id=c0267819-47af-42c9-bb43-4470c04f",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/376f811ff50beefefbfda03047b45ba8b62fccc0...ef6768eefe96ec54dacc1b8cabac1dde2d2f636e",
            "previous_git_commit": "376f811ff50beefefbfda03047b45ba8b62fccc0",
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/376f811ff50beefefbfda03047b45ba8b62fccc0",
            "previous_fingerprint": "68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:376f811@sha256:68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "376f811ff50beefefbfda03047b45ba8b62fccc0",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 16199.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "runner",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b?artifact_id=67c17ef1-1ce5-4810-a8b2-98ea3843",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/8c76df3ae03cf8f4d6be40d4af6d550c2e6f1d25",
            "previous_fingerprint": "68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:376f811@sha256:68910f8c3ee153005cc9e2dbf7eec3d41129d98ad05f2c7e89a0f7b263f279e2",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promotion-one-177",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 8184.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b",
          "template_reference_name": "runner",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/9b6ccf0845871128cd22f33e8ec0e0a29b1794e736b5ef783ade3c8bca11c80b?artifact_id=bb82e38e-0574-40e6-ba02-eeb03b0a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/359c98460f5c3aefb136a77eef08d1be4c4ca08d...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_fingerprint": "5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:6131d76@sha256:5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "runner-5cbe7d6eb91af8e485c9c87a2c9abfcada9773e8773da11b002f50639c2b0845",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 889642.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/83a23b5804b04608a64c3b4ef0b3090b",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:afeb2f3@sha256:0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
      "compliant": true,
      "deployments": [],
      "policy_decisions": [
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "production-promotion"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0002"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            }
          ],
          "policy_name": "pull-request"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
                  "exceptions": []
                }
              },
              "satisfied": null,
              "ignored": true,
              "resolutions": [
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null,
                    "for_control": "SDLC-CTRL-0022"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
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
                    "flow_name": "spooler-ci",
                    "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-41",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
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
      "fingerprint": "0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
      "creationTimestamp": [
        1791648279
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "spooler-ci",
      "git_commit": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
      "commit_url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f?artifact_id=bf8d791d-6bcd-4297-b745-328db4df",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/spooler/compare/28636f69be43a7676d61db98b086eaff507d6e9c...afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
        "previous_git_commit": "28636f69be43a7676d61db98b086eaff507d6e9c",
        "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
        "previous_fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
        "previous_template_reference_name": "spooler"
      },
      "commit_lead_time": 15814.0,
      "flows": [
        {
          "flow_name": "spooler-ci",
          "trail_name": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
          "template_reference_name": "spooler",
          "git_commit": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
          "commit_url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
          "git_commit_info": {
            "sha1": "afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
            "message": "Merge pull request #25 from cyber-dojo/spooler-multi-platform-and-dockerhub\n\nBuild spooler for amd64 and arm64, push to Hub",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "",
            "timestamp": 1791632465.0,
            "url": "https://github.com/cyber-dojo/spooler/commit/afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci/artifacts/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f?artifact_id=bf8d791d-6bcd-4297-b745-328db4df",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/spooler-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/spooler/compare/28636f69be43a7676d61db98b086eaff507d6e9c...afeb2f32f34dfb29fc36ecc3eb3aeb602030eec5",
            "previous_git_commit": "28636f69be43a7676d61db98b086eaff507d6e9c",
            "previous_git_commit_url": "https://github.com/cyber-dojo/spooler/commit/28636f69be43a7676d61db98b086eaff507d6e9c",
            "previous_fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "28636f69be43a7676d61db98b086eaff507d6e9c",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 15814.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-41",
          "template_reference_name": "spooler",
          "git_commit": "54306f735c51413c972b38398da4d0a5fc86d47a",
          "commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a",
          "git_commit_info": {
            "sha1": "54306f735c51413c972b38398da4d0a5fc86d47a",
            "message": "Merge pull request #18 from cyber-dojo/promote-one-requires-a-service\n\nFail promote-one when no service is chosen",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1791640516.0,
            "url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/54306f735c51413c972b38398da4d0a5fc86d47a"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f?artifact_id=fc83823c-fb43-48ff-9c08-7b01c297",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/4b34724777db6edfc8a04174a9926c595f934dd8...54306f735c51413c972b38398da4d0a5fc86d47a",
            "previous_git_commit": "4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/4b34724777db6edfc8a04174a9926c595f934dd8",
            "previous_fingerprint": "c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:28636f6@sha256:c162e3974e3067c3902b2574098819f99d35c24d88f57e70efb73d617e1f653d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "promote-all-39",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 7763.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "spooler-0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f",
          "template_reference_name": "spooler",
          "git_commit": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d",
          "git_commit_info": {
            "sha1": "359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "message": "Merge pull request #6 from cyber-dojo/key-uploads-and-trails-on-component-not-repo\n\nTell apart artifacts built by one repo",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1790759058.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/359c98460f5c3aefb136a77eef08d1be4c4ca08d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/0fe7da2f4c8a0afd88f81bb066bbdd30e02e45f4872f6a0a4538f527185d729f?artifact_id=b12fe22b-260b-47aa-9cd3-8ddaf00a",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/30111f180ac4e3611cdbd7d805381a0bb9f53cff...359c98460f5c3aefb136a77eef08d1be4c4ca08d",
            "previous_git_commit": "30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/30111f180ac4e3611cdbd7d805381a0bb9f53cff",
            "previous_fingerprint": "9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/spooler:5e4740c@sha256:9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_trail_name": "spooler-9ef10b455706661560fee5c47aebcb592f0936fdaa1db1a0ad06590c6f39b86f",
            "previous_template_reference_name": "spooler"
          },
          "commit_lead_time": 889221.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/5916af07ea074242b150d7277c036f7e",
        "cluster_name": null,
        "service_name": null
      }
    }
  ],
  "applied_policies": [
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

