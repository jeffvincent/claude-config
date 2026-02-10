#!/usr/bin/env python3
"""
Fetch original content from a URL (for articles, blog posts, etc.)

Usage:
    python3 fetch_content.py --url "https://example.com/article" --output "/path/to/output.txt"
"""

import sys
import argparse
import requests
from pathlib import Path

def fetch_url_content(url):
    """
    Fetch content from a URL.
    Returns raw HTML - Claude Code's WebFetch should be used for better parsing.

    This is a simple fallback implementation.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        return response.text

    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")

def main():
    parser = argparse.ArgumentParser(
        description="Fetch content from a URL"
    )
    parser.add_argument(
        '--url',
        required=True,
        help='URL to fetch'
    )
    parser.add_argument(
        '--output',
        help='Optional output file path'
    )

    args = parser.parse_args()

    try:
        content = fetch_url_content(args.url)

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Content saved to: {output_path}")
        else:
            print(content)

        return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
