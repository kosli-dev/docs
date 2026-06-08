---
title: "Reporting a custom attestation"
description: "Walk through reporting a kosli attest custom attestation against a trail or an artifact, using the different ways to identify the artifact."
---

In this tutorial, you'll report a <Tooltip tip="A user-defined attestation type in Kosli that validates reported data against a JSON schema and/or a jq compliance rule.">custom attestation</Tooltip> with [`kosli attest custom`](/client_reference/kosli_attest_custom). You'll see how to:

* Bind the attestation to a **trail** *or* to an **artifact** — two alternative options for the same command.
* Identify an artifact by letting Kosli fingerprint it (container image, file, or directory), or by passing a SHA256 fingerprint directly.
* Attest **before** the artifact has been reported, using the artifact's template name and a git commit.

## Prerequisites

* [Install Kosli CLI](/getting_started/install) and [set the common env vars](/getting_started/install/#assigning-flags-via-environment-variables) (`KOSLI_API_TOKEN`, `KOSLI_ORG`, `KOSLI_FLOW`, `KOSLI_TRAIL`).
* A Kosli flow and trail — see the [Getting started guide](/getting_started/flows) if you don't have one.
* A **custom attestation type** that already exists in your org. This is a hard requirement — `kosli attest custom --type <name>` will fail if `<name>` hasn't been created yet.

## 1. Create the custom attestation type first

Before you can report a custom attestation, the type referenced by `--type` must already exist in your Kosli org. You have two ways to create it:

* **CLI** — [`kosli create attestation-type`](/client_reference/kosli_create_attestation-type) (good for quick experiments).
* **Terraform** — the [`kosli_custom_attestation_type` resource](/terraform-reference/resources/custom_attestation_type) (recommended so the type is version-controlled).

For this tutorial we'll create a minimal `coverage-report` type that requires a `coverage` field of at least 80:

```shell
kosli create attestation-type coverage-report \
  --description "Code coverage report" \
  --jq '.coverage >= 80'
```

Prepare a JSON file with the data you want to attest. Save it as `coverage.json`:

```json
{ "coverage": 92, "tool": "pytest-cov" }
```

In every example below, this `coverage.json` is the value of `--attestation-data`.

## 2. Report the attestation

A custom attestation can be bound to either a **trail** or an **artifact**. Pick the option that matches what you want to attest about.

<Tabs>
<Tab title="Against a trail">

Use this when the evidence applies to the trail as a whole (e.g. overall test results, release readiness, change approval) and is not tied to a specific build artifact.

```shell
kosli attest custom \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

`--name` must match an attestation declared in the flow or trail YAML template.

</Tab>
<Tab title="Against an artifact">

Use this when the evidence is about a specific build artifact (a container image, a file, or a directory). You can identify the artifact in two ways: let Kosli compute the SHA256 fingerprint for you, or pass the fingerprint directly.

#### Option A — Let Kosli fingerprint the artifact

Pass the artifact reference as a positional argument together with `--artifact-type`. Supported types:

| `--artifact-type` | Positional argument | Notes |
| :--- | :--- | :--- |
| `oci`    | Container image reference (e.g. `ghcr.io/acme/web:1.2.3`) | Kosli pulls the digest from the registry. For private registries also pass `--registry-username` and `--registry-password`. |
| `docker` | Image present in the local Docker daemon (e.g. `acme/web:1.2.3`) | Reads the digest from the local daemon — no registry call. |
| `file`   | Path to a single file (e.g. `./dist/app.tar.gz`) | |
| `dir`    | Path to a directory (e.g. `./build/`) | Use `--exclude` to skip files/dirs from the fingerprint (e.g. `--exclude '**/*.log,**/node_modules'`). |

**Container image — fingerprint from a registry:**

```shell
kosli attest custom ghcr.io/acme/web:1.2.3 \
  --artifact-type oci \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

**Container image — fingerprint from the local Docker daemon:**

```shell
kosli attest custom acme/web:1.2.3 \
  --artifact-type docker \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

**File artifact:**

```shell
kosli attest custom ./dist/app.tar.gz \
  --artifact-type file \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

**Directory artifact:**

```shell
kosli attest custom ./build/ \
  --artifact-type dir \
  --exclude '**/*.log,**/node_modules' \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

#### Option B — Match the artifact by SHA256 with `--fingerprint`

Use this when you already have the SHA256 (e.g. computed earlier in the pipeline, returned by `kosli fingerprint`, or printed by your build tool). Omit the positional argument and `--artifact-type`.

```shell
kosli attest custom \
  --fingerprint 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json
```

`--fingerprint` and `--artifact-type` are mutually exclusive — pick one.

</Tab>
</Tabs>

## 3. Attest before the artifact exists

You can report an attestation for an artifact that hasn't been reported to Kosli yet. Reference the artifact by its **template name** from the flow YAML and pass `--commit` so Kosli can bind the attestation when the artifact is later reported.

When you pass `--commit` without a fingerprint, Kosli does **not** calculate or assume any fingerprint. Instead, it stores the attestation as *pending* against the artifact's **template name + commit**, and binds it to the real fingerprint later — when an `artifact` attestation arrives for that same template name and commit.

### How it works in practice

Say your flow template defines an artifact called `artifact` with an attestation `test`:

```yml
artifacts:
  - name: artifact
    attestations:
      - name: test
        type: junit
```

You can run tests **before** the artifact is built and report:

```shell
kosli attest junit \
  --name artifact.test \
  --commit $(git rev-parse HEAD) \
  ...
```

Notice:

* `--name` uses the dotted form `<artifact-template-name>.<attestation-name>`.
* No fingerprint, no `--artifact-type`, no positional artifact argument.
* `--commit` is what tells Kosli **which future artifact** this attestation will belong to.

Later, when you build and report the artifact itself:

```shell
kosli attest artifact ./build/artifact.tar.gz \
  --artifact-type file \
  --name artifact \
  --commit $(git rev-parse HEAD)
```

Kosli matches the earlier `artifact.test` attestation to this newly-reported artifact because **both share the same template name (`artifact`) and the same git commit**. At that point the attestation is bound to the artifact's actual SHA256 fingerprint.

### Subtleties worth flagging

1. **The match key is `(template artifact name, git commit)`** — not the fingerprint. The fingerprint is only resolved retroactively once the artifact itself is reported.
2. **The artifact name must match the template.** `artifact.test` only works if your flow YAML declares an artifact named `artifact`. Without a template the dotted form has nothing to bind to.
3. **Same commit, both sides.** If the pre-artifact attestation uses commit `abc123` but the artifact is later reported with commit `def456`, they will not be linked. The attestation will stay floating, unbound to any artifact.
4. **The commit must be resolvable in a git repo.** `--commit` requires access to a real git repo so Kosli can pull commit metadata (author, message, branch, PR info). It's not just a string label.
5. **Multiple artifacts with the same name + commit will all match.** If you report the artifact more than once from the same commit (e.g. rebuilds), every matching artifact picks up the attestation. Attestations are append-only, so this is usually what you want.
6. **Order doesn't matter.** You can report `artifact.test` before or after `artifact` itself — Kosli binds them whenever both sides exist.
7. **Without a template (auto-created flow/trail)**, `--commit`-based pre-artifact attestations still work for binding, but there's no template-defined compliance requirement — the artifact's compliance only reflects the attestations actually made against it.
8. **`--commit` is _only required_ for the pre-artifact case.** If you already have a fingerprint (via `--fingerprint` or `--artifact-type`), `--commit` is optional metadata.

## 4. Add an attachment (optional)

You can attach files or directories as evidence. They are compressed and stored in Kosli's evidence vault.

```shell
kosli attest custom \
  --type coverage-report \
  --name overall-coverage \
  --attestation-data coverage.json \
  --attachments ./coverage-report.html
```

## What you've accomplished

You can now report a `custom` attestation in every relevant shape:
* against a trail, or against an artifact (by fingerprint or by name + commit);
* identifying the artifact via container image, file, directory, or a raw SHA256.

From here:
* [`kosli attest custom`](/client_reference/kosli_attest_custom) reference — full flag list.
* [`kosli create attestation-type`](/client_reference/kosli_create_attestation-type) reference — for managing types via CLI.
* [Terraform: `kosli_custom_attestation_type`](/terraform-reference/resources/custom_attestation_type) — recommended for managing types as code.
* [Tutorial: Creating a custom CTRF attestation type](/tutorials/custom-attestation-ctrf) — a worked example of a real-world custom type.
