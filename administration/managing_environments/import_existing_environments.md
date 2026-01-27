---
title: Import Existing Environments
description: Learn how to manage environments in Kosli trough Terraform, including creating, updating, and archiving environments.
---

The following sections explain how to manage environments in Kosli, including creating, updating, and archiving environments.
The preferred way to manage environments is via Terraform to have your Kosli infrastructure as code. You can also use the Kosli CLI or the Kosli UI to manage environments.

<Tip>
This guide focuses entirely on managing physical (non-logical) environments via Terraform.All documentation and examples are provided at the [Kosli Terraform provider](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/).

For information on creating environments via the CLI or UI, see [Part 8: Environments](/getting_started/environments/).
</Tip>

## Importing existing environments

If you have existing physical environments in Kosli that were created via the UI or CLI, you can import them into your Terraform state following these steps:

<Steps>
  <Step title="Set up your Terraform configuration">

  If you haven't already, set up the Kosli Terraform provider in your Terraform configuration. See the [Kosli Terraform provider documentation](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs) for details.

  Make sure you're using Terraform version 1.8 or later. See [Terraform installation guide](https://learn.hashicorp.com/tutorials/terraform/install-cli) for instructions.

  </Step>
  <Step title="Identify the environment">
  Identify the name of the environment you want to import. You can find this in the Kosli UI under `Environments` or by using the CLI command `kosli list environments`.

  </Step>
  <Step title="Initialize Terraform">

  Run `terraform init` to initialize your Terraform working directory if you haven't done so already.

  </Step>
  <Step title="Create a Terraform resource block">
  Create a Terraform resource block for the environment you want to import. This block should match the existing environment's configuration.

  ```hcl
  resource "kosli_environment" "my_environment" {
    name        = "production"
    description = "Production environment"
    type        = "K8S"  # or other types that match your physical environment
    # Add other attributes
  }
  ```

  <Warning>

  Make sure that the environment `type` in your Terraform configuration matches the type of the existing environment in Kosli. Mismatched types may lead to import errors or misconfigurations.

  Logical environment types is currently not supported for import.
  </Warning>
  </Step>
  <Step title="Import the existing environment">
  Run the following command to import the existing environment into your Terraform state. Replace `my_environment` with the name of your Terraform resource and `production` with the name of the environment in Kosli.

  ```bash
  terraform import kosli_environment.my_environment production
  ```
  </Step>
  <Step title="Verify the import">
  Run `terraform plan` to verify that the environment has been imported correctly. The output should show no changes if the import was successful. From this point on, you can manage the Kosli environment using Terraform the same way as any other Terraform resource.
  </Step>
</Steps>

## Reference

Details on how to manage environments via Terraform can be found in the [Kosli Terraform provider documentation](https://registry.terraform.io/providers/kosli-dev/kosli/latest/docs/resources/environment).
