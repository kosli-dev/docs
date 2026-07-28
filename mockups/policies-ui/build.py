#!/usr/bin/env python3
"""Assemble the proposed-Policies-UI wireframe mockups from shared partials."""
import pathlib, re

HERE = pathlib.Path(__file__).parent
chrome = (HERE / "_chrome.html").read_text()
topbar = (HERE / "_topbar.html").read_text()
footer = (HERE / "_footer.html").read_text()

ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="#4b5563" stroke-width="1.8" '
        'width="17" height="17"><rect x="4" y="3" width="16" height="18" rx="2"/>'
        '<path d="M8 8h8M8 12h8M8 16h5"/></svg>')
CHEV = ' ▾'
TICK = '<span class="dot">✓</span>'
CROSS = '<span class="dot">✕</span>'


def shell(crumb, body, title):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="kosli-mock.css"></head><body>
{chrome}
<div class="main">
{topbar.replace('CRUMB', crumb)}
{body}
{footer}
</div></body></html>"""


POLICIES = [
    ("pr-approved", "V1", "Pull request approved",
     "Every pull request on the trail has at least one approver.",
     ["team=platform", "framework=soc2"]),
    ("no-hardcoded-secrets", "V3", "No hard-coded credentials",
     "No attested source file matches a known credential pattern.",
     ["team=platform", "framework=soc2"]),
    ("vuln-scan-clean", "V2", "Vulnerability scan clean",
     "The Snyk attestation reports no critical or high findings.",
     ["team=security"]),
    ("test-evidence-present", "V1", "Test evidence present",
     "A JUnit attestation exists on the trail and reports zero failures.",
     ["team=quality"]),
]

DECISIONS = [
    ("14:02:11", "14:02:19", "release-99", "nginx:665d6dd", True),
    ("14:00:03", "14:00:11", "release-98", "nginx:665d6dd", True),
    ("13:41:55", "13:42:02", "release-97", "nginx:a6e433a", False),
    ("13:20:47", "13:20:55", "release-96", "nginx:a6e433a", True),
    ("12:58:12", "12:58:19", "release-95", "dashboard:26c6997", True),
    ("12:31:09", "12:31:16", "release-94", "dashboard:26c6997", True),
    ("11:57:44", "11:57:51", "release-93", "languages-start-points:ca386e0", False),
    ("11:12:38", "11:12:46", "release-92", "languages-start-points:ca386e0", True),
]
ECR = "244531986313.dkr.ecr.eu-central-1.amazonaws.com"


def policy_rows():
    out = []
    for ident, ver, name, desc, tags in POLICIES:
        pills = "".join(f'<span class="tag">{t}</span>' for t in tags)
        out.append(f"""    <div class="row">
      <div class="grow">
        <span class="id">{ident}</span> <span class="badge">{ver}</span>
        <span class="name">&nbsp;{name}</span>
        <div class="line2">{desc}</div>
        <div class="tags">{pills}</div>
      </div>
      <span class="kebab">&#8942;</span>
    </div>""")
    return "\n".join(out)


def decision_rows():
    out = []
    for req, rec, trail, art, ok in DECISIONS:
        pill = (f'<span class="pill ok">{TICK}Compliant</span>' if ok
                else f'<span class="pill no">{CROSS}Non-compliant</span>')
        out.append(f"""    <div class="row">
      <div class="grow">
        <b>2026-07-27 &bull; {req}</b>
        <span style="color:#6b7280;font-size:13px">&nbsp;requested &middot; recorded {rec}</span>
        <span style="color:#14263a">&nbsp;&nbsp;my-release-flow / {trail}</span>
        <div class="line2 mono">{ECR}/{art}</div>
      </div>
      <span class="badge">V1</span>
      {pill}
    </div>""")
    return "\n".join(out)


# ---------------------------------------------------------------- page 1: list
list_body = f"""  <div class="page">
    <div class="h1row"><h1>Policies</h1>
      <span class="mock">Mockup &bull; proposed design</span></div>
    <div class="toolrow">
      <div class="field"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="2" width="13" height="13"><circle cx="11" cy="11" r="7"/>
        <path d="m16.5 16.5 4 4"/></svg>Search by name or identifier</div>
    </div>
    <div class="tabs">
      <div class="tab on">{ICON}Evaluation</div>
      <div class="tab">Environment</div>
    </div>
    <div class="card" style="border-radius:0 10px 10px 10px">
      <div class="chead">{ICON}Policies <span class="count">4</span>
        <span class="ctab">Archived</span>
        <span class="filters"><span>Tags{CHEV}</span><span>Sort{CHEV}</span></span>
      </div>
{policy_rows()}
    </div>
    <div class="hint">Policies are created and updated with the CLI or API
      (<code>kosli create policy --type rego</code>). In the beta the UI is read-only,
      apart from tagging.</div>
  </div>"""

# ----------------------------------------------------------- page 2: decisions
detail_head = f"""    <div class="h1row"><h1>pr-approved</h1><span class="badge"
        style="font-size:13px;padding:3px 8px;vertical-align:12px">V1</span>
      <span class="spacer"></span>
      <button class="btn danger">Archive</button>
      <span class="mock" style="margin-left:12px">Mockup &bull; proposed design</span>
    </div>
    <div class="sub">Pull request approved</div>
    <div class="desc">Every pull request on the trail has at least one approver.</div>
    <div class="toolrow" style="margin:14px 0 0">
      <span class="tag">team=platform</span><span class="tag">framework=soc2</span>
      <button class="btn sm">+ Add tag</button>
    </div>
    <div class="tabs">
      <div class="tab TAB_POLICY">{ICON}Policy</div>
      <div class="tab TAB_DECISIONS">{ICON}Decisions</div>
      <div class="tab">{ICON}Versions</div>
    </div>"""

head_decisions = detail_head.replace("TAB_POLICY", "").replace("TAB_DECISIONS", "on")
head_source = detail_head.replace("TAB_POLICY", "on").replace("TAB_DECISIONS", "")

decisions_card = f"""    <div class="card" style="border-radius:0 10px 10px 10px">
      <div class="chead">{ICON}Decisions <span class="count">128</span>
        <span class="filters"><span>Timestamp{CHEV}</span><span>Compliance{CHEV}</span>
          <span>Version{CHEV}</span><span>Sort{CHEV}</span>
          <button class="btn sm">&darr; Export CSV</button></span>
      </div>
{decision_rows()}
    </div>"""

decisions_body = f'  <div class="page">\n{head_decisions}\n{decisions_card}\n  </div>'

# ------------------------------------------------------ page 3: decision detail
tray = f"""<div class="scrim"></div>
<div class="tray">
  <div class="thead">
    <div class="trow1"><h2>pr-approval-decision</h2>
      <span class="pill no">{CROSS}Non-compliant</span>
      <span class="close">&#10005;</span></div>
    <div class="tmeta"><span class="badge">V1</span>
      <span><b>requested</b> 2026-07-27 &bull; 13:41:55</span>
      <span>&middot;</span><span><b>recorded</b> 13:42:02</span>
      <span class="mock" style="margin-left:auto">Mockup &bull; proposed design</span></div>
  </div>
  <dl class="kv">
    <div><dt>Control</dt><dd>RCTL-043 <span style="font-weight:400;color:#4b5563">
      &mdash; Source code review</span></dd></div>
    <div><dt>Trail</dt><dd>my-release-flow / release-97</dd></div>
    <div><dt>Artifact</dt><dd class="mono">{ECR}/nginx:a6e433a<br>
      <span style="font-weight:400;color:#4b5563">sha256:a6e433a6fd3eb29c499b75310756420864b6c346</span></dd></div>
    <div><dt>Policy</dt><dd>pr-approved <span class="badge">V1</span><br>
      <span class="mono" style="font-weight:400;color:#4b5563">digest
      sha256:9f2c1d84e0b7a35c6f1e8d2b47a90c3518fe64d7</span></dd></div>
    <div><dt>Parameters</dt><dd class="mono plain">{{ "pr_attestation_name": "pull-request" }}</dd></div>
    <div><dt>Evaluation engine</dt><dd class="plain mono">opa 1.18.2</dd></div>
    <div><dt>Violations</dt><dd><ul>
      <li>pull-request https://github.com/cyber-dojo/nginx/pull/42 has no approvers</li>
      <li>pull-request https://github.com/cyber-dojo/nginx/pull/45 has no approvers</li>
    </ul></dd></div>
    <div><dt>Evaluation report</dt><dd><button class="btn sm">&darr; evaluation-report.json</button></dd></div>
  </dl>
