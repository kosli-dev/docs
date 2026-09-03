import json
import subprocess
import sys
from pathlib import Path

import audit_navigation as nav_audit

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "audit_navigation.py"


def _write_site(tmp_path, nav, pages):
    """Build a throwaway docs tree: nav config plus page files."""
    nav_file = tmp_path / "config" / "navigation.json"
    nav_file.parent.mkdir(parents=True)
    nav_file.write_text(json.dumps(nav), encoding="utf-8")
    for page in pages:
        target = tmp_path / page
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("---\ntitle: x\n---\n", encoding="utf-8")
    return nav_file


# --- page discovery ---------------------------------------------------------

def test_page_files_strips_both_extensions(tmp_path):
    """Regression: a broken extension strip made every page look orphaned."""
    _write_site(tmp_path, {"tabs": []}, ["a/one.md", "a/two.mdx"])
    assert nav_audit.page_files(tmp_path) == {"a/one", "a/two"}


def test_page_files_skips_excluded_dirs_and_names(tmp_path):
    _write_site(tmp_path, {"tabs": []}, [
        "real/page.md",
        "snippets/frag.mdx",
        ".claude/skills/doc-write/SKILL.md",
        ".github/notes.md",
        "CLAUDE.md",
        "README.md",
    ])
    assert nav_audit.page_files(tmp_path) == {"real/page"}


# --- navigation traversal ---------------------------------------------------

def test_nav_pages_walks_tabs_groups_menu_and_nested_pages():
    nav = {
        "tabs": [
            {"tab": "Docs", "groups": [
                {"group": "A", "pages": [
                    "a/one",
                    {"group": "B", "pages": ["a/b/two"]},
                ]},
            ]},
            {"tab": "Ref", "menu": [
                {"item": "CLI", "groups": [{"group": "C", "pages": ["ref/three"]}]},
                {"item": "API", "openapi": "https://example.test/openapi.json"},
            ]},
        ]
    }
    assert nav_audit.nav_pages(nav) == {"a/one", "a/b/two", "ref/three"}


# --- integrity --------------------------------------------------------------

