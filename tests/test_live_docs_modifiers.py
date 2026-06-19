import json

import live_docs_modifiers_data
from live_docs_fetch import (
    yaml_url,
    event_url,
    _matching_event_query_string,
    _find_event_query_string,
)
from live_docs_helpers import (
    stub_http_get,
    StubResponseJson,
    StubResponseText,
    StubResponseStatusCode,
    head_sha_stub,
    pathed_test_data,
    aws_prod_stub,
    flow_trail_stub,
)


def test_aefa1402(monkeypatch):
    """
    yaml/event returns backup-url when flow is NOT in aws-prod snapshot
    and main.yaml at HEAD does NOT contain the command.
    """
    command = "kosli attest artifact"
    assert live_docs_modifiers_data.has_command(command)
    for ci in live_docs_modifiers_data.cis_for(command):
        flow_name = live_docs_modifiers_data.flow_name(command, ci)
        diag = f"{ci} - {live_docs_modifiers_data.repo_name(command, ci)} - {command}"

        with open(pathed_test_data("cyber_dojo_aws_prod.json"), "rt") as file:
            aws_prod = json.loads(file.read())

        for artifact in aws_prod["artifacts"]:
            for flow in artifact["flows"]:
                if flow["flow_name"] == flow_name:
                    flow["flow_name"] = f"{flow_name}-doctored"

        # yaml
        stub_http_get(
            monkeypatch,
            [
                StubResponseJson(aws_prod),
                head_sha_stub(),
                StubResponseText("hello\nworld"),
            ],
        )
        actual_yaml_url = yaml_url(command, ci)
        assert actual_yaml_url == live_docs_modifiers_data.backup_yaml_url(
            command, ci
        ), diag

        # event
        stub_http_get(monkeypatch, [StubResponseJson(aws_prod)])
        actual_event_url = event_url(command, ci)
        assert actual_event_url == live_docs_modifiers_data.backup_event_url(
            command, ci
        ), diag


def test_aefa1405(monkeypatch):
    """
    When no yaml lines match the command, return backup-yaml-url.
    """
    ci = "github"
    command = "kosli attest snyk"
    stub_http_get(monkeypatch, [aws_prod_stub(), head_sha_stub(), StubResponseText("a\nb\nc\nd")])
    actual_yaml_url = yaml_url(command, ci)
    assert actual_yaml_url == live_docs_modifiers_data.backup_yaml_url(command, ci)


def test_aefa1406(monkeypatch):
    """
    yaml returns backup-yaml-url when main.yml response returns non-200.
    """
    ci = "github"
    command = "kosli attest snyk"
    stub_http_get(monkeypatch, [aws_prod_stub(), head_sha_stub(), StubResponseStatusCode(400)])
    actual_yaml_url = yaml_url(command, ci)
    assert actual_yaml_url == live_docs_modifiers_data.backup_yaml_url(command, ci)


def test_aefa1409(monkeypatch):
    """
    yaml returns backup-yaml-url when the HEAD SHA API returns non-200.
    """
    ci = "github"
    command = "kosli attest snyk"
    stub_http_get(monkeypatch, [aws_prod_stub(), StubResponseStatusCode(400)])
    actual_yaml_url = yaml_url(command, ci)
    assert actual_yaml_url == live_docs_modifiers_data.backup_yaml_url(command, ci)


def test_aefa1410(monkeypatch):
    """
    yaml_url returns backup-yaml-url when the GitLab HEAD SHA API returns non-200.
    """
    ci = "gitlab"
    command = "kosli report approval"
    stub_http_get(monkeypatch, [StubResponseStatusCode(400)])
    actual_yaml_url = yaml_url(command, ci)
    assert actual_yaml_url == live_docs_modifiers_data.backup_yaml_url(command, ci)


def test_aefa1404(monkeypatch):
    """
    When no events in a Trail match the command, return backup-event-url.
    """
    ci = "github"
    command = "kosli attest snyk"
    flow_name = live_docs_modifiers_data.flow_name(command, ci)

    trail_stub = flow_trail_stub(flow_name)
    for event in trail_stub.stubbed["events"]:
        event["type"] = "never-matched"
        event["attestation_type"] = "never-matched"

    stub_http_get(monkeypatch, [aws_prod_stub(), trail_stub])
    actual_event_url = event_url(command, ci)
    assert actual_event_url == live_docs_modifiers_data.backup_event_url(command, ci)


def test_aefa1407(monkeypatch):
    """
    event returns backup-event-url when events API response returns non-200.
    """
    ci = "github"
    command = "kosli attest snyk"
    stub_http_get(monkeypatch, [aws_prod_stub(), StubResponseStatusCode(400)])
    actual_event_url = event_url(command, ci)
    assert actual_event_url == live_docs_modifiers_data.backup_event_url(command, ci)


def test_aefa1408(monkeypatch):
    """
    event returns backup-event-url when Snapshot API response returns non-200.
    """
    ci = "github"
    command = "kosli attest snyk"
    stub_http_get(monkeypatch, [StubResponseStatusCode(400)])
    actual_event_url = event_url(command, ci)
    assert actual_event_url == live_docs_modifiers_data.backup_event_url(command, ci)


def test_aefa1419(monkeypatch):
    """
    event_url returns backup-event-url when the command has no associated Trail event.
    """
    ci = "github"
    command = "kosli report approval"
    actual_event_url = event_url(command, ci)
    assert actual_event_url == live_docs_modifiers_data.backup_event_url(command, ci)


def test_aefa1414():
    """matching_event_query_string() returns False for unknown command"""
    assert _matching_event_query_string(None, "unknown") is False


def test_aefa141d():
    """matching_event_query_string returns the attestation_id for a matching snyk event."""
    event = {"attestation_type": "snyk", "attestation_id": "abc-123"}
    assert (
        _matching_event_query_string(event, "kosli attest snyk")
        == "attestation_id=abc-123"
    )


def test_aefa1415():
    """find_event_query_string() returns False when command is not found"""
    assert _find_event_query_string([], "unknown") is False
