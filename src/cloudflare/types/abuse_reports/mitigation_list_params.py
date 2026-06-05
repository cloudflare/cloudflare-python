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
        "account_suspend",
        "copyright_interstitial",
        "geo_block",
        "legal_block",
        "malware_interstitial",
        "misleading_interstitial",
        "network_block",
        "phishing_interstitial",
        "playfairite_enforce",
        "r2_takedown_account",
        "r2_takedown_bucket",
        "r2_takedown_object",
        "rate_limit_cache",
        "redirect_video_stream",
        "registrar_freeze",
        "registrar_parking",
        "stream_block_account",
        "user_suspend",
        "workers_takedown_by_zone_id",
    ]
    """Filter by the type of mitigation.

    This filter parameter can be specified multiple times to include multiple types
    of mitigations in the result set, e.g. ?type=rate_limit_cache&type=legal_block.
    """
