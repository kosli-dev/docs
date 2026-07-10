---
title: "kosli attest decision"
tag: "BETA"
description: "Record a compliance decision against a control in a Kosli trail.  "
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli attest decision [IMAGE-NAME | FILE-PATH | DIR-PATH] [flags]
```

Record a compliance decision against a control in a Kosli trail.  
Use this command to record the outcome of evaluating a control as part of your delivery
pipeline — whether it was satisfied or not — attached to a specific trail with an optional artifact.
This decision is the evidence that a governance requirement was assessed.


The attestation can be bound to a *trail* using the trail name.
The attestation can be bound to an *artifact* in two ways:
- using the artifact's SHA256 fingerprint which is calculated (based on the `--artifact-type` flag and the artifact name/path argument) or can be provided directly (with the `--fingerprint` flag).
- using the artifact's name in the flow yaml template and the git commit from which the artifact is/will be created. Useful when reporting an attestation before creating/reporting the artifact.

You can optionally associate the attestation to a git commit using `--commit` (requires access to a git repo).
You can optionally redact some of the git commit data sent to Kosli using `--redact-commit-info`.
Note that when the attestation is reported for an artifact that does not yet exist in Kosli, `--commit` is required to facilitate
binding the attestation to the right artifact.
To record repository information, all three of `--repo-id`, `--repo-url`, and `--repository` must be set together.
These are automatically set in GitHub Actions, GitLab CI, Bitbucket Pipelines, and Azure DevOps.
In other CI systems, set them explicitly to capture repository metadata.

## Flags
| Flag | Description |
| :--- | :--- |
|        `--annotate` stringToString  |  [optional] Annotate the attestation with data using key=value.  |
|    `-t`, `--artifact-type` string  |  The type of the artifact to calculate its SHA256 fingerprint. One of: [oci, docker, file, dir]. Only required if you want Kosli to calculate the fingerprint for you (i.e. when you don't specify '`--fingerprint`' on commands that allow it).  |
|        `--attachments` strings  |  [optional] The comma-separated list of paths of attachments for the reported attestation. Attachments can be files or directories. All attachments are compressed and uploaded to Kosli's evidence vault.  |
|    `-g`, `--commit` string  |  [conditional] The git commit for which the attestation is associated to. Becomes required when reporting an attestation for an artifact before reporting it to Kosli. (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |
|    `-C`, `--compliant`  |  [defaulted] Whether the attestation is compliant or not. A boolean flag [docs](/faq/#boolean-flags)  |
|        `--control` string  |  The control identifier being evaluated (e.g. RCTL-043).  |
|        `--description` string  |  [optional] attestation description  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-x`, `--exclude` strings  |  [optional] The comma separated list of directories and files to exclude from fingerprinting. Can take glob patterns. Only applicable for `--artifact-type` dir.  |
|        `--external-fingerprint` stringToString  |  [optional] A SHA256 fingerprint of an external attachment represented by `--external-url`. The format is label=fingerprint (labels cannot contain '.' or '='). This flag can be set multiple times. There must be an external url with a matching label for each external fingerprint.  |
|        `--external-url` stringToString  |  [optional] Add labeled reference URL for an external resource. The format is label=url (labels cannot contain '.' or '='). This flag can be set multiple times. If the resource is a file or dir, you can optionally add its fingerprint via `--external-fingerprint`  |
|    `-F`, `--fingerprint` string  |  [conditional] The SHA256 fingerprint of the artifact to attach the attestation to. Only required if the attestation is for an artifact and `--artifact-type` and artifact name/path are not used.  |
|    `-f`, `--flow` string  |  The Kosli flow name.  |
|    `-h`, `--help`  |  help for decision  |
|    `-n`, `--name` string  |  The name of the attestation as declared in the flow or trail yaml template.  |
|    `-o`, `--origin-url` string  |  [optional] The url pointing to where the attestation came from or is related. (defaulted to the CI url in some CIs: [docs](/integrations/ci_cd/#defaulted-kosli-command-flags-from-ci-variables) ).  |
|        `--redact-commit-info` strings  |  [optional] The list of commit info to be redacted before sending to Kosli. Allowed values are one or more of [author, message, branch].  |
|        `--registry-password` string  |  [conditional] The container registry password or access token. Only required if you want to read container image SHA256 digest from a remote container registry and it is not already accessible via Docker/Podman auth files or a credential helper.  |
|        `--registry-username` string  |  [conditional] The container registry username. Only required if you want to read container image SHA256 digest from a remote container registry and it is not already accessible via Docker/Podman auth files or a credential helper.  |
|        `--repo-id` string  |  [conditional] The stable, unique identifier for the repository in your VCS provider (e.g. a numeric ID). Do not use the repository name as it can change if the repo is renamed. All three of `--repo-id`, `--repo-url` and `--repository` must be set to record repository information (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |
|        `--repo-provider` string  |  [optional] The source code hosting provider. One of: github, gitlab, bitbucket, azure-devops (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |
|        `--repo-root` string  |  [defaulted] The directory where the source git repository is available. Only used if `--commit` is used or defaulted in CI, see [docs](/integrations/ci_cd/#defaulted-kosli-command-flags-from-ci-variables) . (default ".")  |
|        `--repo-url` string  |  [conditional] The URL of the repository. Must be a valid URL. All three of `--repo-id`, `--repo-url` and `--repository` must be set to record repository information (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |
|        `--repository` string  |  [conditional] The name of the repository (e.g. owner/repo-name). All three of `--repo-id`, `--repo-url` and `--repository` must be set to record repository information (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |
|    `-T`, `--trail` string  |  The Kosli trail name.  |
|    `-u`, `--user-data` string  |  [optional] The path to a JSON file containing additional data you would like to attach to the attestation.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    `-a`, `--api-token` string  |  The Kosli API token.  |
|    `-c`, `--config-file` string  |  [optional] The Kosli config file path. (default "kosli")  |
|        `--debug`  |  [optional] Print debug logs to stdout.  |
|    `-H`, `--host` string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        `--http-proxy` string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    `-r`, `--max-api-retries` int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        `--org` string  |  The Kosli organization.  |
|    `-q`, `--quiet`  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins.  |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="record a compliant decision against a trail">
```shell
kosli attest decision 
	--name yourAttestationName 
	--control RCTL-043 
	--compliant=true 

```
</Accordion>
<Accordion title="record a non-compliant decision against a trail">
```shell
kosli attest decision 
	--name yourAttestationName 
	--control RCTL-043 
	--compliant=false 

```
</Accordion>
<Accordion title="record a decision linked to a specific artifact (by fingerprint)">
```shell
kosli attest decision 
	--name yourAttestationName 
	--control RCTL-043 
	--compliant=true 
	--fingerprint yourArtifactFingerprint 

```
</Accordion>
<Accordion title="record a decision with an evidence attachment">
```shell
kosli attest decision 
	--name yourAttestationName 
	--control RCTL-043 
	--compliant=true 
	--attachments eval-report.json 
```
</Accordion>
</AccordionGroup>

