#!/usr/bin/env python3
"""
Sync Readwise Reader articles to local index for fast searching.

Uses the Readwise Reader API (v3) to fetch articles and store in local JSON index.

Usage:
    # Initial sync
    python3 sync_reader_index.py --output-dir "/path/to/Content Notes/.readwise"

    # Incremental sync (only updates since last sync)
    python3 sync_reader_index.py --output-dir "/path/to/Content Notes/.readwise" --incremental
"""

import sys
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from reader_client import ReaderClient

def load_existing_index(index_path):
    """Load existing index file if it exists."""
    if index_path.exists():
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None
    return None

def sync_reader_articles(client, updated_after=None, months_back=12):
    """
    Sync articles from Readwise Reader using v3 API.

    Args:
        client: ReaderClient instance
        updated_after: ISO timestamp for incremental sync (optional)
        months_back: How many months of articles to fetch (for initial sync)

    Returns:
        List of article dictionaries
    """
    print("Fetching articles from Readwise Reader API (v3)...")

    try:
        # Fetch all article documents
        documents = client.list_all_documents(
            category='article',
            updated_after=updated_after
        )

        print(f"Retrieved {len(documents)} article documents")

        articles = []
        cutoff_date = None

        if not updated_after:
            # For initial sync, filter by date
            cutoff_date = datetime.now() - timedelta(days=months_back * 30)

        for doc in documents:
            # Filter by date for initial sync
            if not updated_after and cutoff_date:
                updated_str = doc.get('updated_at', '')
                if updated_str:
                    try:
                        updated_date = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
                        if updated_date.replace(tzinfo=None) < cutoff_date:
                            continue
                    except Exception:
                        pass  # Include if we can't parse date

            # Skip if it's a highlight/note (these have parent_id)
            if doc.get('parent_id'):
                continue

            # Count highlights for this article
            # Note: We'd need to fetch all docs to count highlights accurately
            # For now, we'll fetch on-demand during import

            article = {
                'id': doc.get('id'),
                'title': doc.get('title', 'Untitled'),
                'author': doc.get('author', 'Unknown'),
                'source_url': doc.get('source_url') or doc.get('url', ''),
                'category': doc.get('category', 'article'),
                'location': doc.get('location', ''),
                'num_highlights': 0,  # Will be counted during import
                'last_updated': doc.get('updated_at', ''),
                'tags': [tag.get('name') if isinstance(tag, dict) else tag for tag in doc.get('tags', [])],
                'reading_progress': doc.get('reading_progress', 0),
                'word_count': doc.get('word_count', 0),
                'summary': doc.get('summary', ''),
                'site_name': doc.get('site_name', ''),
                'published_date': doc.get('published_date', ''),
                'readwise_url': f"https://readwise.io/reader/document/{doc.get('id', '')}"
            }

            articles.append(article)

        # Sort by last updated (most recent first)
        articles.sort(key=lambda x: x.get('last_updated', ''), reverse=True)

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
        description="Sync Readwise Reader articles to local index"
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
        client = ReaderClient()

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
        new_articles = sync_reader_articles(
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
            'api_version': 'reader_v3',
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
