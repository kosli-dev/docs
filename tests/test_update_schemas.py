import json

import pytest
import requests

import update_schemas


class FakeResponse:
    """Minimal stand-in for a requests.Response."""

    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self._payload


def _stub_get(monkeypatch, payload):
    monkeypatch.setattr(
        update_schemas.requests, "get", lambda url, **kwargs: FakeResponse(payload)
    )


def test_render_is_pretty_and_newline_terminated():
    out = update_schemas.render({"b": 1, "a": [1, 2]})
    assert out.endswith("}\n")
    # 2-space indent
    assert '\n  "b": 1' in out


def test_render_round_trips():
    payload = {"$id": "x", "nested": {"k": [1, 2, 3]}}
    assert json.loads(update_schemas.render(payload)) == payload


def test_write_mode_creates_versioned_path(tmp_path, monkeypatch):
    payload = {"$id": "https://docs.kosli.com/schemas/flow-template/v1"}
    monkeypatch.setattr(update_schemas, "_REPO_ROOT", tmp_path)
    monkeypatch.setattr(update_schemas, "_SCHEMAS", {"flow-template/v1": "schemas/flow-template/v1.json"})
    monkeypatch.setattr(update_schemas, "_CAPABILITIES", {})
    _stub_get(monkeypatch, payload)
    monkeypatch.setattr("sys.argv", ["update_schemas.py"])

    update_schemas.main()

    written = tmp_path / "schemas" / "flow-template" / "v1.json"
    assert written.exists()
    assert json.loads(written.read_text()) == payload
    assert written.read_text() == update_schemas.render(payload)


def test_check_mode_passes_when_in_sync(tmp_path, monkeypatch):
    payload = {"$id": "x"}
    target = tmp_path / "schemas" / "policy" / "v1.json"
    target.parent.mkdir(parents=True)
    target.write_text(update_schemas.render(payload), encoding="utf-8")

    monkeypatch.setattr(update_schemas, "_REPO_ROOT", tmp_path)
    monkeypatch.setattr(update_schemas, "_SCHEMAS", {"environment-policy/v1": "schemas/policy/v1.json"})
    monkeypatch.setattr(update_schemas, "_CAPABILITIES", {})
    _stub_get(monkeypatch, payload)
    monkeypatch.setattr("sys.argv", ["update_schemas.py", "--check"])

    update_schemas.main()  # exits 0 (no SystemExit)


def test_check_mode_fails_on_drift(tmp_path, monkeypatch):
    target = tmp_path / "schemas" / "policy" / "v1.json"
    target.parent.mkdir(parents=True)
    target.write_text(update_schemas.render({"$id": "stale"}), encoding="utf-8")

    monkeypatch.setattr(update_schemas, "_REPO_ROOT", tmp_path)
    monkeypatch.setattr(update_schemas, "_SCHEMAS", {"environment-policy/v1": "schemas/policy/v1.json"})
    monkeypatch.setattr(update_schemas, "_CAPABILITIES", {})
    _stub_get(monkeypatch, {"$id": "fresh"})
    monkeypatch.setattr("sys.argv", ["update_schemas.py", "--check"])

    with pytest.raises(SystemExit) as exc:
        update_schemas.main()
    assert exc.value.code == 1


class FakeGitHub:
    """Answers the two opa-lambda requests: the release tags, then a file's contents."""

    def __init__(self, tags, contents, status=200):
        self.tags = tags
        self.contents = contents
        self.status = status
        self.requests = []

    def get(self, url, headers=None, params=None, **kwargs):
        self.requests.append((url, headers, params))
        if url.endswith("/git/matching-refs/tags/release-"):
            return FakeResponse([{"ref": f"refs/tags/{tag}"} for tag in self.tags])
        if self.status == 404:
            response = requests.Response()
            response.status_code = 404
            raise requests.HTTPError(response=response)
        return FakeResponse(self.contents)


def _stub_github(monkeypatch, tmp_path, github):
    monkeypatch.setenv("OPA_LAMBDA_READ_TOKEN", "t0ken")
    monkeypatch.setattr(update_schemas, "_REPO_ROOT", tmp_path)
    monkeypatch.setattr(update_schemas, "_SCHEMAS", {})
    monkeypatch.setattr(update_schemas, "_CAPABILITIES", {"capabilities.json": "rego/capabilities/v1.json"})
    monkeypatch.setattr(update_schemas.requests, "get", github.get)
    monkeypatch.setattr("sys.argv", ["update_schemas.py"])


def test_capabilities_come_from_the_newest_release_tag(tmp_path, monkeypatch):
    capabilities = {"allow_net": [], "builtins": [{"name": "abs"}]}
    github = FakeGitHub(
        tags=["release-2026-10-28-09-49-06", "release-2026-11-04-11-02-33", "release-2026-10-22-13-03-15"],
        contents=capabilities,
    )
    _stub_github(monkeypatch, tmp_path, github)

    update_schemas.main()

    written = tmp_path / "rego" / "capabilities" / "v1.json"
    assert json.loads(written.read_text()) == capabilities
    url, headers, params = github.requests[-1]
    assert url == "https://api.github.com/repos/kosli-dev/opa-lambda/contents/capabilities.json"
    assert params == {"ref": "release-2026-11-04-11-02-33"}
    assert headers["Authorization"] == "Bearer t0ken"


def test_capabilities_missing_from_the_release_fails_naming_the_tag(tmp_path, monkeypatch):
    github = FakeGitHub(tags=["release-2026-10-28-09-49-06"], contents=None, status=404)
    _stub_github(monkeypatch, tmp_path, github)

    with pytest.raises(SystemExit) as exc:
        update_schemas.main()
    assert "release-2026-10-28-09-49-06" in str(exc.value.code)
    assert not (tmp_path / "rego").exists()


def test_capabilities_need_a_token(tmp_path, monkeypatch):
    github = FakeGitHub(tags=["release-2026-10-28-09-49-06"], contents={})
    _stub_github(monkeypatch, tmp_path, github)
    monkeypatch.delenv("OPA_LAMBDA_READ_TOKEN")

    with pytest.raises(SystemExit) as exc:
        update_schemas.main()
    assert "OPA_LAMBDA_READ_TOKEN" in str(exc.value.code)
    assert github.requests == []
