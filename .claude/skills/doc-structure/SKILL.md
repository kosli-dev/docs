---
name: doc-structure
description: Periodic whole-site audit of documentation navigation, information architecture, and changelog coverage, filing GitHub issues for what it finds. Use for a scheduled or on-demand health check of the docs site as a whole — not for reviewing a single page or a pull request. Triggers on "audit the docs structure", "is the navigation still sensible", "what shipped that we never documented", "run a docs health check", "check changelog coverage".
---

# Doc structure audit

Audit the whole site for navigation and coverage problems, then file one GitHub issue per finding.

This is the counterpart to `doc-review`, which sees only the files a PR touched. Problems that no single PR causes — a group that grew past its label, a feature three products shipped that no page explains — are invisible to per-PR review and accumulate silently. This skill exists to find those.

Run it monthly or on demand. It is read-only against the docs and write-only against the issue tracker: **never edit docs pages or navigation here.** The output is issues, so a human decides what to change.

## Step 1 — Load current state

```bash
gh issue list --state open --limit 100 --json number,title,labels,body
```

Read every open issue before auditing. The backlog already tracks known gaps, and a monthly job that re-files them is worse than one that files nothing. Keep this list in mind through every step below.

## Step 2 — Mechanical checks

These are cheap and either pass or fail. Run all of them.

**Navigation integrity** — every page routed, no dangling entries:

```bash
python3 -c "
import json
nav=json.load(open('config/navigation.json')); out=[]
def walk(o):
    if isinstance(o,str): out.append(o)
    elif isinstance(o,list): [walk(i) for i in o]
    elif isinstance(o,dict): [walk(v) for k,v in o.items() if k in ('pages','groups','menu','tabs')]
walk(nav); open('/tmp/innav.txt','w').write('\n'.join(sorted(out))+'\n')"

find . \( -name '*.md' -o -name '*.mdx' \) \
  | grep -vE 'node_modules|^\./\.(github|mintlify|claude)|^\./snippets|/(CLAUDE|README)\.md$' \
  | sed -E 's|^\./||; s|\.mdx?$||' | sort > /tmp/onfile.txt

echo "--- on disk, not in nav (orphans) ---"; comm -23 /tmp/onfile.txt /tmp/innav.txt
echo "--- in nav, no such file ---";          comm -13 /tmp/onfile.txt /tmp/innav.txt
```

`index` is the site landing page and is correctly absent from navigation. Anything else in the first list is an orphan — the page is live but unreachable from the sidebar. Anything in the second list is a broken nav entry.

**Shape** — walk the tree and record, for each group: depth, child count, and whether the label is sentence case. Flag:

- Any group with exactly one child. It costs a click and a disclosure triangle and returns nothing.
- Any page more than three levels below its tab.
- Any group label in Title Case. CLAUDE.md mandates sentence case for headings, and nav labels are the most-read headings on the site.
- Any group past ~12 children with no internal grouping.
- Icon inconsistency: groups that have `icon` sitting beside sibling groups that do not.

**Cross-reference rot** — pages nothing links to, and headings whose anchors are referenced from a page that no longer has them.

## Step 3 — Information architecture

Judgment, not mechanics. Read the group labels and the pages under them and ask:

- **Does each group's label still describe its contents?** A group named for a doc type that holds a different type sends readers to the wrong place. Check the Diátaxis form of every page in a group against the group's promise.
- **Is one topic split across two homes?** Two groups that each hold half of a subject force the reader to know the org chart. Look for the same noun appearing in two top-level groups.
- **Does a top-level tab deliver what it promises?** A tab is the strongest navigational claim the site makes. A tab holding a handful of stub pages under an ambitious name over-promises.
- **Where would a reader look first?** For the five or six most common tasks, trace the path from the landing page. Count the clicks and the guesses.

Weigh a finding by how many readers hit it. A mislabeled group at the top of the Documentation tab matters; a nesting quirk four levels into a reference section does not.

## Step 4 — Changelog coverage

`changelog/index.mdx` is the record of what shipped. Compare it against what the docs explain.

**Find the pages the changelog leans on:**

```bash
grep -o '](/[a-z_/#-]*' changelog/index.mdx | sed 's|](||; s|#.*||' | sort | uniq -c | sort -rn | head -25
```

**Then, for each feature named in an entry from roughly the last quarter, check that the page the entry links to actually explains it.** Take the feature's own keyword — the flag, attribute, or noun the entry is about — and grep the linked page for it. A changelog entry that links to a page which never mentions the thing is a concrete, high-confidence gap.

This check has caught a real gap. Custom attestation summaries shipped across three products — a CLI `--summary` flag, a Terraform `summary` attribute, and a Platform release rendering them in the UI. All three changelog entries linked to `/getting_started/attestations` to explain the feature. That page contained no occurrence of the word "summary".

Also flag:

- A feature named in the changelog with **no** docs page mentioning it anywhere.
- A feature shipped across two or more products with docs for only one of them. Multi-product features are the ones that fall between owners.
- A **breaking change** with no corresponding guidance for readers who need to migrate.

Skip bug fixes, internal changes, and performance work unless they change something a reader was told to do.

Weight recent entries more heavily, and treat an entry that is several months old with still no coverage as evidence of a real gap rather than a lag.

## Step 5 — Deduplicate

For each candidate finding, search the open issues from step 1 for the same subject. Match on subject, not on wording — "document summary definitions on custom attestation types" and "attestations page missing --summary" are the same issue.

If an open issue covers the finding:
- Skip it silently when the issue is adequate.
- Add a comment only when this run found something genuinely new about it — another product shipping the same feature, or a second page with the same gap.

Prefer commenting on an existing issue over opening a near-duplicate. When unsure whether two findings are the same, they are.

## Step 6 — File issues

Cap each run at **8 issues**. If more findings survive, file the 8 highest-impact ones and list the rest in the run summary. A backlog nobody can work through is the same as no backlog.

Follow the repo's conventions:

- **Title** — `type: imperative description`, matching recent issues (`docs: document summary definitions on custom attestation types`, `automation: add kosli-dev/mcp-server to the update-changelog workflow`).
- **Labels** — `content` on nearly everything. Add `documentation` for a missing or incomplete page, `enhancement` for a structural change, `automation` for a generator or workflow fix. Add `priority: high` only for something actively misleading readers. Confirm against `gh label list` rather than assuming.
- **Body** — state the finding, the evidence that proves it (file paths, line numbers, the grep that found it, the changelog entries involved), and what a fix would look like. Someone should be able to act on the issue without re-running the audit.

Do not assign, milestone, or set priority beyond the labels above.

## Step 7 — Summarize

Report: issues filed with numbers and titles, findings skipped as duplicates and which existing issue covers each, findings that cleared the bar but exceeded the cap, and one line on whether site structure improved or degraded since the last run.
