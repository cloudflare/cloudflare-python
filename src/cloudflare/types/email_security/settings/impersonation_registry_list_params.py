# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImpersonationRegistryListParams"]


class ImpersonationRegistryListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    order: Literal["name", "email", "created_at"]
    """Field to sort by."""

    page: int
    """Current page within paginated list of results."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]

    search: str
    """Search term for filtering records. Behavior may change."""
