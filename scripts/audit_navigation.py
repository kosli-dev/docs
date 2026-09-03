#!/usr/bin/env python3
"""Audit config/navigation.json against the page files on disk.

Two kinds of finding, deliberately separated:

**Integrity** — objectively broken, and the only thing `--check` fails on:

| Finding  | Meaning                                                        |
|----------|----------------------------------------------------------------|
| orphan   | A page file exists but no navigation entry points at it, so it |
|          | is live on the site and unreachable from the sidebar. This is  |
|          | CLAUDE.md rule 2 ("never create a page file without also       |
|          | adding it to navigation").                                     |
| dangling | A navigation entry names a page with no file behind it.        |

**Shape** — information-architecture signals. Heuristics, reported but never
fatal: single-child groups, over-deep nesting, Title Case labels (CLAUDE.md
mandates sentence case), inconsistent icons among sibling groups, and
oversized groups.

Usage:
    python scripts/audit_navigation.py           # human-readable report
    python scripts/audit_navigation.py --check    # exit 1 on integrity findings only
    python scripts/audit_navigation.py --json     # machine-readable, for the doc-structure skill
"""
import argparse
import json
import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent

# Pages live at the repo root in topic directories. Everything here is either
# not a site page or not routed through navigation.
_EXCLUDED_DIRS = {".github", ".mintlify", ".claude", "node_modules", "snippets", "styles", "tests"}
_EXCLUDED_NAMES = {"CLAUDE.md", "README.md"}

# The site landing page is configured outside `navigation`, so it is never an orphan.
_NOT_ROUTED = {"index"}

# Keys whose values hold nested navigation structure.
_CONTAINER_KEYS = ("tabs", "groups", "menu", "pages")

# Words allowed to be capitalised mid-label: proper nouns, acronyms, and
# command names. Extend this rather than loosening the sentence-case check.
_PROPER_NOUNS = {
    "API", "APIs", "AWS", "Azure", "Bitbucket", "CLI", "CTRF", "Docker", "ECS",
    "FAQ", "GitHub", "GitLab", "Helm", "Jira", "JSON", "JUnit", "K8S", "Karpenter",
    "Kosli", "Kubernetes", "Lambda", "LaunchDarkly", "MCP", "OPA", "Rego", "S3",
    "SAML", "SCIM", "SSO", "Slack", "Snyk", "Sonar", "TLS", "Terraform",
}

# Multi-word product names, where a word that would otherwise look like Title
# Case is part of the name. Matched and removed before the word check, so
# "Actions" is allowed in "GitHub Actions" but still flagged on its own.
_PROPER_PHRASES = (
    "GitHub Actions",
    "GitHub Action",
    "Cloud Run",
    "Evidence Vault",
    "Audit Log",
)

_MAX_NESTING_DEFAULT = 2
_MAX_GROUP_CHILDREN_DEFAULT = 12

# Navigation subtrees written by a generator. Their shape mirrors an upstream
# structure (the CLI's own command tree), so a single-child `kosli allow` group
# is correct rather than a defect, and reshaping it here would be reverted on
# the next release. Integrity still applies - a dangling generated entry is a
# real bug. Keyed by the label that roots the subtree.
_GENERATED_SUBTREES = {
    "CLI Reference": "scripts/update-cli-nav.py",
}


def load_nav(nav_file):
    """Return the parsed navigation config."""
    return json.loads(Path(nav_file).read_text(encoding="utf-8"))


def nav_pages(nav):
    """Return the set of page paths referenced anywhere in nav."""
    found = set()

    def walk(node):
        if isinstance(node, str):
            found.add(node)
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            for key, value in node.items():
                if key in _CONTAINER_KEYS:
                    walk(value)

    walk(nav)
    return found


def page_files(root):
    """Return the set of extensionless page paths on disk, relative to root."""
    root = Path(root)
    found = set()
    for path in root.rglob("*"):
        if path.suffix not in (".md", ".mdx") or not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts[0] in _EXCLUDED_DIRS or rel.name in _EXCLUDED_NAMES:
            continue
        found.add(rel.with_suffix("").as_posix())
    return found


def integrity_findings(nav, root):
    """Return (orphans, dangling) as sorted lists."""
    on_disk = page_files(root)
    in_nav = nav_pages(nav)
    orphans = sorted(on_disk - in_nav - _NOT_ROUTED)
    dangling = sorted(in_nav - on_disk)
    return orphans, dangling


def _label(node):
    """Return a node's display label, or None if it is not a labelled container."""
    for key in ("tab", "item", "group"):
        if key in node:
            return node[key]
    return None


def _children(node):
    for key in ("groups", "menu", "pages"):
        if key in node:
            return node[key]
    return []


def is_title_case(label):
    """True if a word after the first is capitalised without being a known proper noun."""
    # Drop known multi-word product names so their internal capitals don't count,
    # keeping a placeholder so the remaining words keep their position.
    stripped = label
    for phrase in _PROPER_PHRASES:
        stripped = stripped.replace(phrase, "x" if stripped.startswith(phrase) else "x x")

    words = re.findall(r"[\w'&/-]+", stripped)
    for word in words[1:]:
        bare = word.strip("&/-")
        if not bare or not bare[0].isupper():
            continue
        if bare in _PROPER_NOUNS or bare.rstrip("s") in _PROPER_NOUNS:
            continue
        if bare.isupper() and len(bare) <= 4:  # unlisted short acronym
            continue
        return True
    return False


