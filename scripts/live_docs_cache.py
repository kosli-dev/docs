"""Permanent cache infrastructure, cached HTTP functions, and background warm-up for live-docs.

See docs/ADRs/20260423-live-docs-caching.md for the caching design.

To see the effect of the cache, run test/scripts/test-live-docs-cache.sh
immediately after a 'make demo_restart' (cold first call, warm subsequent calls).
"""
import logging
import threading
from enum import Enum
from functools import wraps
from urllib import parse

import requests

import live_docs_modifiers_data


def external_http():
    """Return a requests shim matching the server's external_http() interface."""
    return requests

logger = logging.getLogger(__name__)

_cache_stores = []


def _make_cache():
    """Return a decorator that caches results permanently, thread-safely.

    Each call registers the backing store in _cache_stores so that
    clear_live_docs_caches() picks it up automatically.
    """
    store = {}
    _cache_stores.append(store)
    lock = threading.Lock()

    def decorator(fn):
        """Wrap fn with permanent memoization."""
        @wraps(fn)
        def wrapper(*args):
            """Return a cached result if present, otherwise call fn and cache its result.

            Falsy results (None, []) are not cached so that a transient external API
            failure does not get locked in permanently. The next call will retry.
            """
            with lock:
                if args in store:
                    return store[args]
            result = fn(*args)
            if result:
                with lock:
                    store[args] = result
            return result
        return wrapper

    return decorator


def clear_live_docs_caches():
    """Clear all live-docs caches. Intended for use in tests."""
    for store in _cache_stores:
        store.clear()


_snapshot_cache = _make_cache()
_yaml_lines_cache = _make_cache()
_trail_cache = _make_cache()
_head_sha_cache = _make_cache()

@_yaml_lines_cache
def yaml_lines(command, ci, commit_sha):
    """Fetch the raw workflow YAML for command/ci at commit_sha and return it as a list of lines."""
    url = live_docs_modifiers_data.raw_yaml_url(command, ci, commit_sha)
    response = external_http().get(url)
    if response.status_code != 200:
        return []
    else:
        return response.text.split("\n")


@_head_sha_cache
def resolve_head_sha(command, ci):
    """Return the HEAD commit SHA for the repo of command/ci, or None on failure.

    None is falsy and therefore not cached, so a transient API failure (including
    rate-limiting) causes the next request to retry rather than locking in the failure.
    """
    if ci == "github":
        repo = live_docs_modifiers_data.repo_name(command, ci)
        url = f"https://api.github.com/repos/cyber-dojo/{repo}/commits/HEAD"
        response = external_http().get(url)
        if response.status_code != 200:
            return None
        return response.json().get("sha")
    if ci == "gitlab":
        repo = live_docs_modifiers_data.repo_name(command, ci)
        encoded = parse.quote(f"cyber-dojo/{repo}", safe="")
        url = f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits/HEAD"
        response = external_http().get(url)
        if response.status_code != 200:
            return None
        return response.json().get("id")
    return None


@_trail_cache
def fetch_trail(flow_name, trail_name):
    """Fetch trail JSON from app.kosli.com; return None if the request fails."""
    url = f"https://app.kosli.com/api/v2/trails/cyber-dojo/{flow_name}/{trail_name}"
    response = external_http().get(url)
    if response.status_code != 200:
        return None
    return response.json()


@_snapshot_cache
def _fetch_latest_snapshot():
    """Fetch and return the latest aws-prod snapshot JSON, or None on failure."""
    url = "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/@{now}"
    response = external_http().get(url)
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


class WarmResult(Enum):
    """Outcome of a single _warm_one_cache call."""
    FLOW_NOT_FOUND = "flow_not_found"
    SHA_UNAVAILABLE = "sha_unavailable"
    WARMED = "warmed"


def _warm_one_cache(command, ci):
    """Warm the caches for a single command/ci entry."""
    if not live_docs_modifiers_data.has_trail_event(command, ci):
        commit_sha = resolve_head_sha(command, ci)
        if commit_sha is None:
            return WarmResult.SHA_UNAVAILABLE
        yaml_lines(command, ci, commit_sha)
        return WarmResult.WARMED

    flow_name = live_docs_modifiers_data.flow_name(command, ci)
    flow = flow_in_latest_snapshot(flow_name)
    if not flow:
        return WarmResult.FLOW_NOT_FOUND

    if live_docs_modifiers_data.repo_directly_corresponds_to_flow(command, ci):
        commit_sha = flow["git_commit"]
    else:
        commit_sha = resolve_head_sha(command, ci)
        if commit_sha is None:
            return WarmResult.SHA_UNAVAILABLE

    yaml_lines(command, ci, commit_sha)
    fetch_trail(flow_name, flow["trail_name"])
    return WarmResult.WARMED


def _warm_all_caches():  # pragma: no cover
    """Resolve every entry in _MODIFIERS, populating all four caches."""
    for command, ci in live_docs_modifiers_data.all_entries():
        _warm_one_cache(command, ci)


def _background_cache_warmup():  # pragma: no cover
    """Warm all live-docs caches once at server startup."""
    try:
        _warm_all_caches()
    except Exception:
        logger.exception("live-docs background cache warm-up failed")


def start_background_cache_warmup():  # pragma: no cover
    """Start the background cache warm-up daemon thread.

    Must be called from gunicorn's post_fork hook so that each worker process
    gets its own thread. Threads do not survive fork(), so a module-level
    Thread.start() would only run in the master process and workers would
    start with cold caches.
    """
    _THREAD_NAME = "live-docs-cache-warmup"
    if any(t.name == _THREAD_NAME for t in threading.enumerate()):
        return
    threading.Thread(target=_background_cache_warmup, daemon=True, name=_THREAD_NAME).start()
