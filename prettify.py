"""
Django Template Prettifier
===========================
IMPORTANT: This script is SAFE for Django templates.
It fixes split template tags WITHOUT breaking them.

Usage: python prettify.py [file_path]
If no file_path is given, it processes all HTML files in templates/
"""

import os
import re
import sys


def fix_django_tags(content):
    """
    Fix Django template tags that have been split across multiple lines.
    This is the ONLY safe formatting operation for Django templates.
    
    Examples of what this fixes:
        {% trans "Hello
            World" %}  ->  {% trans "Hello World" %}
        
        {% url 'home'
            %}  ->  {% url 'home' %}
    """
    def normalize_tag(match):
        tag = match.group(0)
        # Collapse internal whitespace (including newlines) into single spaces
        if tag.startswith('{%'):
            inner = tag[2:-2].strip()
            normalized = ' '.join(inner.split())
            return '{%- ' + normalized + ' -%}' if tag.startswith('{%-') else '{% ' + normalized + ' %}'
        elif tag.startswith('{{'):
            inner = tag[2:-2].strip()
            normalized = ' '.join(inner.split())
            return '{{ ' + normalized + ' }}'
        return tag

    # Match {% ... %} and {{ ... }} across multiple lines (non-greedy)
    content = re.sub(r'\{%.*?%\}', normalize_tag, content, flags=re.DOTALL)
    content = re.sub(r'\{\{.*?\}\}', normalize_tag, content, flags=re.DOTALL)
    
    return content


def prettify_template(file_path):
    """Process a single template file."""
    if not os.path.exists(file_path):
        print(f"  File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    fixed = fix_django_tags(original)
    
    if fixed != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"  FIXED: {file_path}")
        return True
    else:
        print(f"  OK: {file_path} (no changes needed)")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Process specific file
        prettify_template(sys.argv[1])
    else:
        # Process all HTML files in templates/
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        if os.path.isdir(templates_dir):
            count = 0
            for fname in sorted(os.listdir(templates_dir)):
                if fname.endswith('.html'):
                    if prettify_template(os.path.join(templates_dir, fname)):
                        count += 1
            print(f"\nDone. Fixed {count} file(s).")
        else:
            print(f"Templates directory not found: {templates_dir}")
