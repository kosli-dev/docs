---
name: doc-review
description: Review documentation for quality, structure, and convention compliance. Use when the user wants to review docs, audit a page or section, check if content is clear, evaluate information architecture, or assess navigation. Do NOT use when the user wants to write or fix docs — use doc-write for that. For a periodic whole-site navigation and coverage audit that files issues, use doc-structure. Triggers on "review the docs", "audit this page", "is this getting-started page clear", "check the implementation guide section".
---

# Doc review

Review changed documentation against this repo's CLAUDE.md, the Diátaxis framework, and the site's information architecture.

Most of this review's value comes from checks a human reviewer cannot do cheaply: verifying prose against generated reference pages, catching pages the change forgot to update, and questioning where a new page lives. Spend your turns there.

## What is already checked for you

Do not re-do this work:

- **Spelling and Vale rules** — the `Mintlify Validation (kosli) - vale-spellcheck` check runs on every PR and enforces `styles/Kosli/AmericanSpelling.yml`. Never report a spelling finding. Never report "American spelling: pass".
- **PR title format** — the `Validate PR Title` job enforces Conventional Commits.
- **Live-docs script behavior** — the `Test live-docs scripts` job runs `pytest tests/`.

Note that `Mintlify Validation (kosli) - link-rot` reports `skipping` on most PRs, so **internal link resolution is not reliably enforced** — keep verifying link targets yourself.

## Before reviewing

1. **Read CLAUDE.md** — the compliance checklist for frontmatter, components, links, writing style, and the don'ts.
2. **Read `config/navigation.json`** for the navigation tree. Navigation lives there, not in `docs.json` — `docs.json` only holds a `$ref` to it.
3. **Read each changed file at the current branch head**, not just the diff. A finding that was already fixed in a later commit must not be reported.
4. **Determine scope** — a single page, a section, or the changed files in a PR. If unclear, ask.

## The checks that matter most

Run these first. They found the real defects in past reviews.

### 1. Cross-file consistency

A change is rarely confined to the files it touches. Grep the rest of the site for what the change contradicts.

- **Prose vs. generated reference.** Pages under `client_reference/`, `terraform-reference/`, and `helm/` are generated. When prose names a command, flag, resource, or attribute, verify it exists in the generated page. *Precedent: a changelog entry documented `kosli update attestation-type`, a command with no reference page — it did not exist.*
- **Prose vs. generated schema.** `schemas/flow-template/v1.json` and `schemas/policy/v1.json` come from the API. When a page enumerates valid values, diff that list against the schema. *Precedent: `template-reference/flow_template.md` listed an attestation-type set the regenerated schema had already outgrown.*
- **Incomplete sweeps.** When a change removes or renames a concept, grep the whole site for the old term and list every file still using it. *Precedent: an approvals-removal PR updated `glossary.md` and `controls.md` but left `understand_kosli/how_kosli_works.md:22` still calling approvals a built-in attestation type.*

### 2. Placement and navigation

- Every new page must appear in `config/navigation.json`. Missing entry is **Critical**.
- **Ask whether the page is in the right tab and group**, not just whether it is listed somewhere. Apply the placement table in the `doc-write` skill. A page whose content is complete factual lookup belongs in the **Reference** tab even when it documents an integration. *Precedent: a GitHub Action reference page was first authored into `integrations/`; a human reviewer had to ask for the move to Reference. That question should come from this review.*
- Flag a new group created to hold a single page, and any page nested more than three levels below its tab.

### 3. Redirects

Three of the last fourteen doc PRs needed `config/redirects.json` entries. Any PR that renames, moves, or deletes a page needs one. A missing redirect for a page that was live is **Critical** — the URL is in customers' bookmarks, in CLI error output, and in the changelog.

### 4. Anchor stability

Headings are link targets. Before accepting a renamed heading, grep for its anchor across the repo. Some anchors are referenced from outside the docs — `faq/faq.md#boolean-flags` is emitted in CLI error messages. A renamed heading that breaks an inbound anchor is **Critical**.

### 5. Page-level quality

- **Diátaxis fit** — tutorial, how-to, reference, or explanation? Does the content match the form? Report a mismatch only when it would send a reader down the wrong path, not as a taxonomy note.
- **Frontmatter** — `title` and `description` present and accurate.
- **Links** — root-relative (`/getting_started/install`), never relative (`../install`). A relative link is **Critical**. Verify every internal target resolves to a file that exists.
- **Correctness** — commands, flags, output blocks, and screenshots that match the current product.

## What not to report

The bar is: **would a reader be measurably better off after this change?** If not, leave it out. Specifically, never report:

- A finding already fixed at the current branch head.
- Rewording that is a matter of taste. Grammar that is merely awkward is not a finding; grammar that is ambiguous or wrong is.
- Whitespace or column alignment inside pasted command output.
- Anything the automated checks above already cover.
- A finding you immediately talk yourself out of. If the recommendation ends in "which it already does" or "no change needed", it was never a finding.
- Praise, "what looks good" sections, and tables of checks that passed. The author knows what they wrote. Reviews are re-rendered into a sticky comment on every push, so recital costs the reader on every read.

Report at most **8 findings**. If more clear the bar, report the 8 that matter most and say how many were left out.

## Output

Group findings by file. For each: **Location** (`file:line`), **Issue** (one or two sentences), **Recommendation** (concrete).

Categorize:

- **Critical** — missing nav entry, relative link, broken internal link or anchor, missing redirect, factually wrong instruction.
- **Improvement** — a reader is likely to be misled, blocked, or sent to the wrong page.
- **Suggestion** — a real but minor gain. If you have no Improvements, question whether the Suggestions are worth posting at all.

Close with one line: counts by category, and a merge verdict. When nothing clears the bar, say exactly that in one sentence and stop — a short review is a good review.
