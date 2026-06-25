---
title: "Platform Engineers"
description: "Role guide for Platform and DevOps Engineers using Kosli"
---

You build the internal tooling, workflows, and golden paths that help developers ship software reliably and securely. You care about scaling delivery without scaling your team.

If you’re supporting CI/CD pipelines, infrastructure, or compliance enablement across multiple services or teams, this page is for you.

## How Kosli helps you

Kosli gives you a single, unified way to track everything that moves through your delivery pipelines: code, artifacts, tests, approvals, deployments and prove it’s been done safely and correctly.

With Kosli, you can:
- Automate compliance and eliminate manual change approval processes.
- Capture tamper-proof evidence across your SDLC (without slowing down delivery).
- Monitor all runtime environments and deployments across teams.
- Offer developers secure paved paths that embed governance from the start.


## Your role in using Kosli

As a platform engineer, you're typically responsible for:
- Setting up Kosli in CI/CD and infrastructure environments.
- Creating and maintaining **Flows**, which model how changes move through pipelines.
- Defining and triggering **Trails** to capture each run of those pipelines.
- Configuring **Attestations** for tests, scans, and internal checks (e.g., Jira, Snyk).
- Capturing **Environment Snapshots** and enforcing **Policies** to govern deployments.
- Building reusable Kosli integrations (e.g., GitHub Actions, GitLab CI templates) so your dev teams don’t have to think about it.

You’ll often be the first person to integrate Kosli into your platform and roll it out to the rest of the org.

## What you’ll work with

You’ll primarily interact with:
- **Kosli CLI:** integrated into your CI/CD pipelines and scripts.
- **Flows** and **Trails:** to represent and track software delivery runs.
- **Artifacts** and **Attestations:** to connect builds and compliance evidence.
- **Environment Snapshots** & **Policies:** to enforce governance in prod and staging.
- **Kosli UI:** to review deployment status, compliance views, and audits.

If you're running Kubernetes, Terraform, or other infrastructure tools, Kosli also integrates easily to monitor state and changes.

## What success looks like

When Kosli is successfully adopted by platform engineering, you’ll see:

- Your pipelines continuously produce verifiable, compliant deployments.
- You eliminate the need for spreadsheet-driven approvals and CAB meetings.
- Developers onboard Kosli passively via the platform, they rarely have to learn it directly.
- Security and compliance teams get everything they need with minimal friction.
- Audits are a non-event: you already have the evidence.

## Common questions you might have

<AccordionGroup>
  <Accordion title="Do I need to change our pipelines to use Kosli?" icon="comment-question">

  No major changes. Kosli integrates via CLI commands you can drop into any pipeline.
  </Accordion>
  <Accordion title="Can I templatize this across many teams?" icon="comment-question">

  Yes. Use flow templates and reusable CI snippets to roll out a consistent setup.
  </Accordion>

  <Accordion title="Does Kosli work with our existing tools?" icon="comment-question">
  Almost certainly. Kosli is tool-agnostic and supports GitHub Actions, GitLab, Jenkins, Kubernetes, Terraform, and more.
  </Accordion>

  <Accordion title="How do I know it's working?" icon="comment-question">
  Kosli automatically gives you compliance status per environment and per change. You can inspect Trails, download audit packages, and integrate with Slack or through Webhooks for alerts.
  </Accordion>
</AccordionGroup>

## Required Kosli User Roles

To perform the responsibilities described above, users in this role typically need:
- **Recommended role**: Member
- **Alternative role**: Admin (for lead platform engineers managing organization-wide setup)

Platform engineers need to set up flows, manage service accounts, configure integrations, and implement Kosli across teams. The Member role provides these capabilities. Lead platform engineers who manage the overall organizational setup may require Admin access to manage users and organization settings.

Learn more about [Kosli user roles and permissions](/administration/managing_users/roles_in_kosli).

## Where to start

- [**Getting Started Guide**](): For a complete technical setup walkthrough.
- [**CLI Reference**](): Full list of commands.
- [**Concepts Overview**](): Understand how Flows, Trails, and Attestations fit together.