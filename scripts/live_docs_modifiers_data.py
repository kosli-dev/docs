"""Data table for live-docs modifier (POST) commands.

_MODIFIERS maps CLI commands to per-CI metadata. Each CI entry has:
- yaml: repo, workflow, and backup (commit and line for the fallback YAML URL)
- event: flow, and backup (trail and attestation_id for the fallback event URL)

To audit backup commit ages and check which commands are still present at HEAD:
  docker exec -it test_unit /app/test/scripts/audit_live_docs_backup_commits.py
Both scripts call the GitHub/GitLab APIs unauthenticated (60 req/hour limit).
If dates show as "?" the rate limit has been hit -- wait an hour and retry.

To update stale backup commit SHAs and line numbers to HEAD, run:
  docker exec -i test_unit /app/test/scripts/refresh_live_docs_backup_commits.py > update_live_docs_backup_commits.py
  python3 update_live_docs_backup_commits.py  # run from repo root
Only entries where the command is still present in their workflows at HEAD are updated.
"""


def has_entry(command, ci):
    """Return True if command/ci is a known live-docs entry."""
    return command in _MODIFIERS and ci in _MODIFIERS[command]


def all_entries():
    """Yield (command, ci) for every entry in _MODIFIERS."""
    for command, cis in _MODIFIERS.items():
        for ci in cis:
            yield command, ci


def flow_name(command, ci):
    """Return the Kosli flow name for command/ci, or '' if the command creates no event."""
    return _MODIFIERS[command][ci]["event"]["flow"]


def has_trail_event(command, ci):
    """Return True if command/ci creates a Trail event (i.e. its Kosli flow is non-empty)."""
    return flow_name(command, ci) != ""


def backup_yaml_url(command, ci):
    """Return the fallback YAML URL for command/ci."""
    if ci == "github":
        y = _MODIFIERS[command][ci]["yaml"]
        b = y["backup"]
        return f"https://github.com/cyber-dojo/{y['repo']}/blob/{b['commit']}/{y['workflow']}#L{b['line']}"
    if ci == "gitlab":
        y = _MODIFIERS[command][ci]["yaml"]
        b = y["backup"]
        return f"https://gitlab.com/cyber-dojo/{y['repo']}/-/blob/{b['commit']}/{y['workflow']}#L{b['line']}"
    return ""


def backup_event_url(command, ci):
    """Return the fallback event URL for command/ci."""
    e = _MODIFIERS[command][ci]["event"]
    b = e["backup"]
    if not b["trail"]:
        return ""
    return f"https://app.kosli.com/cyber-dojo/flows/{e['flow']}/trails/{b['trail']}?attestation_id={b['attestation_id']}"


def raw_yaml_url(command, ci, commit_sha):
    """Return the raw content URL for the workflow file at the given commit."""
    if ci == "github":
        y = _MODIFIERS[command][ci]["yaml"]
        return f"https://raw.githubusercontent.com/cyber-dojo/{y['repo']}/{commit_sha}/{y['workflow']}"
    if ci == "gitlab":
        y = _MODIFIERS[command][ci]["yaml"]
        return f"https://gitlab.com/cyber-dojo/{y['repo']}/-/raw/{commit_sha}/{y['workflow']}"
    return ""


def lined_yaml_url(command, ci, line, commit_sha):
    """Return the browser URL pointing to a specific line in the workflow file."""
    if ci == "github":
        y = _MODIFIERS[command][ci]["yaml"]
        return f"https://github.com/cyber-dojo/{y['repo']}/blob/{commit_sha}/{y['workflow']}#L{line}"
    if ci == "gitlab":
        y = _MODIFIERS[command][ci]["yaml"]
        return f"https://gitlab.com/cyber-dojo/{y['repo']}/-/blob/{commit_sha}/{y['workflow']}#L{line}"
    return ""


def repo_directly_corresponds_to_flow(command, ci):
    """Return True if the repo name implies the flow name (repo + '-ci' == flow).

    When True, the git commit is read from the snapshot flow entry.
    When False (e.g. kosli attest artifact, whose YAML is in reusable-actions-workflows
    but whose Trail event is in differ-ci), the HEAD SHA is fetched separately.
    """
    data = _MODIFIERS[command][ci]
    return f"{data['yaml']['repo']}-ci" == data["event"]["flow"]


def repo_name(command, ci):
    """Return the cyber-dojo repo name for command/ci."""
    return _MODIFIERS[command][ci]["yaml"]["repo"]


def has_command(command):
    """Return True if command is a known live-docs command."""
    return command in _MODIFIERS


def cis_for(command):
    """Yield all CI names registered for command."""
    yield from _MODIFIERS[command]


