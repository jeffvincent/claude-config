#!/usr/bin/env python3
"""
Check if Readwise index needs updating and run incremental sync if stale.

Called automatically before search/import operations to keep index fresh.

Usage:
    python3 check_updates.py --index-dir "/path/to/Content Notes/.readwise"
"""

import sys
import json
import argparse
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

def check_and_update(index_dir, max_age_hours=24):
    """
    Check if index is stale and update if needed.

    Args:
        index_dir: Path to .readwise directory
        max_age_hours: Maximum age before triggering update (default: 24)

    Returns:
        dict with status information
    """
    index_path = Path(index_dir) / 'articles-index.json'

    # Check if index exists
    if not index_path.exists():
        return {
            'needs_sync': True,
            'reason': 'Index does not exist',
            'sync_type': 'initial'
        }

    # Load index
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
    except Exception as e:
        return {
            'needs_sync': True,
            'reason': f'Could not read index: {str(e)}',
            'sync_type': 'initial'
        }

    # Check last sync time
    last_synced_str = index_data.get('last_synced')
    if not last_synced_str:
        return {
            'needs_sync': True,
            'reason': 'No last_synced timestamp',
            'sync_type': 'initial'
        }

    try:
        last_synced = datetime.fromisoformat(last_synced_str)
        now = datetime.now()

        # Make both timezone-aware or naive for comparison
        if last_synced.tzinfo is not None:
            # last_synced is aware, make now aware too
            import sys
            if sys.version_info >= (3, 9):
                from zoneinfo import ZoneInfo
                now = now.astimezone()
            else:
                # Fallback for older Python
                now = now.replace(tzinfo=last_synced.tzinfo)
        else:
            # last_synced is naive, make sure now is naive too
            now = now.replace(tzinfo=None)

        age = now - last_synced
        max_age = timedelta(hours=max_age_hours)

        if age > max_age:
            hours_old = age.total_seconds() / 3600
            return {
                'needs_sync': True,
                'reason': f'Index is {hours_old:.1f} hours old (max: {max_age_hours})',
                'sync_type': 'incremental',
                'last_synced': last_synced_str,
                'age_hours': hours_old
            }
        else:
            hours_old = age.total_seconds() / 3600
            return {
                'needs_sync': False,
                'reason': f'Index is fresh ({hours_old:.1f} hours old)',
                'last_synced': last_synced_str,
                'age_hours': hours_old
            }

    except Exception as e:
        return {
            'needs_sync': True,
            'reason': f'Could not parse last_synced: {str(e)}',
            'sync_type': 'initial'
        }

def run_sync(index_dir, sync_type):
    """Run sync_index.py with appropriate parameters."""
    script_dir = Path(__file__).parent
    sync_script = script_dir / 'sync_index.py'

    cmd = [
        'python3',
        str(sync_script),
        '--output-dir', str(index_dir)
    ]

    if sync_type == 'incremental':
        cmd.append('--incremental')

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode == 0:
            return {
                'success': True,
                'output': result.stdout
            }
        else:
            return {
                'success': False,
                'error': result.stderr or result.stdout
            }

    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Sync timed out after 5 minutes'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def main():
    parser = argparse.ArgumentParser(
        description="Check if Readwise index needs updating"
    )
    parser.add_argument(
        '--index-dir',
        required=True,
        help='Path to .readwise directory'
    )
    parser.add_argument(
        '--max-age-hours',
        type=int,
        default=24,
        help='Maximum age in hours before update (default: 24)'
    )
    parser.add_argument(
        '--auto-sync',
        action='store_true',
        help='Automatically run sync if needed'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )

    args = parser.parse_args()

    # Check status
    status = check_and_update(args.index_dir, args.max_age_hours)

    if args.json:
        print(json.dumps(status, indent=2))
    else:
        if status['needs_sync']:
            print(f"⚠️  {status['reason']}")
            if args.auto_sync:
                print(f"Running {status.get('sync_type', 'initial')} sync...")
                sync_result = run_sync(args.index_dir, status.get('sync_type', 'initial'))

                if sync_result['success']:
                    print("✅ Sync completed successfully")
                    return 0
                else:
                    print(f"❌ Sync failed: {sync_result['error']}", file=sys.stderr)
                    return 1
            else:
                print(f"Run: python3 sync_index.py --output-dir {args.index_dir} --incremental")
                return 1
        else:
            print(f"✅ {status['reason']}")
            return 0

    return 0 if not status['needs_sync'] else 1

if __name__ == "__main__":
    sys.exit(main())
