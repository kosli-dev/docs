#!/usr/bin/env python3
"""
Prints an update script to stdout that, when run, updates the backup commit
SHA and line number in _MODIFIERS to HEAD for every entry where the command
is still present in the workflow at HEAD.

Entries where the command is no longer present at HEAD are skipped.

Run from the repo root:
  python3 scripts/refresh_live_docs_backup_commits.py > update_live_docs_backup_commits.py
  python3 update_live_docs_backup_commits.py

To verify the commands are still present in their workflows at HEAD
(and the backup commits are not too old), run:
  python3 scripts/audit_live_docs_backup_commits.py
"""

import datetime
import os
import sys
import requests
from urllib import parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from live_docs_modifiers_data import _MODIFIERS

_head_sha_cache = {}
_head_content_cache = {}

MODIFIERS_PATH = "scripts/live_docs_modifiers_data.py"
INDENT = "                    "


def fetch_github_head_sha(repo):
    """Fetch the current HEAD commit SHA for cyber-dojo/{repo} on GitHub, or None."""
    url = f"https://api.github.com/repos/cyber-dojo/{repo}/commits/HEAD"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json().get("sha")


def fetch_gitlab_head_sha(repo):
    """Fetch the current HEAD commit SHA for cyber-dojo/{repo} on GitLab, or None."""
    encoded = parse.quote(f"cyber-dojo/{repo}", safe="")
    url = f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits/HEAD"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json().get("id")


def head_sha(ci, repo):
    """Return the cached HEAD SHA for ci/repo, fetching on first access."""
    key = (ci, repo)
    if key not in _head_sha_cache:
        if ci == "github":
            _head_sha_cache[key] = fetch_github_head_sha(repo)
        elif ci == "gitlab":
            _head_sha_cache[key] = fetch_gitlab_head_sha(repo)
        else:
            _head_sha_cache[key] = None
    return _head_sha_cache[key]


def fetch_head_workflow(ci, repo, workflow):
    """Fetch the raw workflow file content at HEAD for ci/repo/workflow, or None."""
    if ci == "github":
        url = f"https://raw.githubusercontent.com/cyber-dojo/{repo}/HEAD/{workflow}"
    elif ci == "gitlab":
        url = f"https://gitlab.com/cyber-dojo/{repo}/-/raw/HEAD/{workflow}"
    else:
        return None
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.text


def head_workflow(ci, repo, workflow):
    """Return cached HEAD content for ci/repo/workflow, fetching on first access."""
    key = (ci, repo, workflow)
    if key not in _head_content_cache:
        _head_content_cache[key] = fetch_head_workflow(ci, repo, workflow)
    return _head_content_cache[key]


def find_line_number(content, command):
    """Return the 1-based line number of the first non-comment occurrence of command in content, or None."""
    for n, line in enumerate(content.split("\n"), 1):
        if command in line and not line.lstrip().startswith("#"):
            return n
    return None


def make_replacement(old_commit, old_line, new_commit, new_line):
    """Return (old_str, new_str) targeting the backup block for old_commit/old_line."""
    old = f'{INDENT}"commit": "{old_commit}",\n{INDENT}"line": {old_line},'
    new = f'{INDENT}"commit": "{new_commit}",\n{INDENT}"line": {new_line},'
    return old, new


def progress(msg):
    """Print a progress message to stderr so it does not pollute stdout."""
    print(msg, end="\r", flush=True, file=sys.stderr)


def build_replacements():
    """Return list of (old_str, new_str) for entries present at HEAD with a changed backup."""
    replacements = []
    seen = set()
    for command, cis in _MODIFIERS.items():
        for ci, data in cis.items():
            y = data["yaml"]
            repo, workflow = y["repo"], y["workflow"]
            old_commit = y["backup"]["commit"]
            old_line = y["backup"]["line"]

            progress(f"  checking {ci}/{repo} -- {command}...   ")

            content = head_workflow(ci, repo, workflow)
            if content is None or command not in content:
                continue

            new_sha = head_sha(ci, repo)
            if new_sha is None:
                continue

            new_line = find_line_number(content, command)
            if new_line is None:
                continue

            if new_sha == old_commit and new_line == old_line:
                continue

            key = (old_commit, old_line)
            if key in seen:
                continue
            seen.add(key)

            replacements.append(make_replacement(old_commit, old_line, new_sha, new_line))

    progress(" " * 60)
    return replacements


def print_script(replacements):
    """Print the update script to stdout."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "#!/usr/bin/env python3",
        '"""',
        f"Auto-generated by refresh_live_docs_backup_commits.py on {now}.",
        "Updates backup commit SHAs and line numbers in _MODIFIERS to HEAD.",
        "",
        "Run from the repo root:",
        "  python3 update_live_docs_backup_commits.py",
        '"""',
        "",
        f'PATH = "{MODIFIERS_PATH}"',
        "",
        "replacements = [",
    ]
    for old, new in replacements:
        lines.append("    (")
        lines.append(f"        {old!r},")
        lines.append(f"        {new!r},")
        lines.append("    ),")
    lines += [
        "]",
        "",
        "with open(PATH) as f:",
        "    content = f.read()",
        "",
        "for old, new in replacements:",
        '    assert old in content, f"Pattern not found:\\n{old}"',
        "    content = content.replace(old, new)",
        "",
        'with open(PATH, "w") as f:',
        "    f.write(content)",
        "",
        f'print("Updated {{PATH}} with {len(replacements)} replacement(s).")',
    ]
    print("\n".join(lines))


if __name__ == "__main__":
    replacements = build_replacements()
    if not replacements:
        print("No updates needed.", file=sys.stderr)
    else:
        print_script(replacements)
        print(f"{len(replacements)} replacement(s) written to stdout.", file=sys.stderr)