</div>"""


# ------------------------------------------------------- page 4: policy source
REGO = """package policy

import rego.v1
import data.lib.approvals

# METADATA
# scope: document
# schemas:
#   - input: schema["trail-v1"]
default allow = false

allow if {
    approvals.all_approved(input.trail, data.params.pr_attestation_name)
}

violations contains msg if {
    some pr in approvals.unapproved(input.trail, data.params.pr_attestation_name)
    msg := sprintf("pull-request %v has no approvers", [pr.url])
}"""

KEYWORDS = ("package", "import", "default", "allow", "violations", "contains",
            "every", "some", "if", "in")


def highlight(src):
    out = []
    for line in src.split("\n"):
        line = (line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
        line = re.sub(r'"([^"]*)"', lambda m: f'<span class="s">"{m.group(1)}"</span>', line)
        line = re.sub(r'\b(' + "|".join(KEYWORDS) + r')\b',
                      lambda m: f'<span class="k">{m.group(1)}</span>', line)
        out.append(line)
    return "\n".join(out)


nlines = len(REGO.split("\n"))
gutter = "<br>".join(str(i) for i in range(1, nlines + 1))

FILES = """      <div class="files">
        <div class="cap">FILES</div>
        <div class="fi sel">policy.rego</div>
        <div class="dir">lib/</div>
        <div class="fi nest">approvals.rego</div>
        <div class="fi nest">severity.rego</div>
        <div class="fi">policy_test.rego<span class="flag">not executed</span></div>
        <div class="tot">4 files &middot; 110 lines</div>
      </div>"""

source_card = f"""    <div class="card" style="border-radius:0 10px 10px 10px">
      <div class="chead">{ICON}Policy bundle
        <span class="vsel">V1 &middot; current{CHEV}</span>
        <span class="filters"><button class="btn sm">Copy</button>
          <button class="btn sm">&darr; bundle</button></span>
      </div>
      <div class="srcmeta">
        <span>Bundle <b>sha256:9f2c1d84&hellip;</b></span>
        <span>roots <b>policy</b></span>
        <span>entrypoint <b>policy.allow</b></span>
        <span>schema <b>trail</b></span>
        <span>params read <b>pr_attestation_name</b></span>
        <span>published <b>2026-07-20 by alex@kosli.com</b></span>
      </div>
      <div class="bundle">
{FILES}
        <div class="viewer">
          <div class="vhead"><span class="fn">policy.rego</span>
            <span class="ep">entrypoint</span>
            <span class="meta mono">sha256:9f2c1d84&hellip; &middot; {nlines} lines</span></div>
          <div class="src"><div class="gutter">{gutter}</div><div class="code">{highlight(REGO)}</div></div>
        </div>
      </div>
    </div>
    <div class="hint">The bundle is read-only here. Edit it in your repository and publish a new
      version with <code>kosli create policy</code> &mdash; the version shown is the one that runs
      when an evaluation names this policy. Tests are stored with the bundle for audit but are not
      executed server-side.</div>"""

source_body = f'  <div class="page">\n{head_source}\n{source_card}\n  </div>'

PAGES = {
    "policy-list.html": ("cyber-dojo / <b>policies</b>", list_body, "Policies", ""),
    "policy-decisions.html": ("cyber-dojo / policies / <b>pr-approved</b>",
                              decisions_body, "pr-approved", ""),
    "policy-decision-detail.html": ("cyber-dojo / policies / <b>pr-approved</b>",
                                    decisions_body, "pr-approved decision", tray),
    "policy-source.html": ("cyber-dojo / policies / <b>pr-approved</b>",
                           source_body, "pr-approved policy", ""),
}

for fn, (crumb, body, title, extra) in PAGES.items():
    html = shell(crumb, body, title)
    if extra:
        html = html.replace("</body>", extra + "\n</body>")
    (HERE / fn).write_text(html)
    print("wrote", fn)
