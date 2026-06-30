import json

import pytest

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
    _stub_get(monkeypatch, payload)
    monkeypatch.setattr("sys.argv", ["update_schemas.py", "--check"])

    update_schemas.main()  # exits 0 (no SystemExit)


def test_check_mode_fails_on_drift(tmp_path, monkeypatch):
    target = tmp_path / "schemas" / "policy" / "v1.json"
    target.parent.mkdir(parents=True)
    target.write_text(update_schemas.render({"$id": "stale"}), encoding="utf-8")

    monkeypatch.setattr(update_schemas, "_REPO_ROOT", tmp_path)
    monkeypatch.setattr(update_schemas, "_SCHEMAS", {"environment-policy/v1": "schemas/policy/v1.json"})
    _stub_get(monkeypatch, {"$id": "fresh"})
    monkeypatch.setattr("sys.argv", ["update_schemas.py", "--check"])

    with pytest.raises(SystemExit) as exc:
        update_schemas.main()
    assert exc.value.code == 1
