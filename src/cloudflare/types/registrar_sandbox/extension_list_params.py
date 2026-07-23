# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtensionListParams"]


class ExtensionListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cursor: str
    """
    Opaque token from a previous response's `result_info.cursor`. Pass this value to
    fetch the next page of results. Omit (or pass an empty string) for the first
    page.
    """

    direction: Literal["asc", "desc"]
    """Sort direction for results. Defaults to ascending order."""

    name: str
    """
    Filter extensions by exact name match. For example, `name=com` returns only the
    `com` extension.
    """

    per_page: int
    """Number of items to return per page."""

    sort_by: Literal["name", "created_at", "updated_at"]
    """Column to sort results by. Defaults to `name` when omitted."""
