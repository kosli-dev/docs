"""Every Rego policy shown in the docs must compile and follow Kosli's contract.

A reader copies these. A block that does not compile wastes their time; one that
compiles but never defines `allow` denies everything, which is worse because it
looks like it worked.
"""

import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

DOCS_ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"^[ \t]*```([a-zA-Z0-9_+-]*)([^\n]*)\n(.*?)^[ \t]*```", re.S | re.M)
PACKAGE = re.compile(r"^\s*package\s+([A-Za-z_][\w.]*)", re.M)
# A rule that can become true, so `default allow := false` on its own does not count.
ALLOW_RULE = re.compile(r"^\s*allow\b(?!\s*:?=\s*false)", re.M)


def _dedent(body):
    indent = min(
        (len(l) - len(l.lstrip()) for l in body.splitlines() if l.strip()), default=0
    )
    return "\n".join(l[indent:] if len(l) >= indent else l for l in body.splitlines())


def rego_policies():
    """Rego blocks a reader is meant to copy whole.

    Two ways a block says that: it declares its own package, or its fence carries a
    filename, as in ```rego pr-compliant.rego. Give a block a filename whenever the
    page tells someone to create the file, and this will hold it to compiling.

    Anything else is a fragment illustrating one rule. It cannot compile alone
    because its inputs are unbound, so there is nothing here to check.
    """
    for path in sorted(DOCS_ROOT.rglob("*")):
        if path.suffix not in (".md", ".mdx"):
            continue
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in FENCE.finditer(text):
            if match.group(1).lower() != "rego":
                continue
            filename = match.group(2).strip()
            if filename and not filename.endswith(".rego"):
                filename = ""  # a fence attribute, not a file the reader creates
            body = _dedent(match.group(3))
            package = PACKAGE.search(body)
            if not package and not filename:
                continue
            line = text[: match.start()].count("\n") + 1
            yield pytest.param(
                body,
                package.group(1) if package else None,
                id=f"{path.relative_to(DOCS_ROOT)}:{line}",
            )


POLICIES = list(rego_policies())


def test_the_docs_still_contain_rego_policies():
    assert POLICIES, (
        "no Rego policies found, so the checks below all pass without checking "
        "anything; the fence pattern has stopped matching the docs"
    )


def _opa():
    opa = shutil.which("opa")
    if opa:
        return opa
    if os.environ.get("CI"):
        pytest.fail("opa is not installed, so the Rego examples went unchecked")
    pytest.skip("opa is not installed; install it to check the Rego examples")


@pytest.mark.parametrize("body,package", POLICIES)
def test_rego_policy_compiles(body, package):
    opa = _opa()
    with tempfile.TemporaryDirectory() as tmp:
        policy = Path(tmp) / "policy.rego"
        policy.write_text(body, encoding="utf-8")
        result = subprocess.run(
            [opa, "check", str(policy)], capture_output=True, text=True
        )
    assert result.returncode == 0, (result.stdout + result.stderr).strip()


@pytest.mark.parametrize("body,package", POLICIES)
def test_rego_policy_follows_the_kosli_contract(body, package):
    # policy-reference/rego_policy.mdx: Kosli reads data.policy.allow, and exits 0
    # when it is true and 1 when it is false.
    assert package is not None, "is shown as a file to create but declares no package"
    assert package == "policy", f"declares package {package}, so Kosli never reads it"
    assert ALLOW_RULE.search(body), (
        "defines no allow rule that can be true, so it denies everything"
    )
