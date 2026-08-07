# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AllowPolicyEditResponse"]


class AllowPolicyEditResponse(BaseModel):
    """An email allow policy."""

    id: str
    """Allow policy identifier."""

    created_at: datetime

    last_modified: datetime
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    comments: Optional[str] = None

    is_acceptable_sender: Optional[bool] = None
    """
    Exempts messages from this sender from Spam, Spoof and Bulk dispositions only;
    Malicious and Suspicious dispositions still apply.
    """

    is_exempt_recipient: Optional[bool] = None
    """Bypasses all detections for messages to this recipient."""

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
    """Bypasses all detections and link following for messages from this sender."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The pattern value to match.

    The format depends on `pattern_type`: a valid email address for EMAIL (e.g.
    `user@example.com`), a valid domain name for DOMAIN (e.g. `example.com`), or a
    plain IPv4 address or IPv4 CIDR block for IP (e.g. `1.2.3.4` or `1.2.3.0/24`);
    the API accepts only globally reachable IP addresses and rejects private,
    loopback, link-local, and unspecified addresses.
    """

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] = None
    """Type of pattern matching.

    - EMAIL: matches a full email address (e.g. `user@example.com`)
    - DOMAIN: matches a domain name (e.g. `example.com`)
    - IP: matches a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). The API accepts only globally reachable addresses.
    - UNKNOWN: deprecated; you cannot use this when creating or updating policies,
      but it may appear on existing entries.
    """

    verify_sender: Optional[bool] = None
    """Enforce DMARC, SPF or DKIM authentication.

    When on, Email Security only honors policies that pass authentication.
    """
