---
title: "kosli get trail"
beta: false
deprecated: false
description: "Get the metadata of a specific trail."
---

## Synopsis

```shell
kosli get trail TRAIL-NAME [flags]
```

Get the metadata of a specific trail.

## Flags
| Flag | Description |
| :--- | :--- |
|    -f, --flow string  |  The Kosli flow name.  |
|    -h, --help  |  help for trail  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. 'http://proxy-server-ip:proxy-port'  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |

## Live Example

To view a live example of 'kosli get trail' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli get trail dashboard-ci 1159a6f1193150681b8484545150334e89de6c1c --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
{
  "name": "1159a6f1193150681b8484545150334e89de6c1c",
  "description": "zhelezovartem - ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
  "git_commit_info": {
    "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
    "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
    "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
    "branch": "main",
    "timestamp": 1711534976.0,
    "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c"
  },
  "origin_url": "https://github.com/cyber-dojo/dashboard/actions/runs/8450201221",
  "user_data": {},
  "repo_ids": [],
  "last_modified_at": 1714814180.0268202,
  "created_at": 1711534991.83214,
  "compliance_status": {
    "status": "COMPLIANT",
    "is_compliant": true,
    "attestations_statuses": [
      {
        "attestation_name": "pull-request",
        "attestation_type": null,
        "attestation_id": "76a44125-eccc-4fb7-8260-d4ff1866",
        "overridden_attestation_id": null,
        "status": "COMPLETE",
        "is_compliant": true,
        "unexpected": false
      }
    ],
    "artifacts_statuses": {
      "dashboard": {
        "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
        "artifact_id": "8803e410-8ab6-4ba7-af7a-4c769a92",
        "status": "COMPLIANT",
        "is_compliant": true,
        "attestations_statuses": [
          {
            "attestation_name": "aws-beta-snyk-scan",
            "attestation_type": null,
            "attestation_id": "60bde45d-4724-4c46-a963-85fe1972",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": true
          },
          {
            "attestation_name": "aws-prod-snyk-scan",
            "attestation_type": null,
            "attestation_id": "333725e9-e82b-4a22-a81c-721adbae",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": true
          },
          {
            "attestation_name": "snyk-container-scan",
            "attestation_type": null,
            "attestation_id": "70421c36-d79f-4813-8635-e77b760a",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "snyk-code-scan",
            "attestation_type": null,
            "attestation_id": "bb3acddd-5336-4b6a-a7ea-e5b3e972",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          },
          {
            "attestation_name": "lint",
            "attestation_type": null,
            "attestation_id": "d3752b67-aefc-444c-a7dc-8115c5ef",
            "overridden_attestation_id": null,
            "status": "COMPLETE",
            "is_compliant": true,
            "unexpected": false
          }
        ],
        "unexpected": false,
        "evaluated_at": 1714814180.0264866,
        "flow_template_id": null
      }
    },
    "evaluated_at": 1714814180.0265083,
    "flow_template_id": "cd1860d5-dc06-41e7-9a3b-be078e7f"
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
              "name": "lint",
              "type": "generic"
            },
            {
              "name": "snyk-code-scan",
              "type": "snyk"
            },
            {
              "name": "snyk-container-scan",
              "type": "snyk"
            }
          ]
        }
      ]
    },
    "content": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: dashboard\n      attestations:\n        - name: lint\n          type: generic\n        - name: snyk-code-scan\n          type: snyk\n        - name: snyk-container-scan\n          type: snyk\n"
  },
  "compliance_state": "COMPLIANT",
  "is_compliant": true,
  "events": [
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711534991.83214,
      "type": "trail_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "setting_user_id": "da5d4ee8-aec0-4264-ab85-c491040c",
      "trail_data_json": {
        "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
        "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
        "name": "1159a6f1193150681b8484545150334e89de6c1c",
        "creating_user_id": "da5d4ee8-aec0-4264-ab85-c491040c",
        "description": "zhelezovartem - ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "git_commit_info": {
          "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
          "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
          "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
          "branch": "main",
          "timestamp": 1711534976.0,
          "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c"
        },
        "template_id": "cd1860d5-dc06-41e7-9a3b-be078e7f",
        "origin_url": "https://github.com/cyber-dojo/dashboard/actions/runs/8450201221",
        "user_data": "{}"
      }
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535010.2210565,
      "type": "trail_attestation_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "pull_request",
      "is_compliant": true,
      "attestation_id": "76a44125-eccc-4fb7-8260-d4ff1866",
      "template_reference_name": "pull-request"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535018.95352,
      "type": "trail_attestation_for_artifact_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "generic",
      "is_compliant": true,
      "attestation_id": "d3752b67-aefc-444c-a7dc-8115c5ef",
      "template_reference_name": "lint",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535027.3128896,
      "type": "artifact_creation_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "artifact_id": "8803e410-8ab6-4ba7-af7a-4c769a92",
      "template_reference_name": "dashboard",
      "git_commit": "1159a6f1193150681b8484545150334e89de6c1c"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535054.2601902,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "bb3acddd-5336-4b6a-a7ea-e5b3e972",
      "template_reference_name": "snyk-code-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535059.1866503,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "1159a6f1193150681b8484545150334e89de6c1c",
        "message": "ci: update gh-workflow-tf-plan-apply action to get rid of deprecations",
        "author": "Artem Zhelezov <36639304+zhelezovartem@users.noreply.github.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711534976.0,
        "url": "https://github.com/cyber-dojo/dashboard/commit/1159a6f1193150681b8484545150334e89de6c1c",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "70421c36-d79f-4813-8635-e77b760a",
      "template_reference_name": "snyk-container-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535086.4269938,
      "type": "artifact_approval_reported",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "approval_id": "fd9de9dd-37e7-4680-8353-c5082609",
      "approval_number": 70,
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "state": "APPROVED",
      "reviewer": "external://zhelezovartem"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535216.8064907,
      "type": "artifact_started_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 3429,
      "replica_number": 1,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535375.2659616,
      "type": "artifact_approval_reported",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "approval_id": "2380af36-a5ff-4c52-ba30-a8483bb9",
      "approval_number": 71,
      "environment_id": "73965c45-e9a1-4bb9-ad01-dc5a526f",
      "state": "APPROVED",
      "reviewer": "external://zhelezovartem"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711535487.4472156,
      "type": "artifact_started_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "73965c45-e9a1-4bb9-ad01-dc5a526f",
      "environment_name": "aws-prod",
      "snapshot_index": 2509,
      "replica_number": 1,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711789650.9179683,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "95e89ff9-077d-4528-a09d-c7898047",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1711790067.348031,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "0a45d133-25c4-46d2-bc59-27fece47",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1712394532.589705,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "e616f223-2016-4c28-85c5-00176db6",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1712394916.8546758,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "a7d0fdd4-33a0-4e50-8a3b-d3928e1f",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1712999261.7330244,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "3e4ef819-db8e-4f1f-b665-1ac0e061",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1712999606.647108,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "d6a3266d-7e43-426f-853c-a2bab6f2",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1713604064.640139,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "b7a8fb46-f99e-4228-96a2-7cd55355",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1713604482.316237,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "a58e5d10-44fa-4918-a732-283d8541",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714208898.3243415,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "020b7686-d2f2-4d30-b890-cbfe56c2",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714209298.3530078,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "555c60fe-769e-40b9-98df-fc181634",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714563833.9450486,
      "type": "artifact_stopped_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 3510,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714564003.09481,
      "type": "artifact_started_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 3513,
      "replica_number": 1,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714813781.150341,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "333725e9-e82b-4a22-a81c-721adbae",
      "template_reference_name": "aws-prod-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714814179.9960504,
      "type": "artifact_attestation_reported",
      "git_commit_info": {
        "sha1": "cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "message": "Run ci workflows with fixed Kosli trail-name",
        "author": "JonJagger <jon@kosli.com>",
        "author_username": null,
        "branch": "main",
        "timestamp": 1711195944.0,
        "url": "https://github.com/cyber-dojo/live-snyk-scans/commit/cf3896a8bbd2f74c9e36336b69d8ee64eae1ff25",
        "parents": null
      },
      "repo_info": null,
      "attestation_type": "snyk",
      "is_compliant": true,
      "attestation_id": "60bde45d-4724-4c46-a963-85fe1972",
      "template_reference_name": "aws-beta-snyk-scan",
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "artifact_name": "cyberdojo/dashboard:1159a6f",
      "target_artifact": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714832154.1066768,
      "type": "artifact_stopped_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "e44779bb-311d-4bac-9d19-a64a0843",
      "environment_name": "aws-beta",
      "snapshot_index": 3539,
      "template_reference_name": "dashboard"
    },
    {
      "org_id": "83acb2bc-2c26-48a7-8b87-90dfcce7",
      "flow_id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
      "trail_id": "7cc627bd-78ff-4051-b7b8-ef46fa15",
      "timestamp": 1714832517.3628683,
      "type": "artifact_stopped_running",
      "git_commit_info": null,
      "repo_info": null,
      "artifact_fingerprint": "dddd83bf5038e81c228b222f01a0184ce2a8492cb45075b66be5baf5be803ca1",
      "environment_id": "73965c45-e9a1-4bb9-ad01-dc5a526f",
      "environment_name": "aws-prod",
      "snapshot_index": 2592,
      "template_reference_name": "dashboard"
    }
  ],
  "created_by": "ci-pipelines",
  "flow": {
    "name": "dashboard-ci",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/dashboard",
      "kind": "build"
    }
  },
  "external_urls": null,
  "html_url": "https://app.kosli.com/cyber-dojo/flows/dashboard-ci/trails/1159a6f1193150681b8484545150334e89de6c1c"
}
```

</div>
</Accordion>

