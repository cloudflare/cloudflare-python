# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SendingDomainRestrictionListResponse"]


class SendingDomainRestrictionListResponse(BaseModel):
    """
    A sending domain restriction that enforces TLS (Transport Layer Security) requirements for emails from specific domains. If TLS is required, mail without TLS from the specified domain will be dropped.
    """

    id: Optional[str] = None
    """Sending domain restriction identifier."""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """Domain that requires TLS enforcement."""

    exclude: Optional[List[str]] = None
    """Excluded subdomains that are exempt from TLS requirements."""

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None
