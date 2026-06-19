---
title: Managing Tags
description: Use tags to label and organize Kosli resources with custom key-value pairs via Terraform, CLI, or API.
---

Tags are custom key-value pairs you attach to Kosli resources. They let you categorize, filter, and add metadata to your flows and environments without changing the resources themselves.

## Why use tags

- **Organize resources** — group related flows or environments by team, project, region, or any other dimension.
- **Drive policy behavior** — reference tags in [Environment Policy](/getting_started/policies) expressions to make attestation requirements conditional. For example, require security scans only for flows tagged `risk-level=high`.
- **Add operational metadata** — store context such as cost center, service tier, or owner directly on the resource.

## Supported resources

You can tag the following Kosli resource types:

| Resource type | Terraform resource | CLI identifier |
| :--- | :--- | :--- |
| Flow | [`kosli_flow`](/terraform-reference/resources/flow) | `flow` |
| Environment | [`kosli_environment`](/terraform-reference/resources/environment) | `env` |

## Tag key and value rules

- **Keys** must start with a letter or digit and can contain letters, digits, hyphens (`-`), underscores (`_`), dots (`.`), and tildes (`~`).
- **Values** are strings. If a value is a valid URL (e.g. `https://example.com`), Kosli automatically renders it as a clickable link in the UI.
- There is no fixed limit on the number of tags per resource, but keep them concise for readability.

## Add or update tags

<Tabs>
  <Tab title="Terraform" icon="cubes">
  Add a `tags` map to any `kosli_environment` or `kosli_flow` resource. Tags are applied via a diff — only changed tags are sent to the API.

  Tag an environment:

  ```hcl
  resource "kosli_environment" "production" {
    name        = "production-k8s"
    type        = "K8S"
    description = "Production Kubernetes cluster"
    tags = {
      region     = "eu-west-1"
      tier       = "critical"
      managed-by = "platform-team"
    }
  }
  ```

  Tag a flow:

  ```hcl
  resource "kosli_flow" "api_service" {
    name        = "api-service"
    description = "API service pipeline"
    tags = {
      team       = "platform"
      risk-level = "high"
    }
  }
  ```

  See the [`kosli_environment` resource](/terraform-reference/resources/environment) and [`kosli_flow` resource](/terraform-reference/resources/flow) for the full schema.
  </Tab>
  <Tab title="CLI" icon="terminal">
  Pass one or more `--set` flags with `key=value` pairs. If a key already exists, its value is updated:

  ```shell
  kosli tag flow my-flow \
    --set team=platform \
    --set risk-level=high
  ```

  ```shell
  kosli tag env production \
    --set region=eu-west-1 \
    --set tier=critical
  ```

  See [`kosli tag`](/client_reference/kosli_tag) for all flags and options.
  </Tab>
  <Tab title="API" icon="code">
  Use the tags endpoint with `set_tags`:

  <CodeGroup>
  ```shell EU
  curl -X PATCH "https://app.kosli.com/api/v2/tags/{org}/flow/my-flow" \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "set_tags": {"team": "platform", "risk-level": "high"}
    }'
  ```
  ```shell US
  curl -X PATCH "https://app.us.kosli.com/api/v2/tags/{org}/flow/my-flow" \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "set_tags": {"team": "platform", "risk-level": "high"}
    }'
  ```
  </CodeGroup>
  </Tab>
</Tabs>

## Remove tags

<Tabs>
  <Tab title="Terraform" icon="cubes">
  Remove individual tags by deleting them from the `tags` map. Set `tags = {}` to remove all tags:

  ```hcl
  resource "kosli_environment" "production" {
    name = "production-k8s"
    type = "K8S"
    tags = {}
  }
  ```
  </Tab>
  <Tab title="CLI" icon="terminal">
  Pass one or more `--unset` flags with the keys to remove:

  ```shell
  kosli tag env production \
    --unset region
  ```
  </Tab>
  <Tab title="API" icon="code">
  Use the tags endpoint with `remove_tags`:

  <CodeGroup>
  ```shell EU
  curl -X PATCH "https://app.kosli.com/api/v2/tags/{org}/env/production" \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "remove_tags": ["region"]
    }'
  ```
  ```shell US
  curl -X PATCH "https://app.us.kosli.com/api/v2/tags/{org}/env/production" \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "remove_tags": ["region"]
    }'
  ```
  </CodeGroup>
  </Tab>
</Tabs>

## Read tags

<Tabs>
  <Tab title="Terraform" icon="cubes">
  Use data sources to read tags from existing resources:

  ```hcl
  data "kosli_environment" "production" {
    name = "production-k8s"
  }

  output "production_tags" {
    value = data.kosli_environment.production.tags
  }

  output "managed_by" {
    value = try(data.kosli_environment.production.tags["managed-by"], "unknown")
  }
  ```
  </Tab>
  <Tab title="API" icon="code">
  Tags are included in the resource response when you fetch an environment or flow via the API.
  </Tab>
</Tabs>

## Recommended tag patterns

A consistent tagging strategy makes it easier to organize resources as your Kosli usage grows. Here are common patterns:

| Tag key | Example values | Purpose |
| :--- | :--- | :--- |
| `tier` | `dev`, `staging`, `prod` | Distinguish environment stages |
| `team` | `platform`, `payments`, `mobile` | Identify the owning team |
| `region` | `eu-west-1`, `us-east-1` | Track geographic location |
| `risk-level` | `high`, `medium`, `low` | Drive conditional policy behavior |
| `cost-center` | `eng-1234`, `ops-5678` | Map to internal accounting |

<Tip>
Pick a small set of tag keys and document them for your organization. Consistent keys across environments and flows make filtering and policy expressions predictable.
</Tip>

### Example: categorizing environments by stage

Tag your environments to reflect their deployment stage. This lets you quickly identify which environments are production-critical and apply policies accordingly:

<Tabs>
  <Tab title="Terraform" icon="cubes">
  ```hcl
  resource "kosli_environment" "staging_k8s" {
    name        = "staging-k8s"
    type        = "K8S"
    description = "Staging Kubernetes cluster"
    tags = {
      tier   = "staging"
      team   = "platform"
      region = "eu-west-1"
    }
  }

  resource "kosli_environment" "production_k8s" {
    name        = "production-k8s"
    type        = "K8S"
    description = "Production Kubernetes cluster"
    tags = {
      tier   = "prod"
      team   = "platform"
      region = "eu-west-1"
    }
  }
  ```
  </Tab>
  <Tab title="CLI" icon="terminal">
  ```shell
  kosli tag env staging-k8s \
    --set tier=staging \
    --set team=platform \
    --set region=eu-west-1
  ```

  ```shell
  kosli tag env production-k8s \
    --set tier=prod \
    --set team=platform \
    --set region=eu-west-1
  ```
  </Tab>
</Tabs>

## Using tags in policies

Tags become powerful when combined with [Environment Policies](/getting_started/policies). You can reference flow tags in policy expressions to conditionally require attestations:

```yaml
attestations:
  - if: ${{ flow.tags.risk-level == "high" }}
    name: security-scan
    type: snyk
```

In this example, the `security-scan` attestation is only required when the flow is tagged with `risk-level=high`. This lets you enforce stricter compliance for high-risk services while keeping lighter requirements for lower-risk ones.

For the full expression syntax, see the [Environment Policy reference](/policy-reference/environment_policy).
