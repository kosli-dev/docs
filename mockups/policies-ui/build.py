#!/usr/bin/env python3
"""Assemble the proposed-Policies-UI wireframe mockups from shared partials."""
import pathlib, re

HERE = pathlib.Path(__file__).parent

CSS = r"""/* Wireframe mockup chrome for proposed Kosli Policies UI.
   Palette sampled from real screenshots in images/tutorials/controls-*.png */
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --navy: #101c2b;
  --ink: #14263a;
  --grey: #6b7280;
  --line: #e6e7e9;
  --line-soft: #eef0f2;
  --band: #f7f9fc;
  --topbar: #f2f2f6;
  --blue: #1e55cd;
  --green: #3ca36f;
  --red: #ce4a3e;
  --chip: #eceef2;
}
body {
  width: 1535px; min-height: 1011px; display: flex;
  font: 400 15px/1.45 -apple-system, "Segoe UI", Inter, Helvetica, Arial, sans-serif;
  color: var(--ink); background: #fcfcff; -webkit-font-smoothing: antialiased;
}

/* ---------- sidebar ---------- */
.sidebar { width: 250px; flex: 0 0 250px; background: var(--navy); padding: 16px 0 0; }
.logo { display: block; width: 130px; height: 48px; margin: 0 0 18px 10px; }
.org { display: flex; align-items: center; gap: 10px; color: #fff; font-weight: 600;
       padding: 0 24px 0 20px; height: 34px; }
.org .home { opacity: .85; }
.org .name { flex: 1; }
.org .chev { opacity: .7; }
hr.sep { border: 0; border-top: 1px solid rgba(255,255,255,.16); margin: 14px 24px 12px; }
nav a { display: flex; align-items: center; gap: 14px; padding: 9px 20px;
        color: #b9c2cd; text-decoration: none; font-size: 15px; }
nav a.on { color: #fff; font-weight: 600; }
nav svg { width: 19px; height: 19px; flex: 0 0 19px; }

/* ---------- top bar ---------- */
.main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.topbar { height: 51px; background: var(--topbar); display: flex; align-items: center;
          padding: 0 22px 0 36px; gap: 14px; }
.crumb { font-size: 13.5px; color: var(--grey); flex: 1; }
.crumb b { color: var(--ink); }
.search { width: 278px; height: 32px; border: 1px solid #d8dbe0; border-radius: 999px;
          background: #fff; display: flex; align-items: center; gap: 8px; padding: 0 14px;
          font-size: 13px; color: #9aa1ab; }
.avatar { display: flex; align-items: center; gap: 5px; color: #5b6472; }
.avatar .ring { width: 26px; height: 26px; border-radius: 50%; background: #dfe3e9;
                display: grid; place-items: center; }

/* ---------- page ---------- */
.page { flex: 1; padding: 26px 36px 0; }
h1 { font-size: 34px; font-weight: 700; letter-spacing: -.4px; line-height: 1.1; }
.h1row { display: flex; align-items: flex-start; gap: 12px; }
.sub { font-size: 16px; font-weight: 600; margin-top: 9px; }
.desc { font-size: 13.5px; color: var(--grey); margin-top: 6px; max-width: 1030px; }
.spacer { flex: 1; }
.toolrow { display: flex; align-items: center; gap: 10px; margin: 18px 0 22px; }

/* ---------- controls ---------- */
.field { width: 240px; height: 34px; border: 1px solid #d8dbe0; border-radius: 7px;
         background: #fff; display: flex; align-items: center; gap: 8px; padding: 0 11px;
         font-size: 13px; color: #9aa1ab; }
.btn { height: 34px; padding: 0 15px; border-radius: 7px; border: 1px solid #d8dbe0;
       background: #fff; color: #374151; font-size: 13.5px; font-weight: 500;
       display: inline-flex; align-items: center; gap: 7px; }
.btn.pri { background: var(--blue); border-color: var(--blue); color: #fff; font-weight: 600; }
.btn.danger { border-color: #ffdad5; color: #b4433a; }
.btn.sm { height: 27px; padding: 0 10px; font-size: 12.5px; border-radius: 6px; }

.mock { margin-left: auto; align-self: flex-start; background: #fff7e6; border: 1px solid #f0d18a;
        color: #8a6212; border-radius: 6px; font-size: 11.5px; font-weight: 600;
        padding: 5px 10px; letter-spacing: .2px; white-space: nowrap; }

/* ---------- tabs ---------- */
.tabs { display: flex; gap: 4px; margin-top: 20px; }
.tab { display: flex; align-items: center; gap: 8px; padding: 9px 16px; font-size: 14px;
       color: var(--grey); border: 1px solid transparent; border-radius: 8px 8px 0 0; }
.tab.on { background: #fff; border-color: var(--line); border-bottom-color: #fff;
          color: var(--ink); font-weight: 600; }

/* ---------- card ---------- */
.card { border: 1px solid var(--line); border-radius: 10px; background: #fff; overflow: hidden; }
.card + .card { margin-top: 18px; }
.chead { background: var(--band); border-bottom: 1px solid var(--line);
         display: flex; align-items: center; gap: 11px; padding: 13px 18px; font-size: 14.5px;
         font-weight: 600; }
.count { background: var(--chip); color: #4b5563; border-radius: 6px; font-size: 12px;
         font-weight: 600; padding: 2px 9px; }
.ctab { font-weight: 400; color: var(--grey); font-size: 14px; margin-left: 14px; }
.filters { margin-left: auto; display: flex; gap: 18px; font-size: 13px; color: #4b5563;
           font-weight: 400; }
.row { display: flex; align-items: center; gap: 14px; padding: 14px 18px;
       border-bottom: 1px solid var(--line-soft); }
.row:last-child { border-bottom: 0; }
.row .grow { flex: 1; min-width: 0; }
.id { font-size: 15px; font-weight: 700; }
.badge { display: inline-block; border: 1px solid #e2e4e8; background: #f7f8fa; color: #4b5563;
         border-radius: 4px; font-size: 11px; font-weight: 600; padding: 1px 6px;
         vertical-align: 2px; }
.name { font-weight: 400; }
.line2 { font-size: 13px; color: var(--grey); margin-top: 5px; }
.tags { display: flex; gap: 6px; margin-top: 8px; }
.tag { background: #eef2f7; color: #44526a; border-radius: 4px; font-size: 11px;
       padding: 2px 8px; }
.kebab { color: #9aa1ab; font-size: 17px; line-height: 1; }
.pill { border-radius: 999px; color: #fff; font-size: 12.5px; font-weight: 600;
        padding: 6px 15px 6px 11px; display: inline-flex; align-items: center; gap: 7px;
        white-space: nowrap; }
.pill.ok { background: var(--green); }
.pill.no { background: var(--red); }
.pill .dot { width: 15px; height: 15px; border-radius: 50%; background: rgba(255,255,255,.28);
             display: grid; place-items: center; font-size: 10px; }
.mono { font: 12.5px/1.55 ui-monospace, SFMono-Regular, Menlo, monospace; }
.hint { font-size: 13px; color: var(--grey); margin-top: 14px; }
.hint code { font: 12.5px ui-monospace, Menlo, monospace; background: #f3f4f6;
             border-radius: 4px; padding: 1px 5px; }

/* ---------- footer ---------- */
footer { display: flex; align-items: center; gap: 18px; padding: 20px 36px 22px;
         font-size: 12.5px; color: #4b5563; }
footer .gen { background: var(--chip); color: #6b7280; border-radius: 5px; font-size: 11px;
              padding: 3px 9px; }
footer img { width: 82px; height: 34px; }
footer .links { display: flex; gap: 15px; color: var(--blue); }

/* ---------- detail tray ---------- */
.scrim { position: fixed; inset: 0; background: rgba(0,0,0,.5); }
.tray { position: fixed; top: 0; right: 0; bottom: 0; width: 843px; background: #fff;
        display: flex; flex-direction: column; }
.thead { padding: 30px 32px 20px; }
.trow1 { display: flex; align-items: center; gap: 16px; }
.trow1 h2 { font-size: 30px; font-weight: 700; letter-spacing: -.3px; }
.close { margin-left: auto; color: #6b7280; font-size: 22px; line-height: 1; }
.tmeta { display: flex; align-items: center; gap: 12px; margin-top: 13px; font-size: 13.5px;
         color: #4b5563; }
.kv { margin: 0 32px; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
.kv > div { display: flex; border-bottom: 1px solid var(--line); }
.kv > div:last-child { border-bottom: 0; }
.kv dt { flex: 0 0 168px; background: var(--band); border-right: 1px solid var(--line);
         padding: 13px 15px; font-size: 13.5px; color: var(--grey); }
.kv dd { flex: 1; min-width: 0; padding: 13px 15px; font-size: 13.5px; font-weight: 600;
         word-break: break-all; }
.kv dd.plain { font-weight: 400; }
.kv dd ul { margin: 0; padding-left: 18px; font-weight: 400; }
.kv dd li + li { margin-top: 5px; }

/* ---------- source view ---------- */
.srcmeta { display: flex; gap: 26px; padding: 13px 18px; border-bottom: 1px solid var(--line-soft);
           font-size: 13px; color: var(--grey); }
.srcmeta b { color: var(--ink); font-weight: 600; }
.src { display: flex; font: 12.5px/1.75 ui-monospace, SFMono-Regular, Menlo, monospace; }
.gutter { flex: 0 0 46px; text-align: right; padding: 14px 12px 16px 0; color: #b6bcc5;
          background: #fcfcfd; border-right: 1px solid var(--line-soft); user-select: none; }
.code { flex: 1; padding: 14px 0 16px 16px; white-space: pre; overflow: hidden; color: var(--ink); }
.k { color: #8250df; }
.s { color: #0a6e5c; }
.vsel { display: inline-flex; align-items: center; gap: 7px; border: 1px solid #d8dbe0;
        background: #fff; border-radius: 6px; padding: 3px 9px; font-size: 12.5px;
        font-weight: 500; color: #374151; }

/* ---------- bundle: file tree + viewer ---------- */
.bundle { display: flex; align-items: stretch; }
.files { flex: 0 0 252px; border-right: 1px solid var(--line); background: #fcfcfd;
         padding: 14px 0 16px; }
.files .cap { font-size: 11px; font-weight: 700; letter-spacing: .6px; color: #9aa1ab;
              padding: 0 16px 10px; }
.fi { display: flex; align-items: center; gap: 7px; padding: 6px 16px; font-size: 13px;
      color: #374151; border-left: 2px solid transparent; }
.fi.sel { background: #eef3fd; border-left-color: var(--blue); color: var(--blue);
          font-weight: 600; }
.fi.nest { padding-left: 34px; }
.fi .flag { margin-left: auto; font-size: 10.5px; color: #9aa1ab; font-weight: 400; }
.dir { padding: 7px 16px 3px; font-size: 13px; color: #6b7280; }
.files .tot { border-top: 1px solid var(--line-soft); margin-top: 12px; padding: 11px 16px 0;
              font-size: 12px; color: #9aa1ab; }
.viewer { flex: 1; min-width: 0; }
.vhead { display: flex; align-items: baseline; gap: 12px; padding: 13px 18px;
         border-bottom: 1px solid var(--line-soft); font-size: 13.5px; }
.vhead .fn { font-weight: 700; font-size: 14px; }
.vhead .ep { background: #eef3fd; color: var(--blue); border-radius: 4px; font-size: 11px;
             font-weight: 600; padding: 2px 7px; }
.vhead .meta { margin-left: auto; color: var(--grey); font-size: 12.5px; }
"""

(HERE / "kosli-mock.css").write_text(CSS)
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
    <div><dt>Evaluation context</dt><dd class="mono">evc_7f31a92c
      <span style="font-weight:400;color:#1e55cd">&nbsp;view</span></dd></div>
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
