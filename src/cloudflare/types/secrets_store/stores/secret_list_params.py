# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretListParams"]


class SecretListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to sort objects"""

    order: Literal["name", "comment", "created", "modified", "status"]
    """Order secrets by values in the given field"""

    page: int
    """Page number"""

    per_page: int
    """Number of objects to return per page"""

    search: str
    """Search secrets using a filter string, filtering across name and comment"""
