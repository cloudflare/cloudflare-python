# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthMethodListParams"]


class AuthMethodListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """A page number within the paginated result set."""

    page_size: int
    """Number of results to return per page."""
