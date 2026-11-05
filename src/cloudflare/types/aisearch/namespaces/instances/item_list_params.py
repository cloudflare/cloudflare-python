# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemListParams"]


class ItemListParams(TypedDict, total=False):
    account_id: Required[str]

    namespace: Required[str]

    item_id: str
    """Return only the item with this unique ID. Returns at most one item."""

    key: str
    """Return only items with this exact key (object key / filename).

    Each key is unique within a source, so combine with `source` to disambiguate
    across data sources.
    """

    metadata_filter: str
    """JSON-encoded metadata filter using Vectorize filter syntax.

    Examples: {"folder":"reports/"},
    {"timestamp":{"$gte":1700000000000}}, {"folder":{"$in":["docs/","reports/"]}}.
    """

    page: int

    per_page: int

    search: str

    sort_by: Literal["status", "modified_at"]
    """Sort order for items.

    "status" (default) sorts items according to status priority, then last_seen_at.
    "modified_at" sorts items according to file modification time (most recent
    first), falling back to created_at.
    """

    source: str
    """Return only items with this source_id.

    Use "builtin" for uploaded files, or a source identifier like
    "web-crawler:https://example.com".
    """

    status: Literal["queued", "running", "completed", "error", "skipped", "outdated"]
