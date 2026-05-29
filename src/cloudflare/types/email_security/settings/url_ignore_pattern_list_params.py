# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLIgnorePatternListParams"]


class URLIgnorePatternListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    page: int
    """Current page within paginated list of results."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""
