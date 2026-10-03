# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChangelogListParams"]


class ChangelogListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the Flagship app."""

    app_id: Required[str]
    """Flagship app ID returned when the app was created."""

    cursor: str
    """Pagination cursor from a previous response."""

    limit: int
    """Max items to return (1–200)."""
