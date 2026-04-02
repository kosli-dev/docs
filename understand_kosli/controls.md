---
title: 'Controls'
description: 'Why SDLC controls exist, how they mitigate software delivery risks, and how Kosli implements them.'
---

The [risks page](/understand_kosli/risks) describes what can go wrong in software delivery. A control is the counterpart: a repeatable, verifiable activity that mitigates one or more of those risks. Controls are what stand between an identified risk and a security or compliance incident.

The challenge is not defining controls (most teams already know what "good" looks like) but enforcing them consistently and proving they ran. Manual checklists drift, spreadsheets go stale, and tribal knowledge leaves with the people who hold it. Kosli automates the recording and enforcement of controls so you get continuous evidence that the right things happened.

## The SDLC control model

Controls are organized by the phase of the software delivery lifecycle where they apply:

<CardGroup cols={2}>
  <Card title="Build controls" icon="hammer">
    Securing the build chain: dependency management, secrets scanning, artifact provenance, controlled build environments, infrastructure as code.
  </Card>
  <Card title="Release controls" icon="rocket">
    Validation before deployment: code review, quality assurance, vulnerability scanning, deployment approvals.
  </Card>
  <Card title="Runtime controls" icon="server">
    Monitoring and enforcement in production: change records, deployment controls, secrets management, workload monitoring, drift detection.
  </Card>
  <Card title="Lifecycle controls" icon="arrows-spin">
    Human and organizational factors: security training, penetration testing, service ownership.
  </Card>
</CardGroup>

<Tip>
  Kosli's [SDLC Controls Framework](https://sdlc.kosli.com) contains a rich catalog of controls with risk mappings. Your organization may define additional controls or adapt these to fit your specific compliance requirements.
</Tip>

## Example controls by phase

The following examples show representative controls from each phase, the risks they mitigate, and the Kosli concepts that implement them.

### <Icon icon="hammer"/> Build

Build controls secure the build chain itself. The reason these controls exist at the build phase (rather than later) is that a compromised dependency, an exposed secret, or an unverifiable artifact is cheapest to catch before it enters the release pipeline. Once a tainted artifact passes the build stage, every downstream control has to work harder to detect it.

| Control | Risk mitigated | Kosli concept |
|---------|---------------|---------------|
| Dependency management | Supply chain compromise, Vulnerable software in production | Attestation (`snyk` type) |
| Secrets scanning | Credential and secret exposure | Attestation (custom type) |
| Artifact binary provenance | Supply chain compromise | Artifact (SHA256 fingerprint) |

### <Icon icon="rocket"/> Release

Release controls validate that software is ready for production. While build controls secure the ingredients, release controls verify the result: has the code been reviewed, do the tests pass, are there known vulnerabilities, and has someone authorized the deployment? The reason code review sits here (rather than in build) is that it is a validation of the change as a whole, not of the build toolchain.

| Control | Risk mitigated | Kosli concept |
|---------|---------------|---------------|
| Code review | Insider threat, Unreviewed changes | Attestation (`pullrequest` type) |
| Quality assurance | Vulnerable software in production | Attestation (`junit` type) |
| Vulnerability scanning | Vulnerable software in production, Supply chain compromise | Attestation (`snyk` type) |
| Deployment approvals | Unauthorized deployment | Attestation (`approval` type) |

### <Icon icon="server"/> Runtime

Runtime controls address what happens after deployment. Even if every build and release control passes, the production environment can still diverge from expectations. Configuration drift happens gradually as manual fixes accumulate. Shadow changes appear when someone bypasses the pipeline altogether. The reason runtime monitoring matters is that it closes the loop: you verify not just what you intended to deploy, but what is actually running.

| Control | Risk mitigated | Kosli concept |
|---------|---------------|---------------|
| Runtime workload monitoring | Shadow changes, Unauthorized deployment | Environment Snapshot |
| Drift detection | Configuration drift | Environment Snapshot + notifications |
| Change records | Lack of auditability | Trail |

### <Icon icon="arrows-spin"/> Lifecycle

Lifecycle controls address the human and organizational factors that underpin all other controls. While build, release, and runtime controls target specific phases, lifecycle controls ensure that teams have the knowledge, accountability, and validation processes to operate a secure SDLC. Without them, the technical controls may be in place but the people and processes behind them are fragile.

| Control | Risk mitigated | Kosli concept |
|---------|---------------|---------------|
| Security training | Insider threat | Attestation (custom type) |
| Penetration testing | Vulnerable software in production | Attestation (custom type) |
| Service ownership | Lack of auditability | Trail |

## From controls to Kosli concepts

The controls above are abstract: they describe *what* needs to happen. Kosli provides the building blocks that *implement* them. The reason Kosli models controls this way (rather than, say, embedding them as pipeline plugins or CI-specific integrations) is that controls span tools and environments. A single control like "code review" might originate in GitHub, get recorded in a CI pipeline, and need to be verifiable months later during an audit. Kosli's model is designed to be tool-agnostic so that evidence from any source fits into the same structure.

Kosli organizes controls through a hierarchy. At the top is a **Flow**, which models a process that contains controls (your CI pipeline, your Terraform workflow, your onboarding procedure). Each time that process runs, it creates a **Trail**, a single execution that collects all the evidence for that run. The reason this layered approach matters is that a single attestation is meaningless without the context of which process produced it and which execution it belongs to.

Within a Trail, **Attestations** record that specific controls were executed and capture their results. A **Flow Template** defines which attestations are required for a Trail to be compliant. If a required attestation is missing, Kosli flags the Trail as non-compliant.

At the runtime level, **Environment Policies** enforce controls over what may run in production, and **Environment Snapshots** provide the data that makes runtime controls like drift detection possible. The reason Environments are modeled separately from Flows is that what you build and what you run are fundamentally different concerns. An artifact may pass every build and release control but still create a compliance problem if it appears in an environment where it does not belong.

To understand each of these building blocks in detail, continue to [How Kosli works](/understand_kosli/how_kosli_works).

<CardGroup cols={2}>
  <Card title="How Kosli works" icon="cubes" href="/understand_kosli/how_kosli_works">
    Explore each building block and how they connect.
  </Card>
  <Card title="Build controls lab" icon="flask" href="/labs/lab-03-build-controls">
    See build controls in action through a hands-on lab.
  </Card>
  <Card title="Release controls lab" icon="flask" href="/labs/lab-04-release-controls">
    See release controls in action through a hands-on lab.
  </Card>
  <Card title="Runtime controls lab" icon="flask" href="/labs/lab-05-runtime-controls">
    See runtime controls in action through a hands-on lab.
  </Card>
</CardGroup>
