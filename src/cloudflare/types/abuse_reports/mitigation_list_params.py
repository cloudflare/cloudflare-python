# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MitigationListParams"]


class MitigationListParams(TypedDict, total=False):
    account_id: Required[str]

    effective_after: str
    """Returns mitigation that were dispatched after the given date"""

    effective_before: str
    """Returns mitigations that were dispatched before the given date"""

    entity_type: Literal["url_pattern", "account", "zone"]
    """Filter by the type of entity the mitigation impacts."""

    page: int
    """Where in pagination to start listing abuse reports"""

    per_page: int
    """How many abuse reports per page to list"""

    sort: Literal[
        "type,asc",
        "type,desc",
        "effective_date,asc",
        "effective_date,desc",
        "status,asc",
        "status,desc",
        "entity_type,asc",
        "entity_type,desc",
    ]
    """A property to sort by, followed by the order"""

    status: Literal["pending", "active", "in_review", "cancelled", "removed"]
    """Filter by the status of the mitigation."""

    type: Literal[
        "legal_block",
        "phishing_interstitial",
        "network_block",
        "rate_limit_cache",
        "account_suspend",
        "redirect_video_stream",
    ]
    """Filter by the type of mitigation.

    This filter parameter can be specified multiple times to include multiple types
    of mitigations in the result set, e.g. ?type=rate_limit_cache&type=legal_block.
    """
