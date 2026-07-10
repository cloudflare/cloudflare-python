# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    enabled: Literal[True, False]
    """Filter by enabled routing rules."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
