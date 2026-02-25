"""
Readwise Reader API client for documents and highlights.
"""

import requests
from readwise_client import ReadwiseClient

class ReaderClient(ReadwiseClient):
    """Client for Readwise Reader API (v3)."""

    def list_documents(self, category=None, location=None, updated_after=None, page_cursor=None):
        """
        List documents from Readwise Reader.

        Args:
            category: Filter by category (article, pdf, epub, video, tweet, etc.)
            location: Filter by location (new, later, archive, feed)
            updated_after: ISO 8601 timestamp for incremental sync
            page_cursor: Pagination cursor

        Returns:
            Dictionary with results and nextPageCursor
        """
        params = {}

        if category:
            params['category'] = category
        if location:
            params['location'] = location
        if updated_after:
            params['updatedAfter'] = updated_after
        if page_cursor:
            params['pageCursor'] = page_cursor

        import time

        # Retry logic for network errors
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Use Reader API v3 endpoint
                url = "https://readwise.io/api/v3/list/"
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
                raise Exception(f"Failed to list documents: HTTP error: {e.response.status_code} - {e.response.text}")
            except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:
                if attempt < max_retries - 1:
                    print(f"Connection error (attempt {attempt + 1}/{max_retries}), retrying in 5 seconds...")
                    time.sleep(5)
                    continue
                raise Exception(f"Failed to list documents after {max_retries} attempts: {str(e)}")
            except Exception as e:
                raise Exception(f"Failed to list documents: {str(e)}")

    def list_all_documents(self, category=None, location=None, updated_after=None):
        """
        Get all documents with pagination.

        Args:
            category: Filter by category
            location: Filter by location
            updated_after: ISO timestamp for incremental sync

        Returns:
            List of all documents
        """
        all_documents = []
        page_cursor = None

        while True:
            response = self.list_documents(
                category=category,
                location=location,
                updated_after=updated_after,
                page_cursor=page_cursor
            )

            results = response.get('results', [])
            all_documents.extend(results)

            page_cursor = response.get('nextPageCursor')
            if not page_cursor:
                break

        return all_documents

    def get_document_highlights(self, parent_id):
        """
        Get highlights for a specific document.

        In Reader API, highlights are documents with parent_id set.

        Args:
            parent_id: The document ID to get highlights for

        Returns:
            List of highlight documents
        """
        # Highlights are documents with parent_id matching our document
        all_docs = self.list_all_documents()

        highlights = [
            doc for doc in all_docs
            if doc.get('parent_id') == parent_id and doc.get('category') in ['highlight', 'note']
        ]

        return highlights
