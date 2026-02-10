"""
Readwise API client for authentication and API calls.
"""

import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path

class ReadwiseClient:
    BASE_URL = "https://readwise.io/api/v2"

    def __init__(self):
        # Load environment variables from secrets directory
        secrets_path = Path.home() / ".claude" / "secrets" / "readwise" / ".env"
        load_dotenv(secrets_path)

        self.api_token = os.getenv("READWISE_API_TOKEN")
        if not self.api_token:
            raise ValueError(
                "READWISE_API_TOKEN not found. "
                "Please set up ~/.claude/secrets/readwise/.env with your token."
            )

        self.headers = {
            "Authorization": f"Token {self.api_token}"
        }

    def test_auth(self):
        """Test authentication by calling the auth endpoint."""
        try:
            response = requests.get(
                f"{self.BASE_URL}/auth/",
                headers=self.headers,
                timeout=10
            )

            if response.status_code == 204:
                return {"success": True, "message": "Authentication successful"}
            elif response.status_code == 401:
                return {"success": False, "message": "Invalid API token"}
            else:
                return {
                    "success": False,
                    "message": f"Unexpected response: {response.status_code}"
                }
        except requests.exceptions.RequestException as e:
            return {"success": False, "message": f"Connection error: {str(e)}"}

    def get(self, endpoint, params=None):
        """Make a GET request to the Readwise API."""
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                retry_after = e.response.headers.get('Retry-After', 'unknown')
                raise Exception(f"Rate limit exceeded. Retry after {retry_after} seconds.")
            raise Exception(f"HTTP error: {e.response.status_code} - {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")

    def get_paginated(self, endpoint, params=None):
        """Get all results from a paginated endpoint."""
        results = []
        next_page = None

        while True:
            if next_page:
                # Extract pageCursor from next URL
                from urllib.parse import urlparse, parse_qs
                parsed = urlparse(next_page)
                query_params = parse_qs(parsed.query)
                page_cursor = query_params.get('pageCursor', [None])[0]

                if params is None:
                    params = {}
                params['pageCursor'] = page_cursor

            data = self.get(endpoint, params)

            if isinstance(data, dict):
                results.extend(data.get('results', []))
                next_page = data.get('next')
                if not next_page:
                    break
            else:
                # Some endpoints return lists directly
                results = data
                break

        return results

if __name__ == "__main__":
    # Test authentication when run directly
    try:
        client = ReadwiseClient()
        result = client.test_auth()
        print(result["message"])
        sys.exit(0 if result["success"] else 1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
