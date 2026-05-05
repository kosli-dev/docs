---
title: "kosli list flows"
beta: false
deprecated: false
description: "List flows for an org."
---

## Synopsis

```shell
kosli list flows [flags]
```

List flows for an org.

## Flags
| Flag | Description |
| :--- | :--- |
|    -h, --help  |  help for flows  |
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

To view a live example of 'kosli list flows' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A  # read-only
kosli list flows --output=json
```

<Accordion title="View example output">
```json
[
  {
    "name": "creator-ci",
    "description": "UX for Group/Kata creation",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations: []\n  artifacts:\n  - name: artifact\n    attestations: []\n",
    "repo_url": "https://gitlab.com/cyber-dojo/creator",
    "tags": {
      "ci": "gitlab",
      "repo_url": "https://gitlab.com/cyber-dojo/creator",
      "kind": "build"
    }
  },
  {
    "name": "custom-start-points-ci",
    "description": "Custom exercises choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: custom-start-points\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/custom-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/custom-start-points",
      "kind": "build"
    }
  },
  {
    "name": "dashboard-ci",
    "description": "UX for a group practice dashboard",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: dashboard\n      attestations:\n        - name: rubocop-lint\n          type: junit\n        - name: snyk-container-scan\n          type: generic\n        - name: sonarcloud-scan\n          type: sonar\n        - name: unit-test\n          type: junit\n        - name: unit-test-coverage\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/dashboard",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/dashboard",
      "kind": "build"
    }
  },
  {
    "name": "differ-ci",
    "description": "Diff files from two traffic-lights",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: differ\n      attestations:\n        - name: rubocop-lint\n          type: junit\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: sonarcloud-scan\n          type: sonar\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/differ",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/differ",
      "kind": "build"
    }
  },
  {
    "name": "differ-ci-tf",
    "description": "Terraform human-readable plan and state file fingerprint",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: tf-plan\n      type: generic\n  artifacts:\n    - name: tf-state\n",
    "repo_url": "https://github.com/cyber-dojo/differ",
    "tags": {}
  },
  {
    "name": "docker-base-ci",
    "description": "Build cyber-dojo/docker-base image",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  artifacts:\n    - name: docker-base\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/docker-base",
    "tags": {}
  },
  {
    "name": "exercises-start-points-ci",
    "description": "Exercises choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: exercises-start-points\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/exercises-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/exercises-start-points",
      "kind": "build"
    }
  },
  {
    "name": "languages-start-points-ci",
    "description": "Language+TestFramework choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: languages-start-points\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/languages-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/languages-start-points",
      "kind": "build"
    }
  },
  {
    "name": "nginx-ci",
    "description": "Reverse proxy",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: nginx\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/nginx",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/nginx",
      "kind": "build"
    }
  },
  {
    "name": "production-promotion",
    "description": "Promotes sets of Artifacts from aws-beta to aws-prod",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: one-promotion\n      type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/aws-prod-co-promotion",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/aws-prod-co-promotion",
      "kind": "release"
    }
  },
  {
    "name": "production-server-access",
    "description": "Flow to track production server access",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n  - name: command-logs\n    type: generic\n  - name: user-identity\n    type: generic\n  - name: service-identity\n    type: generic\n  - name: sso-session-data\n    type: generic\n",
    "repo_url": "",
    "tags": {}
  },
  {
    "name": "runner-ci",
    "description": "Test runner",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: runner\n      attestations:\n        - name: rubocop-lint\n          type: junit\n\n        - name: snyk-container-scan\n          type: generic\n\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n",
    "repo_url": "https://github.com/cyber-dojo/runner",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/runner",
      "kind": "build"
    }
  },
  {
    "name": "saver-ci",
    "description": "Group/Kata model+persistence",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: saver\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n\n",
    "repo_url": "https://github.com/cyber-dojo/saver",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/saver",
      "kind": "build"
    }
  },
  {
    "name": "secrets",
    "description": "Kosli new/expiring secrets check",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations: []\n  artifacts:\n  - name: artifact\n    attestations: []\n",
    "repo_url": "",
    "tags": {
      "ci": "github",
      "kind": "run",
      "repo_url": "https://github.com/cyber-dojo/secrets"
    }
  },
  {
    "name": "snyk-vulns-aws-beta",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations: []\n  artifacts:\n  - name: artifact\n    attestations: []\n",
    "repo_url": "https://github.com/cyber-dojo/snyk-scanning",
    "tags": {
      "ci": "github",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/aws-beta.yml"
    }
  },
  {
    "name": "snyk-vulns-aws-prod",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations: []\n  artifacts:\n  - name: artifact\n    attestations: []\n",
    "repo_url": "https://github.com/cyber-dojo/snyk-scanning",
    "tags": {
      "ci": "github",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/aws-prod.yml"
    }
  },
  {
    "name": "terraform-base-infra-prs",
    "description": "Kosli flow to track terraform PRs for base infra",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n  - name: tf-plan\n    type: generic\n  - name: tf-apply-plan\n    type: generic\n  - name: pull-request\n    type: pull_request\n  - name: tf-validation\n    type: generic",
    "repo_url": "",
    "tags": {}
  },
  {
    "name": "web-ci",
    "description": "UX for practicing TDD",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n\n  artifacts:\n    - name: web\n      attestations:\n        - name: snyk-container-scan\n          type: generic\n        - name: provenance-attestation\n          type: generic\n        - name: sbom\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/web",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/web",
      "kind": "build"
    }
  }
]
```
</Accordion>

