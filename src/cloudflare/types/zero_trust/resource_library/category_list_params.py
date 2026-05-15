# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CategoryListParams"]


class CategoryListParams(TypedDict, total=False):
    account_id: Required[str]

    limit: int
    """Limit of number of results to return."""

    offset: int
    """Offset of results to return."""
