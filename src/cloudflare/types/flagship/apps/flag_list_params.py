# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FlagListParams"]


class FlagListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID."""

    cursor: str
    """Pagination cursor from a previous response."""

    limit: str
    """Max items to return (1–200)."""
