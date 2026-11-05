# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedListParams"]


class FeedListParams(TypedDict, total=False):
    account_id: Required[str]

    category: str
    """Exact feed-category filter, up to 100 characters.

    Omit to include all categories.
    """

    enabled: bool
    """Filter by enabled state.

    Accepts true, false, 1, or 0; omit to include enabled and disabled feeds.
    """

    limit: int
    """Optional 1–100 alias for per_page. When provided, limit takes precedence."""

    page: int
    """1-based page number. Minimum 1; defaults to 1."""

    per_page: int
    """Number of feeds per page, from 1 to 100. Defaults to 20."""

    sort: str
    """Sort by created_at, title, category, or url.

    Prefix the field with - for descending order; defaults to -created_at.
    """

    source_type: Literal["curated", "custom"]
    """Filter by curated or custom feed source. Omit to include both source types."""

    status: str
    """Exact stored polling-status filter, such as active or error.

    Omit to include every status.
    """
