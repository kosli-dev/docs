---
title: 'Glossary'
description: 'Quick-reference definitions of Kosli terms and concepts.'
---

A reference list of Kosli terms. For a narrative explanation of how these concepts fit together, see [How Kosli works](/understand_kosli/how_kosli_works).

### Artifact

A software deliverable (binary, container image, archive) reported to Kosli and identified by its SHA256 fingerprint. Kosli uses the fingerprint to link an artifact's build-time origin to its runtime presence.

### Attestation

A record that a specific control or check was performed on an Artifact or Trail, along with its result. Built-in types include `snyk`, `junit`, `sonar`, `pullrequest`, and `approval`. Custom types support jq-based compliance evaluation.

### Audit Package

A downloadable tar file containing metadata and evidence for a Trail, Artifact, or Attestation. Used for audit investigations and compliance reviews.

### Binary Provenance

The chain of custody that links an artifact's fingerprint to its origin, build evidence, and runtime deployment history.

### Control

A repeatable, verifiable activity that mitigates one or more [risks](/understand_kosli/risks). Controls span build, release, runtime, and lifecycle phases.

### Environment

A Kosli representation of a runtime system you want to monitor (Kubernetes cluster, ECS service, Lambda function, S3 bucket, server directory, Docker host, Azure Web App).

### Environment Policy

A set of compliance requirements defining what may run in an Environment. Non-compliant artifacts are flagged. Trusted third-party artifacts can be allowlisted.

### Environment Snapshot

A point-in-time capture of the artifacts running in an Environment. Kosli traces each running artifact back to the Flow and Trail that produced it.

### Evidence Vault

Secure storage for evidence files attached to attestations (test reports, scan output, approval records). Retrievable on demand for audits.

### Flow

A model of a repeatable business or software process (e.g., a CI pipeline, a Terraform workflow) for which you want to track changes and monitor compliance.

### Flow Template

The compliance definition for a Flow. It specifies the artifacts and attestations that every Trail in the Flow must contain to be considered compliant. Each Trail can override its Flow's template.

### Organization

The account that owns Kosli resources (Flows, Environments, Policies). Most teams work within a shared organization that maps to their company. Members are invited with specific roles that control access.

### Risk

A condition or event in the software delivery lifecycle that could compromise the integrity, security, or compliance posture of your software.

### Trail

A single execution of a Flow (e.g., one CI build, one pull request). Each Trail has a unique identifier you choose, such as a git commit SHA or PR number.

### Trail Evaluation

The process by which Kosli checks a Trail against its Flow Template to determine whether all required artifacts and attestations are present and compliant.
