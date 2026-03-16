---
title: Managing Custom Attestation Types
description: Learn how to manage Kosli custom attestation types via Terraform, including creating and importing types with JSON Schema and jq evaluation rules.
---

The preferred way to manage custom attestation types is via the <Tooltip tip="An official HashiCorp-registered Terraform provider that lets you manage Kosli resources (environments, flows, policies, etc.) as infrastructure as code." cta="View on Terraform Registry" href="https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/">Kosli Terraform provider</Tooltip>, so your Kosli configuration is version-controlled alongside your infrastructure. You can also manage custom attestation types through the Kosli CLI.

<Info>
This page covers managing custom attestation types via Terraform. For an introduction to custom attestation types and creating them via the CLI, see [Getting started: Attestations](/getting_started/attestations).
</Info>

Custom attestation types define how Kosli validates evidence from tools that don't have a built-in Kosli attestation command. Each type can include:

- A **JSON Schema** (optional) that defines the expected structure of attestation data
- **jq rules** (optional) that evaluate the data to determine compliance

At least one of the two must be provided.

## Create a custom attestation type

### With schema and jq rules

```hcl
resource "kosli_custom_attestation_type" "security_scan" {
  name        = "security-scan"
  description = "Validates security scan results"

  schema = jsonencode({
    type = "object"
    properties = {
      critical_vulnerabilities = { type = "integer" }
      high_vulnerabilities     = { type = "integer" }
      scan_date                = { type = "string" }
    }
    required = ["critical_vulnerabilities", "high_vulnerabilities", "scan_date"]
  })

  jq_rules = [
    ".critical_vulnerabilities == 0",
    ".high_vulnerabilities < 5"
  ]
}
```

### With jq rules only

```hcl
resource "kosli_custom_attestation_type" "code_coverage" {
  name        = "code-coverage"
  description = "Requires at least 80% line coverage"

  jq_rules = [".line_coverage >= 80"]
}
```

### With schema only

```hcl
resource "kosli_custom_attestation_type" "deployment_record" {
  name        = "deployment-record"
  description = "Validates deployment record structure"

  schema = jsonencode({
    type = "object"
    properties = {
      deployed_by = { type = "string" }
      deployed_at = { type = "string" }
      environment = { type = "string" }
    }
    required = ["deployed_by", "deployed_at", "environment"]
  })
}
```

## Import an existing custom attestation type

If you have custom attestation types created via the CLI, you can bring them under Terraform management by importing them into your <Tooltip tip="The Terraform state file tracks the mapping between your configuration and real-world resources. Importing adds an existing resource to this state without recreating it.">Terraform state</Tooltip>.

1. Find the attestation type name in the Kosli UI or run:

```shell
kosli list attestation-types
```

2. Add a matching `kosli_custom_attestation_type` resource block to your configuration.

3. Run the import:

```shell
terraform import kosli_custom_attestation_type.security_scan security-scan
```

4. Verify with `terraform plan` — no changes should be planned if the import succeeded.

## Reference

- [`kosli_custom_attestation_type` resource](/terraform-reference/resources/custom_attestation_type)
- [`kosli_custom_attestation_type` data source](/terraform-reference/data-sources/custom_attestation_type)
- [Kosli Terraform provider on the Terraform Registry](https://registry.terraform.io/providers/kosli-dev/kosli/latest)
