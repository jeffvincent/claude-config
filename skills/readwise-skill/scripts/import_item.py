#!/usr/bin/env python3
"""
Import a book/article from Readwise into Content Notes as a source document.

Usage:
    python3 import_item.py --book-id 12345 --output-dir "/path/to/Content Notes/sources"
"""

import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from readwise_client import ReadwiseClient

def get_book_details(client, book_id):
    """Get book/document details from Readwise."""
    try:
        return client.get(f'/books/{book_id}/')
    except Exception as e:
        raise Exception(f"Failed to get book details: {str(e)}")

def get_highlights(client, book_id):
    """Get all highlights for a book."""
    try:
        return client.get_paginated(f'/highlights/', {'book_id': book_id})
    except Exception as e:
        raise Exception(f"Failed to get highlights: {str(e)}")

def sanitize_filename(text):
    """Convert text to a safe filename."""
    # Remove or replace problematic characters
    safe = text.replace('/', '-').replace('\\', '-').replace(':', '-')
    safe = safe.replace('?', '').replace('*', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
    # Limit length
    return safe[:100].strip()

def format_highlight_location(highlight):
    """Format the location/position of a highlight."""
    location = highlight.get('location')
    location_type = highlight.get('location_type')

    if not location:
        return "Location unknown"

    if location_type == 'page':
        return f"Page {location}"
    elif location_type == 'order':
        return f"Position {location}"
    else:
        return f"Location {location}"

def generate_markdown(book, highlights):
    """Generate markdown content for the source document."""
    # Extract book metadata
    title = book.get('title', 'Untitled')
    author = book.get('author', 'Unknown')
    category = book.get('category', 'unknown')
    source = book.get('source', 'unknown')
    source_url = book.get('source_url', '')
    cover_url = book.get('cover_image_url', '')
    num_highlights = book.get('num_highlights', len(highlights))
    document_note = book.get('document_note', '')
    tags = book.get('tags', [])

    # Format date
    today = datetime.now().strftime('%Y-%m-%d')

    # Sort highlights by location (chronological order)
    sorted_highlights = sorted(
        highlights,
        key=lambda h: (h.get('location') or 0, h.get('highlighted_at') or '')
    )

    # Generate markdown
    lines = []
    lines.append(f"# {title} | {author} - Readwise\n")

    # Metadata section
    lines.append("## Metadata\n")
    lines.append(f"- **Type**: {category.title()}")
    lines.append(f"- **Author**: {author}")
    if source_url:
        lines.append(f"- **Source URL**: {source_url}")
    lines.append(f"- **Source**: {source}")
    lines.append(f"- **Date Imported**: {today}")
    lines.append(f"- **Total Highlights**: {num_highlights}")
    if tags:
        tag_str = ', '.join([f"#{tag['name']}" for tag in tags])
        lines.append(f"- **Readwise Tags**: {tag_str}")
    if cover_url:
        lines.append(f"- **Cover**: {cover_url}")
    lines.append("")

    # Document note if exists
    if document_note:
        lines.append("## Document Notes\n")
        lines.append(document_note)
        lines.append("")

    # Highlights section
    lines.append("## Your Highlights\n")

    for i, highlight in enumerate(sorted_highlights, 1):
        location_str = format_highlight_location(highlight)
        text = highlight.get('text', '').strip()
        note = highlight.get('note', '').strip()
        highlighted_at = highlight.get('highlighted_at', '')
        highlight_tags = highlight.get('tags', [])

        lines.append(f"### Highlight {i} ({location_str})\n")
        lines.append(f"> {text}\n")

        if note:
            lines.append(f"**Your Note**: {note}\n")

        if highlight_tags:
            tag_str = ', '.join([f"#{tag['name']}" for tag in highlight_tags])
            lines.append(f"**Tags**: {tag_str}\n")

        # Add a subtle separator between highlights
        lines.append("---\n")

    # Empty sections for manual analysis
    lines.append("## Synthesis Analysis\n")
    lines.append("_To be completed during analysis phase_\n")

    lines.append("## Key Themes Identified\n")
    lines.append("_To be completed during analysis phase_\n")

    lines.append("## Related Synthesis Documents\n")
    lines.append("_Add connections to existing themes:_\n")
    lines.append("- [[Theme 1]]")
    lines.append("- [[Theme 2]]\n")

    lines.append("## Source Information\n")
    lines.append(f"- **Readwise Book ID**: {book.get('id')}")
    lines.append(f"- **Category**: {category}")
    if source_url:
        lines.append(f"- **Original URL**: {source_url}")
    lines.append("")

    return '\n'.join(lines)

def import_book(client, book_id, output_dir):
    """Import a book from Readwise."""
    # Get book details
    book = get_book_details(client, book_id)

    # Get highlights
    highlights = get_highlights(client, book_id)

    if not highlights:
        return {
            "success": False,
            "message": f"No highlights found for this item."
        }

    # Generate filename
    title = book.get('title', 'Untitled')
    author = book.get('author', 'Unknown')
    today = datetime.now().strftime('%Y-%m-%d')

    author_safe = sanitize_filename(author.split(',')[0].strip())  # Take first author
    title_safe = sanitize_filename(title)

    filename = f"{today}_{author_safe}_{title_safe}_Readwise.md"

    # Generate markdown content
    content = generate_markdown(book, highlights)

    # Write to file
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return {
        "success": True,
        "filename": filename,
        "filepath": str(output_path),
        "title": title,
        "author": author,
        "category": book.get('category'),
        "num_highlights": len(highlights),
        "book_id": book_id
    }

def main():
    parser = argparse.ArgumentParser(
        description="Import a book/article from Readwise to Content Notes"
    )
    parser.add_argument(
        '--book-id',
        required=True,
        help='Readwise book ID'
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Output directory for the source document'
    )

    args = parser.parse_args()

    try:
        client = ReadwiseClient()
        result = import_book(client, args.book_id, args.output_dir)

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
