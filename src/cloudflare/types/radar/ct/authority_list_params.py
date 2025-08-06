# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AuthorityListParams"]


class AuthorityListParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Limits the number of objects returned in the response."""

    offset: int
    """Skips the specified number of objects before fetching the results."""