def walk_containers(nav):
    """Yield one record per labelled container: label, path, depth, and child counts.

    `depth` counts labelled containers between the tab and this one, so a group
    sitting directly under a tab has depth 1.
    """
    records = []

    def walk(node, trail):
        if isinstance(node, list):
            for item in node:
                walk(item, trail)
            return
        if not isinstance(node, dict):
            return
        label = _label(node)
        if label is None:
            return
        children = _children(node)
        path = trail + [label]
        records.append(
            {
                "label": label,
                "path": path,
                "depth": len(trail),
                "children": len(children),
                "pages": sum(1 for c in children if isinstance(c, str)),
                "icon": bool(node.get("icon")),
                # Tabs and menu items are top-level section names, not headings,
                # so the sentence-case rule does not apply to them.
                "is_section": "tab" in node or "item" in node,
                "generated_by": next(
                    (_GENERATED_SUBTREES[p] for p in path if p in _GENERATED_SUBTREES), None
                ),
            }
        )
        walk(children, path)

    walk(nav.get("tabs", []), [])
    return records


def shape_findings(nav, max_nesting=_MAX_NESTING_DEFAULT,
                   max_children=_MAX_GROUP_CHILDREN_DEFAULT):
    """Return a list of information-architecture findings. Never fatal."""
    records = walk_containers(nav)
    findings = []

    for record in records:
        where = " > ".join(record["path"])

        # A generated subtree mirrors an upstream structure. Reshaping it here
        # would be reverted, so its shape is not this audit's business.
        if record["generated_by"]:
            continue

        if not record["is_section"] and record["children"] == 1:
            findings.append({
                "kind": "single-child group",
                "where": where,
                "detail": "a group wrapping one entry costs a click and returns nothing",
            })

        if record["depth"] > max_nesting:
            findings.append({
                "kind": "deep nesting",
                "where": where,
                "detail": f"{record['depth']} containers below its tab (limit {max_nesting})",
            })

        if not record["is_section"] and is_title_case(record["label"]):
            findings.append({
                "kind": "Title Case label",
                "where": where,
                "detail": "CLAUDE.md mandates sentence case; nav labels are the most-read headings",
            })

        if record["children"] > max_children:
            findings.append({
                "kind": "oversized group",
                "where": where,
                "detail": f"{record['children']} children with no internal grouping",
            })

    # Icon consistency is a property of a sibling set, not of one container.
    by_parent = {}
    for record in records:
        if record["generated_by"]:
            continue
        by_parent.setdefault(" > ".join(record["path"][:-1]), []).append(record)
    for parent, siblings in by_parent.items():
        if len(siblings) < 2:
            continue
        with_icon = [s["label"] for s in siblings if s["icon"]]
        without = [s["label"] for s in siblings if not s["icon"]]
        if with_icon and without:
            findings.append({
                "kind": "inconsistent icons",
                "where": parent or "(top level)",
                "detail": f"has icons: {', '.join(with_icon)}; missing: {', '.join(without)}",
            })

    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--nav-file", default=str(_REPO_ROOT / "config" / "navigation.json"),
                        help="Path to navigation.json.")
    parser.add_argument("--root", default=str(_REPO_ROOT),
                        help="Repo root to scan for page files.")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if there are integrity findings. Shape findings never fail.")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="Emit findings as JSON.")
    parser.add_argument("--max-nesting", type=int, default=_MAX_NESTING_DEFAULT,
                        help=f"Containers allowed below a tab (default {_MAX_NESTING_DEFAULT}).")
    parser.add_argument("--max-group-children", type=int, default=_MAX_GROUP_CHILDREN_DEFAULT,
                        help=f"Children before a group is oversized (default {_MAX_GROUP_CHILDREN_DEFAULT}).")
    args = parser.parse_args()

    nav = load_nav(args.nav_file)
    orphans, dangling = integrity_findings(nav, args.root)
    shape = shape_findings(nav, args.max_nesting, args.max_group_children)

    if args.as_json:
        json.dump({"orphans": orphans, "dangling": dangling, "shape": shape},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"{len(nav_pages(nav))} pages in navigation, "
              f"{len(page_files(args.root))} page files on disk\n")

        if orphans:
            print(f"ORPHANS ({len(orphans)}) - live but unreachable from the sidebar:")
            for page in orphans:
                print(f"  {page}")
        if dangling:
            print(f"\nDANGLING ({len(dangling)}) - navigation entry with no file:")
            for page in dangling:
                print(f"  {page}")
        if not orphans and not dangling:
            print("integrity: ok")

        if shape:
            print(f"\nSHAPE ({len(shape)}) - advisory, never fails the build:")
            for finding in shape:
                print(f"  [{finding['kind']}] {finding['where']}")
                print(f"      {finding['detail']}")

    if args.check and (orphans or dangling):
        print(
            f"\n{len(orphans)} orphaned page(s) and {len(dangling)} dangling entry(s). "
            "Every page file must be listed in navigation (CLAUDE.md rule 2).",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
