# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CrawlGetParams"]


class CrawlGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    cache_ttl: Annotated[float, PropertyInfo(alias="cacheTTL")]
    """Cache TTL default is 5s. Set to 0 to disable."""

    cursor: float
    """Cursor for pagination."""

    limit: float
    """Limit for pagination."""

    status: Literal["queued", "errored", "completed", "disallowed", "skipped", "cancelled"]
    """Filter by URL status."""
