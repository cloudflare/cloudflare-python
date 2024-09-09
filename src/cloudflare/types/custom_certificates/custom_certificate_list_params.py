# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomCertificateListParams"]


class CustomCertificateListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    match: Literal["any", "all"]
    """Whether to match all search requirements or at least one (any)."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of zones per page."""

    status: Literal["active", "expired", "deleted", "pending", "initializing"]
    """Status of the zone's custom SSL."""
