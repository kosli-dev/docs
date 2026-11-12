---
title: "kosli attest in-toto"
tag: "BETA"
description: "Record an in-toto attestation, such as SLSA provenance or an SBOM, that a build already produced.  "
---

import CliBetaNotice from "/snippets/cli-beta-notice.mdx";

<CliBetaNotice />

## Synopsis

```shell
kosli attest in-toto [IMAGE-NAME | FILE-PATH | DIR-PATH] [flags]
```

Record an in-toto attestation, such as SLSA provenance or an SBOM, that a build already produced.  
Build systems produce in-toto attestations as they build: `actions/attest`, `cosign attest`
and `docker buildx --provenance --sbom` among them. This command records one in Kosli,
verifying its signature first, rather than regenerating the same evidence with other
`kosli attest` commands.

`--predicate-type` chooses what to record, one kind per command:

- `provenance` (SLSA provenance v1 or v0.2) reports the artifact named by `--name`, as
  `kosli attest artifact` does. The commit, branch, repository and build URL come from the
  statement, never from the CI environment, so the build's own commit and run are recorded
  even when this command runs in a different job or workflow.
- `sbom` (SPDX or CycloneDX) reports an SBOM attestation named by `--name`, as
  `kosli attest sbom` does, with the attestation attached in place of the SBOM file.

Recording provenance and an SBOM takes two commands.

The attestation is read from the file given with `--bundle`: a Sigstore bundle
(`.sigstore.json`), a DSSE envelope, an in-toto statement, or an `.intoto.jsonl` file with
one of these per line. Attestations of other kinds are ignored. When several qualify, a
verified one is preferred, then the newest.

The statement must list the artifact as its subject. A signed attestation is verified with
Sigstore against a signer you pin: `--certificate-identity` (or
`--certificate-identity-regexp`) with `--certificate-oidc-issuer`, or `--key`. There is no
way to accept any valid certificate. An unsigned attestation is refused unless
`--allow-unsigned` is given, and is then recorded as unverified. An attestation that fails
verification, because another signer made it or it was changed after signing, fails the
command and nothing is recorded, even when another attestation in the file would qualify. So
does a signed attestation whose signature cannot be checked, such as when no signer is
pinned, a trust root cannot be fetched or the signer flags do not fit how it was signed; the
error then says it could not be verified, not that it failed.

Verifying a certificate-signed attestation needs the trust root of the Sigstore instance
that signed it: Sigstore's public-good instance, or GitHub's own, which signs attestations
for private repositories. It is fetched over TUF on every run that verifies one, from
`https://tuf-repo-cdn.sigstore.dev` or `https://tuf-repo.github.com` respectively, and
cached under `~/.sigstore`, so the runner needs outbound HTTPS to that host and a writable
`~/.sigstore` directory. A key-signed attestation needs neither, unless it carries a
transparency log entry or a signed timestamp, which are checked against Sigstore's
public-good trust root. An unsigned attestation needs neither.

The record is annotated with `verified` and, for a signed attestation, `signer_identity`,
`signer_issuer`, `log_index`, `integrated_time` and `signed_timestamp` where they apply.
Provenance adds `builder_id`, `build_type` and `workflow`, and an SBOM adds `sbom_format`
and `sbom_sha256`. A transparency log entry is linked as the `attestation` external URL,
pinned by the SHA-256 of the attestation's bytes.

For provenance, the commit's message, author and time are looked up on GitHub with
`--github-token` when the statement names a GitHub repository, or else read from the git
checkout at `--repo-root` if it holds the commit. Failing both, only the commit's SHA is
recorded, without its details or branch. A repository on GitHub Enterprise Server needs
`--repo-provider github` and `--github-base-url` to be looked up there: the token is only
sent to the server you name, never to a host taken from the statement. A build URL or
commit URL the statement does not carry can be given with `--build-url` and `--commit-url`.

