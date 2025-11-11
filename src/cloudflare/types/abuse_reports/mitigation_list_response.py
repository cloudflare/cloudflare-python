# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MitigationListResponse", "Mitigation"]


class Mitigation(BaseModel):
    id: str
    """ID of remediation."""

    effective_date: str
    """Date when the mitigation will become active.

    Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html)
    """

    entity_id: str

    entity_type: Literal["url_pattern", "account", "zone"]

    status: Literal["pending", "active", "in_review", "cancelled", "removed"]
    """The status of a mitigation"""

    type: Literal[
        "legal_block",
        "phishing_interstitial",
        "network_block",
        "rate_limit_cache",
        "account_suspend",
        "redirect_video_stream",
    ]
    """The type of mitigation"""


class MitigationListResponse(BaseModel):
    mitigations: List[Mitigation]
