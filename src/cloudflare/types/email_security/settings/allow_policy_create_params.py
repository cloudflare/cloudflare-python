# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyCreateParams"]


class AllowPolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    is_acceptable_sender: Required[bool]
    """
    Exempts messages from this sender from Spam, Spoof and Bulk dispositions only;
    Malicious and Suspicious dispositions still apply.
    """

    is_exempt_recipient: Required[bool]
    """Bypasses all detections for messages to this recipient."""

    is_regex: Required[bool]

    is_trusted_sender: Required[bool]
    """Bypasses all detections and link following for messages from this sender."""

    pattern: Required[str]
    """The pattern value to match.

    The format depends on `pattern_type`: a valid email address for EMAIL (e.g.
    `user@example.com`), a valid domain name for DOMAIN (e.g. `example.com`), or a
    plain IPv4 or IPv6 address or CIDR block for IP (e.g. `1.2.3.4`, `1.2.3.0/24`,
    `2606:4700:4700::1111`, or `2606:4700:4700::/48`); the API rejects private or
    unique-local, loopback, link-local, unspecified, and IPv4 broadcast addresses,
    including their IPv4-mapped IPv6 equivalents.
    """

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]
    """Type of pattern matching.

    - EMAIL: matches a full email address (e.g. `user@example.com`)
    - DOMAIN: matches a domain name (e.g. `example.com`)
    - IP: matches a plain IPv4 or IPv6 address (e.g. `1.2.3.4` or
      `2606:4700:4700::1111`) or CIDR block (e.g. `1.2.3.0/24` or
      `2606:4700:4700::/48`). The API rejects private or unique-local, loopback,
      link-local, unspecified, and IPv4 broadcast addresses, including their
      IPv4-mapped IPv6 equivalents.
    - UNKNOWN: deprecated; you cannot use this when creating or updating policies,
      but it may appear on existing entries.
    """

    verify_sender: Required[bool]
    """Enforce DMARC, SPF or DKIM authentication.

    When on, Email Security only honors policies that pass authentication.
    """

    comments: Optional[str]

    is_recipient: bool
    """Deprecated as of July 1, 2025.

    Use `is_exempt_recipient` instead. End of life: July 1, 2026.
    """

    is_sender: bool
    """Deprecated as of July 1, 2025.

    Use `is_trusted_sender` instead. End of life: July 1, 2026.
    """

    is_spoof: bool
    """Deprecated as of July 1, 2025.

    Use `is_acceptable_sender` instead. End of life: July 1, 2026.
    """
