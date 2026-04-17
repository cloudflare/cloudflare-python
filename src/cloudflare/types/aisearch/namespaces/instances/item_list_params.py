# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    account_id: str

    name: Required[str]

    item_id: str
    """Filter items by their unique ID. Returns at most one item."""

    metadata_filter: str
    """JSON-encoded metadata filter using Vectorize filter syntax.

    Examples: {"folder":"reports/"},
    {"timestamp":{"$gte":1700000000000}}, {"folder":{"$in":["docs/","reports/"]}}
    """

    page: int

    per_page: int

    search: str

    sort_by: Literal["status", "modified_at"]
    """Sort order for items.

    "status" (default) sorts by status priority then last_seen_at. "modified_at"
    sorts by file modification time (most recent first), falling back to created_at.
    """

    source: str
    """Filter items by source_id.

    Use "builtin" for uploaded files, or a source identifier like
    "web-crawler:https://example.com".
    """

    status: Literal["queued", "running", "completed", "error", "skipped", "outdated"]
