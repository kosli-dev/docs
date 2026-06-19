import live_docs_queries_data
from live_docs_fetch import fetch_cli_json
from live_docs_helpers import (
    stub_http_get,
    StubResponseJson,
    StubResponseStatusCode,
)


def test_491e4f02(monkeypatch):
    """
    The CLI live-docs JSON response is the proxied JSON
    from an upstream Kosli CLI command.
    """
    stub = {"k": "v"}
    for command in live_docs_queries_data._CLI_COMMANDS:
        stub_http_get(monkeypatch, [StubResponseJson(stub)])
        result = fetch_cli_json(command)
        assert result is not None, f"Failed for command: {command}"


def test_491e4f03(monkeypatch):
    """fetch_cli_json returns None when the Kosli API call fails."""
    stub_http_get(monkeypatch, [StubResponseStatusCode(500)])
    result = fetch_cli_json(sorted(live_docs_queries_data._CLI_COMMANDS.keys())[0])
    assert result is None
