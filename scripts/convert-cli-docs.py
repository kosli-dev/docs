#!/usr/bin/env python3
"""
Convert Hugo-format CLI reference markdown files to Mintlify format.

Usage:
    python scripts/convert-cli-docs.py --input-dir staging/ --output-dir client_reference/
"""

import argparse
import os
import re
import sys
import yaml


def parse_hugo_frontmatter(content):
    """Extract YAML front matter and body from Hugo markdown."""
    match = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not match:
        return {}, content
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        fm = {}
    return fm or {}, match.group(2)


def convert_frontmatter(fm):
    """Convert Hugo front matter to Mintlify format."""
    new_fm = {}
    if 'title' in fm:
        new_fm['title'] = fm['title']
    if 'summary' in fm:
        new_fm['description'] = fm['summary'].strip()
    elif 'description' in fm:
        new_fm['description'] = fm['description'].strip()
    # Sanitize description for MDX compatibility
    if 'description' in new_fm:
        desc = new_fm['description']
        # Remove caret-delimited code references (Hugo convention)
        desc = re.sub(r'\^([^^]+)\^', r'`\1`', desc)
        # Use only the first sentence if description is very long
        # (long descriptions with special chars cause MDX parsing issues)
        if len(desc) > 200:
            first_sentence = re.match(r'^[^.!?]+[.!?]\s*', desc)
            if first_sentence:
                desc = first_sentence.group(0).strip()
        new_fm['description'] = desc
    # deprecated flag is preserved for nav grouping but not in front matter
    return new_fm, fm.get('deprecated', False)


def convert_hints(body):
    """Convert Hugo hint shortcodes to Mintlify components."""
    # Handle both {{% hint type %}} and {{<hint type>}} variants
    hint_map = {
        'info': 'Info',
        'warning': 'Warning',
        'danger': 'Warning',
        'success': 'Tip',
    }
    for hugo_type, mintlify_tag in hint_map.items():
        # {{% hint type %}} ... {{% /hint %}}
        pattern = (
            r'\{{% hint ' + hugo_type + r' %\}\}(.*?)\{{% /hint %\}\}'
        )
        body = re.sub(
            pattern,
            lambda m, tag=mintlify_tag: f'<{tag}>\n{m.group(1).strip()}\n</{tag}>',
            body,
            flags=re.DOTALL,
        )
        # {{<hint type>}} ... {{</hint>}} (no spaces/percent variant)
        pattern = r'\{\{<\s*hint\s+' + hugo_type + r'\s*>\}\}(.*?)\{\{<\s*/hint\s*>\}\}'
        body = re.sub(
            pattern,
            lambda m, tag=mintlify_tag: f'<{tag}>\n{m.group(1).strip()}\n</{tag}>',
            body,
            flags=re.DOTALL,
        )
    return body


def convert_tabs(body):
    """Convert Hugo tabs shortcodes to Mintlify Tabs/Tab components.

    Mintlify MDX requires Tabs/Tab components on their own lines with
    proper spacing, not inline.
    """
    # Match {{< tabs "id" "class" >}} or {{< tabs "id" >}}
    body = re.sub(
        r'\{\{<\s*tabs\s+"[^"]*"(?:\s+"[^"]*")?\s*>\}\}',
        '\n<Tabs>',
        body,
    )
    body = re.sub(r'\{\{<\s*/tabs\s*>\}\}', '\n</Tabs>', body)

    # Match {{< tab "Title" >}} → <Tab title="Title">
    body = re.sub(
        r'\{\{<\s*tab\s+"([^"]+)"\s*>\}\}',
        r'\n\t<Tab title="\1">\n',
        body,
    )
    body = re.sub(r'\{\{<\s*/tab\s*>\}\}', '\n\t</Tab>', body)
    return body


def convert_figures(body):
    """Convert Hugo figure shortcodes to Mintlify Frame/img."""
    # {{< figure src="..." alt="..." width="..." >}} or {{<figure ...>}}
    def replace_figure(m):
        attrs = m.group(1)
        src = re.search(r'src="([^"]+)"', attrs)
        alt = re.search(r'alt="([^"]+)"', attrs)
        src_str = src.group(1) if src else ''
        alt_str = alt.group(1) if alt else ''
        return f'<Frame>\n  <img src="{src_str}" alt="{alt_str}" />\n</Frame>'

    body = re.sub(
        r'\{\{<\s*figure\s+(.*?)\s*>\}\}',
        replace_figure,
        body,
    )
    return body


