---
title: Managing Environments
description: Learn how to manage Kosli environments via Terraform, including creating and importing physical and logical environments.
---

<Note>
Archiving environments requires the Admin role.
</Note>

The preferred way to manage environments is via the <Tooltip tip="An official HashiCorp-registered Terraform provider that lets you manage Kosli resources (environments, flows, policies, etc.) as infrastructure as code." cta="View on Terraform Registry" href="https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/">Kosli Terraform provider</Tooltip>, so your Kosli configuration is version-controlled alongside your infrastructure. You can also manage environments through the Kosli CLI or UI.

<Info>
This page covers managing environments via Terraform. For creating environments via the CLI or UI, see [Getting started: Environments](/getting_started/environments).
</Info>

Kosli has two environment types:

- **<Tooltip tip="A physical environment directly corresponds to a single runtime system. Supported types: K8S, ECS, S3, docker, server, lambda.">Physical environments</Tooltip>** — each maps to a single runtime (e.g. a Kubernetes cluster or ECS service). Managed with the `kosli_environment` resource.
- **<Tooltip tip="A logical environment aggregates multiple physical environments into a single view. It can only contain physical environments, not other logical environments.">Logical environments</Tooltip>** — aggregate one or more physical environments into a single view. Managed with the `kosli_logical_environment` resource.

## Managing physical environments

### Create a physical environment

```hcl
resource "kosli_environment" "production" {
  name        = "production-k8s"
  description = "Production Kubernetes cluster"
  type        = "K8S"
}
```

Supported types: `K8S`, `ECS`, `S3`, `docker`, `server`, `lambda`.

### Import an existing physical environment

If you have environments created via the UI or CLI, you can bring them under Terraform management by importing them into your <Tooltip tip="The Terraform state file tracks the mapping between your configuration and real-world resources. Importing adds an existing resource to this state without recreating it.">Terraform state</Tooltip>.

1. Find the environment name in the Kosli UI under **Environments**, or run:

```shell
kosli list environments
```

2. Add a matching `kosli_environment` resource block to your configuration:

```hcl
resource "kosli_environment" "my_environment" {
  name        = "production"
  description = "Production environment"
  type        = "K8S"  # must match the existing environment's type
}
```

3. Run the import:

```shell
terraform import kosli_environment.my_environment production
```

4. Verify with `terraform plan` — no changes should be planned if the import succeeded.

<Warning>
The `type` in your Terraform configuration must exactly match the type of the existing environment in Kosli. A mismatch will cause import errors or misconfiguration.
</Warning>

## Managing logical environments

Logical environments group physical environments into a combined view — useful for representing a full production tier across multiple runtimes.

### Create a logical environment

```hcl
resource "kosli_logical_environment" "production_all" {
  name                  = "production-all"
  description           = "All production environments"
  included_environments = ["production-k8s", "production-ecs", "production-lambda"]
}
```

`included_environments` must reference the names of existing physical environments. Logical environments cannot include other logical environments.

### Import an existing logical environment

1. Find the logical environment name:

```shell
kosli list environments
```

2. Add a matching `kosli_logical_environment` resource block:

```hcl
resource "kosli_logical_environment" "production_all" {
  name                  = "production-all"
  included_environments = ["production-k8s", "production-ecs"]
}
```

3. Run the import:

```shell
terraform import kosli_logical_environment.production_all production-all
```

4. Verify with `terraform plan` — no changes should be planned if the import succeeded.

## Reference

- [`kosli_environment` resource](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/resources/environment)
- [`kosli_environment` data source](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/data-sources/environment)
- [`kosli_logical_environment` resource](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/resources/logical_environment)
- [`kosli_logical_environment` data source](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/data-sources/logical_environment)
