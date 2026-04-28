# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["TrustedDomainEditResponse"]


class TrustedDomainEditResponse(BaseModel):
    """A trusted email domain"""

    id: Optional[str] = None
    """Trusted domain identifier"""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_recent: Optional[bool] = None
    """
    Select to prevent recently registered domains from triggering a Suspicious or
    Malicious disposition.
    """

    is_regex: Optional[bool] = None

    is_similarity: Optional[bool] = None
    """
    Select for partner or other approved domains that have similar spelling to your
    connected domains. Prevents listed domains from triggering a Spoof disposition.
    """

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
