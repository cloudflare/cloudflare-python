# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
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
