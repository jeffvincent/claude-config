#!/usr/bin/env python3
"""
PostToolUse hook: suggest wiki-links after writing/editing a .md note in the Knowledge System.
Fires after Edit, Write, or MultiEdit tool calls.
Prints suggestions to stdout, which Claude sees as in-context output.
"""

import json
import os
import re
import sys

KS_NOTES = os.path.expanduser("~/Projects/Knowledge System/notes")
KS_ROOT = os.path.expanduser("~/Projects/Knowledge System")

# Tags to skip for link suggestions (too generic to be meaningful)
GENERIC_TAGS = {
    "strategy", "leadership", "product", "ai", "work", "notes", "thinking",
    "note", "synthesis", "seed", "developing", "mature", "note-type",
}


def get_file_path(tool_name, tool_input):
    """Extract the file path from tool input."""
    if tool_name in ("Edit", "Write"):
        return tool_input.get("file_path", "")
    elif tool_name == "MultiEdit":
        return tool_input.get("file_path", "")
    return ""


def is_ks_note(file_path):
    """Check if this is a .md file in the Knowledge System notes directory."""
    if not file_path.endswith(".md"):
        return False
    abs_path = os.path.abspath(file_path)
    ks_notes_abs = os.path.abspath(KS_NOTES)
    # Also check conversations/ and project notes
    ks_root_abs = os.path.abspath(KS_ROOT)

    # Include notes/ but exclude management-journal, hex-notes (logs not concept nodes)
    if abs_path.startswith(ks_notes_abs):
        rel = os.path.relpath(abs_path, ks_notes_abs)
        excluded = ("management-journal", "hex-notes", "transcripts")
        if any(rel.startswith(e) for e in excluded):
            return False
        return True
    return False


def extract_tags(file_path):
    """Extract frontmatter tags from a markdown file."""
    try:
        with open(file_path, "r") as f:
            content = f.read(2000)  # Only need frontmatter
    except (OSError, IOError):
        return set()

    # Look for YAML frontmatter
    if not content.startswith("---"):
        return set()

    end = content.find("\n---", 3)
    if end == -1:
        return set()

    frontmatter = content[3:end]

    # Extract tags field: tags: [a, b, c] or tags:\n  - a\n  - b
    tags = set()

    # Inline array: tags: [foo, bar, baz]
    m = re.search(r'^tags:\s*\[([^\]]+)\]', frontmatter, re.MULTILINE)
    if m:
        for tag in re.split(r'[,\s]+', m.group(1)):
            tag = tag.strip().strip('"\'')
            if tag and tag not in GENERIC_TAGS:
                tags.add(tag.lower())

    # YAML list: tags:\n  - foo
    m = re.search(r'^tags:\s*\n((?:\s*-\s*.+\n?)+)', frontmatter, re.MULTILINE)
    if m:
        for line in m.group(1).split('\n'):
            tag = line.strip().lstrip('- ').strip().strip('"\'')
            if tag and tag not in GENERIC_TAGS:
                tags.add(tag.lower())

    return tags


def count_wikilinks(file_path):
    """Count existing [[wiki-links]] in a file."""
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return len(re.findall(r'\[\[', content))
    except (OSError, IOError):
        return 0


def find_related_notes(tags, current_file):
    """Find vault notes that share 2+ specific tags with the current file."""
    if not tags:
        return []

    matches = []
    current_abs = os.path.abspath(current_file)

    # Search notes/ and syntheses
    search_dirs = [
        KS_NOTES,
        os.path.join(KS_ROOT, "conversations"),
    ]

    for search_dir in search_dirs:
        if not os.path.isdir(search_dir):
            continue
        for root, dirs, files in os.walk(search_dir):
            # Skip excluded dirs
            dirs[:] = [d for d in dirs if d not in ("management-journal", "hex-notes", "transcripts", ".git")]
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(root, fname)
                if os.path.abspath(fpath) == current_abs:
                    continue

                other_tags = extract_tags(fpath)
                if not other_tags:
                    continue

                overlap = tags & other_tags
                if len(overlap) >= 2:
                    # Score by overlap count
                    stem = os.path.splitext(fname)[0]
                    matches.append((len(overlap), stem, fpath))

    # Sort by overlap count (desc), take top 3
    matches.sort(reverse=True)
    return matches[:3]


def already_linked(file_path, target_stem):
    """Check if target is already wiki-linked in file."""
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return f"[[{target_stem}" in content or f"[[{target_stem}]]" in content
    except (OSError, IOError):
        return True  # Assume linked to avoid false positives


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    file_path = get_file_path(tool_name, tool_input)
    if not file_path:
        sys.exit(0)

    # Expand ~ if needed
    file_path = os.path.expanduser(file_path)

    if not is_ks_note(file_path):
        sys.exit(0)

    tags = extract_tags(file_path)
    if not tags:
        sys.exit(0)

    # Skip if file already has several wiki-links (already well-connected)
    if count_wikilinks(file_path) >= 5:
        sys.exit(0)

    matches = find_related_notes(tags, file_path)
    if not matches:
        sys.exit(0)

    # Filter out already-linked notes
    new_links = [
        (score, stem, fpath)
        for score, stem, fpath in matches
        if not already_linked(file_path, stem)
    ]

    if not new_links:
        sys.exit(0)

    fname = os.path.basename(file_path)
    suggestions = ", ".join(f"[[{stem}]]" for _, stem, _ in new_links)
    print(f"[KS Link Suggestions] {fname} shares tags with: {suggestions}. Consider adding these wiki-links.")


if __name__ == "__main__":
    main()
