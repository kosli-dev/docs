---
file: CLAUDE.md
evaluated_commit: untracked
head_commit: 16e6d6867149d48c627bf8242d26e06ad52b963c
dirty: true
evaluated_at: 2026-03-04T00:00:00Z
grade: C
percentage: 55
weighted_score: 44
max_score: 80
context: project
weights_source: defaults
---

# CLAUDE.md Evaluation Report

- **File**: `CLAUDE.md` @ *untracked*
- **Evaluated at**: 2026-03-04
- **Context**: project
- **Grade**: **C** (55%) — Functional foundation, significant coverage gaps
- **Weighted score**: 44 / 80

---

## Score breakdown

| Dimension | Score | Weight | Weighted | Max |
|---|---|---|---|---|
| Clarity | 3/5 | ×3 | 9 | 15 |
| Prioritization | 2/5 | ×2 | 4 | 10 |
| Context efficiency | 4/5 | ×3 | 12 | 15 |
| Behavioral coverage | 2/5 | ×3 | 6 | 15 |
| Composability | 2/5 | ×2 | 4 | 10 |
| Testability | 3/5 | ×2 | 6 | 10 |
| Maintainability | 3/5 | ×1 | 3 | 5 |
| **Total** | | | **44** | **80** |

---

## Biggest opportunity

**Behavioral Coverage** (currently 2/5, weight ×3)

To move from Basic → Targeted:
- Add a commit message convention (Conventional Commits)
- Add at least 3 explicit "do NOT" rules
- Add a writing style pointer (Diátaxis framework)

---

## Quick wins

1. **Prioritization 2→3**: Add a `## Core rules` section at the top with 3–5 non-negotiable items
2. **Behavioral Coverage 2→3**: Add a `## Don'ts` section — 5 bullets would be enough
3. **Composability 2→3**: Add one sentence scoping what this file covers vs. what skills govern

---

## Dimension scores

### Clarity — 3/5 (×3)

**Evidence**: Commands are precise. Internal links rule has a concrete example. Architecture section names the exact routing path.

**Gap**: MDX components list is a flat enumeration with no guidance on when to choose one over another. No frontmatter example. Font Awesome lookup unspecified.

**Recommendation**: Add a one-line frontmatter example and a note on `<Steps>` vs `<Tabs>` usage.

---

### Prioritization — 2/5 (×2)

**Evidence**: Sections imply a loose ordering but no explicit priority markers, no MUST/SHOULD language, no conflict resolution.

**Gap**: No guidance on what takes precedence when a convention conflicts with a user instruction.

**Recommendation**: Add a `## Core rules` block with 3–5 non-negotiable items.

---

### Context efficiency — 4/5 (×3)

**Evidence**: 42 lines, no padding, code blocks and bullet lists used appropriately. Every line influences behaviour.

**Gap**: MDX component list could be a two-column table pairing component with use-case.

**Recommendation**: Minor — convert component list to a table.

---

### Behavioral coverage — 2/5 (×3)

**Evidence**: Covers structural basics: frontmatter, link format, navigation registration, deploy mechanism.

**Gap**: No commit conventions, PR workflow, branch naming, writing style, image handling, or anti-patterns. `essentials/` flagged as non-Kosli content but no instruction on what to do with it.

**Recommendation**: Add a `## Don'ts` section: no relative links, no pages without `docs.json` update, no direct commits to `main`.

---

### Composability — 2/5 (×2)

**Evidence**: No mention of skills, MCP servers, or other instruction layers. No scope boundaries.

**Gap**: When a skill is active, there's no scope boundary to prevent overlap with e.g. `pr-creator` conventions.

**Recommendation**: Add: *"This file governs repo-specific conventions. Skills and system prompts govern their own domains."*

---

### Testability — 3/5 (×2)

**Evidence**: Several binary-verifiable instructions: frontmatter requirements, root-relative links, navigation registration.

**Gap**: MDX usage and writing quality have no testable criteria. No commit format rule to verify.

**Recommendation**: Add a Conventional Commits rule — immediately makes commit messages mechanically verifiable.

---

### Maintainability — 3/5 (×1)

**Evidence**: Five clean independent sections. Readable in under a minute.

**Gap**: No version markers, no "why" comments. `essentials/` note lacks context.

**Recommendation**: Add a comment explaining why `essentials/` is in the repo.
