#!/usr/bin/env python3
"""
Search for books and highlights in your Readwise library.

Usage:
    python3 search.py --query "atomic habits"
    python3 search.py --query "tim urban" --category articles
"""

import sys
import json
import argparse
from readwise_client import ReadwiseClient

def search_books(client, query, category=None):
    """
    Search for books/documents in Readwise library.

    Args:
        client: ReadwiseClient instance
        query: Search query string
        category: Optional category filter (books, articles, tweets, podcasts)

    Returns:
        List of matching books with metadata
    """
    params = {}
    if category:
        params['category'] = category

    try:
        # Get all books (the API doesn't have text search, so we filter locally)
        all_books = client.get_paginated('/books/', params)

        # Filter by query (case-insensitive search in title and author)
        query_lower = query.lower()
        results = []

        for book in all_books:
            title = (book.get('title') or '').lower()
            author = (book.get('author') or '').lower()

            if query_lower in title or query_lower in author:
                results.append({
                    'id': book['id'],
                    'title': book.get('title', 'Untitled'),
                    'author': book.get('author', 'Unknown'),
                    'category': book.get('category', 'unknown'),
                    'source': book.get('source', 'unknown'),
                    'num_highlights': book.get('num_highlights', 0),
                    'updated': book.get('updated', ''),
                    'source_url': book.get('source_url', ''),
                    'cover_image_url': book.get('cover_image_url', ''),
                    'document_note': book.get('document_note', '')
                })

        return results

    except Exception as e:
        raise Exception(f"Search failed: {str(e)}")

def format_results(results):
    """Format search results for display."""
    if not results:
        return "No results found."

    output = []
    output.append(f"\nFound {len(results)} result(s):\n")

    for i, item in enumerate(results, 1):
        output.append(f"{i}. [{item['category'].upper()}] {item['title']}")
        output.append(f"   Author: {item['author']}")
        output.append(f"   Highlights: {item['num_highlights']}")
        output.append(f"   ID: {item['id']}")
        if item['source_url']:
            output.append(f"   URL: {item['source_url']}")
        output.append("")

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description="Search your Readwise library"
    )
    parser.add_argument(
        '--query',
        required=True,
        help='Search query (title or author)'
    )
    parser.add_argument(
        '--category',
        choices=['books', 'articles', 'tweets', 'podcasts', 'supplementals', 'videos'],
        help='Filter by category'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    try:
        client = ReadwiseClient()
        results = search_books(client, args.query, args.category)

        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(format_results(results))

        return 0

    except Exception as e:
        if args.json:
            print(json.dumps({
                "error": str(e)
            }))
        else:
            print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
