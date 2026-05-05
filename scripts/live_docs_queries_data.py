"""Data table for live-docs query (GET) commands.

_QUERIES maps full query-style CLI commands to the corresponding Kosli API v2 path.
_CLI_COMMANDS maps command names (as they appear in md file frontmatter titles) to
the corresponding full command string in _QUERIES.
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

_CLI_COMMANDS = {
    "kosli list environments": "kosli list environments --output=json",
    "kosli get environment":   "kosli get environment aws-prod --output=json",
    "kosli log environment":   "kosli log environment aws-prod --output=json",
    "kosli list snapshots":    "kosli list snapshots aws-prod --output=json",
    "kosli get snapshot":      "kosli get snapshot aws-prod --output=json",
    "kosli diff snapshots":    "kosli diff snapshots aws-beta aws-prod --output=json",
    "kosli list flows":        "kosli list flows --output=json",
    "kosli get flow":          "kosli get flow dashboard-ci --output=json",
    "kosli get trail":         "kosli get trail dashboard-ci 1159a6f1193150681b8484545150334e89de6c1c --output=json",
    "kosli get attestation":   "kosli get attestation snyk-container-scan --flow=differ-ci --fingerprint=0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0 --output=json",
}


def has_cli_command(command):
    """Return True if command (a short command name) has a live CLI query entry."""
    return command in _CLI_COMMANDS


def full_command(command):
    """Return the full command string in _QUERIES for the given short command name."""
    return _CLI_COMMANDS[command]


def api_path(full_cmd):
    """Return the Kosli API v2 path for the given full command string."""
    return _QUERIES[full_cmd]
