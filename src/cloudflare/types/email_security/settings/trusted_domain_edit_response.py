# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TrustedDomainEditResponse"]


class TrustedDomainEditResponse(BaseModel):
    id: int
    """The unique identifier for the trusted domain."""

    created_at: datetime

    is_recent: bool
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: bool

    is_similarity: bool
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    last_modified: datetime

    pattern: str

    comments: Optional[str] = None