The artifact fingerprint can be provided directly with the `--fingerprint` flag, or
calculated based on `--artifact-type` flag.

Artifact type can be one of: "file" for files, "dir" for directories, "oci" for container
images in registries or "docker" for local docker images.

Note: `--artifact-type=docker` reads the image's repo digest via the local Docker daemon.
The image must have been pushed to or pulled from a registry for a repo digest to exist;
a freshly built image (just `docker build`) will not have one. If the image is already in
a registry, prefer `--artifact-type=oci`, which fetches the digest directly from the
registry without needing a local Docker daemon.

For `--artifact-type=oci` (and for `--artifact-type=docker` when `--registry-username`
is set), registry credentials are resolved as follows:
  1) If `--registry-username` (and optionally `--registry-password`) is set, it is used directly.
  2) Otherwise, credentials are discovered automatically from:
     - the Docker config file (`~/.docker/config.json`, populated by `docker login`)
     - the Podman/containers auth file (`~/.config/containers/auth.json`, or `$REGISTRY_AUTH_FILE`)
     - any Docker credential helper configured in that config (e.g. `docker-credential-ecr-login`
       for AWS ECR, `docker-credential-gcloud` for GCR/Artifact Registry, an ACR helper for Azure,
       or a local keychain helper), invoked as an external binary on `$PATH`
     - if none of the above yield credentials, the registry is accessed anonymously, which works
       for public images
  `--registry-provider` is deprecated and no longer used.

