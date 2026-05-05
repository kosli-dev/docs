"""
Live-docs are live examples of Kosli CLI commands embedded in https://docs.kosli.com/client_reference.
They are used early in demos to prospective clients, where a slow response undermines the initial impression.
Each endpoint resolves the current state of a real cyber-dojo CI pipeline by making
external HTTP calls; cold-hit latency is multiple seconds, warm-hit latency is ~4ms.
Speed is therefore a correctness requirement, not just a quality concern.
Caching, HTTP-fetching, and background refresh are handled in live_docs_cache.py.

The three main live-docs API GET endpoints are:
  1. api/v2/livedocs/<ORG>/cli   ?command=kosli get snapshot...
  2. api/v2/livedocs/<ORG>/yaml  ?ci=github&command=kosli attest snyk
  3. api/v2/livedocs/<ORG>/event ?ci=github&command=kosli attest snyk

There is also a corresponding _exists? endpoint for each one, to determine if its partner will
return a usable redirect if called.

1 is for QUERIES (such as kosli-get-snapshot) that make an HTTP GET when called from the CLI.
    Its implementation:
    - Uses the _QUERIES data structure (live_docs_queries_data.py)
    - DOES call the API end-point for the given command argument

2 is for MODIFIERS (such as kosli-attest-snyk) that make an HTTP POST when called from the CLI.
    Its implementation:
    - Uses the _MODIFIERS data structure (live_docs_modifiers_data.py)
    - Does NOT call the given command argument
    - Returns a redirect-URL pointing to the exact line containing the
        given command, in a CI workflow file for a cyber-dojo repo.
    - Implementation overview
        - get the target Flow for the given command, from _MODIFIERS, eg runner-ci
        - get the latest Snapshot for org=cyber-dojo, env=aws-prod
        - find the Flow in the Snapshot json, for the Artifact whose provenance matches the target Flow
        - get the commit-sha for the found Flow
        - get the raw source of the CI workflow file, for this commit, from the repo for this Flow
        - find the line-number of the given command, in this raw source
        - return a redirect URL for the line number, in the workflow file, for the commit, in the repo
        - Note: the URL is returned as a redirect; clicking the end-point URL, in the CLI doc's .md page,
          takes you directly to the line containing the given command.

3 is for MODIFIERS (such as kosli-attest-snyk) that make an HTTP POST when called from the CLI.
    Its implementation:
    - Uses the _MODIFIERS data structure (live_docs_modifiers_data.py)
    - Does NOT call the given command argument
    - Returns a redirect-URL pointing to the event, in https://app.kosli.com,
        created when the command pointed to in 2) actually ran in its CI workflow file.
    - Implementation overview
        - get the target Flow for the given command, from _MODIFIERS, eg runner-ci
        - get the latest Snapshot for org=cyber-dojo, env=aws-prod
        - find the Flow in the Snapshot json, for the Artifact whose provenance matches the target Flow
        - get the JSON for the Trail, in https://app.kosli.com, for the found Flow/Trail
        - return a URL for the exact UX event in https://app.kosli.com, for the given command in this Flow/Trail

Note: In 2 and 3, the query parameter is called "command", but can be any string to search for in a CI
workflow file. For example, a live-docs URL for a sonar attestation using a webhook exists in
_MODIFIERS with a key of "-Dsonar.analysis.kosli_flow", and this string exists in the CI
workflow file of the differ repo.
"""
import logging

import requests

import live_docs_modifiers_data
import live_docs_queries_data
from live_docs_fetch import (
    resolve_head_sha,
    fetch_trail,
    flow_in_latest_snapshot,
    yaml_lines,
)


class BadRequest(Exception):
    """Shim for werkzeug BadRequest."""


class HTTPException(Exception):
    """Shim for FastAPI HTTPException."""
    def __init__(self, status_code, detail):
        """Initialise with status_code and detail."""
        self.status_code = status_code
        self.detail = detail


def record_trace(fn):
    """Shim for the server telemetry decorator."""
    return fn

logger = logging.getLogger(__name__)


def raise_bad_request_when_unknown(command, ci):
    """Raise BadRequest if command or ci is not a known live-docs entry."""
    if not live_docs_modifiers_data.has_entry(command, ci):
        raise BadRequest(f"Unknown command {command!r} or ci {ci!r}")


