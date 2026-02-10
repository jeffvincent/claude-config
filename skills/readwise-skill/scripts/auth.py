#!/usr/bin/env python3
"""
Test Readwise API authentication.

Usage:
    python3 auth.py
"""

import sys
import json
from readwise_client import ReadwiseClient

def main():
    try:
        client = ReadwiseClient()
        result = client.test_auth()

        # Output as JSON for easier parsing
        print(json.dumps(result, indent=2))

        return 0 if result["success"] else 1

    except Exception as e:
        print(json.dumps({
            "success": False,
            "message": str(e)
        }, indent=2))
        return 1

if __name__ == "__main__":
    sys.exit(main())
