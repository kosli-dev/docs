"""Data table for live-docs query (GET) commands.

_QUERIES maps query-style CLI commands to the corresponding Kosli API path.
"""

_QUERIES = {
    "kosli list environments --output=json": "environments/cyber-dojo",
    "kosli get environment aws-prod --output=json": "environments/cyber-dojo/aws-prod",
    "kosli log environment aws-prod --output=json": "environments/cyber-dojo/aws-prod/events",
    "kosli list snapshots aws-prod --output=json": "snapshots/cyber-dojo/aws-prod",
    "kosli get snapshot aws-prod --output=json": "snapshots/cyber-dojo/aws-prod/-1",
    "kosli diff snapshots aws-beta aws-prod --output=json": "env-diff/cyber-dojo?snappish1=aws-beta&snappish2=aws-prod",
    "kosli list flows --output=json": "flows/cyber-dojo",
    "kosli get flow dashboard-ci --output=json": "flows/cyber-dojo/dashboard-ci",
    "kosli list trails dashboard-ci --output=json": "trails/cyber-dojo/dashboard-ci",
    "kosli get trail dashboard-ci 1159a6f1193150681b8484545150334e89de6c1c --output=json": "trails/cyber-dojo/dashboard-ci/1159a6f1193150681b8484545150334e89de6c1c",
    "kosli get attestation snyk-container-scan --flow=differ-ci --fingerprint=0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0 --output=json": "attestations/cyber-dojo/differ-ci/artifact/0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0/snyk-container-scan",
    "kosli list artifacts --flow=differ-ci --output=json": "artifacts/cyber-dojo/differ-ci",
    "kosli get artifact differ-ci@0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0 --output=json": "artifacts/cyber-dojo/differ-ci/fingerprint/0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0",
    "kosli list attestation-types --output=json": "custom-attestation-types/cyber-dojo",
    "kosli get attestation-type single-snyk-vuln --output=json": "custom-attestation-types/cyber-dojo/single-snyk-vuln",
    "kosli list policies --output=json": "policies/cyber-dojo",
    "kosli get policy artifact-provenance --output=json": "policies/cyber-dojo/artifact-provenance",
}


def all_query_entries():
    """Yield each query command in _QUERIES."""
    yield from _QUERIES


def has_query_entry(command):
    """Return True if command is a known live query entry."""
    return command in _QUERIES


def query_url(command):
    """Return the Kosli API path for the given query command."""
    return _QUERIES[command]
