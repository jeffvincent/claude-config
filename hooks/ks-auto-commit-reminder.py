#!/usr/bin/env python3
"""
PostToolUse hook: remind Claude to commit and push after accumulating
Knowledge System changes. Fires after Edit, Write, or MultiEdit.

Prints a reminder to stdout (which Claude sees as in-context output)
when there are 3+ uncommitted changes in the Knowledge System repo.
"""

import json
import os
import subprocess
import sys

KS_ROOT = os.path.expanduser("~/Projects/Knowledge System")

# File categories for commit message hints
CATEGORIES = {
    "people/": "people",
    "conversations/": "conversations",
    "notes/management-journal/": "journal",
    "notes/hex-notes/": "hex-notes",
    "notes/running-notes/": "running-notes",
    "notes/content notes/": "content-notes",
    "notes/customer-research/": "customer-research",
    "notes/competitive-intelligence/": "competitive-intel",
    "notes/": "notes",
    "projects/": "projects",
    "resources/": "resources",
    "_system/": "system",
}


def get_file_path(tool_name, tool_input):
    """Extract the file path from tool input."""
    if tool_name in ("Edit", "Write", "MultiEdit"):
        return tool_input.get("file_path", "")
    return ""


def is_ks_file(file_path):
    """Check if this file is in the Knowledge System repo."""
    if not file_path:
        return False
    abs_path = os.path.abspath(os.path.expanduser(file_path))
    ks_abs = os.path.abspath(KS_ROOT)
    return abs_path.startswith(ks_abs)


def categorize_file(rel_path):
    """Categorize a file path into a human-readable category."""
    for prefix, category in CATEGORIES.items():
        if rel_path.startswith(prefix):
            return category
    return "other"


def get_uncommitted_changes():
    """Get uncommitted changes in the Knowledge System repo."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=KS_ROOT,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode != 0:
            return []
        lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
        return lines
    except (subprocess.TimeoutExpired, OSError):
        return []


def parse_changes(lines):
    """Parse git status lines into categories and counts."""
    categories = set()
    for line in lines:
        # git status --porcelain format: XY filename
        # Skip untracked transcript files (those are committed via /process-transcripts)
        path = line[3:].strip().strip('"')
        if path.startswith("_system/transcripts/"):
            continue
        categories.add(categorize_file(path))
    return categories


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    file_path = get_file_path(tool_name, tool_input)
    if not is_ks_file(file_path):
        sys.exit(0)

    changes = get_uncommitted_changes()
    if not changes:
        sys.exit(0)

    # Filter out untracked transcript files from count
    meaningful = [
        l for l in changes
        if not l[3:].strip().strip('"').startswith("_system/transcripts/")
    ]

    if len(meaningful) < 3:
        sys.exit(0)

    categories = parse_changes(meaningful)
    if not categories:
        sys.exit(0)

    cats = ", ".join(sorted(categories))
    print(
        f"[KS Auto-Commit] {len(meaningful)} uncommitted Knowledge System changes "
        f"across: {cats}. Commit and push now."
    )


if __name__ == "__main__":
    main()
