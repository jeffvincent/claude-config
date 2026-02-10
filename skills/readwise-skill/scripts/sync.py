#!/usr/bin/env python3
"""
Sync an existing source document with new highlights from Readwise.

Usage:
    python3 sync.py --filepath "/path/to/source.md"
"""

import sys
import json
import argparse
import re
from pathlib import Path
from import_item import get_book_details, get_highlights, generate_markdown
from readwise_client import ReadwiseClient

def extract_book_id(filepath):
    """Extract Readwise book ID from an existing source document."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for Readwise Book ID in the Source Information section
        match = re.search(r'\*\*Readwise Book ID\*\*:\s*(\d+)', content)
        if match:
            return match.group(1)

        return None

    except Exception as e:
        raise Exception(f"Failed to read source document: {str(e)}")

def count_highlights_in_file(filepath):
    """Count how many highlights are currently in the file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count "### Highlight" sections
        matches = re.findall(r'^### Highlight \d+', content, re.MULTILINE)
        return len(matches)

    except Exception:
        return 0

def sync_document(client, filepath):
    """Sync an existing source document with new highlights."""
    # Extract book ID from existing file
    book_id = extract_book_id(filepath)
    if not book_id:
        return {
            "success": False,
            "message": "Could not find Readwise Book ID in source document. "
                       "Make sure this is a valid Readwise source document."
        }

    # Count existing highlights
    old_count = count_highlights_in_file(filepath)

    # Get fresh data from Readwise
    book = get_book_details(client, book_id)
    highlights = get_highlights(client, book_id)

    new_count = len(highlights)

    # Generate updated markdown
    content = generate_markdown(book, highlights)

    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    added = new_count - old_count

    return {
        "success": True,
        "filepath": str(filepath),
        "title": book.get('title'),
        "author": book.get('author'),
        "old_count": old_count,
        "new_count": new_count,
        "added": added,
        "message": f"Updated: {added} new highlight(s)" if added > 0 else "No new highlights"
    }

def main():
    parser = argparse.ArgumentParser(
        description="Sync a Readwise source document with new highlights"
    )
    parser.add_argument(
        '--filepath',
        required=True,
        help='Path to the existing source document'
    )

    args = parser.parse_args()

    try:
        client = ReadwiseClient()
        result = sync_document(client, args.filepath)

        print(json.dumps(result, indent=2))
        return 0 if result["success"] else 1

    except Exception as e:
        print(json.dumps({
            "success": False,
            "error": str(e)
        }), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
