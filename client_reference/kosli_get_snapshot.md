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
  "index": 4661,
  "is_latest": true,
  "next_snapshot_timestamp": null,
  "artifact_compliance_count": {
    "true": 10,
    "false": 0,
    "null": 0
  },
  "timestamp": 1780207378.4202626,
  "type": "ECS",
  "compliant": true,
  "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/4661",
  "artifacts": [
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:3a06618@sha256:bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-19",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
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
      "fingerprint": "bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
      "creationTimestamp": [
        1779648032
      ],
      "pods": null,
      "annotation": {
        "type": "updated-provenance",
        "was": 1,
        "now": 1
      },
      "flow_name": "creator-ci",
      "git_commit": "3a066186b7fbbcec0130419518c5bb81b50e71db",
      "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=2eb0aee4-1eca-40b7-a914-1f9e9338",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
      "deployment_diff": {
        "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4...3a066186b7fbbcec0130419518c5bb81b50e71db",
        "previous_git_commit": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
        "previous_fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
        "previous_trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
        "previous_template_reference_name": "creator"
      },
      "commit_lead_time": 34847.0,
      "flows": [
        {
          "flow_name": "creator-ci",
          "trail_name": "3a066186b7fbbcec0130419518c5bb81b50e71db",
          "template_reference_name": "creator",
          "git_commit": "3a066186b7fbbcec0130419518c5bb81b50e71db",
          "commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db",
          "git_commit_info": {
            "sha1": "3a066186b7fbbcec0130419518c5bb81b50e71db",
            "message": "Merge branch 'remove-v0-group-join-test' into 'main'\n\nRemove v0 group join test\n\nSee merge request cyber-dojo/creator!249",
            "author": "Jon Jagger <jon@jaggersoft.com>",
            "branch": "main",
            "timestamp": 1779613185.0,
            "url": "https://gitlab.com/cyber-dojo/creator/-/commit/3a066186b7fbbcec0130419518c5bb81b50e71db"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=2eb0aee4-1eca-40b7-a914-1f9e9338",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/creator-ci",
          "deployment_diff": {
            "diff_url": "https://gitlab.com/cyber-dojo/creator/-/compare/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4...3a066186b7fbbcec0130419518c5bb81b50e71db",
            "previous_git_commit": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
            "previous_fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://gitlab.com/cyber-dojo/creator/-/commit/dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
            "previous_trail_name": "dba05d3ce9e8013805dc4c8ddeb31cff87acb3d4",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 34847.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-19",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=41c0e868-dca1-4d61-9613-adfcf597",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/010eb0ade7ba91559181b4b35a85f2fb175e8af8...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/010eb0ade7ba91559181b4b35a85f2fb175e8af8",
            "previous_trail_name": "promote-all-16",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": 283608.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
          "template_reference_name": "creator",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=9515c3be-2901-4f45-b78b-03a37312",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -225150.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "creator-bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e",
          "template_reference_name": "creator",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/bd66850aada99245f34fe2302aa00023d00c8165e8409e4f7be82f8fd768797e?artifact_id=792c3a97-6288-4202-9a5a-f22e47e1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:dba05d3@sha256:87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "creator-87c2ae3209e66bfb2470ffccfb9bff93a47bc7cbb215c2a68261bf13211dda41",
            "previous_template_reference_name": "creator"
          },
          "commit_lead_time": -225150.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/e4fb3be7654d4b199443b658adc8e845",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:2643878@sha256:2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-61",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
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
      "fingerprint": "2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
      "creationTimestamp": [
        1779809079
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "nginx-ci",
      "git_commit": "26438788f75a9a39db985b87100b9b32a2d962a2",
      "commit_url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=853d1420-fd3e-439b-ab85-549ba34d",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/nginx/compare/fd9c3f5f40529596ffe8641b379e46bba036cf5e...26438788f75a9a39db985b87100b9b32a2d962a2",
        "previous_git_commit": "fd9c3f5f40529596ffe8641b379e46bba036cf5e",
        "previous_fingerprint": "a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fd9c3f5@sha256:a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/fd9c3f5f40529596ffe8641b379e46bba036cf5e",
        "previous_trail_name": "fd9c3f5f40529596ffe8641b379e46bba036cf5e",
        "previous_template_reference_name": "nginx"
      },
      "commit_lead_time": 77144.0,
      "flows": [
        {
          "flow_name": "nginx-ci",
          "trail_name": "26438788f75a9a39db985b87100b9b32a2d962a2",
          "template_reference_name": "nginx",
          "git_commit": "26438788f75a9a39db985b87100b9b32a2d962a2",
          "commit_url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2",
          "git_commit_info": {
            "sha1": "26438788f75a9a39db985b87100b9b32a2d962a2",
            "message": "Merge pull request #124 from cyber-dojo/udpate-base-image\n\nDockerfile: update base image",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779731935.0,
            "url": "https://github.com/cyber-dojo/nginx/commit/26438788f75a9a39db985b87100b9b32a2d962a2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=853d1420-fd3e-439b-ab85-549ba34d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/nginx-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/nginx/compare/fd9c3f5f40529596ffe8641b379e46bba036cf5e...26438788f75a9a39db985b87100b9b32a2d962a2",
            "previous_git_commit": "fd9c3f5f40529596ffe8641b379e46bba036cf5e",
            "previous_fingerprint": "a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fd9c3f5@sha256:a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/nginx/commit/fd9c3f5f40529596ffe8641b379e46bba036cf5e",
            "previous_trail_name": "fd9c3f5f40529596ffe8641b379e46bba036cf5e",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 77144.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-61",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=bc318c45-c22c-4885-a963-d6703684",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:fd9c3f5@sha256:a4234758eea2da8831d46aaf5d000f958ef5c1782e10ea55f28e7f2a61a34370",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promote-all-20",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": 444655.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
          "template_reference_name": "nginx",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=d9ddc2c2-26fd-44a0-b31b-a17eb7ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/nginx:a275152@sha256:06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "nginx-06bf15ad0c4f03b40ff2c54528d89c18c0d6809aaa3d9c87c9fcec558a57cad0",
            "previous_template_reference_name": "nginx"
          },
          "commit_lead_time": -64103.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "nginx-2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831",
          "template_reference_name": "nginx",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/2a4818ad632c3625cdc69012aa4671b45dfff0fe62ac1d2fbdd149206e624831?artifact_id=1cf57ab2-8c64-49ff-abc7-afa680ba",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -64103.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/c8e27d9a3e904351819cbb1dbdd2f0ad",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:f2e8fa7@sha256:6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "differ-ci",
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-20",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
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
      "fingerprint": "6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
      "creationTimestamp": [
        1779731496
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "differ-ci",
      "git_commit": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
      "commit_url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=02347f6a-ae14-4473-879e-7d4c10b7",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/differ/compare/75e174eb5045e8dd5c72079d2e2032a1488c51ef...f2e8fa718ca3b72527625bd182beb2950bea3a77",
        "previous_git_commit": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
        "previous_fingerprint": "68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:75e174e@sha256:68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef",
        "previous_trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
        "previous_template_reference_name": "differ"
      },
      "commit_lead_time": 33004.0,
      "flows": [
        {
          "flow_name": "differ-ci",
          "trail_name": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
          "template_reference_name": "differ",
          "git_commit": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
          "commit_url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77",
          "git_commit_info": {
            "sha1": "f2e8fa718ca3b72527625bd182beb2950bea3a77",
            "message": "Remove saver dependency from differ: callers now pass was_files/now_f\u2026 (#386)\n\n* Remove saver dependency from differ: callers now pass was_files/now_files directly\n\nThe differ no longer fetches file contents from saver using (id, was_index,\nnow_index). Callers pass the file contents directly as (was_files:, now_files:).\nThis removes the saver client from the differ entirely, along with all\nsaver-backed test data and the tests that depended on it.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Fix Rubocop violations in html_demo.rb and prober.rb\n\nExtract was_files as a top-level frozen constant (WAS_FILES) to avoid\nlong escaped string literals that triggered the line-length cop. Collapse\nProber#initialize to a single line and suppress Style/RedundantInitialize,\nwhich must be kept to satisfy the klass.new(@externals) contract in get_json.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779698492.0,
            "url": "https://github.com/cyber-dojo/differ/commit/f2e8fa718ca3b72527625bd182beb2950bea3a77"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=02347f6a-ae14-4473-879e-7d4c10b7",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/differ/compare/75e174eb5045e8dd5c72079d2e2032a1488c51ef...f2e8fa718ca3b72527625bd182beb2950bea3a77",
            "previous_git_commit": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
            "previous_fingerprint": "68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:75e174e@sha256:68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/differ/commit/75e174eb5045e8dd5c72079d2e2032a1488c51ef",
            "previous_trail_name": "75e174eb5045e8dd5c72079d2e2032a1488c51ef",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 33004.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promote-all-20",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=a62fef1c-c683-4759-9dee-ca5cb000",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:75e174e@sha256:68fc5e6744afb8a2df828a12d430d9081adf052a3b21d79069d6895edb423b6d",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": 367072.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
          "template_reference_name": "differ",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=a638df97-098a-4eee-82ba-bec47232",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:fd71a71@sha256:dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "differ-dc7e55a08ec45a9ab4a2323ce7b1aae3a9f4a0742bb44b06b7bc1370f5c11a6b",
            "previous_template_reference_name": "differ"
          },
          "commit_lead_time": -141686.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "differ-6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d",
          "template_reference_name": "differ",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/6c4c72c37b15c0261309b65400bb60d78b2071c9f8a82d2ec6d050399834762d?artifact_id=9f1d5da5-8d17-4e27-a194-e40fa270",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -141686.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d520628e976a400ba4edf0dccb6a6049",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:0a839a4@sha256:3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-60",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
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
      "fingerprint": "3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
      "creationTimestamp": [
        1779639453
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "dashboard-ci",
      "git_commit": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
      "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=4fdc2f6b-8933-4edd-959d-0bd53cbf",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/dashboard/compare/18fb2702a5109248489b8a562399101f803b3d8d...0a839a472d41bf860d1d6dc3ded45ff63144018d",
        "previous_git_commit": "18fb2702a5109248489b8a562399101f803b3d8d",
        "previous_fingerprint": "e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:18fb270@sha256:e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d",
        "previous_trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
        "previous_template_reference_name": "dashboard"
      },
      "commit_lead_time": 995.0,
      "flows": [
        {
          "flow_name": "dashboard-ci",
          "trail_name": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
          "template_reference_name": "dashboard",
          "git_commit": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
          "commit_url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d",
          "git_commit_info": {
            "sha1": "0a839a472d41bf860d1d6dc3ded45ff63144018d",
            "message": "Fix diff_summary route - remove erroneous /dashboard prefix (#382)\n\nThe Sinatra app's routes must not carry the /dashboard prefix since\nthe reverse proxy strips it before forwarding. /dashboard/diff_summary\nin app.rb would only be reachable at /dashboard/dashboard/diff_summary\non the deployed site, causing 404s. The JS correctly calls\n/dashboard/diff_summary; the app route must be /diff_summary to match.\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779638458.0,
            "url": "https://github.com/cyber-dojo/dashboard/commit/0a839a472d41bf860d1d6dc3ded45ff63144018d"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=4fdc2f6b-8933-4edd-959d-0bd53cbf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/dashboard/compare/18fb2702a5109248489b8a562399101f803b3d8d...0a839a472d41bf860d1d6dc3ded45ff63144018d",
            "previous_git_commit": "18fb2702a5109248489b8a562399101f803b3d8d",
            "previous_fingerprint": "e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:18fb270@sha256:e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/dashboard/commit/18fb2702a5109248489b8a562399101f803b3d8d",
            "previous_trail_name": "18fb2702a5109248489b8a562399101f803b3d8d",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 995.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-60",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=12c15e64-164b-4559-840f-82590dd4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:18fb270@sha256:e3b3dafc318a980b558ce219fbec89c32588bf6801d11af1c42f07b0e7e05e78",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promotion-one-55",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": 275029.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
          "template_reference_name": "dashboard",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=4b4f4e55-96ce-4cd4-803b-8020d243",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:9cd9145@sha256:ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "dashboard-ce124c6f3f157fb1e6e456cef8d7e518997b4612bd0f40608a5f2728b2d9a0c7",
            "previous_template_reference_name": "dashboard"
          },
          "commit_lead_time": -233729.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "dashboard-3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39",
          "template_reference_name": "dashboard",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/3e17f5432489791b25c9b30a879b5542ca0999ef5597cab8c8485a30ebca8d39?artifact_id=a7f12e07-a3a1-463a-9f47-8dadf37d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -233729.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/f3096d84702840fe89feb1fbd3bde576",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:d9ac74a@sha256:b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "web-ci",
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-59",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
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
      "fingerprint": "b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
      "creationTimestamp": [
        1779625987,
        1779625987,
        1779625987
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "web-ci",
      "git_commit": "d9ac74a950cadda60541db9781e9458832ffd6f8",
      "commit_url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=045a2c84-f7fc-4601-96f5-0f068ec4",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/web/compare/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847...d9ac74a950cadda60541db9781e9458832ffd6f8",
        "previous_git_commit": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
        "previous_fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
        "previous_trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
        "previous_template_reference_name": "web"
      },
      "commit_lead_time": 832.0,
      "flows": [
        {
          "flow_name": "web-ci",
          "trail_name": "d9ac74a950cadda60541db9781e9458832ffd6f8",
          "template_reference_name": "web",
          "git_commit": "d9ac74a950cadda60541db9781e9458832ffd6f8",
          "commit_url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8",
          "git_commit_info": {
            "sha1": "d9ac74a950cadda60541db9781e9458832ffd6f8",
            "message": "Route diff calls through kata, improve review navigation UX (#349)\n\n* Route diff calls through kata, improve review navigation UX\n\nReplace direct browser-to-differ calls for diff_summary and diff_lines\nwith kata/diff_summary and kata/diff_lines routes backed by the saver\nservice, keeping all external service calls server-side.\n\nRemove the yin-yang wait spinner from review getJSON calls. Add smooth\nfadeTo transitions when navigating within the review page, with file and\noutput refreshes sequenced so they are never both visible at the same time.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Update tests to use v2 katas only\n\nThe saver no longer supports writes on v0/v1 katas, so all tests must\ncreate v2 katas. starter_manifest now explicitly sets version=2 and\nnormalises visible_files to hash format. stdout/stderr are passed as\n{content, truncated} hashes rather than plain strings, and status is\ncompared as a string since v2 stores it as a plain file. The v_tests\nversioning scaffolding (v_test?, v_tests, captured_stdout loop) is\nremoved entirely. Fb9824 (saver-outage gap test) is deleted because v2\nenforces strictly sequential indexes. Fb9825 and Fb9860 are updated to\nuse result['next_index'] rather than hardcoded indexes, as v2 may\ninsert file_edit events that consume index slots.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Verify diff routes have test coverage at service and controller layers\n\nThe diff_lines and diff_summary routes added in the previous commit had no\ntests. These smoke tests confirm the routes work: after editing hiker.sh\nbetween two traffic-light events, both endpoints correctly report 1 changed\nfile (with expected line counts) and 4 unchanged files.\n\nAlso removes the unused html() helper from AppControllerTestBase.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Avoid spurious option_set write on page load\n\nsetupPrediction called predictOff() which persisted the value to the\nserver on every page load, even when nothing had changed. Split into\napplyPredictOn/applyPredictOff (UI only) and keep predictOn/predictOff\nfor the user-interaction path (persist then apply). setupPrediction now\ncalls the apply-only variants so page load never triggers a write.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Pre-pull kata image before tests run to fix flaky CI\n\nThe runner's pull_image endpoint is async: calling it from inside the\ntest left the image still downloading when run_cyber_dojo_sh was called,\ncausing a timeout. Instead, pull the image synchronously on the host\nbefore the test suite starts. The runner shares the host Docker socket,\nso an image pulled on the host is immediately available to it.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Declare platform: linux/amd64 on all compose services\n\nSuppresses the \"image's platform does not match the detected host\nplatform\" warning when running on arm64 hosts (Apple Silicon, Graviton).\nAlso pass --quiet to the pre-pull to silence Docker Scout output.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Fix 2BD812: pre-pull kata image before runner starts, not after\n\nThe runner's config.ru runs docker image ls at startup and pre-loads\nevery present image into the in-memory @pulled set before forking Puma\nworkers. The previous fix called pull_runner_test_image inside\nrun_tests_in_container(), which runs after containers_up -- so the\nrunner had already forked with an empty @pulled for the kata image.\nEvery worker would see the image as unknown, kick off its own async\npull, and return 'pulling' immediately.\n\nMoving the pull to before containers_up means the image is present when\nthe runner starts, picked up by docker image ls in config.ru, and\ninherited by all workers before any test runs.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Use explicit requires\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779625155.0,
            "url": "https://github.com/cyber-dojo/web/commit/d9ac74a950cadda60541db9781e9458832ffd6f8"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=045a2c84-f7fc-4601-96f5-0f068ec4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/web-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/web/compare/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847...d9ac74a950cadda60541db9781e9458832ffd6f8",
            "previous_git_commit": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
            "previous_fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/web/commit/a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
            "previous_trail_name": "a190e53bf7fffbdfbb1b3d4fdf826e47c906e847",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 832.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-59",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=4f0a45f1-fa30-4100-afa7-3aabcc5c",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": 261563.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
          "template_reference_name": "web",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=c8d82f55-edb9-4992-8ca8-a7be9c00",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/web:a190e53@sha256:870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "web-870605b3cce93df2b5a3379aef57550a66ac4ce79c5a72e186c1a0fc503a31f4",
            "previous_template_reference_name": "web"
          },
          "commit_lead_time": -247195.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "web-b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac",
          "template_reference_name": "web",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/b3d32cebf352c66af4980a905f46a5f3d8ada0ddde55048499fa5dfe0fd2daac?artifact_id=6b9c29bd-738e-4738-acca-6588a980",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -247195.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/d4773e1b52b14b2cb7b7971ca06a1b26",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:a11b758@sha256:a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "saver-ci",
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-58",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
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
      "fingerprint": "a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
      "creationTimestamp": [
        1779624714
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 1,
        "now": 1
      },
      "flow_name": "saver-ci",
      "git_commit": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
      "commit_url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=f723473e-93e9-4367-9110-76bbc5a1",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/saver/compare/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38...a11b7588b2d2333e1346f1a2bb100395f11f42d2",
        "previous_git_commit": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
        "previous_fingerprint": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
        "previous_trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
        "previous_template_reference_name": "saver"
      },
      "commit_lead_time": 1958.0,
      "flows": [
        {
          "flow_name": "saver-ci",
          "trail_name": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
          "template_reference_name": "saver",
          "git_commit": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
          "commit_url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2",
          "git_commit_info": {
            "sha1": "a11b7588b2d2333e1346f1a2bb100395f11f42d2",
            "message": "Diff via differ (#381)\n\n* Delegate diff_lines and diff_summary to the differ service\n\nWires differ as an external service in saver (client class, externals\naccessor, docker-compose depends_on, hostname override) and introduces\na shared DifferDiff module. Kata_v0 and Kata_v1 now delegate diff_lines\nand diff_summary to differ rather than raising NoLongerImplementedError.\nTests updated to expect actual diff results with string keys.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Symbolize differ HTTP responses so v0/v1 diffs match v2's symbol key format\n\nThe HTTP differ service returns string-keyed hashes, but the git-based v2\nimplementation uses Ruby symbol keys throughout. DifferDiff now converts the\nresponse so all three versions present a consistent interface to callers.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Reorganise diff tests by version and port all differ use cases as v2 tests\n\nReplace the separate diff_lines/diff_summary test files with per-version\nfiles (kata_diff_v0.rb, kata_diff_v1.rb) and a comprehensive v2 test file\n(kata_diff.rb) that ports all use cases from the differ service's own test\nsuite.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n* Add client diff tests per version, matching server test structure\n\nSplit v0/v1 client diff tests into separate files, consolidate v2 tests\ninto kata_diff_v2.rb covering all 16 differ use-cases. Fix class names\nin server v0/v1 tests and replace assert_nil with refute key? to\ncorrectly distinguish absent keys from nil values.\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>\n\n---------\n\nCo-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779622756.0,
            "url": "https://github.com/cyber-dojo/saver/commit/a11b7588b2d2333e1346f1a2bb100395f11f42d2"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=f723473e-93e9-4367-9110-76bbc5a1",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/saver-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/saver/compare/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38...a11b7588b2d2333e1346f1a2bb100395f11f42d2",
            "previous_git_commit": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
            "previous_fingerprint": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/saver/commit/e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
            "previous_trail_name": "e0a34b9fb2ad62a74dcbd2bf83890c6abdff4e38",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 1958.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-58",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=085daa97-bc5f-4dd5-8311-5fcc09f4",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_fingerprint": "312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:e0a34b9@sha256:312f321678e102b82d880d6692dfa6cde9ff15ddb89c894371b26fa522753534",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/5fd1b6bba27771e4c93b8c29b3ff69465dff1c26",
            "previous_trail_name": "promote-all-18",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": 260290.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
          "template_reference_name": "saver",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=a586a19f-16b2-4068-a338-6ac1789b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/saver:42c8baf@sha256:e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "saver-e753a48a8a8f2a3a0b3c8429e786fa543d4c3298ed28a369cf7381435f113a1a",
            "previous_template_reference_name": "saver"
          },
          "commit_lead_time": -248468.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "saver-a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc",
          "template_reference_name": "saver",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a6cf2805f1dd2105257cc0febeb475f707b7de3ee664d172957f71943b64c4bc?artifact_id=14e4b060-a46c-4135-a957-a20e8316",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -248468.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/456a50433e7d4f67a4fed6df2017445e",
        "cluster_name": null,
        "service_name": null
      }
    },
    {
      "name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:576bf1d@sha256:afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "runner-ci",
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": "COMPLIANT"
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
                    "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promotion-one-57",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-beta-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
                    "artifact_status": null
                  }
                },
                {
                  "type": "rule_not_applicable",
                  "context": {
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
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
      "fingerprint": "afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
      "creationTimestamp": [
        1779606189,
        1779606189,
        1779606194
      ],
      "pods": null,
      "annotation": {
        "type": "unchanged",
        "was": 3,
        "now": 3
      },
      "flow_name": "runner-ci",
      "git_commit": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
      "commit_url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
      "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=3884ff27-d621-48bf-8c89-3228169b",
      "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
      "deployment_diff": {
        "diff_url": "https://github.com/cyber-dojo/runner/compare/8ddbce96e5c898779c653c1ac1872fb5643a6bc2...576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
        "previous_git_commit": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
        "previous_fingerprint": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
        "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
        "previous_artifact_compliance_state": "COMPLIANT",
        "previous_running": false,
        "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
        "previous_trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
        "previous_template_reference_name": "runner"
      },
      "commit_lead_time": 89240.0,
      "flows": [
        {
          "flow_name": "runner-ci",
          "trail_name": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
          "template_reference_name": "runner",
          "git_commit": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
          "commit_url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
          "git_commit_info": {
            "sha1": "576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
            "message": "Merge pull request #237 from cyber-dojo/assess-new-ssh-cves\n\nAssess 12 new x/crypto/ssh CVEs; extend all .snyk expiries to 2026-06-21",
            "author": "Jon Jagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779516949.0,
            "url": "https://github.com/cyber-dojo/runner/commit/576bf1dcccc1e6fcb56da1e6ac0a14857c9496db"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=3884ff27-d621-48bf-8c89-3228169b",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/runner-ci",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/runner/compare/8ddbce96e5c898779c653c1ac1872fb5643a6bc2...576bf1dcccc1e6fcb56da1e6ac0a14857c9496db",
            "previous_git_commit": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
            "previous_fingerprint": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/runner/commit/8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
            "previous_trail_name": "8ddbce96e5c898779c653c1ac1872fb5643a6bc2",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 89240.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "production-promotion",
          "trail_name": "promotion-one-57",
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
          "html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=04505430-f51d-4f2d-92d2-d0d7ef65",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/production-promotion",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/compare/0f823ea52be90061b69b3f8f6056ca1203ac3d81...0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_git_commit": "0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_fingerprint": "d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:8ddbce9@sha256:d22738a128115e2248092a527174e848cdb04f48b11219facf073fb04fc69f5a",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/aws-prod-co-promotion/commit/0f823ea52be90061b69b3f8f6056ca1203ac3d81",
            "previous_trail_name": "promotion-one-56",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": 241765.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
          "template_reference_name": "runner",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=34799212-74db-427e-85d0-7f3796fc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/runner:ff9225b@sha256:1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "runner-1eaf5e79b9339afee08235095190bdfde9907ec3c4190ef4a2b77c82a6f36f57",
            "previous_template_reference_name": "runner"
          },
          "commit_lead_time": -266993.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "runner-afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe",
          "template_reference_name": "runner",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/afecf29dd8c14dd39a5bfff6b7a98a2c39cdd5550f3ce7cad81c7401c9134ebe?artifact_id=505459d7-6416-4c99-bfe6-260073bf",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -266993.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/bc6c6a19b4de4b65b00a515e801a0da2",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "custom-start-points-ci",
                    "trail_name": "a300e4c15cff321ef952a60bbc3a4729772a2419",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
                    "artifact_status": "COMPLIANT"
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
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
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
          "template_reference_name": "custom-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=55fc36e9-2e0d-44ca-aaf1-940d06ca",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/custom-start-points:3f0c4e5@sha256:dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "custom-start-points-dc03284d20b98563dc4e57c1a6f0ca76e0abdf151677ddfd6612bdace9bc5473",
            "previous_template_reference_name": "custom-start-points"
          },
          "commit_lead_time": -511304.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "custom-start-points-434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d",
          "template_reference_name": "custom-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/434d14680ac3762f42c8ee761b801d8202776cf49389572e351955741b89be7d?artifact_id=f2908727-13d5-478b-a50f-64652174",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": null,
          "commit_lead_time": -511304.0,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "exercises-start-points-ci",
                    "trail_name": "545cccbc91f4030fb4004421e1076bd7c2abbc93",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
                    "artifact_status": "COMPLIANT"
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
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
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
          "template_reference_name": "exercises-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=645eb6d7-a2b4-4eb0-9196-7f586e5d",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:49dc284@sha256:3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "exercises-start-points-3db8f47104744eab8919b12e9ef85caaa29f8c44521bdc7f2ef3f7ee4c6629d7",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -511655.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "exercises-start-points-a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90",
          "template_reference_name": "exercises-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/a1e2d8e458a3813b1f8ab835befba1c1dea56a6fcc6ae2e165e7d7c6e3665c90?artifact_id=699d8d42-2067-42e8-bbfa-20aa131e",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/exercises-start-points:f3cf3ba@sha256:f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "exercises-start-points-f08c1b6607812ab5357032dd6acbf94348247d37901a409c721696b6d11ba6e4",
            "previous_template_reference_name": "exercises-start-points"
          },
          "commit_lead_time": -511655.0,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
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
                    "flow_name": "languages-start-points-ci",
                    "trail_name": "16d155bdd120fe5a926504069dd18a98b8275fa8",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": null
                  }
                }
              ]
            },
            {
              "rule": {
                "type": "trail-compliance",
                "definition": {
                  "required": false,
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
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
                    "artifact_status": "COMPLIANT"
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
                  "type": "rule_satisfied",
                  "context": {
                    "flow_name": "production-promotion",
                    "trail_name": "promote-all-18",
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
                    "flow_name": "snyk-aws-prod-per-artifact",
                    "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
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
        },
        {
          "flow_name": "snyk-aws-beta-per-artifact",
          "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
          "template_reference_name": "languages-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=96fa8263-a57e-42e2-87d8-6a8fbdfc",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-beta-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/4cca3cf991dc8340b82c03e0a80b7b7a1b136bda",
            "previous_trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -511666.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        },
        {
          "flow_name": "snyk-aws-prod-per-artifact",
          "trail_name": "languages-start-points-83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd",
          "template_reference_name": "languages-start-points",
          "git_commit": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06",
          "git_commit_info": {
            "sha1": "822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "message": "The write permission - the find-snyk-vulns job only needs read permission",
            "author": "JonJagger <jon@kosli.com>",
            "branch": "main",
            "timestamp": 1779873182.0,
            "url": "https://github.com/cyber-dojo/snyk-scanning/commit/822a5831653b0901ce5256c6e16d7eedb63ebc06"
          },
          "html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact/artifacts/83a90c5556aa83e18b36983267ed9d160f665cb35d9fb0572b0f7c410de5e2bd?artifact_id=4c8f5e58-b817-4a3c-8dfd-d1059ccb",
          "flow_html_url": "https://app.kosli.com/cyber-dojo/flows/snyk-aws-prod-per-artifact",
          "deployment_diff": {
            "diff_url": "https://github.com/cyber-dojo/snyk-scanning/compare/60fd5bffe45bc9618e81fabf8dd6793f92d10817...822a5831653b0901ce5256c6e16d7eedb63ebc06",
            "previous_git_commit": "60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_fingerprint": "61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/languages-start-points:20ff3f9@sha256:61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_artifact_compliance_state": "COMPLIANT",
            "previous_running": false,
            "previous_git_commit_url": "https://github.com/cyber-dojo/snyk-scanning/commit/60fd5bffe45bc9618e81fabf8dd6793f92d10817",
            "previous_trail_name": "languages-start-points-61efd6bdd33f8aefaca42f60b29303634cd82c912eecbce570abe2eca9bd20c7",
            "previous_template_reference_name": "languages-start-points"
          },
          "commit_lead_time": -511666.0,
          "artifact_compliance_in_flow": true,
          "flow_reasons_for_non_compliance": []
        }
      ],
      "ecs_context": {
        "task_arn": "arn:aws:ecs:eu-central-1:274425519734:task/app/27516a6e0f704dd0a4ccf20e2b5f72cc",
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

