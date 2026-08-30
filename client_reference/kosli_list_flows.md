---
title: "kosli list flows"
description: "List flows for an org. "
---

## Synopsis

```shell
kosli list flows [flags]
```

List flows for an org. By default, all flows for the org are returned.
Pass --page-limit and/or --page to paginate the results; when pagination is requested the output
includes pagination metadata and a page footer (table) or a "data"/"pagination" envelope (JSON).
The list can be filtered by name with --name (and --ignore-case for case-insensitive matching).

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-h`, `--help` | bool | help for flows |
| `-i`, `--ignore-case` | bool | [optional] Perform case-insensitive matching for `--name`. By default matching is case sensitive. |
| `-N`, `--name` | string | [optional] Only list flows whose name contains this substring. The Kosli API supports alphanumeric characters and '-'. |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 20) |


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

To view a live example of 'kosli list flows' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
# The API token below is read-only
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A
kosli list flows --output=json
```

<Accordion title="View example output">
<div style={{maxHeight: "50vh", overflowY: "auto"}}>

```json
[
  {
    "id": "e4e08b57-e36e-4724-acc8-04e7e437",
    "name": "creator-ci",
    "description": "UX for Group/Kata creation",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: creator\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n        - name: unit-test\n          type: junit\n        - name: unit-test-coverage\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/creator",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/creator",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787835864.1788104,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "217f4b82-2fe6-41ef-8214-e34c3a47",
    "name": "custom-start-points-ci",
    "description": "Custom exercises choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: custom-start-points\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n",
    "repo_url": "https://github.com/cyber-dojo/custom-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/custom-start-points",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787838923.90539,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "f60c8f3f-67cd-4496-8e17-ed6fdb1e",
    "name": "dashboard-ci",
    "description": "UX for a group practice dashboard",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: dashboard\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n        - name: sonarcloud-scan\n          type: sonar\n        - name: unit-test\n          type: junit\n        - name: unit-test-coverage\n          type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/dashboard",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/dashboard",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787842344.00542,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "d398561b-b0a9-4f0e-95a3-bbb0e347",
    "name": "differ-ci",
    "description": "Diff files from two traffic-lights",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: differ\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: sonarcloud-scan\n          type: sonar\n",
    "repo_url": "https://github.com/cyber-dojo/differ",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/differ",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787837303.971501,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "c1bb83be-5195-4814-9fae-eac6bf67",
    "name": "exercises-start-points-ci",
    "description": "Exercises choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: exercises-start-points\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n",
    "repo_url": "https://github.com/cyber-dojo/exercises-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/exercises-start-points",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787838923.90539,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "0b4a3bb0-4f77-41a9-8dea-733d1dc3",
    "name": "languages-start-points-ci",
    "description": "Language+TestFramework choices",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: languages-start-points\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n",
    "repo_url": "https://github.com/cyber-dojo/languages-start-points",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/languages-start-points",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787838923.90539,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "d81371fe-6264-4bb1-aace-9b0af86c",
    "name": "monorepo-co-deployment",
    "description": "Bind shared commit deployments",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1",
    "repo_url": "https://github.com/cyber-dojo/monorepo",
    "tags": {},
    "latest_activity_at": 1781600733.1821082,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "10751390-44e0-4d32-a860-bd5f7584",
    "name": "monorepo-creator",
    "description": "UX for Group/Kata creation",
    "visibility": "public",
    "org": "cyber-dojo",
    "template": "\nversion: 1\ntrail:\n  attestations:\n    - { name: pull-request, type: pull_request }\n  artifacts:\n    - name: creator\n      attestations:\n        - { name: unit-test, type: junit }\n",
    "repo_url": "https://github.com/cyber-dojo/monorepo",
    "tags": {},
    "latest_activity_at": 1781600708.1972978,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "0f0e3f56-f7ac-4830-acc3-3a36e111",
    "name": "monorepo-dashboard",
    "description": "UX for a group practice dashboard",
    "visibility": "public",
    "org": "cyber-dojo",
    "template": "\nversion: 1\ntrail:\n  attestations:\n    - { name: pull-request, type: pull_request }\n  artifacts:\n    - name: dashboard\n      attestations:\n        - { name: rubocop,             type: junit }\n        - { name: snyk-container-scan, type: generic }\n",
    "repo_url": "https://github.com/cyber-dojo/monorepo",
    "tags": {},
    "latest_activity_at": 1781600707.3320358,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "c03d5ba2-cb6e-4f6c-a5ec-05805c49",
    "name": "monorepo-web",
    "description": "UX for practicing TDD",
    "visibility": "public",
    "org": "cyber-dojo",
    "template": "\nversion: 1\ntrail:\n  attestations:\n    - { name: pull-request, type: pull_request }\n  artifacts:\n    - name: web\n      attestations:\n        - { name: lint,      type: generic }\n        - { name: unit-test, type: junit }\n",
    "repo_url": "https://github.com/cyber-dojo/monorepo",
    "tags": {},
    "latest_activity_at": 1781600712.989079,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "28447c7d-904b-4594-8b05-88d5d938",
    "name": "nginx-ci",
    "description": "Reverse proxy",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: nginx\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n",
    "repo_url": "https://github.com/cyber-dojo/nginx",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/nginx",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787293944.0598202,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "d454e45e-3746-417f-992c-e41515d5",
    "name": "production-promotion",
    "description": "Promotes sets of Artifacts from aws-beta to aws-prod",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: one-promotion\n      type: generic\n",
    "repo_url": "https://github.com/cyber-dojo/aws-prod-co-promotion",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/aws-prod-co-promotion",
      "kind": "release",
      "env": "aws-prod"
    },
    "latest_activity_at": 1788074713.2619398,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "4afd2a1f-5045-4145-934a-64b533a6",
    "name": "production-server-access",
    "description": "Flow to track production server access",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n  - name: command-logs\n    type: generic\n  - name: user-identity\n    type: generic\n  - name: service-identity\n    type: generic\n  - name: sso-session-data\n    type: generic\n",
    "repo_url": "",
    "tags": {},
    "latest_activity_at": 1711724314.4139948,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "a81e8c6d-bb00-474f-b986-a6cb9b08",
    "name": "runner-ci",
    "description": "Test runner",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: runner\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n",
    "repo_url": "https://github.com/cyber-dojo/runner",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/runner",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1788074398.5222037,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "e54bdf65-de27-448f-807a-08e09590",
    "name": "saver-ci",
    "description": "Group/Kata model+persistence",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: saver\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n\n",
    "repo_url": "https://github.com/cyber-dojo/saver",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/saver",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1787838984.0144842,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "9a967617-89c5-4121-ab26-99e1f4ae",
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
    },
    "latest_activity_at": 1787927160.5753644,
    "latest_state": "NON-COMPLIANT"
  },
  {
    "id": "a43239d6-fa3d-4e58-b7c4-f00b7432",
    "name": "snyk-aws-beta-per-artifact",
    "description": "Snyk vulns in aws-beta artifacts",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1",
    "repo_url": "https://github.com/cyber-dojo/snyk-scanning",
    "tags": {
      "ci": "github",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/aws-beta.yml",
      "env": "aws-beta"
    },
    "latest_activity_at": 1788074762.8814502,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "e0f4dbb0-0d25-44d0-8aa1-ced9876e",
    "name": "snyk-aws-beta-per-vuln",
    "description": "Individual Snyk vuln trails for aws-beta artifacts",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1",
    "repo_url": "",
    "tags": {
      "ci": "github",
      "env": "aws-beta",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/artifact_snyk_test.yml"
    },
    "latest_activity_at": 1788074738.0863786,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "021d42e3-f52e-4e48-959b-33f1fd60",
    "name": "snyk-aws-prod-per-artifact",
    "description": "Snyk vulns in aws-prod artifacts",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1",
    "repo_url": "https://github.com/cyber-dojo/snyk-scanning",
    "tags": {
      "ci": "github",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/aws-prod.yml",
      "env": "aws-prod"
    },
    "latest_activity_at": 1788074713.0553374,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "7fc06a03-241f-4b17-baa1-05cf7585",
    "name": "snyk-aws-prod-per-vuln",
    "description": "Individual Snyk vuln trails for aws-prod artifacts",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1",
    "repo_url": "",
    "tags": {
      "ci": "github",
      "env": "aws-prod",
      "kind": "run",
      "workflow_url": "https://github.com/cyber-dojo/snyk-scanning/blob/main/.github/workflows/artifact_snyk_test.yml"
    },
    "latest_activity_at": 1788074670.473346,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "6d59cdf1-0d6b-412a-bd81-ecdc8767",
    "name": "spooler-ci",
    "description": "Async write spooler: durable, ordered forwarding to saver",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: spooler\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: unit-test\n          type: junit\n        - name: unit-test-metrics\n          type: custom:test-metrics\n        - name: unit-test-coverage-metrics\n          type: custom:coverage-metrics\n        - name: integration-test\n          type: junit\n        - name: integration-test-metrics\n          type: custom:test-metrics\n        - name: integration-test-coverage-metrics\n          type: custom:coverage-metrics\n",
    "repo_url": "https://github.com/cyber-dojo/spooler",
    "tags": {
      "env": "aws-beta"
    },
    "latest_activity_at": 1787903663.937315,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "57de7461-f687-4b93-a1d7-d4268e44",
    "name": "terraform-apply-beta-creator",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/creator",
    "tags": {},
    "latest_activity_at": 1787836208.8569806,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "63ea4110-f185-4a04-ae62-8519474b",
    "name": "terraform-apply-beta-custom-start-points",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/custom-start-points",
    "tags": {},
    "latest_activity_at": 1787839208.4459617,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "ceb02030-a523-436d-86a5-c45270dc",
    "name": "terraform-apply-beta-dashboard",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/dashboard",
    "tags": {},
    "latest_activity_at": 1787843108.7875247,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "92d8c902-3dc1-4db5-ad07-6ceabc1e",
    "name": "terraform-apply-beta-differ",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/differ",
    "tags": {},
    "latest_activity_at": 1787837408.908393,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "3a0768fb-33b4-47f6-ba63-5c69df8e",
    "name": "terraform-apply-beta-exercises-start-points",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/exercises-start-points",
    "tags": {},
    "latest_activity_at": 1787839208.4459617,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "03286d89-1428-4077-9294-fddf609b",
    "name": "terraform-apply-beta-languages-start-points",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/languages-start-points",
    "tags": {},
    "latest_activity_at": 1787839208.4459617,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "152592aa-87a9-46e5-9b4b-2180b0b5",
    "name": "terraform-apply-beta-nginx",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/nginx",
    "tags": {},
    "latest_activity_at": 1787294408.6792488,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "091c0875-2863-48cb-b1f5-e08bb8dd",
    "name": "terraform-apply-beta-runner",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/runner",
    "tags": {},
    "latest_activity_at": 1788073820.4463117,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "348ea96a-84ba-4c17-8ed9-55b397f2",
    "name": "terraform-apply-beta-saver",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/saver",
    "tags": {},
    "latest_activity_at": 1787839208.4459617,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "418dcba5-0f85-44c1-9bfa-73fe61a2",
    "name": "terraform-apply-beta-spooler",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/spooler",
    "tags": {},
    "latest_activity_at": 1787904009.021726,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "0408259b-db9a-47b4-bd5d-2cafb533",
    "name": "terraform-apply-beta-terraform-base-infra",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/terraform-base-infra",
    "tags": {},
    "latest_activity_at": 1785232808.6739333,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "60bfe410-ffe9-421e-a347-0bbd1554",
    "name": "terraform-apply-beta-web",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/web",
    "tags": {},
    "latest_activity_at": 1787905808.789012,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "61ab4b1c-5b59-4f2b-a484-86b887cb",
    "name": "terraform-apply-prod-aws-prod-co-promotion",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/web",
    "tags": {},
    "latest_activity_at": 1788075211.9398148,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "72787a36-70df-447a-9fae-9c860aa7",
    "name": "terraform-apply-prod-runner",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/runner",
    "tags": {},
    "latest_activity_at": 1788074911.8576832,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "d32a5b61-d72c-4279-824a-55226c4b",
    "name": "terraform-apply-prod-terraform-base-infra",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n    - name: terraform-apply\n      type: generic\n    - name: pull-request\n      type: pull_request\n  artifacts:\n    - name: terraform-state\n    - name: drift-plan\n",
    "repo_url": "https://github.com/cyber-dojo/terraform-base-infra",
    "tags": {},
    "latest_activity_at": 1785236322.8149745,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "cf915667-e09e-4451-b689-8efe0605",
    "name": "terraform-plan-beta-terraform-base-infra",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n",
    "repo_url": "",
    "tags": {},
    "latest_activity_at": 1785166016.9913907,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "27cb0696-7226-4420-b4c9-b8c91ed7",
    "name": "terraform-plan-prod-terraform-base-infra",
    "description": "",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\ntrail:\n  attestations:\n    - name: terraform-plan\n      type: generic\n",
    "repo_url": "",
    "tags": {},
    "latest_activity_at": 1785232718.7436328,
    "latest_state": "COMPLIANT"
  },
  {
    "id": "fd583a48-28de-4b5c-b4a7-b6356e94",
    "name": "web-ci",
    "description": "UX for practicing TDD",
    "visibility": "private",
    "org": "cyber-dojo",
    "template": "version: 1\n\ntrail:\n  attestations:\n    - name: pull-request\n      type: pull_request\n\n  artifacts:\n    - name: web\n      attestations:\n        - name: provenance-facts\n          type: custom:provenance-facts\n        - name: provenance-decision\n          type: decision\n\n        - name: sbom-facts\n          type: custom:sbom-facts\n        - name: sbom-decision\n          type: decision\n\n        - name: snyk-container-scan\n          type: decision\n\n        - name: rubocop-lint\n          type: junit\n\n        - name: server-test\n          type: junit\n\n        - name: test-facts\n          type: custom:test-facts\n        - name: test-decision\n          type: decision\n\n        - name: coverage-facts\n          type: custom:coverage-facts\n        - name: coverage-decision\n          type: decision\n",
    "repo_url": "https://github.com/cyber-dojo/web",
    "tags": {
      "ci": "github",
      "repo_url": "https://github.com/cyber-dojo/web",
      "kind": "build",
      "env": "aws-beta"
    },
    "latest_activity_at": 1788074998.5362537,
    "latest_state": "COMPLIANT"
  }
]
```

</div>
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list all flows for an org">
```shell
kosli list flows 

```
</Accordion>
<Accordion title="list the first 30 flows (paginated)">
```shell
kosli list flows 
	--page-limit 30 

```
</Accordion>
<Accordion title="show the second page of flows (30 per page)">
```shell
kosli list flows 
	--page-limit 30 
	--page 2 

```
</Accordion>
<Accordion title="list flows whose name contains 'backend' (in JSON)">
```shell
kosli list flows 
	--name backend 
	--output json
```
</Accordion>
</AccordionGroup>

