#!/usr/bin/env bash
trap 'git restore client_reference/' EXIT

python3 scripts/resolve_livedocs.py
(sleep 3 && open http://localhost:3000/client_reference/kosli_attest_artifact) &
mint dev
