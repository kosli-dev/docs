"""HTTP fetch functions and URL resolution logic for live-docs.

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


def yaml_url(command, ci):
    """Return a URL to the exact line in a CI workflow file containing command.

    Falls back to backup_yaml_url when the live flow or commit cannot be resolved.
    """
    backup = live_docs_modifiers_data.backup_yaml_url(command, ci)

    if live_docs_modifiers_data.has_trail_event(command, ci):
        flow = flow_in_latest_snapshot(live_docs_modifiers_data.flow_name(command, ci))
    else:
        flow = None

    if flow and live_docs_modifiers_data.repo_directly_corresponds_to_flow(command, ci):
        commit_sha = flow["git_commit"]
    else:
        commit_sha = resolve_head_sha(command, ci)
        if commit_sha is None:
            return backup

    for n, line in enumerate(yaml_lines(command, ci, commit_sha), 1):
        if command in line and not line.lstrip().startswith("#"):
            return live_docs_modifiers_data.lined_yaml_url(command, ci, n, commit_sha)

    return backup


def event_url(command, ci):
    """Return a URL to the matching event in app.kosli.com for command and ci.

    Falls back to backup_event_url when live data cannot be resolved.
    """
    backup = live_docs_modifiers_data.backup_event_url(command, ci)

    if not live_docs_modifiers_data.has_trail_event(command, ci):
        return backup

    flow_name = live_docs_modifiers_data.flow_name(command, ci)
    flow = flow_in_latest_snapshot(flow_name)
    if not flow:
        return backup

    trail_name = flow["trail_name"]
    trail_json = fetch_trail(flow_name, trail_name)
    if trail_json is None:
        return backup

    query_string = _find_event_query_string(trail_json["events"], command)
    if query_string:
        return f"https://app.kosli.com/cyber-dojo/flows/{flow_name}/trails/{trail_name}?{query_string}"
    return backup


def _find_event_query_string(events, command):
    """Return a query string identifying the event for command in events, or False if not found."""
    if command == "kosli begin trail":
        return "attestation_id=1"
    for event in reversed(events):
        query_string = _matching_event_query_string(event, command)
        if query_string:
            return query_string
    return False


def _matching_event_query_string(event, command):
    """Return the query string that identifies event as matching command, or False."""
    if command == "kosli attest snyk":
        if _is_attestation_type(event, "snyk"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest sonar":
        if _is_attestation_type(event, "sonar"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "-Dsonar.analysis.kosli_flow":
        if _is_attestation_type(event, "sonar"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest junit":
        if _is_attestation_type(event, "junit"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest generic":
        if _is_attestation_type(event, "generic"):
            return f"attestation_id={event['attestation_id']}"
    elif command in ("kosli attest pullrequest github", "kosli attest pullrequest gitlab"):
        if _is_attestation_type(event, "pull_request"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest artifact":
        if _is_attestation_type(event, "artifact_creation_reported"):
            return f"attestation_id={event['artifact_id']}"
    elif command == "kosli attest custom":
        if _is_attestation_type(event, "custom"):
            return f"attestation_id={event['attestation_id']}"
    else:
        return False


def _is_attestation_type(event, wanted_type):
    """Return True if event matches the wanted attestation type."""
    actual_type = event.get("type", None)
    if wanted_type == "artifact_creation_reported":
        return actual_type == wanted_type
    if wanted_type == "custom" and actual_type == "artifact_attestation_reported":
        attestation_type = event.get("attestation_type", None)
        return isinstance(attestation_type, str) and attestation_type.startswith("custom:")
    return event.get("attestation_type", None) == wanted_type
