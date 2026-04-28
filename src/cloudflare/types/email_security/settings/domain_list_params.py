# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]
    """Currently active delivery mode to filter by."""

    allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]
    """Delivery mode to filter by."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    domain: SequenceNotStr[str]
    """Domain names to filter by."""

    integration_id: str
    """Integration ID to filter by."""

    order: Literal["domain", "created_at"]
    """Field to sort by."""

    page: int
    """Current page within paginated list of results."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    search: str
    """Search term for filtering records. Behavior may change."""

    status: Literal["pending", "active", "failed", "timeout"]
    """Filters response to domains with the provided status."""
