# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppGetParams"]


class AppGetParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    page_no: int
    """The page number from which you want your page search results to be displayed."""

    per_page: int
    """Number of results per page."""

    search: str
    """Search string that matches apps by name."""

    sort_order: Literal["ASC", "DESC"]
    """Sort order for apps by creation time."""
