# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyCreateParams"]


class AllowPolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    is_acceptable_sender: Required[bool]
    """
    Messages from this sender will be exempted from Spam, Spoof and Bulk
    dispositions. Note: This will not exempt messages with Malicious or Suspicious
    dispositions.
    """

    is_exempt_recipient: Required[bool]
    """Messages to this recipient will bypass all detections."""

    is_regex: Required[bool]

    is_trusted_sender: Required[bool]
    """Messages from this sender will bypass all detections and link following."""

    pattern: Required[str]

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]

    verify_sender: Required[bool]
    """
    Enforce DMARC, SPF or DKIM authentication. When on, Email Security only honors
    policies that pass authentication.
    """

    comments: Optional[str]

    is_recipient: bool

    is_sender: bool

    is_spoof: bool
