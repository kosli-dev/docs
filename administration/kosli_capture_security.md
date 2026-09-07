---
title: Kosli Capture - Security
sidebarTitle: Security
description: "Learn about the security of Kosli Capture"
tag: "ALPHA"
---

<Warning>
Kosli Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

## Kosli capture permissions

The Kosli Capture managed service uses the public AWS, GCP and Azure APIs to extract information about your cloud environments.  In order to do this, you need to provide Kosli with an IAM role that allows access to these APIs.  The role is created and owned by you.  Kosli publishes a CloudFormation template, for use in AWS, showing the permissions needed.  The template is publicly accessible and can be used directly within an `aws cloudformation create-stack` call.

### Assume role

The IAM role defined within the CloudFormation template includes an "assume role" policy granting permission from Kosli.  This appears as:

```
  KosliCaptureAccessRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref RoleName
      Description: >-
        Read-only access for Kosli Capture SDLC compliance evidence collection.
        Managed by CloudFormation; do not edit in place.
      MaxSessionDuration: 3600
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Sid: AllowKosliToAssumeWithExternalId
            Effect: Allow
            Principal:
              AWS: !Ref TrustedPrincipalArn
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                sts:ExternalId: !Ref ExternalId
```

### All permissions needed

The IAM role defined within the Cloudformation template includes a number of IAM policy statements, granting read-only access to some AWS APIs.  The statements are:

```
Statement:

  # How Capture finds what to snapshot. Discovery lists the ECS
  # clusters in the account and reads each cluster's tags from the
  # same DescribeClusters call; those tags are what decide which
  # Kosli environment a cluster is reported into. Without
  # ListClusters and DescribeClusters a role created from this
  # template cannot run discovery at all.
  #
  # Worth knowing for a security review: these are inventory calls
  # and none of them returns application data. DescribeTaskDefinition
  # is the widest - a task definition holds the container image, the
  # command, and any environment variables written into the
  # definition itself in plain text. Values injected from Secrets
  # Manager or Parameter Store are named there rather than resolved,
  # so what comes back is the reference and not the secret.
  - Sid: EcsInventory
    Effect: Allow
    Action:
      - ecs:DescribeCapacityProviders
      - ecs:DescribeClusters
      - ecs:DescribeContainerInstances
      - ecs:DescribeServices
      - ecs:DescribeTaskDefinition
      - ecs:DescribeTasks
      - ecs:ListClusters
      - ecs:ListContainerInstances
      - ecs:ListServices
      - ecs:ListTagsForResource
      - ecs:ListTaskDefinitionFamilies
      - ecs:ListTaskDefinitions
      - ecs:ListTasks
    Resource: "*"

  - Sid: LambdaInventory
    Effect: Allow
    Action:
      - lambda:GetFunctionConfiguration
      - lambda:GetPolicy
      - lambda:ListAliases
      - lambda:ListFunctions
      - lambda:ListTags
      - lambda:ListVersionsByFunction
    Resource: "*"

  - Sid: S3BucketMetadataOnly
    Effect: Allow
    Action:
      - s3:GetBucketLocation
      - s3:GetBucketLogging
      - s3:GetBucketPolicyStatus
      - s3:GetBucketPublicAccessBlock
      - s3:GetBucketTagging
      - s3:GetBucketVersioning
      - s3:GetEncryptionConfiguration
      - s3:ListAllMyBuckets
    Resource: "*"

  # The explicit denies below are redundant given the allow-list
  # above, but they are here so that a reviewer can verify the
  # boundary without having to reason about IAM defaults, and so
  # that any future widening of this policy cannot accidentally
  #  grant data-plane access.
  - Sid: NeverReadObjectData
    Effect: Deny
    Action:
      - s3:GetObject
      - s3:GetObjectAcl
      - s3:GetObjectAttributes
      - s3:GetObjectTagging
      - s3:GetObjectTorrent
      - s3:GetObjectVersion
      - s3:GetObjectVersionAcl
      - s3:GetObjectVersionAttributes
      - s3:GetObjectVersionTagging
      - s3:ListMultipartUploadParts
    Resource: "*"

  # lambda:GetFunction returns a pre-signed URL to the deployment
  # package. That is source-code access, so it is denied outright.
  - Sid: NeverDownloadFunctionCode
    Effect: Deny
    Action:
      - lambda:GetFunction
      - lambda:GetLayerVersion
    Resource: "*"
````

