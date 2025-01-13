# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    id: str
    """The unique identifier of the firewall rule."""

    action: str
    """The action to search for. Must be an exact match."""

    description: str
    """A case-insensitive string to find in the description."""

    page: float
    """Page number of paginated results."""

    paused: bool
    """When true, indicates that the firewall rule is currently paused."""

    per_page: float
    """Number of firewall rules per page."""
