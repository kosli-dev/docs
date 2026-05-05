#!/usr/bin/env python3
"""
Strip any existing live-docs section from client_reference .md files and
regenerate it with static resolved URLs, driven by _MODIFIERS data.

Usage:
    python scripts/resolve_livedocs.py
    python scripts/resolve_livedocs.py --docs-dir path/to/client_reference/
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from live_docs_modifiers_data import has_command, cis_for, has_trail_event
from live_docs_fetch import yaml_url as _resolve_yaml_url, event_url as _resolve_event_url


_CI_ORDER = ["github", "gitlab"]
_CI_DISPLAY = {"github": "GitHub", "gitlab": "GitLab"}

_FRONTMATTER = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
_TITLE = re.compile(r'^title:\s*"([^"]+)"', re.MULTILINE)
_LIVE_SECTION = re.compile(
    r'## Live Examples in different CI systems\n.*?(?=## |\Z)',
    re.DOTALL,
)


def command_from_text(text):
    """Return the CLI command name from the frontmatter title, or None if not found."""
    fm = _FRONTMATTER.match(text)
    if not fm:
        return None
    title = _TITLE.search(fm.group(1))
    if not title:
        return None
    return title.group(1)


def yaml_url(command, ci):
    """Return the resolved static URL for a YAML live example."""
    return _resolve_yaml_url(command, ci)


def event_url(command, ci):
    """Return the resolved static URL for a Kosli Event live example."""
    return _resolve_event_url(command, ci)


def generate_section(command):
    """Return the full MDX live-docs section string for command."""
    parts = ["## Live Examples in different CI systems\n\n<Tabs>\n"]
    for ci in (ci for ci in _CI_ORDER if ci in list(cis_for(command))):
        display = _CI_DISPLAY[ci]
        parts.append(f'\t<Tab title="{display}">\n')
        parts.append(f'\tView an example of the `{command}` command in {display}.\n\n')
        parts.append(f'\tIn [this YAML file]({yaml_url(command, ci)})')
        if has_trail_event(command, ci):
            resolved_event = event_url(command, ci)
            if resolved_event:
                parts.append(f', which created [this Kosli Event]({resolved_event}).')
        parts.append('\n\t</Tab>\n')
    parts.append('</Tabs>\n\n')
    return ''.join(parts)


def resolve_file(filepath):
    """Strip and regenerate the live-docs section in one file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    command = command_from_text(text)
    if command is None:
        return False

    new_text = _LIVE_SECTION.sub('', text)

    if has_command(command):
        section = generate_section(command)
        if '## Examples Use Cases' in new_text:
            new_text = new_text.replace('## Examples Use Cases', section + '## Examples Use Cases', 1)
        else:
            new_text = new_text.rstrip('\n') + '\n\n' + section

    if new_text == text:
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    return True


def main():
    """Strip and regenerate live-docs sections in all CLI reference markdown files."""
    parser = argparse.ArgumentParser(
        description='Regenerate live-docs sections in CLI reference markdown files',
    )
    parser.add_argument(
        '--docs-dir',
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'client_reference'),
        help='Directory containing CLI reference markdown files (default: client_reference/)',
    )
    args = parser.parse_args()

    docs_dir = os.path.normpath(args.docs_dir)
    if not os.path.isdir(docs_dir):
        print(f'Error: Directory {docs_dir} does not exist', file=sys.stderr)
        sys.exit(1)

    modified = 0
    for filename in sorted(os.listdir(docs_dir)):
        if not filename.endswith('.md'):
            continue
        if resolve_file(os.path.join(docs_dir, filename)):
            print(f'  resolved: {filename}')
            modified += 1

    print(f'{modified} file(s) updated.')


if __name__ == '__main__':
    main()
