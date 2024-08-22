# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """Direction to order organizations."""

    match: Literal["any", "all"]
    """Whether to match all search requirements or at least one (any)."""

    name: str
    """Organization name."""

    order: Literal["id", "name", "status"]
    """Field to order organizations by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of organizations per page."""

    status: Literal["member", "invited"]
    """Whether the user is a member of the organization or has an inivitation pending."""
