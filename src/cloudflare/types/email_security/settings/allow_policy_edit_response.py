# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AllowPolicyEditResponse"]


class AllowPolicyEditResponse(BaseModel):
    id: int
    """The unique identifier for the allow policy."""

    created_at: datetime

    is_acceptable_sender: bool
    """
    Messages from this sender will be exempted from Spam, Spoof and Bulk
    dispositions. Note: This will not exempt messages with Malicious or Suspicious
    dispositions.
    """

    is_exempt_recipient: bool
    """Messages to this recipient will bypass all detections."""

    is_regex: bool

    is_trusted_sender: bool
    """Messages from this sender will bypass all detections and link following."""

    last_modified: datetime

    pattern: str

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]

    verify_sender: bool
    """
    Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
    policies that pass authentication.
    """

    comments: Optional[str] = None

    is_recipient: Optional[bool] = None

    is_sender: Optional[bool] = None

    is_spoof: Optional[bool] = None
