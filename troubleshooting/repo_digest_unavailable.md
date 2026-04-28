---
title: "Repo digest unavailable"
description: 'How to fix the "repo digest unavailable for the image" error when running kosli attest artifact with --artifact-type=docker.'
---

## Error

```
Error: repo digest unavailable for the image, has it been pushed to or pulled from a registry?
```

## Why this happens

When `kosli attest artifact` is called with `--artifact-type=docker`, Kosli asks the local Docker daemon for the image's **repo digest** (the SHA256 of the image manifest in a registry). A repo digest is only attached to an image once it has been pushed to or pulled from a registry. A freshly built image (just `docker build`) has an image ID, but no repo digest, and Kosli will refuse to attest it.

This often surfaces in CI even when the same command appears to work locally. Locally, the image may have been pushed or pulled at some earlier point and the digest is cached on the machine. On a fresh CI runner, the image is only ever built, so the digest is genuinely missing.

You can confirm the difference with:

```bash
docker inspect --format '{{json .RepoDigests}}' <image>
```

A built-but-never-pushed image returns `[]`. An image pulled from or pushed to a registry returns one or more digest entries.

## Solutions

Pick whichever fits your pipeline best.

### Push the image first, then attest

```bash
docker push <registry>/<image>:<tag>
kosli attest artifact <registry>/<image>:<tag> --artifact-type=docker ...
```

This is the most direct fix and produces an attestation tied to the registry digest.

### Use `--artifact-type=oci`

If the image is already in a registry, `oci` fetches the digest directly via the registry API and does not require a local Docker daemon at all:

```bash
kosli attest artifact <registry>/<image>:<tag> \
  --artifact-type=oci \
  --registry-username=$REGISTRY_USER \
  --registry-password=$REGISTRY_TOKEN \
  ...
```

### Fingerprint the source directory instead

If you want the attestation to be deterministic from the source rather than dependent on the registry, use `--artifact-type=dir` against the build context:

```bash
kosli attest artifact ./build-context --artifact-type=dir ...
```

The fingerprint is then a SHA256 of the directory contents and is identical regardless of where (or whether) the image is pushed.

### Provide the fingerprint directly

If you have already computed a fingerprint elsewhere in your pipeline, pass it with `--fingerprint` and drop `--artifact-type` entirely.
