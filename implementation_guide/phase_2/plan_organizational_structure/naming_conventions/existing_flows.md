---
title: "Adopting a convention on existing flows"
description: "How to move flows that are already in use onto a naming convention without losing history or coordinating a cutover."
---

The [Flows and Trails](/implementation_guide/phase_2/plan_organizational_structure/naming_conventions/flows_and_trails) conventions assume you are naming flows for the first time. If your organization already has flows in use, this page explains how to move them onto a convention safely.

## Rename, do not recreate

Rename each existing flow to its new name with [`kosli rename flow`](/client_reference/kosli_rename_flow):

```bash
kosli rename flow OLD-NAME NEW-NAME
```

Renaming keeps the flow's history attached to it, and the old name keeps routing to it. Do not create a new flow under the new name and retire the old one: every pipeline that still uses the old name keeps writing to the old flow, and the history splits across two flows.

## How the old name behaves after a rename

After renaming, the old name still resolves to the renamed flow for both reads and writes:

- `kosli get flow`, `kosli list trails` and similar queries act on the renamed flow.
- `kosli begin trail` and `kosli attest` commands that still use the old name record into the renamed flow rather than auto-creating a new one.

The only operation that requires the current name is a further rename.

The old name stops resolving once another flow is created with, or renamed to, that name. From then on, commands using the old name act on the new flow.

<Warning>
Do not reuse an old name for a different flow until every pipeline that used it has been updated. Once the name is taken, any job still using it writes into the wrong flow.
</Warning>

## Rollout order

No simultaneous cutover is needed, because jobs that still use the old name keep landing in the right flow.

<Steps>
  <Step title="Rename the flow in Kosli">
    Run `kosli rename flow` for each flow you are moving onto the convention.
  </Step>
  <Step title="Update pipelines at your own pace">
    Change the flow name in each CI job when convenient, across any number of CI systems. Jobs that have not been updated yet continue to record into the renamed flow.
  </Step>
  <Step title="Retire the old name">
    Once no pipeline uses the old name, it needs no further action. Leave it unused so it keeps pointing at the renamed flow.
  </Step>
</Steps>

## When the convention also changes trail names

Renaming a flow does not change how trails inside it are named. A job that has not been updated still writes trail names in the old style into the renamed flow.

For flows whose trail naming also changes, either:

- update the pipeline before renaming the flow, so the first trails under the new flow name already follow the convention, or
- rename the flow first and accept a short window of off-convention trail names until the pipeline is updated.

## Limits

- **A rename cannot split a flow.** A flow that mixes build and release activity cannot be turned into a Build Flow and a Release Flow by renaming. Create the new flows, point the pipelines at them, and archive the old flow once it is no longer used.
- **Archiving retires a name from auto-creation.** Archiving a flow renames it to `<name>-archived-at-<timestamp>`, but Kosli remembers the original name. A stale `kosli attest` or `kosli begin trail` job that still uses it fails with `Cannot auto-create Flow because '<name>' previously existed` instead of silently creating a new flow. An explicit `kosli create flow` with that name still succeeds and takes the name over. See [`kosli archive flow`](/client_reference/kosli_archive_flow).
