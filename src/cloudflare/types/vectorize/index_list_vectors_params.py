# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndexListVectorsParams"]


class IndexListVectorsParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    count: int
    """Maximum number of vectors to return"""

    cursor: str
    """Cursor for pagination to get the next page of results"""
