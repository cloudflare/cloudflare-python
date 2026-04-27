# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AllowPolicyGetResponse"]


class AllowPolicyGetResponse(BaseModel):
    """An email allow policy"""

    id: str
    """Allow policy identifier"""

    created_at: datetime

    last_modified: datetime
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    comments: Optional[str] = None

    is_acceptable_sender: Optional[bool] = None
    """
    Messages from this sender will be exempted from Spam, Spoof and Bulk
    dispositions. Note - This will not exempt messages with Malicious or Suspicious
    dispositions.
    """

    is_exempt_recipient: Optional[bool] = None
    """Messages to this recipient will bypass all detections"""

    is_recipient: Optional[bool] = None
    """Deprecated as of July 1, 2025.

    Use `is_exempt_recipient` instead. End of life: July 1, 2026.
    """

    is_regex: Optional[bool] = None

    is_sender: Optional[bool] = None
    """Deprecated as of July 1, 2025.

    Use `is_trusted_sender` instead. End of life: July 1, 2026.
    """

    is_spoof: Optional[bool] = None
    """Deprecated as of July 1, 2025.

    Use `is_acceptable_sender` instead. End of life: July 1, 2026.
    """

    is_trusted_sender: Optional[bool] = None
    """Messages from this sender will bypass all detections and link following"""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] = None
    """
    Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
    creating or updating policies, but may be returned for existing entries.
    """

    verify_sender: Optional[bool] = None
    """Enforce DMARC, SPF or DKIM authentication.

    When on, Email Security only honors policies that pass authentication.
    """