def strip_code_fence_classes(body):
    """Remove Hugo-specific classes from code fences."""
    # ```shell {.command} → ```shell
    body = re.sub(r'```(\w+)\s+\{[^}]*\}', r'```\1', body)
    return body


def strip_cli_version(body):
    """Replace {{< cli-version >}} with a placeholder."""
    body = re.sub(r'\{\{<\s*cli-version\s*>\}\}', 'CLI_VERSION', body)
    return body


def strip_ref_shortcodes(body):
    """Convert Hugo ref shortcodes to plain paths."""
    # {{< ref "/some/path" >}} → /some/path
    body = re.sub(r'\{\{<\s*ref\s+"([^"]+)"\s*>\}\}', r'\1', body)
    # {{% ref "/some/path" %}} variant
    body = re.sub(r'\{{% ref "([^"]+)" %\}\}', r'\1', body)
    return body


def remove_duplicate_title(body, title):
    """Remove the first # heading if it matches the front matter title."""
    pattern = r'^\s*#\s+' + re.escape(title) + r'\s*\n'
    body = re.sub(pattern, '', body, count=1)
    return body


def remove_html_comments(body):
    """Remove HTML comments."""
    body = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    return body


def fix_internal_links(body):
    """Remove trailing slashes from internal links and strip domain."""
    # Remove docs.kosli.com domain from links
    body = re.sub(
        r'https://docs\.kosli\.com(/[^)\s]*)',
        r'\1',
        body,
    )
    # Remove trailing slashes from internal link paths
    body = re.sub(r'\]\((/[^)]+?)/\)', r'](\1)', body)
    return body


def convert_examples_to_accordions(body):
    """Convert ##### example headings to Accordion components."""
    # Find sections with ##### headings followed by code blocks
    lines = body.split('\n')
    result = []
    in_examples_section = False
    in_accordion_group = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect "## Examples Use Cases" or similar section
        if re.match(r'^##\s+Examples?\s+Use\s+Cases?', line):
            in_examples_section = True
            result.append(line)
            i += 1
            continue

        # New ## section ends examples
        if in_examples_section and re.match(r'^##\s+', line) and not re.match(r'^##\s+Examples?', line):
            if in_accordion_group:
                result.append('</AccordionGroup>')
                in_accordion_group = False
            in_examples_section = False
            result.append(line)
            i += 1
            continue

        if in_examples_section and re.match(r'^#{5}\s+', line):
            heading_text = re.sub(r'^#{5}\s+', '', line).strip()
            if not in_accordion_group:
                result.append('<AccordionGroup>')
                in_accordion_group = True
            result.append(f'\t<Accordion title="{heading_text}">')
            result.append('')
            i += 1
            # Collect content until next ##### or ## or end
            while i < len(lines):
                if re.match(r'^#{2,5}\s+', lines[i]):
                    break
                result.append('\t' + lines[i])
                i += 1
            result.append('\t</Accordion>')
            continue

        result.append(line)
        i += 1

    if in_accordion_group:
        result.append('</AccordionGroup>')

    return '\n'.join(result)


def convert_live_examples(body):
    """Convert the live examples tabs section to Mintlify format."""
    # The Hugo format uses inline tabs; we already converted them in convert_tabs
    # Just ensure proper formatting with newlines
    return body


def convert_raw_html(body):
    """Convert Hugo raw-html shortcodes to plain HTML content."""
    body = re.sub(r'\{\{<\s*/?\s*raw-html\s*>\}\}', '', body)
    return body


