---
title: "Report AWS environments to Kosli"
description: "Learn how to report running artifacts from ECS, Lambda, and S3 environments to Kosli — using the CLI for a quick test or a Terraform module for production."
---

By the end of this tutorial, you will have reported a snapshot of your AWS environment to Kosli, making its running artifacts visible and trackable.

There are two ways to do this:

- **Kosli CLI** — quick to run, suitable for testing only
- **<Tooltip tip="An open-source Terraform module that deploys an AWS Lambda function to automatically report ECS, Lambda, or S3 environment changes to Kosli." cta="View on Terraform Registry" href="https://registry.terraform.io/modules/kosli-dev/kosli-reporter/aws/latest">Kosli reporter Terraform module</Tooltip>** — deploys a <Tooltip tip="An AWS Lambda function triggered by EventBridge events whenever your ECS, Lambda, or S3 resources change, reporting the current state to Kosli automatically.">Lambda reporter</Tooltip> for continuous, production-grade reporting

Follow the section that matches your needs.

## Prerequisites

* Have access to AWS.
* [Create a Kosli account](https://app.kosli.com/sign-up) if you do not have one.
* [Create an ECS, Lambda, or S3 Kosli environment](/getting_started/environments#create-an-environment) named `aws-env-tutorial`.
* [Get a Kosli API token](/getting_started/service-accounts).

## Report using Kosli CLI

This approach is suitable for testing only.

[Install Kosli CLI](/getting_started/install) if you have not done so, then export your AWS credentials:

```shell
export AWS_REGION=yourAWSRegion
export AWS_ACCESS_KEY_ID=yourAWSAccessKeyID
export AWS_SECRET_ACCESS_KEY=yourAWSSecretAccessKey
```

Run the snapshot command for your environment type:

<Tabs>
<Tab title="ECS">
```shell
kosli snapshot ecs aws-env-tutorial \
    --cluster <your-ecs-cluster-name> \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```
</Tab>
<Tab title="Lambda">
```shell
kosli snapshot lambda aws-env-tutorial \
    --function-names function1,function2 \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```
</Tab>
<Tab title="S3">
```shell
kosli snapshot s3 aws-env-tutorial \
    --bucket <your-bucket-name> \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```
</Tab>
</Tabs>

## Report using Terraform module

[Install Terraform](https://developer.hashicorp.com/terraform/install) if you have not done so.

1. [Authenticate to AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

2. Store your Kosli API token in <Tooltip tip="AWS Systems Manager Parameter Store — a managed service for storing configuration data and secrets. Use SecureString type to encrypt the value at rest. The module looks for a parameter named kosli_api_token by default, but you can override this with the kosli_api_token_ssm_parameter_name variable.">AWS SSM Parameter Store</Tooltip> as a `SecureString` parameter named `kosli_api_token`.

3. Create a `main.tf` file with the configuration for your environment type:

<Tabs>
<Tab title="ECS">
```hcl
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.63"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.5.1"
    }
  }
}

provider "aws" {
  region = local.region

  # Make it faster by skipping some checks
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

locals {
  reporter_name = "reporter-${random_pet.this.id}"
  region        = "eu-central-1"
}

data "aws_caller_identity" "current" {}

data "aws_canonical_user_id" "current" {}

resource "random_pet" "this" {
  length = 2
}

module "lambda_reporter" {
  source  = "kosli-dev/kosli-reporter/aws"
  version = "0.5.7"

  name                              = local.reporter_name
  kosli_environment_type            = "ecs"
  kosli_cli_version                 = "v2.11.0"
  kosli_environment_name            = "aws-env-tutorial"
  kosli_org                         = "<your-org-name>"
  reported_aws_resource_name        = "<your-ecs-cluster-name>"
}
```
</Tab>

<Tab title="Lambda">
```hcl
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.63"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.5.1"
    }
  }
}

provider "aws" {
  region = local.region

  # Make it faster by skipping some checks
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

locals {
  reporter_name = "reporter-${random_pet.this.id}"
  region        = "eu-central-1"
}

data "aws_caller_identity" "current" {}

data "aws_canonical_user_id" "current" {}

resource "random_pet" "this" {
  length = 2
}

variable "my_lambda_functions" {
  type    = string
  default = "function_name1, function_name2"
}

module "lambda_reporter" {
  source  = "kosli-dev/kosli-reporter/aws"
  version = "0.5.7"

  name                           = local.reporter_name
  kosli_environment_type         = "lambda"
  kosli_cli_version              = "v2.11.0"
  kosli_environment_name         = "aws-env-tutorial"
  kosli_org                      = "<your-org-name>"
  reported_aws_resource_name     = var.my_lambda_functions
  use_custom_eventbridge_pattern = true
  custom_eventbridge_pattern     = local.custom_event_pattern
}

locals {
  lambda_function_names_list = split(",", var.my_lambda_functions)

  custom_event_pattern = jsonencode({
    source      = ["aws.lambda"]
    detail-type = ["AWS API Call via CloudTrail"]
    detail = {
      requestParameters = {
        functionName = local.lambda_function_names_list
      }
      responseElements = {
        functionName = local.lambda_function_names_list
      }
    }
  })
}
```
</Tab>

<Tab title="S3">
```hcl
terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.63"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.5.1"
    }
  }
}

provider "aws" {
  region = local.region

  # Make it faster by skipping some checks
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

locals {
  reporter_name = "reporter-${random_pet.this.id}"
  region        = "eu-central-1"
}

data "aws_caller_identity" "current" {}

data "aws_canonical_user_id" "current" {}

resource "random_pet" "this" {
  length = 2
}

module "lambda_reporter" {
  source  = "kosli-dev/kosli-reporter/aws"
  version = "0.5.7"

  name                       = local.reporter_name
  kosli_environment_type     = "s3"
  kosli_cli_version          = "v2.11.0"
  kosli_environment_name     = "aws-env-tutorial"
  kosli_org                  = "<your-org-name>"
  reported_aws_resource_name = "<your-s3-bucket-name>"
}
```
</Tab>
</Tabs>

4. Initialize and apply the Terraform configuration:

```shell
terraform init
terraform apply
```

5. To verify the Lambda reporter is running, go to the AWS console → Lambda → your reporter function → Monitor → Logs.

## What you've accomplished

You have reported a snapshot of your AWS environment to Kosli. Kosli now tracks the running artifacts in that environment and will record changes as they happen.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
