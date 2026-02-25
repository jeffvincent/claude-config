#!/usr/bin/env python3
"""
Sync Readwise articles to local index for fast searching.

Uses the Readwise Export API to fetch articles from the last 12 months
and store them in a local JSON index.

Usage:
    # Initial sync
    python3 sync_index.py --output-dir "/path/to/Content Notes/.readwise"

    # Incremental sync (only updates since last sync)
    python3 sync_index.py --output-dir "/path/to/Content Notes/.readwise" --incremental
"""

import sys
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from readwise_client import ReadwiseClient

def load_existing_index(index_path):
    """Load existing index file if it exists."""
    if index_path.exists():
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    return None

def sync_articles(client, updated_after=None, months_back=12):
    """
    Sync articles from Readwise using Export API.

    Args:
        client: ReadwiseClient instance
        updated_after: ISO timestamp for incremental sync (optional)
        months_back: How many months of articles to fetch (for initial sync)

    Returns:
        List of article dictionaries
    """
    print("Fetching articles from Readwise Export API...")

    # Use Export API for efficient bulk fetch
    params = {}

    if updated_after:
        # Incremental sync - only get updates since last sync
        params['updatedAfter'] = updated_after
        print(f"Fetching articles updated after: {updated_after}")

    try:
        # Export API returns highlights with book metadata
        all_highlights = client.get_paginated('/export/', params)

        print(f"Retrieved {len(all_highlights)} highlights total")

        # Extract unique articles (books) from highlights
        articles_dict = {}

        for highlight in all_highlights:
            book_id = highlight.get('book_id')
            category = highlight.get('category')

            # Filter to articles only
            if category != 'articles':
                continue

            # Check if within time window (for initial sync)
            if not updated_after:
                updated_str = highlight.get('updated', '')
                if updated_str:
                    try:
                        updated_date = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
                        cutoff_date = datetime.now().replace(tzinfo=updated_date.tzinfo) - timedelta(days=months_back * 30)
                        if updated_date < cutoff_date:
                            continue
                    except Exception:
                        pass  # Include if we can't parse date

            # Build article entry (or update if we've seen this book_id)
            if book_id not in articles_dict:
                articles_dict[book_id] = {
                    'id': book_id,
                    'title': highlight.get('title', 'Untitled'),
                    'author': highlight.get('author', 'Unknown'),
                    'source_url': highlight.get('source_url', ''),
                    'category': category,
                    'num_highlights': 0,
                    'last_updated': highlight.get('updated', ''),
                    'tags': [],
                    'readwise_url': f"https://readwise.io/bookreview/{book_id}"
                }

            # Count highlights for this article
            articles_dict[book_id]['num_highlights'] += 1

            # Collect unique tags
            highlight_tags = highlight.get('tags', [])
            for tag in highlight_tags:
                tag_name = tag.get('name') if isinstance(tag, dict) else tag
                if tag_name and tag_name not in articles_dict[book_id]['tags']:
                    articles_dict[book_id]['tags'].append(tag_name)

            # Keep most recent update date
            current_updated = articles_dict[book_id]['last_updated']
            new_updated = highlight.get('updated', '')
            if new_updated > current_updated:
                articles_dict[book_id]['last_updated'] = new_updated

        articles = list(articles_dict.values())

        # Sort by last updated (most recent first)
        articles.sort(key=lambda x: x['last_updated'], reverse=True)

        print(f"Found {len(articles)} unique articles")

        return articles

    except Exception as e:
        raise Exception(f"Sync failed: {str(e)}")

def merge_articles(existing_articles, new_articles):
    """Merge new articles with existing index, updating as needed."""
    articles_by_id = {a['id']: a for a in existing_articles}

    for new_article in new_articles:
        articles_by_id[new_article['id']] = new_article

    return list(articles_by_id.values())

def save_index(index_data, index_path, log_path):
    """Save index and log sync operation."""
    # Save main index
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    # Log sync operation
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'sync_type': 'incremental' if index_data.get('sync_count', 0) > 1 else 'initial',
        'total_articles': index_data['total_articles'],
        'articles_updated': len(index_data.get('articles', []))
    }

    log_data = []
    if log_path.exists():
        try:
            with open(log_path, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        except Exception:
            pass

    log_data.append(log_entry)

    # Keep last 100 log entries
    log_data = log_data[-100:]

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(
        description="Sync Readwise articles to local index"
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Output directory for index files (.readwise directory)'
    )
    parser.add_argument(
        '--incremental',
        action='store_true',
        help='Incremental sync (only fetch updates since last sync)'
    )
    parser.add_argument(
        '--months',
        type=int,
        default=12,
        help='Number of months back to sync (initial sync only, default: 12)'
    )

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    index_path = output_dir / 'articles-index.json'
    log_path = output_dir / 'sync-log.json'

    try:
        client = ReadwiseClient()

        # Load existing index
        existing_data = load_existing_index(index_path)
        existing_articles = existing_data.get('articles', []) if existing_data else []

        # Determine sync type
        updated_after = None
        if args.incremental and existing_data:
            updated_after = existing_data.get('last_synced')
            if not updated_after:
                print("Warning: No last_synced timestamp found, performing full sync")

        # Sync articles
        new_articles = sync_articles(
            client,
            updated_after=updated_after,
            months_back=args.months
        )

        # Merge with existing
        if updated_after:
            print(f"Merging {len(new_articles)} updated articles with existing index...")
            all_articles = merge_articles(existing_articles, new_articles)
        else:
            all_articles = new_articles

        # Sort by last updated
        all_articles.sort(key=lambda x: x.get('last_updated', ''), reverse=True)

        # Create index data
        index_data = {
            'last_synced': datetime.now().isoformat(),
            'sync_count': (existing_data.get('sync_count', 0) + 1) if existing_data else 1,
            'total_articles': len(all_articles),
            'months_covered': args.months,
            'articles': all_articles
        }

        # Save
        save_index(index_data, index_path, log_path)

        # Report
        print(f"\n✅ Sync complete!")
        print(f"   Total articles: {len(all_articles)}")
        print(f"   Index file: {index_path}")
        print(f"   Last synced: {index_data['last_synced']}")

        return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
