#!/usr/bin/env python3
"""
Update the CLI Reference navigation in docs.json based on files in client_reference/.

Usage:
    python scripts/update-cli-nav.py --docs-dir client_reference/ --config docs.json
"""

import argparse
import json
import os
import re
import sys
import yaml


def get_command_info(filepath):
    """Extract command name and deprecated status from a CLI reference file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

    if not fm or 'title' not in fm:
        return None

    title = fm['title']
    deprecated = fm.get('deprecated', False)

    # Check for deprecated warning in body (for converted files that don't have
    # the deprecated field but have a Warning about deprecation)
    if not deprecated:
        body = content[match.end():]
        if re.search(r'is deprecated', body[:500], re.IGNORECASE):
            deprecated = True

    return {
        'title': title,
        'deprecated': deprecated,
    }


def get_command_group(title):
    """Determine the logical group for a CLI command based on its name."""
    # Remove 'kosli ' prefix
    cmd = title.replace('kosli ', '').strip()

    if cmd == '':
        return 'General'

    # Top-level commands (no subcommand)
    parts = cmd.split(' ')
    if len(parts) == 1:
        # Single-word commands like 'search', 'version', 'status', etc.
        return 'General'

    # Group by first word for multi-word commands
    group_word = parts[0]

    group_map = {
        'allow': 'allow',
        'archive': 'archive',
        'assert': 'assert',
        'attach': 'attach / detach',
        'attest': 'attest',
        'begin': 'begin',
        'completion': 'General',
        'config': 'General',
        'create': 'create',
        'detach': 'attach / detach',
        'diff': 'diff',
        'disable': 'disable / enable',
        'enable': 'disable / enable',
        'expect': 'expect',
        'get': 'get',
        'join': 'join',
        'list': 'list',
        'log': 'log',
        'rename': 'rename',
        'report': 'report',
        'request': 'request',
        'search': 'General',
        'snapshot': 'snapshot',
        'tag': 'General',
    }

    return group_map.get(group_word, group_word)


def build_nav_groups(docs_dir):
    """Scan CLI reference files and build navigation groups."""
    commands = []

    for filename in sorted(os.listdir(docs_dir)):
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(docs_dir, filename)
        info = get_command_info(filepath)
        if info is None:
            continue

        page_path = f'client_reference/{filename[:-3]}'  # Remove .md
        commands.append({
            'page': page_path,
            'title': info['title'],
            'deprecated': info['deprecated'],
            'group': get_command_group(info['title']),
        })

    # Separate active and deprecated commands
    active = [c for c in commands if not c['deprecated']]
    deprecated = [c for c in commands if c['deprecated']]

    # Group active commands
    groups_dict = {}
    for cmd in active:
        group = cmd['group']
        if group not in groups_dict:
            groups_dict[group] = []
        groups_dict[group].append(cmd['page'])

    # Build ordered navigation groups
    # Put General first, then alphabetical
    nav_groups = []

    if 'General' in groups_dict:
        nav_groups.append({
            'group': 'General',
            'pages': groups_dict.pop('General'),
        })

    for group_name in sorted(groups_dict.keys()):
        display_name = f'kosli {group_name}'
        nav_groups.append({
            'group': display_name,
            'pages': groups_dict[group_name],
        })

    # Add deprecated group if there are deprecated commands
    if deprecated:
        nav_groups.append({
            'group': 'Deprecated',
            'pages': [c['page'] for c in deprecated],
        })

    return nav_groups


def update_docs_json(config_path, nav_groups):
    """Update the CLI Reference section in docs.json."""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Find the Reference tab and CLI Reference menu item
    for product in config.get('navigation', {}).get('products', []):
        for tab in product.get('tabs', []):
            if tab.get('tab') == 'Reference':
                menu = tab.get('menu', [])
                for item in menu:
                    if item.get('item') == 'CLI Reference':
                        item['groups'] = nav_groups
                        break
                else:
                    # CLI Reference not found, add it
                    menu.insert(0, {
                        'item': 'CLI Reference',
                        'icon': 'terminal',
                        'groups': nav_groups,
                    })
                break

    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write('\n')

    print(f'Updated {config_path} with {len(nav_groups)} CLI groups')


def main():
    parser = argparse.ArgumentParser(
        description='Update CLI Reference navigation in docs.json'
    )
    parser.add_argument(
        '--docs-dir',
        required=True,
        help='Directory containing CLI reference markdown files',
    )
    parser.add_argument(
        '--config',
        required=True,
        help='Path to docs.json config file',
    )
    args = parser.parse_args()

    if not os.path.isdir(args.docs_dir):
        print(f'Error: Directory {args.docs_dir} does not exist')
        sys.exit(1)

    if not os.path.isfile(args.config):
        print(f'Error: Config file {args.config} does not exist')
        sys.exit(1)

    nav_groups = build_nav_groups(args.docs_dir)

    for group in nav_groups:
        print(f"  {group['group']}: {len(group['pages'])} pages")

    update_docs_json(args.config, nav_groups)


if __name__ == '__main__':
    main()
