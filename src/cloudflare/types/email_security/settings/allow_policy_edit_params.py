# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyEditParams"]


class AllowPolicyEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    comments: Optional[str]

    is_acceptable_sender: Optional[bool]
    """
    Messages from this sender will be exempted from Spam, Spoof and Bulk
    dispositions. Note: This will not exempt messages with Malicious or Suspicious
    dispositions.
    """

    is_exempt_recipient: Optional[bool]
    """Messages to this recipient will bypass all detections."""

    is_regex: Optional[bool]

    is_trusted_sender: Optional[bool]
    """Messages from this sender will bypass all detections and link following."""

    pattern: Optional[str]

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]

    verify_sender: Optional[bool]
    """
    Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
    policies that pass authentication.
    """