def yaml_url(_org, command, ci):
    """Return a redirect URL to the line in a CI workflow yaml file that contains command.

    Falls back to backup_yaml_url when the live flow or commit cannot be resolved.
    """
    raise_bad_request_when_unknown(command, ci)
    backup = live_docs_modifiers_data.backup_yaml_url(command, ci)

    if live_docs_modifiers_data.has_trail_event(command, ci):
        flow_name = live_docs_modifiers_data.flow_name(command, ci)
        flow = flow_in_latest_snapshot(flow_name)
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
    """Return a URL to an event in https://app.kosli.com for the given command and ci.

    Attempts to return a URL for the most recent compliant Trail.
    Falls back to backup_event_url when live data cannot be resolved.
    """
    raise_bad_request_when_unknown(command, ci)
    backup = live_docs_modifiers_data.backup_event_url(command, ci)

    flow_name = live_docs_modifiers_data.flow_name(command, ci)
    if live_docs_modifiers_data.has_trail_event(command, ci):
        flow = flow_in_latest_snapshot(flow_name)
    else:
        flow = None

    if not flow:
        return backup

    trail_name = flow["trail_name"]

    trail_json = fetch_trail(flow_name, trail_name)
    if trail_json is None:
        return backup

    events = trail_json["events"]
    query_string = find_event_query_string(events, command)
    if query_string:
        return f"https://app.kosli.com/cyber-dojo/flows/{flow_name}/trails/{trail_name}?{query_string}"
    else:
        return backup


def find_event_query_string(events, command):
    """Return a query string identifying the event for command in events, or False if not found."""
    # begin trail is always the first event of a trail and the HTML does not include the event ID (yet)
    if command == "kosli begin trail":
        return "attestation_id=1"

    # eg command = "kosli attest snyk"
    for event in reversed(events):
        query_string = matching_event_query_string(event, command)
        if query_string:
            return query_string

    return False


def matching_event_query_string(event, command):
    """Return the query string that identifies event as matching command, or False."""
    if command == "kosli attest snyk":
        if is_attestation_type(event, "snyk"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest sonar":
        if is_attestation_type(event, "sonar"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "-Dsonar.analysis.kosli_flow":
        if is_attestation_type(event, "sonar"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest junit":
        if is_attestation_type(event, "junit"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest generic":
        if is_attestation_type(event, "generic"):
            return f"attestation_id={event['attestation_id']}"
    elif command in ("kosli attest pullrequest github", "kosli attest pullrequest gitlab"):
        if is_attestation_type(event, "pull_request"):
            return f"attestation_id={event['attestation_id']}"
    elif command == "kosli attest artifact":
        if is_attestation_type(event, "artifact_creation_reported"):
            return f"attestation_id={event['artifact_id']}"
    elif command == "kosli attest custom":
        if is_attestation_type(event, "custom"):
            return f"attestation_id={event['attestation_id']}"
    else:
        return False


def is_attestation_type(event, wanted_type):
    """Return True if event matches the wanted attestation type."""
    actual_type = event.get("type", None)
    if wanted_type == "artifact_creation_reported":
        return actual_type == wanted_type
    elif wanted_type == "custom" and actual_type == "artifact_attestation_reported":
        attestation_type = event.get("attestation_type", None)
        return isinstance(attestation_type, str) and attestation_type.startswith(
            "custom:"
        )
    else:
        return event.get("attestation_type", None) == wanted_type


@record_trace
def get_yaml_url(org, command: str, ci: str) -> str:
    """Return the redirect URL for the given CLI command in a CI system yaml pipeline.

    Raises HTTPException(400) if the command or CI system is unknown.
    """
    try:
        return yaml_url(org, command, ci)
    except BadRequest as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@record_trace
def get_event_url(command: str, ci: str) -> str:
    """Return a URL to an event in https://app.kosli.com for the given command and CI system.

    Raises HTTPException(400) if the command or CI system is unknown or no URL is available.
    """
    try:
        url = event_url(command, ci)
    except BadRequest as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    if url == "":
        raise HTTPException(
            status_code=400,
            detail=f"No event URL available for command {command}",
        )
    return url


@record_trace
def get_cli_json(command: str):
    """Fetch the live CLI command output from app.kosli.com and return the raw JSON.

    Raises HTTPException(400) if the command is not supported.
    Raises HTTPException(503) if the Kosli API request fails.
    """
    if not live_docs_queries_data.has_query_entry(command):
        raise HTTPException(
            status_code=400,
            detail=f"Command '{command}' not supported",
        )
    url = live_docs_queries_data.query_url(command)
    response = external_http().get(f"https://app.kosli.com/api/v2/{url}")
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        raise HTTPException(status_code=503, detail="Failed to fetch live Kosli API response") from exc
    return response.json()