def test_orphan_is_reported(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "A", "pages": ["a/one"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md", "a/lonely.md"])
    orphans, dangling = nav_audit.integrity_findings(nav_audit.load_nav(nav_file), tmp_path)
    assert orphans == ["a/lonely"]
    assert dangling == []


def test_dangling_entry_is_reported(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [
        {"group": "A", "pages": ["a/one", "a/ghost"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md"])
    orphans, dangling = nav_audit.integrity_findings(nav_audit.load_nav(nav_file), tmp_path)
    assert orphans == []
    assert dangling == ["a/ghost"]


def test_index_is_never_an_orphan(tmp_path):
    """The landing page is configured outside `navigation`."""
    nav_file = _write_site(tmp_path, {"tabs": []}, ["index.mdx"])
    orphans, _ = nav_audit.integrity_findings(nav_audit.load_nav(nav_file), tmp_path)
    assert orphans == []


def test_clean_site_has_no_integrity_findings(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "A", "pages": ["a/one"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md", "index.mdx"])
    assert nav_audit.integrity_findings(nav_audit.load_nav(nav_file), tmp_path) == ([], [])


# --- sentence case ----------------------------------------------------------

def test_sentence_case_labels_pass():
    for label in ["Getting started", "Naming conventions", "Users & roles",
                  "Multi-flow workflows", "Understand Kosli", "kosli attest"]:
        assert not nav_audit.is_title_case(label), label


def test_title_case_labels_are_flagged():
    for label in ["Naming Conventions", "Data Sources", "Helm Charts",
                  "Managing Environments", "Roles & Responsibilities"]:
        assert nav_audit.is_title_case(label), label


def test_proper_nouns_and_acronyms_are_allowed_mid_label():
    for label in ["Report AWS environments", "The Kosli CLI", "Using GitHub Actions",
                  "Attest with Snyk", "Kubernetes and Terraform"]:
        assert not nav_audit.is_title_case(label), label


# --- shape ------------------------------------------------------------------

def test_single_child_group_is_flagged():
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "Lonely", "pages": ["a/one"]}]}]}
    kinds = {f["kind"] for f in nav_audit.shape_findings(nav)}
    assert "single-child group" in kinds


def test_deep_nesting_is_flagged_against_the_limit():
    nav = {"tabs": [{"tab": "Docs", "groups": [
        {"group": "One", "pages": [
            {"group": "Two", "pages": [
                {"group": "Three", "pages": ["a/deep"]}]}]}]}]}
    deep = [f for f in nav_audit.shape_findings(nav, max_nesting=2)
            if f["kind"] == "deep nesting"]
    assert [f["where"] for f in deep] == ["Docs > One > Two > Three"]
    assert not [f for f in nav_audit.shape_findings(nav, max_nesting=5)
                if f["kind"] == "deep nesting"]


def test_tabs_and_menu_items_are_exempt_from_sentence_case():
    """Tabs and menu items are section names, not headings."""
    nav = {"tabs": [{"tab": "Implementation Guide", "menu": [
        {"item": "CLI Reference", "groups": [{"group": "General", "pages": ["a/one", "a/two"]}]}]}]}
    assert not [f for f in nav_audit.shape_findings(nav) if f["kind"] == "Title Case label"]


def test_generated_subtree_is_exempt_from_shape_checks():
    """`kosli allow` having one subcommand is upstream truth, not a defect."""
    nav = {"tabs": [{"tab": "Reference", "menu": [
        {"item": "CLI Reference", "groups": [
            {"group": "kosli allow", "pages": ["client_reference/kosli_allow_artifact"]}]}]}]}
    assert nav_audit.shape_findings(nav) == []


def test_non_generated_subtree_is_still_checked():
    nav = {"tabs": [{"tab": "Reference", "menu": [
        {"item": "Template Reference", "groups": [
            {"group": "Templates", "pages": ["template-reference/flow_template"]}]}]}]}
    kinds = {f["kind"] for f in nav_audit.shape_findings(nav)}
    assert "single-child group" in kinds


def test_oversized_group_is_flagged():
    nav = {"tabs": [{"tab": "Docs", "groups": [
        {"group": "Big", "pages": [f"a/p{n}" for n in range(20)]}]}]}
    kinds = {f["kind"] for f in nav_audit.shape_findings(nav, max_children=12)}
    assert "oversized group" in kinds


def test_inconsistent_icons_reported_once_per_sibling_set():
    nav = {"tabs": [{"tab": "Docs", "groups": [
        {"group": "A", "icon": "book", "pages": ["a/one", "a/two"]},
        {"group": "B", "pages": ["b/one", "b/two"]},
    ]}]}
    icons = [f for f in nav_audit.shape_findings(nav) if f["kind"] == "inconsistent icons"]
    assert len(icons) == 1
    assert "A" in icons[0]["detail"] and "B" in icons[0]["detail"]


# --- CLI contract -----------------------------------------------------------

def _run(nav_file, root, *args):
    return subprocess.run(
        [sys.executable, str(_SCRIPT), "--nav-file", str(nav_file), "--root", str(root), *args],
        capture_output=True, text=True,
    )


def test_check_exits_nonzero_on_orphan(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "A", "pages": ["a/one"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md", "a/lonely.md"])
    result = _run(nav_file, tmp_path, "--check")
    assert result.returncode == 1
    assert "a/lonely" in result.stdout


def test_check_passes_on_clean_site(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "A", "pages": ["a/one", "a/two"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md", "a/two.md"])
    result = _run(nav_file, tmp_path, "--check")
    assert result.returncode == 0, result.stderr


def test_check_does_not_fail_on_shape_findings_alone(tmp_path):
    """Shape is advisory. A single-child group must never block a PR."""
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "Lonely", "pages": ["a/one"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md"])
    result = _run(nav_file, tmp_path, "--check")
    assert result.returncode == 0, result.stderr
    assert "single-child group" in result.stdout


def test_json_output_is_machine_readable(tmp_path):
    nav = {"tabs": [{"tab": "Docs", "groups": [{"group": "Lonely", "pages": ["a/one"]}]}]}
    nav_file = _write_site(tmp_path, nav, ["a/one.md", "a/lonely.md"])
    payload = json.loads(_run(nav_file, tmp_path, "--json").stdout)
    assert payload["orphans"] == ["a/lonely"]
    assert payload["dangling"] == []
    assert any(f["kind"] == "single-child group" for f in payload["shape"])


def test_real_repo_navigation_has_integrity(tmp_path):
    """The committed navigation must route every page. CLAUDE.md rule 2."""
    repo = Path(__file__).resolve().parent.parent
    orphans, dangling = nav_audit.integrity_findings(
        nav_audit.load_nav(repo / "config" / "navigation.json"), repo
    )
    assert orphans == [], f"orphaned pages: {orphans}"
    assert dangling == [], f"dangling nav entries: {dangling}"
