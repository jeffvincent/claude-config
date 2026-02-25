#!/usr/bin/env python3
"""
Search for articles in local Readwise index (fast, no API calls).

Usage:
    python3 search.py --query "dario amodei" --index-dir "/path/to/.readwise"
    python3 search.py --query "machines loving grace" --index-dir "/path/to/.readwise"
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path

def ensure_index_updated(index_dir):
    """Check if index needs updating and sync if needed."""
    script_dir = Path(__file__).parent
    check_script = script_dir / 'check_updates.py'

    try:
        # Run check with auto-sync
        result = subprocess.run(
            [
                'python3',
                str(check_script),
                '--index-dir', str(index_dir),
                '--auto-sync',
                '--max-age-hours', '24'
            ],
            capture_output=True,
            text=True,
            timeout=300
        )

        # Print output (whether sync happened or not)
        if result.stdout:
            print(result.stdout, end='')

        return result.returncode == 0

    except Exception as e:
        print(f"Warning: Could not check index status: {str(e)}", file=sys.stderr)
        return True  # Continue anyway

def load_index(index_dir):
    """Load articles index from file."""
    index_path = Path(index_dir) / 'articles-index.json'

    if not index_path.exists():
        raise Exception(
            f"Index file not found: {index_path}\n"
            f"Run: python3 sync_index.py --output-dir {index_dir}"
        )

    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data.get('articles', [])

    except Exception as e:
        raise Exception(f"Could not load index: {str(e)}")

def search_articles(articles, query, category=None):
    """
    Search articles in local index.

    Args:
        articles: List of article dictionaries
        query: Search query string
        category: Optional category filter (not needed for articles-only index)

    Returns:
        List of matching articles with scores
    """
    query_lower = query.lower()
    query_terms = query_lower.split()

    results = []

    for article in articles:
        title = (article.get('title') or '').lower()
        author = (article.get('author') or '').lower()
        tags = [tag.lower() for tag in article.get('tags', [])]

        # Calculate relevance score
        score = 0

        # Exact phrase match in title (highest score)
        if query_lower in title:
            score += 100

        # Exact phrase match in author
        if query_lower in author:
            score += 80

        # All terms appear in title
        if all(term in title for term in query_terms):
            score += 50

        # All terms appear in author
        if all(term in author for term in query_terms):
            score += 40

        # Individual term matches in title
        for term in query_terms:
            if term in title:
                score += 10
            if term in author:
                score += 5

        # Tag matches
        for tag in tags:
            if query_lower in tag:
                score += 15
            for term in query_terms:
                if term in tag:
                    score += 5

        # Only include if there's a match
        if score > 0:
            results.append({
                **article,
                'relevance_score': score
            })

    # Sort by relevance score (highest first)
    results.sort(key=lambda x: x['relevance_score'], reverse=True)

    return results

def format_results(results, show_scores=False):
    """Format search results for display."""
    if not results:
        return "No results found."

    output = []
    output.append(f"\nFound {len(results)} result(s):\n")

    for i, item in enumerate(results, 1):
        score_str = f" (score: {item['relevance_score']})" if show_scores else ""
        output.append(f"{i}. {item['title']}")
        output.append(f"   Author: {item['author']}")
        output.append(f"   Highlights: {item['num_highlights']}")
        output.append(f"   ID: {item['id']}")
        if item.get('source_url'):
            output.append(f"   URL: {item['source_url']}")
        if item.get('tags'):
            tags_str = ', '.join([f"#{tag}" for tag in item['tags'][:5]])
            output.append(f"   Tags: {tags_str}")
        if show_scores:
            output.append(f"   Relevance{score_str}")
        output.append("")

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description="Search Readwise articles in local index"
    )
    parser.add_argument(
        '--query',
        required=True,
        help='Search query (title or author)'
    )
    parser.add_argument(
        '--index-dir',
        default="/Users/jvincent/Projects/Personal/Content Notes/.readwise",
        help='Path to .readwise directory'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )
    parser.add_argument(
        '--show-scores',
        action='store_true',
        help='Show relevance scores'
    )
    parser.add_argument(
        '--skip-update-check',
        action='store_true',
        help='Skip checking if index needs updating'
    )

    args = parser.parse_args()

    try:
        # Check if index needs updating (unless skipped)
        if not args.skip_update_check:
            ensure_index_updated(args.index_dir)

        # Load index
        articles = load_index(args.index_dir)

        if not articles:
            print("Index is empty. Run sync_index.py to populate it.")
            return 1

        # Search
        results = search_articles(articles, args.query)

        # Output
        if args.json:
            # Remove relevance scores from JSON output unless requested
            if not args.show_scores:
                for r in results:
                    r.pop('relevance_score', None)
            print(json.dumps(results, indent=2))
        else:
            print(format_results(results, args.show_scores))

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