_MODIFIERS = {
    # kosli attest artifact and kosli attest snyk are special, in GitHub,
    # as they appear in reusable workflows, called FROM the main differ workflow,
    # and NOT in the main differ workflow itself.
    # So the URL for the workflow yaml is NOT for the differ repo, it is the HEAD
    # of the target repo. But the URL for the Kosli Trail event IS in the differ Trail,
    # and this is as designed.
    "kosli attest artifact": {
        "github": {
            "yaml": {
                "repo": "reusable-actions-workflows",
                "workflow": ".github/workflows/secure-docker-build.yml",
                "backup": {
                    "commit": "25f0b797c18403de1c8490a9a71bbe9789c809a9",
                    "line": 210,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "2e482ef95263c81570a82f0456b026e29203d550",
                    "attestation_id": "1386703c-8d8f-47cf-a03e-d6a3328b",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 111,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "attestation_id": "e2345d6b-2220-414a-9bb1-26ab8e26",
                },
            },
        },
    },
    "kosli attest snyk": {
        "github": {
            "yaml": {
                "repo": "snyk-container-test",
                "workflow": "action.yml",
                "backup": {
                    "commit": "43373102aa2abee72027e2aba050adea9fdb0173",
                    "line": 70,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "2e482ef95263c81570a82f0456b026e29203d550",
                    "attestation_id": "c4d17fb4-05d2-4894-bca7-f21e56ab",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "line": 146,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "attestation_id": "3e9cd5ee-4fd3-403f-ba59-6d431dec",
                },
            },
        },
    },
    # Then we have commands that do NOT have a corresponding trail event
    "kosli create attestation-type": {
        "github": {
            "yaml": {
                "repo": "kosli-attestation-types",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "7ad343982d42654fdf4cf123c5e7aec44af8e1a7",
                    "line": 56,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        }
    },
    "kosli create flow": {
        "github": {
            "yaml": {
                "repo": "runner",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
                    "line": 71,
                },
            },
            "event": {
                "flow": "runner-ci",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 53,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    "kosli begin trail": {
        "github": {
            "yaml": {
                "repo": "runner",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "bcf912346ae0a104698da4560e82d5eb277fc0e9",
                    "line": 78,
                },
            },
            "event": {
                "flow": "runner-ci",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 55,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    "kosli tag": {
        "github": {
            "yaml": {
                "repo": "aws-prod-co-promotion",
                "workflow": ".github/workflows/promote_one.yml",
                "backup": {
                    "commit": "87f1f819ee6eaaf1f811259b0778f5e0cff7a0fa",
                    "line": 74,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "48bdbd3b059d45489e8ae5f9f680f48bc6201ad8",
                    "line": 52,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    "kosli fingerprint": {
        "github": {
            "yaml": {
                "repo": "snyk-scanning",
                "workflow": ".github/workflows/artifact_snyk_test.yml",
                "backup": {
                    "commit": "9cc4c900ed581834931a9596a49b5033b7ffa12f",
                    "line": 177,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        }
    },
    "kosli assert artifact": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 329,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 153,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    "kosli report approval": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 358,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "48bdbd3b059d45489e8ae5f9f680f48bc6201ad8",
                    "line": 200,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    "kosli evaluate trail": {
        "github": {
            "yaml": {
                "repo": "snyk-scanning",
                "workflow": ".github/workflows/artifact_snyk_test.yml",
                "backup": {
                    "commit": "9cc4c900ed581834931a9596a49b5033b7ffa12f",
                    "line": 325,
                },
            },
            "event": {
                "flow": "",
                "backup": {
                    "trail": "",
                    "attestation_id": "",
                },
            },
        },
    },
    # Lastly we have commands that DO create events in a Trail.
    "kosli attest custom": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 265,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "ed88bbeb6e93195d2d8447a69b93431969cc71db",
                    "attestation_id": "4af90662-7e2d-4948-b149-c24f9350",
                },
            },
        }
    },
    "kosli attest junit": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 250,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "ed88bbeb6e93195d2d8447a69b93431969cc71db",
                    "attestation_id": "f54eae29-61cb-4b27-897a-4296a6a2",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 126,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "attestation_id": "dbee2e2c-6397-402f-ae76-267d9fba",
                },
            },
        },
    },
    "kosli attest pullrequest github": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 95,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "ed88bbeb6e93195d2d8447a69b93431969cc71db",
                    "attestation_id": "c8f9c24c-b9d5-4659-8cd6-3121ef9a",
                },
            },
        },
    },
    "kosli attest pullrequest gitlab": {
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 75,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "attestation_id": "2f796a5f-3c49-496f-be16-6faae913",
                },
            },
        },
    },
    "kosli attest sonar": {
        "github": {
            "yaml": {
                "repo": "dashboard",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
                    "line": 166,
                },
            },
            "event": {
                "flow": "dashboard-ci",
                "backup": {
                    "trail": "678e0d67225f16adc9c76596161b673f6eb4ba68",
                    "attestation_id": "82383544-ed40-496a-a0e1-ed1f5cc8",
                },
            },
        },
    },
    "-Dsonar.analysis.kosli_flow": {
        "github": {
            "yaml": {
                "repo": "differ",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "30dffd09c3f896a322c65029247abcea3019c43a",
                    "line": 292,
                },
            },
            "event": {
                "flow": "differ-ci",
                "backup": {
                    "trail": "12fae04cac4bce5bd7a561d86557ed3122dda2d1",
                    "attestation_id": "a0ef02d8-b373-450a-98a8-e3931b4b",
                },
            },
        },
    },
    "kosli attest generic": {
        "github": {
            "yaml": {
                "repo": "dashboard",
                "workflow": ".github/workflows/main.yml",
                "backup": {
                    "commit": "a6ece2b597888f7ab149759daadda08e3afab0c1",
                    "line": 249,
                },
            },
            "event": {
                "flow": "dashboard-ci",
                "backup": {
                    "trail": "44ca5fa2630947cf375fdbda10972a4bedaaaba3",
                    "attestation_id": "6a99303c-b7b3-4f4a-b576-9cdacc1d",
                },
            },
        },
        "gitlab": {
            "yaml": {
                "repo": "creator",
                "workflow": ".gitlab/workflows/main.yml",
                "backup": {
                    "commit": "65fd2bfa2478534ea4bc5ccf30f6bfc6aab7550c",
                    "line": 131,
                },
            },
            "event": {
                "flow": "creator-ci",
                "backup": {
                    "trail": "a184b5b7d2053ce2b2f7064bf46f0b6f72f9f393",
                    "attestation_id": "7befb7ac-ddcf-4e89-a3d7-558eb0c5",
                },
            },
        },
    }
}
