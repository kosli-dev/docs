"""HTTP fetch functions for live-docs URL resolution.

Results are memoized in-process to avoid redundant HTTP calls within a single run.
"""
import requests
from functools import lru_cache
from urllib import parse

import live_docs_modifiers_data


@lru_cache(maxsize=None)
def yaml_lines(command, ci, commit_sha):
    """Fetch the raw workflow YAML for command/ci at commit_sha and return it as a list of lines."""
    url = live_docs_modifiers_data.raw_yaml_url(command, ci, commit_sha)
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.text.split("\n")


@lru_cache(maxsize=None)
def resolve_head_sha(command, ci):
    """Return the HEAD commit SHA for the repo of command/ci, or None on failure."""
    if ci == "github":
        repo = live_docs_modifiers_data.repo_name(command, ci)
        url = f"https://api.github.com/repos/cyber-dojo/{repo}/commits/HEAD"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json().get("sha")
    if ci == "gitlab":
        repo = live_docs_modifiers_data.repo_name(command, ci)
        encoded = parse.quote(f"cyber-dojo/{repo}", safe="")
        url = f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits/HEAD"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json().get("id")
    return None


@lru_cache(maxsize=None)
def fetch_trail(flow_name, trail_name):
    """Fetch trail JSON from app.kosli.com; return None if the request fails."""
    url = f"https://app.kosli.com/api/v2/trails/cyber-dojo/{flow_name}/{trail_name}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


@lru_cache(maxsize=1)
def _fetch_latest_snapshot():
    """Fetch and return the latest aws-prod snapshot JSON, or None on failure."""
    url = "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/@{now}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def flow_in_latest_snapshot(flow_name):
    """Return the flow entry for flow_name from the latest aws-prod snapshot, or None."""
    snapshot = _fetch_latest_snapshot()
    if snapshot is None:
        return None
    for artifact in snapshot["artifacts"]:
        for flow in artifact["flows"]:
            if flow["flow_name"] == flow_name:
                return flow
    return None
