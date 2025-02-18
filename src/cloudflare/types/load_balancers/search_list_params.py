# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchListParams", "SearchParams"]


class SearchListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    page: float

    per_page: float

    search_params: SearchParams


class SearchParams(TypedDict, total=False):
    query: str
    """Search query term."""

    references: Literal["", "*", "referral", "referrer"]
    """The type of references to include ("\\**" for all)."""
