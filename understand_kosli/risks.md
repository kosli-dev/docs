---
title: 'Risks'
description: 'Why modern software delivery introduces risks that are hard to manage, and how to think about them.'
---

Software teams ship faster than ever. Code flows through automated pipelines, pulls in hundreds of open-source dependencies, and deploys to distributed infrastructure multiple times a day. That speed is a strength, but it also means that the number of places where something can go wrong has grown dramatically. A single compromised dependency, an unreviewed commit, or an unnoticed configuration change can reach production before anyone is aware of it.

The reason these risks are hard to manage is not that teams are careless. It is that the delivery process spans so many tools, environments, and people that no single person has full visibility. Evidence of what happened (and whether it should have happened) is scattered across CI logs, chat threads, ticketing systems, and cloud consoles. Reconstructing the full picture after an incident, or during an audit, is slow and unreliable.

## What is a risk?

In this context, a risk is a condition or event in your software delivery lifecycle (SDLC) that could compromise the integrity, security, or compliance posture of your software. These are not hypothetical. They reflect real-world incidents that have affected organizations across industries.

## The risk landscape

Kosli identifies nine categories of risk across the SDLC. They fall into three broad groups depending on where in the lifecycle they originate.

### <Icon icon="box-open"/> Risks from your supply chain and build process

Modern software is largely assembled, not written from scratch. Your application depends on libraries, base images, and build tools maintained by third parties. If any of those components are tampered with, malicious code enters your pipeline without anyone writing a single bad line. At the same time, the build process itself can introduce vulnerabilities if security scanning is skipped or secrets are accidentally embedded in artifacts.

| Risk | Description |
|------|-------------|
| **Supply chain compromise** | Third-party dependencies or build tools are tampered with, injecting malicious code into your software. |
| **Vulnerable software in production** | Known vulnerabilities ship to production because scanning was skipped, ignored, or incomplete. |
| **Credential and secret exposure** | Developers commit API keys, tokens, or passwords to source control or embed them in artifacts. |

### <Icon icon="users"/> Risks from within your team

Not all risks come from outside. Authorized users can introduce problems too, whether through honest mistakes or deliberate circumvention of process. Code that skips peer review, deployments that bypass approval gates, and changes that no one documents all create gaps that are invisible until something breaks or an auditor asks questions.

| Risk | Description |
|------|-------------|
| **Insider threat** | Changes made using authorized credentials without proper review or approval. This includes mistakes by team members, deliberate circumvention of process, or third parties who have compromised legitimate credentials. |
| **Unauthorized deployment** | Software reaches production without passing required gates or approvals. |
| **Unreviewed changes** | Code or configuration changes bypass peer review, increasing the chance of defects or policy violations. |
| **Lack of auditability** | There is no reliable record of what changed, when, why, or by whom, making audits costly and unreliable. |

### <Icon icon="server"/> Risks from your runtime environments

Once software is deployed, the runtime environment becomes its own source of risk. Configurations drift from their expected state, artifacts appear that cannot be traced back to any known build, and changes happen outside the deployment pipeline entirely. These "shadow changes" are particularly dangerous because they bypass every control you have put in place during build and release.

| Risk | Description |
|------|-------------|
| **Configuration drift** | Production environments diverge from their expected state without anyone noticing. |
| **Shadow changes** | Changes appear in production that cannot be traced back to any known build or deployment process. |

<Tip>
  Kosli's [SDLC Controls Framework](https://sdlc.kosli.com) organizes these nine risks with detailed descriptions and risk-to-control mappings. Your organization may identify additional risks or prioritize them differently depending on your industry, regulatory environment, and threat model.
</Tip>

## Risks and compliance frameworks

These risks are not unique to Kosli. They are the same concerns addressed by compliance frameworks like SOC 2, ISO 27001, and FDA 21 CFR Part 11. Each framework codifies requirements for managing some or all of these risks through documented controls and evidence. For example, SOC 2's Change Management criteria address unauthorized deployment and unreviewed changes, while its Logical Access controls relate to insider threat and credential exposure.

Kosli does not replace a compliance framework. The reason it is designed this way is that frameworks define *what* you must demonstrate, while Kosli automates *how* you demonstrate it. The alternative (building compliance tooling into each framework individually) would mean duplicating effort across SOC 2, ISO 27001, and every other standard your organization adopts. Kosli instead provides a single evidence layer that serves all of them. When your CI pipeline attests that a security scan passed, or Kosli detects unexpected changes in a production environment, that is compliance evidence recorded automatically. Without Kosli, producing and maintaining that evidence requires manual effort, and manual evidence has a tendency to be incomplete, inconsistent, or simply missing when you need it most.

Now that you understand what can go wrong, the next step is understanding the [controls](/understand_kosli/controls) that prevent it and how Kosli implements them.
