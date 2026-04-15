# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    page: int
    """Current page."""

    per_page: int
    """Items per-page."""
