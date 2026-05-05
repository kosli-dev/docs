#!/usr/bin/env python3
"""
Audit script that reports the age of every unique backup YAML commit in _MODIFIERS,
and whether each command still appears in its workflow file at HEAD.

Run from the repo root:
  python scripts/audit_live_docs_backup_commits.py
"""

import datetime
import sys
import os
import requests
from urllib import parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from live_docs_modifiers_data import _MODIFIERS

_head_cache = {}


def github_commit_date(repo, sha):
    """Fetch the ISO 8601 commit date for sha in cyber-dojo/{repo} on GitHub, or None."""
    url = f"https://api.github.com/repos/cyber-dojo/{repo}/commits/{sha}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()["commit"]["committer"]["date"]


def gitlab_commit_date(repo, sha):
    """Fetch the ISO 8601 commit date for sha in cyber-dojo/{repo} on GitLab, or None."""
    encoded = parse.quote(f"cyber-dojo/{repo}", safe="")
    url = f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits/{sha}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json().get("committed_date")


def fetch_commit_date(ci, repo, sha):
    """Dispatch to the correct host and return the ISO 8601 commit date, or None."""
    if ci == "github":
        return github_commit_date(repo, sha)
    if ci == "gitlab":
        return gitlab_commit_date(repo, sha)
    return None


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
    if key not in _head_cache:
        _head_cache[key] = fetch_head_workflow(ci, repo, workflow)
    return _head_cache[key]


def command_in_head(command, ci):
    """Return 'yes', 'no', or '?' depending on whether command appears in the HEAD workflow."""
    y = _MODIFIERS[command][ci]["yaml"]
    content = head_workflow(ci, y["repo"], y["workflow"])
    if content is None:
        return "?"
    return "yes" if command in content else "no"


def age_days(date_str):
    """Return the number of whole days between now (UTC) and date_str (ISO 8601)."""
    dt = datetime.datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    now = datetime.datetime.now(datetime.timezone.utc)
    return (now - dt).days


def collect_unique_entries():
    """Return a dict mapping (ci, repo, sha) to the list of commands sharing that backup commit."""
    entries = {}
    for command, cis in _MODIFIERS.items():
        for ci, data in cis.items():
            y = data["yaml"]
            key = (ci, y["repo"], y["backup"]["commit"])
            entries.setdefault(key, []).append(command)
    return entries


def build_rows():
    """Fetch commit dates and HEAD presence for each entry; return rows sorted oldest-first."""
    entries = collect_unique_entries()
    rows = []
    n = len(entries)
    for i, ((ci, repo, sha), commands) in enumerate(entries.items(), 1):
        print(f"  [{i}/{n}] {ci}/{repo}/{sha[:8]}...   ", end="\r", flush=True)
        date_str = fetch_commit_date(ci, repo, sha)
        if date_str is None:
            date_display = "?"
            days = None
        else:
            date_display = date_str[:10]
            days = age_days(date_str)
        cmd_entries = [(cmd, command_in_head(cmd, ci)) for cmd in commands]
        rows.append((days, ci, repo, sha, date_display, cmd_entries))

    print(" " * 60, end="\r")
    rows.sort(key=lambda r: (r[0] is None, -(r[0] or 0)))
    return rows


def print_table(rows):
    """Print rows as a fixed-width table, oldest commits first."""
    w_ci   = max(len("ci"),      max(len(r[1]) for r in rows))
    w_repo = max(len("repo"),    max(len(r[2]) for r in rows))
    w_cmd  = max(len("command"), max(len(cmd) for r in rows for cmd, _ in r[5]))

    header = f"  {'age':>5}  {'date':<10}  {'ci':<{w_ci}}  {'repo':<{w_repo}}  {'sha':<8}  {'command':<{w_cmd}}  in HEAD?"
    print(header)
    print("  " + "-" * (len(header) - 2))

    prefix = 2 + 5 + 2 + 10 + 2 + w_ci + 2 + w_repo + 2 + 8 + 2
    indent = " " * prefix

    for days, ci, repo, sha, date_display, cmd_entries in rows:
        age_str = f"{days}d" if days is not None else "?"
        for i, (cmd, in_head) in enumerate(cmd_entries):
            if i == 0:
                print(f"  {age_str:>5}  {date_display:<10}  {ci:<{w_ci}}  {repo:<{w_repo}}  {sha[:8]}  {cmd:<{w_cmd}}  {in_head}")
            else:
                print(f"{indent}{cmd:<{w_cmd}}  {in_head}")
        print()


if __name__ == "__main__":
    rows = build_rows()
    print_table(rows)
