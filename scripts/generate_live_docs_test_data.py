#!/usr/bin/env python3
"""
Fetch live JSON from app.kosli.com and save as stub files for live-docs unit tests.

Run from the repo root whenever _MODIFIERS changes (new commands, renamed flows):
  python3 scripts/generate_live_docs_test_data.py
"""

import json
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live_docs_modifiers_data

_OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "tests",
    "testdata",
    "live_docs",
)


def save(filename, data):
    """Write data as pretty-printed JSON to the test data directory."""
    os.makedirs(_OUT_DIR, exist_ok=True)
    path = os.path.join(_OUT_DIR, filename)
    with open(path, "wt") as f:
        f.write(json.dumps(data, indent=2))
    print(f"  saved: {filename}")


def fetch_aws_prod_snapshot():
    """Fetch the latest aws-prod snapshot from app.kosli.com and return its JSON."""
    url = "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/%40%7Bnow%7D"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def flow_names_from_modifiers():
    """Return the set of flow names referenced in _MODIFIERS."""
    names = set()
    for command, ci in live_docs_modifiers_data.all_entries():
        fn = live_docs_modifiers_data.flow_name(command, ci)
        if fn:
            names.add(fn)
    return names


def find_trail_urls(snapshot, wanted_flow_names):
    """Return a dict mapping flow_name to its latest trail URL from the snapshot."""
    result = {}
    for artifact in snapshot["artifacts"]:
        for flow in artifact["flows"]:
            flow_name = flow["flow_name"]
            if flow_name not in wanted_flow_names:
                continue
            timestamp = flow["git_commit_info"]["timestamp"]
            if flow_name not in result or timestamp > result[flow_name]["timestamp"]:
                trail_name = flow["trail_name"]
                result[flow_name] = {
                    "timestamp": timestamp,
                    "url": f"https://app.kosli.com/api/v2/trails/cyber-dojo/{flow_name}/{trail_name}",
                }
    return result


def fetch_trail(url):
    """Fetch a trail JSON from app.kosli.com and return it."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("Fetching aws-prod snapshot...")
    snapshot = fetch_aws_prod_snapshot()
    save("cyber_dojo_aws_prod.json", snapshot)

    wanted = flow_names_from_modifiers()
    trail_urls = find_trail_urls(snapshot, wanted)
    missing = wanted - set(trail_urls.keys())
    if missing:
        print(f"WARNING: flows not found in snapshot: {missing}", file=sys.stderr)

    print(f"Fetching {len(trail_urls)} trail(s)...")
    for flow_name, data in sorted(trail_urls.items()):
        trail = fetch_trail(data["url"])
        save(f"cyber_dojo_trail_{flow_name}.json", trail)

    print("Done.")
