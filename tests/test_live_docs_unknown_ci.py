from live_docs_modifiers_data import backup_yaml_url, lined_yaml_url, raw_yaml_url


def test_f5a3b800():
    """raw_yaml_url returns '' when CI is not github or gitlab."""
    assert raw_yaml_url("any", "circleci", "abc123") == ""


def test_f5a3b801():
    """lined_yaml_url returns '' when CI is not github or gitlab."""
    assert lined_yaml_url("any", "circleci", 1, "abc123") == ""


def test_f5a3b803():
    """backup_yaml_url returns '' when CI is not github or gitlab."""
    assert backup_yaml_url("any", "circleci") == ""
