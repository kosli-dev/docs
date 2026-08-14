---
title: "kosli get trail"
description: "Get the metadata of a specific trail."
---

## Synopsis

```shell
kosli get trail TRAIL-NAME [flags]
```

Get the metadata of a specific trail.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-f`, `--flow` | string | The Kosli flow name. |
| `-h`, `--help` | bool | help for trail |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json, markdown]. (default "table") |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |

## Live Example

To view a live example of 'kosli get trail' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli get trail dashboard-ci e4757683b74df7033c95aa544a7824b395c2f8bb --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
{
  "name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
  "description": "",
  "git_commit_info": {
    "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
    "message": "Update kosli template with provenance facts+decision (#414)",
    "author": "Jon Jagger <jon@kosli.com>",
    "branch": "main",
    "timestamp": 1783538510.0,
    "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb"
  },
  "origin_url": "https://github.com/cyber-dojo/dashboard/actions/runs/28969474194",
  "user_data": {},
  "repo_ids": [
    "4c546fde-c5ee-4a39-b399-8c71d7e1"
  ],
  "last_modified_at": 1783538679.7988548,
  "created_at": 1783538535.1534083,
  "compliance_status": {
    "status": "COMPLIANT",
    "is_compliant": true,
    "attestations_statuses": [
      {
        "attestation_name": "pull-request",
        "attestation_type": "pull_request",
        "attestation_id": "60045efd-1851-45f4-9b27-5f7ae946",
        "overridden_attestation_id": null,
        "status": "COMPLETE",
        "is_compliant": true,
        "unexpected": false
      }
    ],
    "artifacts_statuses": {
      "dashboard": {
        "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
        "artifact_id": "cc7c618f-d22e-4d95-b6f1-cea4fded",
        "status": "COMPLIANT",
        "is_compliant": true,
        "attestations_statuses": [
          {
            "attestation_name": "provenance-facts",
            "attestation_type": "custom:provenance-facts",
            "attestation_id": "8753765c-0df9-421c-bfe3-c8aa1f8d",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "provenance-decision",
            "attestation_type": "system:decision",
            "attestation_id": "b0786932-6ff7-4359-bb20-1bb43671",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "sbom-facts",
            "attestation_type": "custom:sbom-facts",
            "attestation_id": "7d834d1e-e7de-4890-870c-a783053b",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "sbom-decision",
            "attestation_type": "system:decision",
            "attestation_id": "d37cd3aa-3909-4d0d-a8c3-0c623de1",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "snyk-container-scan",
            "attestation_type": "system:decision",
            "attestation_id": "2e01c56f-18f9-4e75-8b45-f7d5846e",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "rubocop-lint",
            "attestation_type": "junit",
            "attestation_id": "d81b5df8-7c67-42ce-b332-5f10aba5",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "sonarcloud-scan",
            "attestation_type": "sonar",
            "attestation_id": "c955d971-4600-4b45-950f-cd8b3642",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "unit-test",
            "attestation_type": "junit",
            "attestation_id": "084be09c-f101-4a29-985e-ee305d60",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "unit-test-coverage",
            "attestation_type": "generic",
            "attestation_id": "ede0b52b-d56e-474f-b04c-03e6be01",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          }
        ],
        "unexpected": false,
        "evaluated_at": 1783538679.7988548,
        "flow_template_id": "cba69d3f-7f48-4e00-9c23-fb63f98d"
      }
    },
    "evaluated_at": 1783538658.411656,
    "flow_template_id": "cba69d3f-7f48-4e00-9c23-fb63f98d"
  },
  "template": {
    "version": 1,
    "trail": {
      "attestations": [
        {
          "name": "pull-request",
          "type": "pull_request"
        }
      ],
      "artifacts": [
        {
          "name": "dashboard",
          "attestations": [
            {
              "name": "provenance-facts",
              "type": "custom:provenance-facts"
            },
            {
              "name": "provenance-decision",
              "type": "decision"
            },
            {
              "name": "sbom-facts",
              "type": "custom:sbom-facts"
            },
            {
              "name": "sbom-decision",
              "type": "decision"
            },
            {
              "name": "snyk-container-scan",
              "type": "decision"
            },
            {
              "name": "rubocop-lint",
              "type": "junit"
            },
            {
              "name": "sonarcloud-scan",
              "type": "sonar"
            },
            {
              "name": "unit-test",
              "type": "junit"
            },
            {
              "name": "unit-test-coverage",
              "type": "generic"
            }
          ]
        }
      ]
    },
    "content": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: dashboard\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n        - name: sonarcloud-scan\n          type: sonar\n        - name: unit-test\n          type: junit\n        - name: unit-test-coverage\n          type: generic\n"
  },
  "compliance_state": "COMPLIANT",
  "is_compliant": true,
  "events": [
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538535.1534083,
      "type": "trail_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538535.13884,
        "tags": {}
      },
      "setting_user_id": "da5d4ee8-aec0-4264-ab85-c491040c",
      "trail_data_json": {
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
        "name": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "creating_user_id": "da5d4ee8-aec0-4264-ab85-c491040c",
        "description": "",
        "git_commit_info": {
          "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
          "message": "Update kosli template with provenance facts+decision (#414)",
          "author": "Jon Jagger <jon@kosli.com>",
          "branch": "main",
          "timestamp": 1783538510.0,
          "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb"
        },
        "template_id": "cba69d3f-7f48-4e00-9c23-fb63f98d",
        "origin_url": "https://github.com/cyber-dojo/dashboard/actions/runs/28969474194",
        "user_data": "{}",
        "repo_ids": [
          "4c546fde-c5ee-4a39-b399-8c71d7e1"
        ]
      }
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538554.443048,
      "type": "trail_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538554.4352667,
        "tags": {}
      },
      "attestation_type": "pull_request",
      "is_compliant": true,
      "attestation_id": "60045efd-1851-45f4-9b27-5f7ae946",
      "template_reference_name": "pull-request",
      "is_reattestation": null
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538566.412186,
      "type": "trail_attestation_for_artifact_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538566.275227,
        "tags": {}
      },
      "attestation_type": "junit",
      "is_compliant": true,
      "attestation_id": "d81b5df8-7c67-42ce-b332-5f10aba5",
      "template_reference_name": "rubocop-lint",
      "is_reattestation": null,
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538599.9910955,
      "type": "artifact_creation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538599.9776034,
        "tags": {}
      },
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "artifact_id": "cc7c618f-d22e-4d95-b6f1-cea4fded",
      "template_reference_name": "dashboard",
      "git_commit": "e4757683b74df7033c95aa544a7824b395c2f8bb"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538601.4830513,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538601.4712045,
        "tags": {}
      },
      "attestation_type": "custom:provenance-facts",
      "is_compliant": true,
      "attestation_id": "8753765c-0df9-421c-bfe3-c8aa1f8d",
      "template_reference_name": "provenance-facts",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538605.8901985,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538605.7439284,
        "tags": {}
      },
      "attestation_type": "system:decision",
      "is_compliant": true,
      "attestation_id": "b0786932-6ff7-4359-bb20-1bb43671",
      "template_reference_name": "provenance-decision",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538607.5449562,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538607.5226355,
        "tags": {}
      },
      "attestation_type": "custom:sbom-facts",
      "is_compliant": true,
      "attestation_id": "7d834d1e-e7de-4890-870c-a783053b",
      "template_reference_name": "sbom-facts",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538609.6176646,
      "type": "trail_attestation_for_artifact_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538609.6101015,
        "tags": {}
      },
      "attestation_type": "sonar",
      "is_compliant": true,
      "attestation_id": "c955d971-4600-4b45-950f-cd8b3642",
      "template_reference_name": "sonarcloud-scan",
      "is_reattestation": null,
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538612.6819937,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538612.5687785,
        "tags": {}
      },
      "attestation_type": "system:decision",
      "is_compliant": true,
      "attestation_id": "d37cd3aa-3909-4d0d-a8c3-0c623de1",
      "template_reference_name": "sbom-decision",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538656.9102154,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538656.7741516,
        "tags": {}
      },
      "attestation_type": "junit",
      "is_compliant": true,
      "attestation_id": "084be09c-f101-4a29-985e-ee305d60",
      "template_reference_name": "unit-test",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538658.411656,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538658.4029927,
        "tags": {}
      },
      "attestation_type": "generic",
      "is_compliant": true,
      "attestation_id": "ede0b52b-d56e-474f-b04c-03e6be01",
      "template_reference_name": "unit-test-coverage",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538679.7988548,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "e4757683b74df7033c95aa544a7824b395c2f8bb",
        "message": "Update kosli template with provenance facts+decision (#414)",
        "author": "Jon Jagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1783538510.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/e4757683b74df7033c95aa544a7824b395c2f8bb",
        "parents": null,
        "verified": null,
        "signature_state": null
      },
      "repo_info": {
        "inner_id": "4c546fde-c5ee-4a39-b399-8c71d7e1",
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "repo_id": "290597708",
        "name": "cyber-dojo/dashboard",
        "url": "https://github.com/cyber-dojo/dashboard",
        "provider": "github",
        "description": null,
        "vcs_instance": null,
        "namespace_path": null,
        "additional_info": null,
        "created_at": 1768639963.3866346,
        "last_modified_at": 1783538679.7007914,
        "tags": {}
      },
      "attestation_type": "system:decision",
      "is_compliant": true,
      "attestation_id": "2e01c56f-18f9-4e75-8b45-f7d5846e",
      "template_reference_name": "snyk-container-scan",
      "is_reattestation": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "artifact_name": "244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:e475768",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783538844.1212204,
      "type": "artifact_started_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 7637,
      "replica_number": 1,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783618198.4632592,
      "type": "artifact_started_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "environment_id": "73965c45-e9a1-4bb9-ad01-dc5a526f",
      "environment_name": "aws-prod",
      "snapshot_index": 4974,
      "replica_number": 1,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1783660164.0318449,
      "type": "artifact_stopped_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 7657,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "39e622ec-b847-447b-b7f8-7e9ea745",
      "timestamp": 1784356018.5146132,
      "type": "artifact_stopped_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "54f6da185cd0f0ef001a0b33c099565fa736546562e0411f706832e72dca47bb",
      "environment_id": "73965c45-e9a1-4bb9-ad01-dc5a526f",
      "environment_name": "aws-prod",
      "snapshot_index": 5044,
      "template_reference_name": "dashboard"
    }
  ],
  "created_by": "ci-pipelines",
  "flow": {
    "name": "dashboard-ci",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/dashboard",
      "kind": "build",
      "env": "aws-beta"
    }
  },
  "external_urls": null,
  "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/trails/e4757683b74df7033c95aa544a7824b395c2f8bb"
}
```

</div>
</Accordion>

