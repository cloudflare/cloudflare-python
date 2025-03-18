# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AsePrefixesParams"]


class AsePrefixesParams(TypedDict, total=False):
    country: str
    """Alpha-2 country code."""

    format: Literal["JSON", "CSV"]
    """Format in which results will be returned."""

    limit: int
    """Maximum number of ASes to return."""
