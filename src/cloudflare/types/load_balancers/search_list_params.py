# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchListParams", "SearchParams"]


class SearchListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    page: object

    per_page: object

    search_params: SearchParams


class SearchParams(TypedDict, total=False):
    query: str
    """Search query term."""

    references: Literal["", "*", "referral", "referrer"]
    """The type of references to include ("\\**" for all)."""
