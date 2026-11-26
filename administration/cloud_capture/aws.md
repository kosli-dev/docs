---
title: "Cloud Capture on AWS"
sidebarTitle: "AWS"
description: "Set up Cloud Capture for your AWS accounts, choose which ECS clusters, Lambda functions, and S3 buckets it snapshots, and review the permissions it uses."
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Cloud Capture snapshots the Amazon ECS clusters and AWS Lambda functions in the AWS accounts you register, and the Amazon S3 buckets you opt in. This page covers setting it up, choosing what it captures, and the permissions it uses.

## Set up

<Steps>
  <Step title="Create the IAM role">
    In order for Cloud Capture to reach into your AWS cloud, to discover your ECS clusters, Lambdas, and S3 buckets, you need to grant permission to Kosli to do so. This requires the creation of an IAM role that Kosli can assume; the role will exist within your AWS account.

    To simplify this process, Kosli has created a CloudFormation template that contains a role with the minimum set of permissions needed by Cloud Capture.  The role can be assumed by Kosli and is protected by an external Id; each organization within Kosli has its own external Id.  The CloudFormation template can be downloaded from the Settings page for your organization within the Kosli UI.

    If you would rather create the role yourself, see [Permissions and security](#permissions-and-security) for the trust policy and the full set of permissions the role needs.

    The CloudFormation template can be deployed within an AWS account, or can be attached to an AWS Organizational Unit (OU) as a StackSet; this latter option ensures the correct IAM permissions are rolled out to all AWS accounts within the OU.

    The template's **S3 buckets** parameter is empty by default, and the role can then read no object in any bucket. Leave it empty unless you want S3 buckets snapshotted; see [Capturing S3 buckets](#capturing-s3-buckets).
  </Step>
  <Step title="Register your accounts">
    When you have created the IAM role, using the CloudFormation template, you can activate Cloud Capture within the Kosli user-interface.

    To check environment names, or to exclude resources, before any snapshots are recorded, switch on [Dry run](/administration/cloud_capture/getting_started#dry-run) and add [skip tags](#excluding-resources) now, before you register accounts.

    Kosli is not notified when you create or delete the stack, so you then register each account yourself. Accounts can only be registered while Cloud Capture is enabled. Open your organization's **Settings**, go to **Cloud Capture**, open **AWS**, select **Register account**, and enter the ARN of the role the stack created. Choose the services to scan in the account: ECS and Lambda are selected for a new account, and S3 is not, because it needs the extra steps in [Capturing S3 buckets](#capturing-s3-buckets). If you deploy the template as a StackSet, register every account in the OU, including accounts that join it later. If you delete a stack, also remove its account from the **Registered accounts** table; until you do, scans of that account fail because the role no longer exists.

    Cloud Capture scans every five minutes unless you [choose another frequency](/administration/cloud_capture/getting_started#scan-frequency), and picks up a registered account the next time it runs - you should see environments and snapshots appearing within a few minutes.
  </Step>
</Steps>

## Excluding resources

If there are resources you do not want Cloud Capture to snapshot, such as a test cluster or a service a vendor runs in your account, exclude them by tag. You choose the tags: in your organization's **Settings**, go to **Cloud Capture**, open **AWS**, and edit the AWS defaults. The **Skip tags** panel there takes any number of key and value pairs, and Cloud Capture skips every resource that carries one of them.

1. Tag the resource in AWS, with any key and value you like. For example, to tag an ECS cluster and a Lambda function with `kosli-capture=false`:

   ```bash
   aws ecs tag-resource \
     --resource-arn arn:aws:ecs:eu-west-1:123456789012:cluster/sandbox \
     --tags key=kosli-capture,value=false

   aws lambda tag-resource \
     --resource arn:aws:lambda:eu-west-1:123456789012:function:scratch \
     --tags kosli-capture=false
   ```

2. In the **Skip tags** panel, enter the key `kosli-capture` and the value `false`, select **Add**, then **Save**.

How the tags are matched:

- A resource is skipped when any one of its tags equals any one of the skip tags, key and value both, exactly as AWS stores them. Tags are case-sensitive, so `Env=test` does not match `env=test`. A key on its own does not match: to skip both `env=test` and `env=staging`, add both.
- The tag is read on the resource Cloud Capture snapshots. An ECS cluster is skipped with everything in it, its services and tasks included; tags on a service or a task definition are not read. A Lambda function is skipped on its own, and the region's Lambda environment in Kosli is made up of the functions that remain. An S3 bucket is only ever snapshotted when it carries an [S3 opt-in tag](#capturing-s3-buckets); a bucket that carries an opt-in tag and a skip tag is skipped.
- The change takes effect on the next scan. A Kosli environment that was already being captured keeps its last snapshot and receives no new ones; nothing is deleted. Remove the skip tag from the resource, and the next run picks it up again.
- Skip tags, like the other Cloud Capture settings, can only be changed while Cloud Capture is enabled.
- The IAM role created by the CloudFormation template already grants the permissions needed to read tags, `ecs:DescribeClusters` and `lambda:ListTags`, so no change to the role is needed.

Through the API, the tags are the `aws` list of `skip_tags`; see [Using the API](/administration/cloud_capture/getting_started#using-the-api).

## Capturing S3 buckets

Cloud Capture reports the content of an S3 bucket as one artifact, whose fingerprint is calculated from the SHA256 checksums S3 stores for the bucket's objects. No object is downloaded, with one exception: a `.kosli_ignore` file at the root of the bucket, if there is one, which lists keys to leave out.

S3 is opt-in, bucket by bucket. An account usually holds many buckets you would not want reported, such as CloudTrail and load balancer access logs, and a snapshot makes one request to AWS for every object in the bucket on every scan, which AWS bills to your account. So a bucket is snapshotted only when all of the following are true.

<Steps>
  <Step title="Name the buckets in the CloudFormation stack">
    Deploy version `v0.2.0` or later of the CloudFormation template, or update your existing stack to it, and list the buckets in its **S3 buckets** parameter (`S3BucketNames`): a comma-separated list of bucket names in lowercase, with no spaces. A name may use `*` and `?` as wildcards, for example `acme-releases-*`.

    This is the permission. The role can list and read objects in the buckets you name and in no others. See [What capturing S3 buckets grants](#what-capturing-s3-buckets-grants) for exactly what it grants.
  </Step>
  <Step title="Choose an S3 opt-in tag">
    In your organization's **Settings**, go to **Cloud Capture**, open **AWS**, and edit the AWS defaults. In the **S3 opt-in tags** panel, beneath **Skip tags**, add a key and a value, for example `kosli-capture-s3` and `true`, and save.

    Until you set an opt-in tag, no bucket is captured.
  </Step>
  <Step title="Tag each bucket you want captured">
    ```bash
    aws s3api put-bucket-tagging \
      --bucket acme-releases \
      --tagging 'TagSet=[{Key=kosli-capture-s3,Value=true}]'
    ```

    `put-bucket-tagging` replaces all of a bucket's tags, so include the tags the bucket already carries. Key and value must both match the opt-in tag exactly; tags are case-sensitive.
  </Step>
  <Step title="Select S3 on the account">
    In the **Registered accounts** table, edit the account and select **s3** among its services.
  </Step>
</Steps>

What to expect:

- **Each bucket is its own environment**, of type S3, named by your [environment name template](/administration/cloud_capture/getting_started#environment-names) with the bucket name as `{resource}`.
- **Each bucket reports exactly one artifact, named after the bucket.** A bucket holding several objects is fingerprinted as a directory, and a bucket holding a single object is fingerprinted as that file, so attest that file with `--artifact-type file` for the fingerprints to match. Either way the artifact carries the bucket's name, not the object's.
- **An empty bucket is captured, not failed.** It reports one artifact, named after the bucket, with the fingerprint of an empty directory: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Every empty bucket therefore shares that fingerprint. It is also the fingerprint of an empty file, so an empty bucket matches any artifact attested from one.
- **A bucket needs both the tag and the permission.** A bucket that carries the opt-in tag but is not named in the stack fails its snapshot on every scan, with an access denied error. A bucket that is named in the stack but not tagged is left alone.
- **Skipping wins.** A bucket that carries an opt-in tag and a [skip tag](#excluding-resources) is not captured.
- **Only objects with a SHA256 checksum are fingerprinted.** S3 stores a full-object SHA256 checksum only when the upload asks for one, for example with `aws s3api put-object --checksum-algorithm SHA256`. An object without one, or one uploaded in several parts, is left out of the fingerprint, as if the bucket did not hold it. The fingerprint therefore matches an artifact you attested from the bucket's whole content only once every object carries the checksum, and a bucket where no object does is reported as an empty bucket.
- **Buckets encrypted with a KMS key are not supported.** The role is granted no KMS permission, so a bucket whose objects use SSE-KMS fails its snapshot. S3's default encryption, SSE-S3, needs nothing more.
- **Large buckets cost more and can time out.** A snapshot is one request per object, on every scan. At the default five minute frequency, a bucket of 100,000 objects is about 29 million requests a day. A bucket of more than roughly 100,000 objects may not finish in the time a snapshot is given, and then fails. Consider a longer [scan frequency](/administration/cloud_capture/getting_started#scan-frequency) if you capture large buckets; it applies to everything Cloud Capture scans for you.
- **A newly tagged bucket is picked up on a later scan**, once AWS reports the tag. Removing the tag, or the opt-in tag from your settings, stops new snapshots; the environment keeps its last snapshot and nothing is deleted.

Through the API, the tags are `opt_in_tags` on the [settings resource](/administration/cloud_capture/getting_started#using-the-api), with the same shape as `skip_tags`. The settings PUT replaces every setting, so a PUT that leaves `opt_in_tags` out removes them, and your buckets stop being captured.

## Permissions and security

For the model that is common to every cloud, see [Cloud Capture security](/administration/cloud_capture/security).

Kosli publishes a CloudFormation template, for use in AWS, showing the permissions needed.  The template is publicly accessible and can be used directly within an `aws cloudformation create-stack` call. The [current version](https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/aws/v0.2.0/kosli-cloud-capture-access-role.yaml), `v0.2.0`, is published at `https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/aws/v0.2.0/kosli-cloud-capture-access-role.yaml`, and the permissions shown on this page are taken from it. A published version is never changed; a change to the permissions is a new version, and reaches a role you have deployed only when you update your stack.

Version `v0.2.0` adds one optional parameter to the earlier template, **S3 buckets** (`S3BucketNames`), for [capturing S3 buckets](#capturing-s3-buckets). Left empty, the default, the role is the same as the one the earlier template created: it can read no object and no object key in any bucket. A role created from the earlier template keeps working for ECS and Lambda.

If you wish to build an IAM role for Cloud Capture without using our published CloudFormation template, the permissions needed are those shown below. The role must contain an Assume Role policy that allows the Kosli account to access the resources, and must include an externalId. Both of these values are supplied by Kosli and cannot be derived; you cannot construct the trust policy without them. Whichever way you create the role, then register the account with the role's ARN, as described in [Set up](#set-up).

### Assume role

The IAM role defined within the CloudFormation template includes an "assume role" policy granting permission from Kosli.  This appears as:

```yaml
  KosliCloudCaptureAccessRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref RoleName
      Description: >-
        Read-only access for Kosli Cloud Capture evidence collection.
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

The IAM role defined within the Cloudformation template includes a number of IAM policy statements, granting read-only access to some AWS APIs. In summary:

- **ECS and Lambda**: read-only inventory calls on every cluster and function. None returns application data, and downloading a function's or a layer's code is explicitly denied.
- **S3**: bucket-level metadata for every bucket. Object keys and objects can be read only in the buckets you name, and not at all when you name none; see [What capturing S3 buckets grants](#what-capturing-s3-buckets-grants).

The statements in full, with the template's own comments:

<Accordion title="IAM policy statements, version v0.2.0">

```yaml
Statement:

  # How Cloud Capture finds what to snapshot. Discovery lists the ECS
  # clusters in the account and reads each cluster's tags from the
  # same DescribeClusters call; a cluster carrying the exclusion
  # tag is skipped and everything else is snapshotted. Without
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

  # Lambda is the next snapshot target after ECS. Granted here so
  # that adding it needs no change to a role you have already
  # reviewed and deployed; read-only, like everything above.
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

  # Which buckets exist in a region, and bucket-level metadata,
  # for every bucket; no object key and no object. Cloud Capture
  # lists the buckets of a region to confirm the ones the tagging
  # API named (see S3FindBucketsByTag below) are there.
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

  # How Cloud Capture finds the buckets to snapshot; not granted
  # when S3BucketNames is empty. A bucket is snapshotted only when
  # it carries one of the S3 opt-in tags you set in Kosli, so
  # Cloud Capture asks the Resource Groups Tagging API for the
  # buckets carrying one, in place of reading the tags of every
  # bucket in the account one by one on every scan.
  #
  # Worth knowing for a security review: AWS cannot scope this
  # permission to S3 or to particular resources. It lets the role
  # read the tag keys and values of every taggable resource in
  # the account, whatever its service. Cloud Capture asks for
  # resources of type s3:bucket carrying your opt-in tags, and
  # for nothing else. Tags are metadata, but if yours hold
  # anything you would not show Kosli, leave S3BucketNames empty.
  - !If
    - SnapshotsS3Buckets
    - Sid: S3FindBucketsByTag
      Effect: Allow
      Action:
        - tag:GetResources
      Resource: "*"
    - !Ref AWS::NoValue

  # What an S3 snapshot reads, in the buckets named in
  # S3BucketNames and no others; neither statement exists when
  # that parameter is empty. A snapshot records the fingerprint of
  # a bucket's content: Cloud Capture lists the object keys, then
  # reads the SHA256 checksum S3 stores for each object with a
  # HeadObject request, which returns the object's metadata and no
  # content.
  #
  # Worth knowing for a security review: AWS has no permission for
  # reading an object's checksum alone. HeadObject is authorised by
  # s3:GetObject, the permission that also authorises downloading
  # the object, so this role is able to read the content of every
  # object in the buckets you name. Cloud Capture downloads one
  # object only, and only if it exists: a `.kosli_ignore` file at
  # the root of the bucket, which lists the keys to leave out of
  # the fingerprint. Name only the buckets you want snapshotted.
  #
  # No KMS permission is granted, so objects encrypted with a KMS
  # key (SSE-KMS) cannot be read and their bucket's snapshot
  # fails. Objects under S3's default encryption (SSE-S3) need
  # nothing more than this.
  #
  # The ARNs are built from the list by joining it: for
  # `a,b` the first is arn:aws:s3:::a and arn:aws:s3:::b, and the
  # second arn:aws:s3:::a/* and arn:aws:s3:::b/*.
  - !If
    - SnapshotsS3Buckets
    - Sid: S3ListObjectKeysInNamedBuckets
      Effect: Allow
      Action:
        - s3:ListBucket
      Resource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join [",arn:aws:s3:::", !Ref S3BucketNames]
    - !Ref AWS::NoValue

  - !If
    - SnapshotsS3Buckets
    - Sid: S3ReadObjectChecksumsInNamedBuckets
      Effect: Allow
      Action:
        - s3:GetObject
      Resource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join ["/*,arn:aws:s3:::", !Ref S3BucketNames]
            - "/*"
    - !Ref AWS::NoValue

  # The explicit denies below are redundant given the allow-list
  # above, but they are here so that a security reviewer can
  # verify the boundary without having to reason about IAM
  # defaults, and so that any future widening of this policy cannot
  # accidentally grant data-plane access.
  #
  # s3:GetObject is denied everywhere except in the buckets named
  # in S3BucketNames, and everywhere when none is named.
  - !If
    - SnapshotsS3Buckets
    - Sid: NeverReadObjectDataOutsideNamedBuckets
      Effect: Deny
      Action:
        - s3:GetObject
      NotResource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join ["/*,arn:aws:s3:::", !Ref S3BucketNames]
            - "/*"
    - Sid: NeverReadObjectData
      Effect: Deny
      Action:
        - s3:GetObject
      Resource: "*"

  # Every other way to read an object, its earlier versions, its
  # ACL or its tags is denied in every bucket, named or not: a
  # snapshot needs none of them.
  - Sid: NeverReadObjectVersionsAclsOrTags
    Effect: Deny
    Action:
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
  # GetLayerVersion does the same for a layer's package, and it is
  # also the IAM action behind the GetLayerVersionByArn API call,
  # so both routes to a layer's code are denied here.
  - Sid: NeverDownloadFunctionCode
    Effect: Deny
    Action:
      - lambda:GetFunction
      - lambda:GetLayerVersion
    Resource: "*"
```

</Accordion>

### What capturing S3 buckets grants

The S3 statements above exist only when you name buckets in the **S3 buckets** parameter. Three things are worth knowing for a security review:

- **The role can read the content of every object in the buckets you name.** Cloud Capture reads the SHA256 checksum S3 stores for each object with a `HeadObject` request, which returns metadata and no content. AWS has no permission for reading a checksum alone: `HeadObject` is authorized by `s3:GetObject`, the permission that also authorizes a download. Cloud Capture downloads one object only, a `.kosli_ignore` file at the root of a bucket if there is one. Reads of object versions, ACLs, tags, and attributes stay denied in every bucket, and `s3:GetObject` stays denied in every bucket you did not name.
- **The role can read the tags of every taggable resource in the account.** Cloud Capture finds the buckets that carry one of your S3 opt-in tags by asking the Resource Groups Tagging API (`tag:GetResources`), which avoids reading the tags of every bucket one by one on every scan. AWS cannot scope that permission to S3 or to particular resources. Cloud Capture asks only for resources of type `s3:bucket` that carry an opt-in tag.
- **No KMS permission is granted.** Objects encrypted with a KMS key (SSE-KMS) cannot be read, and their bucket's snapshot fails.

A name in the parameter may use `*` and `?` as wildcards, as an IAM resource may. A bare `*` names every bucket in the account. Naming a bucket is a permission, not a selection: Cloud Capture snapshots a bucket only when it also carries one of your S3 opt-in tags.

### Tenant isolation

* A Cloud Capture worker picks up a job for your organization and assumes the role in your account
  using your externalId. A worker running for a different tenant is unable to read the externalId
  for your cloud account.
* When the job finishes, the temporary credentials for your account are discarded. A worker holding
  credentials for your cloud account has no path to anyone else's account.
* The ExternalId lives in Kosli's Parameter Store and is readable only by the Kosli-side role for your
  organization. The shared task role cannot read any tenant's ExternalId. Separation is enforced
  by IAM, not by application code.

The trust policy on the role in your account limits access to the AWS account in which the Cloud
Capture is running. The ExternalId acts as a shared secret between Kosli and you, so that only
Cloud Capture is permitted to assume the role.
