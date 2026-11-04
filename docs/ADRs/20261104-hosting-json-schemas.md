# 20261104: Hosting the JSON Schemas Kosli serves

Date: 04-11-2026
Who: Dan Grøndahl (author), Claude (claude-opus-5-5)
Status: Accepted

## Overview

The docs site keeps mirroring only the two schemas whose URL users write into their own files:
the environment policy and the flow template. Every other schema the API serves is linked at its
API URL, `https://app.kosli.com/api/v2/schemas/...`, and is not copied into this repo.

## Context

The Kosli API serves four JSON Schemas, listed in its
[OpenAPI spec](https://app.kosli.com/api/v2/openapi.json):

| API endpoint | `$id` the schema declares | Mirrored here |
|---|---|---|
| `/api/v2/schemas/environment-policy/v1` | `https://docs.kosli.com/schemas/policy/v1` | `schemas/policy/v1.json` |
| `/api/v2/schemas/flow-template/v1` | `https://docs.kosli.com/schemas/flow-template/v1` | `schemas/flow-template/v1.json` |
| `/api/v2/schemas/evaluation-input/trail/v1` | `https://docs.kosli.com/schemas/evaluation-input/trail/v1` | no |
| `/api/v2/schemas/evaluation-input/trails/v1` | `https://docs.kosli.com/schemas/evaluation-input/trails/v1` | no |

`scripts/update_schemas.py` copies the first two into `schemas/`, and `update-schemas.yml` opens a
PR when the copies drift from the API. `config/redirects.json` sends the extensionless URLs to the
`.json` files, because the docs site serves static files.

[PR #493](https://github.com/kosli-dev/docs/pull/493) documented the evaluation-input schemas with
a `curl` to the API URL, while every other schema in the docs is linked at `docs.kosli.com`. That
looked inconsistent, so we asked whether the evaluation-input schemas should be mirrored too.

Two facts shaped the answer:

- **A `$id` is a label, not a download location.** Nothing fetches it. It matters when another
  schema `$ref`s it, and none of these schemas use `$ref`. The evaluation-input `$id`s point at
  URLs that return 404 on the docs site, but nothing breaks because of it.
- **The policy URL is part of a file format.** `_schema: https://docs.kosli.com/schemas/policy/v1`
  is written into customers' policy files and checked by Kosli, and editors resolve
  `yaml-language-server: $schema=https://docs.kosli.com/schemas/...` comments in policy and
  flow-template files. Those URLs can never move. No user file names an evaluation-input schema;
  users only download it to run `opa check`.

Mirroring a schema also costs more than the copy. Adding one means editing the `_SCHEMAS` map in
`update_schemas.py`, `config/redirects.json`, the PR body in `update-schemas.yml`, `CLAUDE.md` and
the doc-review skill. That is five hand-kept lists of information the server already holds, with nothing
checking they agree. Between scheduled runs the copy can also lag the API, which matters for a
schema used to type-check a policy before publishing.

## Options

### A. Mirror every schema

Add the evaluation-input schemas to `update_schemas.py` and `config/redirects.json`, and link to
`docs.kosli.com` everywhere. Consistent URLs, and the `$id`s resolve. It grows each of the five
lists, and the docs copy can be stale exactly when someone uses it to type-check a policy.

### B. Mirror every schema, derived from the API

Have `update_schemas.py` read the schema endpoints from the OpenAPI spec and write each file to the
path its `$id` names, with one wildcard redirect. A new server schema then needs no docs change.
It removes the hand-kept lists but keeps the copy and its lag, and relies on Mintlify supporting
the wildcard redirect.

### C. Redirect `docs.kosli.com/schemas/*` to the API

No copies, so nothing drifts, and the existing `$id`s keep resolving. Unverified: whether Mintlify
redirects to another domain, whether editors follow the redirect for `$schema`, and whether the
in-browser policy builder can load the schema across origins after a redirect. `curl` users would
need `-L`.

### D. A dedicated schemas host

`https://schemas.kosli.com/{name}/v1`, a CDN in front of the API that rewrites to
`/api/v2/schemas/{name}/v1`, caches, and sends CORS headers. Short permanent identifiers without
`/api/v2` in them, one source, and one rule for every schema. It needs DNS, a certificate and CDN
configuration owned outside the docs team, and the existing `docs.kosli.com` URLs would remain as
aliases forever. With only one schema URL users depend on, it does not pay for itself yet.

### E. Leave it as it is

Keep mirroring the two schemas whose URL is part of a user-facing format, and link everything else
at the API.

## Decision

Option E: leave it as it is. `docs.kosli.com/schemas/...` hosts only schemas whose URL users write into
their own files, which today means the environment policy and the flow template. Any other schema is linked
at its API URL and is not added to `update_schemas.py`.

## Consequences

- Nothing changes on the site or in `update_schemas.py`. The `curl` in
  `policy-reference/rego_policy.mdx` stays on the API URL.
- Pages use two kinds of schema URL. The rule for which one to use is whether users write the URL
  into a file.
- The evaluation-input schemas declare `$id`s on `docs.kosli.com` that do not resolve. Harmless,
  but untidy; `kosli-dev/server` could change them. If it does, it should pick the URL it means to
  keep, since putting `/api/v2` into a permanent identifier makes a later move to a dedicated host a
  second migration.
- A new schema whose URL users will write into their files, such as a new policy or template format or a
  `v2` of an existing one, is mirrored, and costs an edit to each of the five lists. If that
  happens more than occasionally, revisit deriving the list from the API, or a dedicated host.

## External links

- [PR #493](https://github.com/kosli-dev/docs/pull/493): documented the evaluation-input schemas
- [Kosli API OpenAPI spec](https://app.kosli.com/api/v2/openapi.json)
