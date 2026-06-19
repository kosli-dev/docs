import json
import os
import subprocess
import tempfile


def _write(path, frontmatter):
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + frontmatter + "\n---\n\nbody\n")


def test_nav_skips_hidden_and_has_no_deprecated_group():
    with tempfile.TemporaryDirectory() as d:
        docs_dir = os.path.join(d, "client_reference")
        os.makedirs(docs_dir)
        _write(os.path.join(docs_dir, "overview.md"), 'title: "Overview"')
        _write(os.path.join(docs_dir, "output_and_verbosity.md"), 'title: "Output"')
        _write(os.path.join(docs_dir, "kosli_attest_generic.md"), 'title: "kosli attest generic"')
        _write(os.path.join(docs_dir, "kosli_report_approval.md"),
               'title: "kosli report approval"\ntag: "DEPRECATED"')
        _write(os.path.join(docs_dir, "kosli_attest_decision.md"),
               'title: "kosli attest decision"\ntag: "BETA"\nhidden: true')

        nav_path = os.path.join(d, "navigation.json")
        with open(nav_path, "w", encoding="utf-8") as f:
            json.dump({"tabs": [{"tab": "Reference", "menu": [
                {"item": "CLI Reference", "icon": "terminal", "groups": []}]}]}, f)

        subprocess.run(
            ["python", os.path.join(os.path.dirname(__file__), "update-cli-nav.py"),
             "--docs-dir", docs_dir, "--nav-file", nav_path],
            check=True,
        )

        with open(nav_path, encoding="utf-8") as f:
            nav = json.load(f)
        groups = nav["tabs"][0]["menu"][0]["groups"]
        all_pages = [p for g in groups for p in g["pages"]]
        group_names = [g["group"] for g in groups]

        assert "client_reference/kosli_attest_decision" not in all_pages, "hidden page must be skipped"
        assert "client_reference/kosli_attest_generic" in all_pages
        assert "client_reference/kosli_report_approval" in all_pages, "deprecated page stays in its family group"
        assert "Deprecated" not in group_names, "separate Deprecated group must be removed"


if __name__ == "__main__":
    test_nav_skips_hidden_and_has_no_deprecated_group()
    print("PASS")
