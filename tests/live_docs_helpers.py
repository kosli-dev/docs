"""
Shared helpers for live-docs unit tests.

Stub file helpers (pathed_test_data, aws_prod_stub, flow_trail_stub) rely on
JSON files under tests/testdata/live_docs/. Regenerate them whenever
_MODIFIERS changes (new commands, renamed flows, etc.) by running:

  python3 scripts/generate_live_docs_test_data.py
"""

import json
import os

import live_docs_fetch


def clear_live_docs_caches():
    """Clear all lru_caches in live_docs_fetch so stubs are used on the next call."""
    live_docs_fetch.yaml_lines.cache_clear()
    live_docs_fetch.resolve_head_sha.cache_clear()
    live_docs_fetch.fetch_trail.cache_clear()
    live_docs_fetch._fetch_latest_snapshot.cache_clear()
    live_docs_fetch.fetch_cli_json.cache_clear()


def stub_http_get(monkeypatch, stubs):
    """Clear live-docs caches and replace requests.get with a sequential stub."""
    clear_live_docs_caches()
    http_stub = HttpStub(stubs)
    monkeypatch.setattr("requests.get", http_stub.get)
    return http_stub


class HttpStub:
    """Sequential stub for requests.get() that returns pre-loaded responses in order."""

    def __init__(self, stubs):
        """Initialise with an ordered list of stub responses to return one per call."""
        self.stubs = stubs
        self.index = 0

    def get(self, url, **kwargs):
        """Return the next stub response and advance the index."""
        response = self.stubs[self.index]
        self.index += 1
        return response


class StubResponseStatusCode:
    """Stub response with only a status code."""

    def __init__(self, status_code):
        """Initialise with the given HTTP status code."""
        self.status_code = status_code


class StubResponseJson(StubResponseStatusCode):
    """Stub response that returns JSON data."""

    def __init__(self, stubbed):
        """Initialise with a dict or list to be returned by .json()."""
        super().__init__(200)
        self.stubbed = stubbed

    def json(self):
        """Return the stubbed JSON payload."""
        return self.stubbed


class StubResponseText(StubResponseStatusCode):
    """Stub response that returns plain text."""

    def __init__(self, stubbed):
        """Initialise with a string to be returned as .text."""
        super().__init__(200)
        self.text = stubbed


def head_sha_stub():
    """Return a stub response for a HEAD SHA API call.

    Uses all-zeros so tests asserting live_commit != backup_commit cannot
    accidentally collide with a real backup SHA.
    Both 'sha' (GitHub) and 'id' (GitLab) keys are present so the same stub
    works for both CI platforms.
    """
    return StubResponseJson({"sha": "0" * 40, "id": "0" * 40})


def pathed_test_data(filename):
    """Return the absolute path to a test data file in tests/testdata/live_docs/."""
    my_dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(my_dir_path, "testdata", "live_docs", filename)


def aws_prod_stub():
    """Return a StubResponseJson loaded from the cyber_dojo_aws_prod.json fixture."""
    with open(pathed_test_data("cyber_dojo_aws_prod.json"), "rt") as f:
        return StubResponseJson(json.loads(f.read()))


def flow_trail_stub(flow_name):
    """Return a StubResponseJson loaded from the trail fixture for flow_name."""
    with open(pathed_test_data(f"cyber_dojo_trail_{flow_name}.json"), "rt") as f:
        return StubResponseJson(json.loads(f.read()))
