# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamespaceListParams"]


class NamespaceListParams(TypedDict, total=False):
    account_id: str

    page: int
    """Page number (1-indexed)."""

    per_page: int
    """Number of results per page."""

    search: str
    """
    Filter namespaces whose name or description contains this string
    (case-insensitive).
    """
