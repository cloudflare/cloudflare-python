# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockSenderListResponse"]


class BlockSenderListResponse(BaseModel):
    """A blocked sender pattern."""

    id: Optional[str] = None
    """Blocked sender pattern identifier."""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_regex: Optional[bool] = None

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The pattern value to match.

    The format depends on `pattern_type`: a valid email address for EMAIL (e.g.
    `user@example.com`), a valid domain name for DOMAIN (e.g. `example.com`), or a
    plain IPv4 or IPv6 address or CIDR block for IP (e.g. `1.2.3.4`, `1.2.3.0/24`,
    `2606:4700:4700::1111`, or `2606:4700:4700::/48`); the API rejects private or
    unique-local, loopback, link-local, unspecified, and IPv4 broadcast addresses,
    including their IPv4-mapped IPv6 equivalents.
    """

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] = None
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
