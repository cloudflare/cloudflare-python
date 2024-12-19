# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AddressListParams"]


class AddressListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Sorts results in an ascending or descending order."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""

    verified: Literal[True, False]
    """Filter by verified destination addresses."""
