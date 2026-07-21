# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AllowPolicyEditParams"]


class AllowPolicyEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comments: Optional[str]

    is_acceptable_sender: bool
    """
    Messages from this sender will be exempted from Spam, Spoof and Bulk
    dispositions. Note - This will not exempt messages with Malicious or Suspicious
    dispositions.
    """

    is_exempt_recipient: bool
    """Messages to this recipient will bypass all detections"""

    is_recipient: bool
    """Deprecated as of July 1, 2025.

    Use `is_exempt_recipient` instead. End of life: July 1, 2026.
    """

    is_regex: bool

    is_sender: bool
    """Deprecated as of July 1, 2025.

    Use `is_trusted_sender` instead. End of life: July 1, 2026.
    """

    is_spoof: bool
    """Deprecated as of July 1, 2025.

    Use `is_acceptable_sender` instead. End of life: July 1, 2026.
    """

    is_trusted_sender: bool
    """Messages from this sender will bypass all detections and link following"""

    pattern: str
    """The pattern value to match against. Format depends on `pattern_type`:

    - EMAIL: a valid email address, e.g. `user@example.com`
    - DOMAIN: a valid domain name, e.g. `example.com`
    - IP: a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted; private,
      loopback, link-local, and unspecified addresses are rejected.
    """

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]
    """Type of pattern matching.

    - EMAIL: matches a full email address (e.g. `user@example.com`)
    - DOMAIN: matches a domain name (e.g. `example.com`)
    - IP: matches a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted.
    - UNKNOWN: deprecated, cannot be used when creating or updating policies, but
      may be returned for existing entries.
    """

    verify_sender: bool
    """Enforce DMARC, SPF or DKIM authentication.

    When on, Email Security only honors policies that pass authentication.
    """
