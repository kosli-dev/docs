---
title: 'What is Kosli?'
description: 'Why compliance automation matters and how Kosli approaches it.'
---

Proving compliance in fast-moving software delivery is hard. Evidence is scattered across tools, audits are manual, and changes happen faster than any spreadsheet or CAB meeting can track. Kosli automates this. It is a tool-agnostic platform that integrates with your existing CI systems, scanners, and runtime environments, consolidating compliance data into a single place.

## Kosli in a nutshell

Think of Kosli as a flight recorder for your software delivery lifecycle (SDLC). Like a flight recorder, Kosli does not control the plane. It records what happened so that after the fact you can reconstruct the sequence of events. The reason this matters in software is that incidents and audit questions are inevitable, but the ability to answer "what was running, how did it get there, and did it pass all required checks?" should not depend on someone's memory or a manual audit trail.

You report events of interest (builds, test results, deployments, environment state) through the [CLI](/client_reference) or [API](/api-reference). Kosli stores each record as an immutable entry and evaluates it against the [controls](/understand_kosli/controls) defined in your policies. Change sources include build systems (CI pipelines), runtime environments (Kubernetes clusters, AWS ECS, Lambda), and business processes (onboarding, access management).

<Frame>
  <img
    src="/images/Kosli-overview-docs.png"
    alt="Diagram showing how Kosli records events from CI pipelines, runtime environments, and business processes into immutable audit trails."
  />
</Frame>

## When to use Kosli

- **Compliance automation**: Traditional compliance evidence collection is manual, error-prone, and always playing catch-up with the pace of delivery. Kosli automates evidence collection for frameworks like SOC 2, ISO 27001, or NIST SP 800-53, verifying that artifacts in production have passed required controls (security scans, code review, approval workflows) so you stay audit-ready at all times.
- **Change observability**: In distributed systems, understanding what changed, when, and by whom often requires piecing together logs from half a dozen tools. Kosli provides a unified view of change across your entire delivery pipeline, even without specific compliance requirements.

## Where to go next

<AccordionGroup>
  <Accordion title="New to Kosli?" icon="graduation-cap" defaultOpen>
    Read [Risks](/understand_kosli/risks), [Controls](/understand_kosli/controls), and [How Kosli works](/understand_kosli/how_kosli_works) in order. Use the [Glossary](/understand_kosli/glossary) as a reference along the way. When you are ready to try it hands-on, work through the [Learning Labs](/labs).
  </Accordion>
  <Accordion title="Setting up Kosli for your team?" icon="users">
    Head to [Getting Started](/getting_started/install) for step-by-step setup, or see the [Implementation Guide](/implementation_guide/phase_1/roles_and_responsibilities/overview) for organizational rollout planning.
  </Accordion>
  <Accordion title="Looking up a specific term?" icon="magnifying-glass">
    See the [Glossary](/understand_kosli/glossary) for quick-reference definitions of every Kosli term.
  </Accordion>
</AccordionGroup>
