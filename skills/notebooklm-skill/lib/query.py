#!/usr/bin/env python3
"""Query a NotebookLM notebook and return the answer with citations."""

import asyncio
import argparse
import json
import os
import sys

# Patch httpx for two corporate proxy issues:
# 1. SSL: Zscaler CA cert has non-critical Basic Constraints — newer Python/OpenSSL rejects it
# 2. Timeout: chat endpoint (GenerateFreeFormStreamed) is a streaming response; the proxy
#    buffers the stream, so per-chunk read timeouts fire before the full response arrives.
#    Setting read=None disables the per-read-chunk timeout while keeping connect timeout.
import httpx as _httpx
_orig_async_init = _httpx.AsyncClient.__init__
def _patched_async_init(self, *args, **kwargs):
    kwargs.setdefault("verify", False)
    kwargs["timeout"] = _httpx.Timeout(connect=15, read=None, write=None, pool=None)
    _orig_async_init(self, *args, **kwargs)
_httpx.AsyncClient.__init__ = _patched_async_init

_orig_sync_init = _httpx.Client.__init__
def _patched_sync_init(self, *args, **kwargs):
    kwargs.setdefault("verify", False)
    kwargs["timeout"] = _httpx.Timeout(connect=15, read=None, write=None, pool=None)
    _orig_sync_init(self, *args, **kwargs)
_httpx.Client.__init__ = _patched_sync_init

from notebooklm import NotebookLMClient

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTRY_PATH = os.path.join(SCRIPT_DIR, "notebooks.json")


def resolve_notebook_id(name_or_id: str) -> str:
    """Resolve a friendly alias to a notebook ID, or pass through if already an ID."""
    try:
        with open(REGISTRY_PATH) as f:
            registry = json.load(f)
        notebooks = registry.get("notebooks", {})
        if name_or_id in notebooks:
            return notebooks[name_or_id]
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return name_or_id


async def list_notebooks():
    """List all accessible notebooks."""
    async with await NotebookLMClient.from_storage() as client:
        notebooks = await client.notebooks.list()
        results = []
        for nb in notebooks:
            results.append({
                "id": nb.id,
                "title": nb.title,
                "sources_count": nb.sources_count,
            })
        return results


async def ask_notebook(notebook_id: str, question: str, conversation_id: str = None):
    """Ask a question against a notebook's sources."""
    async with await NotebookLMClient.from_storage(timeout=120) as client:
        result = await client.chat.ask(
            notebook_id=notebook_id,
            question=question,
            conversation_id=conversation_id,
        )

        # Get source details for citations
        sources = []
        if result.references:
            try:
                all_sources = await client.sources.list(notebook_id)
                source_map = {s.id: s for s in all_sources}
                for ref in result.references:
                    source = source_map.get(ref.source_id)
                    sources.append({
                        "citation_number": ref.citation_number,
                        "source_title": source.title if source else "Unknown",
                        "source_type": source.kind if source else "unknown",
                        "cited_text": ref.cited_text,
                    })
            except Exception:
                for ref in result.references:
                    sources.append({
                        "citation_number": ref.citation_number,
                        "source_id": ref.source_id,
                        "cited_text": ref.cited_text,
                    })

        return {
            "answer": result.answer,
            "conversation_id": result.conversation_id,
            "turn_number": result.turn_number,
            "references": sources,
        }


async def get_notebook_summary(notebook_id: str):
    """Get a notebook's description and suggested topics."""
    async with await NotebookLMClient.from_storage() as client:
        desc = await client.notebooks.get_description(notebook_id)
        return {
            "summary": desc.summary,
            "suggested_topics": [
                {"question": t.question, "prompt": t.prompt}
                for t in desc.suggested_topics
            ],
        }


async def list_sources(notebook_id: str):
    """List sources in a notebook."""
    async with await NotebookLMClient.from_storage() as client:
        sources = await client.sources.list(notebook_id)
        return [
            {
                "id": s.id,
                "title": s.title,
                "kind": s.kind,
                "url": s.url,
            }
            for s in sources
        ]


def main():
    parser = argparse.ArgumentParser(description="NotebookLM CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list notebooks
    subparsers.add_parser("list", help="List all notebooks")

    # ask
    ask_parser = subparsers.add_parser("ask", help="Ask a notebook a question")
    ask_parser.add_argument("notebook_id", help="Notebook ID")
    ask_parser.add_argument("question", help="Question to ask")
    ask_parser.add_argument("--conversation-id", help="Continue a conversation")

    # summary
    summary_parser = subparsers.add_parser("summary", help="Get notebook summary")
    summary_parser.add_argument("notebook_id", help="Notebook ID")

    # sources
    sources_parser = subparsers.add_parser("sources", help="List notebook sources")
    sources_parser.add_argument("notebook_id", help="Notebook ID")

    args = parser.parse_args()

    if args.command == "list":
        result = asyncio.run(list_notebooks())
    elif args.command == "ask":
        notebook_id = resolve_notebook_id(args.notebook_id)
        result = asyncio.run(ask_notebook(
            notebook_id,
            args.question,
            args.conversation_id,
        ))
    elif args.command == "summary":
        notebook_id = resolve_notebook_id(args.notebook_id)
        result = asyncio.run(get_notebook_summary(notebook_id))
    elif args.command == "sources":
        notebook_id = resolve_notebook_id(args.notebook_id)
        result = asyncio.run(list_sources(notebook_id))

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