To specify paths in a directory artifact that should always be excluded from the SHA256 calculation, you can add a `.kosli_ignore` file to the root of the artifact.
Each line should specify a relative path or path glob to be ignored. You can include comments in this file, using `#`.
The `.kosli_ignore` file is always treated as part of the artifact: its own entries cannot exclude it, so the exclusion list cannot be changed without changing the fingerprint.
Paths the list already matches stay excluded whatever is later added there, so keep its entries as narrow as possible.
Excluding the file with `--exclude` keeps it out of the fingerprint but still applies the paths it lists, which lets a writable directory change the list again.
To drop the file from the fingerprint safely, move its entries to `--exclude` and delete it.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--allow-unsigned` | bool | [optional] Record an unsigned attestation, marked as unverified. Without it, an unsigned attestation is refused. |
| `--annotate` | stringToString | [optional] Annotate the attestation with data using key=value. |
| `-t`, `--artifact-type` | string | The type of the artifact to calculate its SHA256 fingerprint. One of: [oci, docker, file, dir]. Only required if you want Kosli to calculate the fingerprint for you (i.e. when you don't specify '`--fingerprint`' on commands that allow it). |
| `--build-url` | string | [optional] The build URL to record when the provenance does not say. Provenance only. |
| `--bundle` | string | [conditional] The file holding the attestation, with `--source` bundle: a Sigstore bundle (.sigstore.json), a DSSE envelope, an in-toto statement, or an .intoto.jsonl file with one of these per line. |
| `--certificate-identity` | string | [conditional] The identity a signed attestation's certificate must name, such as a GitHub workflow URL. Use with `--certificate-oidc-issuer`. |
| `--certificate-identity-regexp` | string | [conditional] A regular expression the identity in a signed attestation's certificate must match. Use instead of `--certificate-identity`, with `--certificate-oidc-issuer`. |
| `--certificate-oidc-issuer` | string | [conditional] The OIDC issuer a signed attestation's certificate must name, such as https://token.actions.githubusercontent.com. |
| `--commit-url` | string | [optional] The commit URL to record when the provenance does not say. Provenance only. |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-x`, `--exclude` | strings | [optional] The comma separated list of directories and files to exclude from fingerprinting. Can take glob patterns. Only applicable for `--artifact-type` dir. |
| `--external-fingerprint` | stringToString | [optional] A SHA256 fingerprint of an external attachment represented by `--external-url`. The format is label=fingerprint (labels cannot contain '.' or '='). This flag can be set multiple times. There must be an external url with a matching label for each external fingerprint. |
| `--external-url` | stringToString | [optional] Add labeled reference URL for an external resource. The format is label=url (labels cannot contain '.' or '='). This flag can be set multiple times. If the resource is a file or dir, you can optionally add its fingerprint via `--external-fingerprint` |
| `-F`, `--fingerprint` | string | [conditional] The SHA256 fingerprint of the artifact to attach the attestation to. Only required if the attestation is for an artifact and `--artifact-type` and artifact name/path are not used. |
| `-f`, `--flow` | string | The Kosli flow name. |
| `--github-base-url` | string | [optional] The GitHub Enterprise Server to look the commit up on, such as https://github.example.com, when the provenance names a repository there. Without it the commit is looked up on github.com, never at a host taken from the provenance. |
| `--github-token` | string | [optional] A GitHub token, to look up the commit's message, author and time when the provenance names a GitHub repository. |
| `-h`, `--help` | bool | help for in-toto |
| `--key` | string | [conditional] The path to a PEM public key, to verify an attestation signed with a key rather than a certificate. |
| `-n`, `--name` | string | The name of the record as declared in the flow or trail yaml template: the artifact's name for provenance, the attestation's name for sbom. |
| `--predicate-type` | string | The kind of attestation to record: provenance (SLSA provenance v1 or v0.2) or sbom (SPDX or CycloneDX). |
| `--registry-password` | string | [conditional] The container registry password or access token. Only required if you want to read container image SHA256 digest from a remote container registry and it is not already accessible via Docker/Podman auth files or a credential helper. |
| `--registry-provider` | string | [deprecated] The docker registry provider or url. Only required if you want to read docker image SHA256 digest from a remote docker registry. (DEPRECATED: no longer used) |
| `--registry-username` | string | [conditional] The container registry username. Only required if you want to read container image SHA256 digest from a remote container registry and it is not already accessible via Docker/Podman auth files or a credential helper. |
| `--repo-provider` | string | [optional] The provider of the repository the provenance names, when its host is not github.com, gitlab.com or bitbucket.org. One of: github, gitlab, bitbucket, bitbucket_cloud, bitbucket_dc, azure-devops, azure_devops_services, azure_devops_server, git, subversion. For a GitHub Enterprise host, also give `--github-base-url` to look the commit up there. |
| `--repo-root` | string | [defaulted] The git checkout to read the commit's details from when they cannot be looked up. Provenance only. (default ".") |
| `--source` | string | [defaulted] Where to read the attestation from. Only 'bundle' is supported for now: the file given with `--bundle`. (default "bundle") |
| `-T`, `--trail` | string | The Kosli trail name. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="record verified SLSA provenance from a Sigstore bundle, as the artifact named app">
```shell
kosli attest in-toto app.tar.gz 
	--artifact-type file 
	--bundle app.sigstore.json 
	--predicate-type provenance 
	--name app 
	--certificate-identity https://github.com/yourOrg/yourRepo/.github/workflows/build.yml@refs/heads/main 
	--certificate-oidc-issuer https://token.actions.githubusercontent.com 
	--github-token yourGithubToken 

```
</Accordion>
<Accordion title="record the SBOM attestation from the same build, as app.sbom">
```shell
kosli attest in-toto app.tar.gz 
	--artifact-type file 
	--bundle app-sbom.sigstore.json 
	--predicate-type sbom 
	--name app.sbom 
	--certificate-identity-regexp '^https://github.com/yourOrg/yourRepo/' 
	--certificate-oidc-issuer https://token.actions.githubusercontent.com 

```
</Accordion>
<Accordion title="record unsigned provenance written by docker buildx, marked as unverified">
```shell
kosli attest in-toto yourImageName 
	--artifact-type docker 
	--bundle provenance.json 
	--predicate-type provenance 
	--name app 
	--allow-unsigned 
	--build-url https://ci.example.com/builds/123 
```
</Accordion>
</AccordionGroup>