def escape_jsx_in_prose(body):
    """Escape angle brackets and curly braces that MDX would interpret as JSX.

    Only escapes in prose content — skips code blocks and front matter.
    """
    lines = body.split('\n')
    result = []
    in_code = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            result.append(line)
            continue
        if in_code:
            result.append(line)
            continue

        # Skip lines that are actual MDX component tags
        if re.match(r'^\s*</?(?:Tabs|Tab|Accordion|AccordionGroup|Info|Warning|Tip|Note|Frame|img)\b', stripped):
            result.append(line)
            continue

        # Escape {{ expression }} double-curly patterns first (e.g. {{ github.head_ref }})
        line = re.sub(r'\{\{([^}]+)\}\}', r'\\{\\{\1\\}\\}', line)

        # Escape {expression} patterns outside code blocks
        # Must run BEFORE angle bracket escaping so patterns like
        # {N.<hours|days>.ago} are handled as a unit.
        # But NOT inside backtick-delimited inline code.
        segments = re.split(r'(`[^`]+`)', line)
        for idx, seg in enumerate(segments):
            if idx % 2 == 0:  # Not inside backticks
                seg = re.sub(
                    r'(?<!\\)\{(?!\{)([^}]+)\}(?!\})',
                    r'\\{\1\\}',
                    seg,
                )
            segments[idx] = seg
        line = ''.join(segments)

        # Escape <PLACEHOLDER> patterns (any words/pipes in angle brackets
        # that look like placeholders, not real HTML)
        line = re.sub(r'<([A-Z][A-Z_0-9|]+)>', r'`\1`', line)
        # Also match lowercase placeholders like <fingerprint>, <commit_sha>,
        # <hours|days|weeks|months>
        html_tags = {
            'a', 'br', 'pre', 'code', 'em', 'strong', 'p', 'div',
            'span', 'ul', 'ol', 'li', 'img', 'table', 'tr', 'td',
            'th', 'thead', 'tbody', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        }
        line = re.sub(
            r'<([a-z][a-z_0-9|]+)>',
            lambda m: f'`{m.group(1)}`' if m.group(1) not in html_tags else m.group(0),
            line,
        )

        # Clean up adjacent backticks from consecutive replacements: `` → (space)
        line = re.sub(r'``', '` `', line)

        # Escape <vN.N.N pattern (version references like <v2.8.2)
        line = re.sub(r'<(v\d+\.\d+)', r'\\<\1', line)

        result.append(line)

    return '\n'.join(result)


def convert_file(input_path):
    """Convert a single Hugo CLI reference file to Mintlify format.

    Returns (content, is_deprecated) tuple.
    """
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = parse_hugo_frontmatter(content)
    new_fm, is_deprecated = convert_frontmatter(fm)

    if not new_fm.get('title'):
        return None, False

    # Apply conversions
    body = remove_duplicate_title(body, new_fm['title'])
    body = remove_html_comments(body)
    body = convert_hints(body)
    body = convert_tabs(body)
    body = convert_figures(body)
    body = convert_raw_html(body)
    body = strip_code_fence_classes(body)
    body = strip_cli_version(body)
    body = strip_ref_shortcodes(body)
    body = fix_internal_links(body)
    body = convert_examples_to_accordions(body)
    body = convert_live_examples(body)
    body = escape_jsx_in_prose(body)

    # Clean up excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)

    # Build output
    fm_lines = ['---']
    fm_lines.append(f'title: "{new_fm["title"]}"')
    if 'description' in new_fm:
        desc = new_fm['description'].replace('"', '\\"')
        fm_lines.append(f'description: "{desc}"')
    fm_lines.append('---')

    output = '\n'.join(fm_lines) + '\n' + body.strip() + '\n'
    return output, is_deprecated


def main():
    parser = argparse.ArgumentParser(
        description='Convert Hugo CLI docs to Mintlify format'
    )
    parser.add_argument(
        '--input-dir',
        required=True,
        help='Directory containing Hugo-format CLI markdown files',
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Output directory for Mintlify-format files',
    )
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f'Error: Input directory {args.input_dir} does not exist')
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)

    converted = 0
    skipped = 0

    for filename in sorted(os.listdir(args.input_dir)):
        if not filename.endswith('.md'):
            continue
        if filename == '_index.md':
            skipped += 1
            continue

        input_path = os.path.join(args.input_dir, filename)
        output, is_deprecated = convert_file(input_path)

        if output is None:
            skipped += 1
            continue

        output_path = os.path.join(args.output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)

        status = ' [DEPRECATED]' if is_deprecated else ''
        print(f'  Converted: {filename}{status}')
        converted += 1

    print(f'\nDone: {converted} files converted, {skipped} skipped')


if __name__ == '__main__':
    main()
