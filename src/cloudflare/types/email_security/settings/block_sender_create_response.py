# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BlockSenderCreateResponse"]


class BlockSenderCreateResponse(BaseModel):
    """A blocked sender pattern"""

    id: Optional[str] = None
    """Blocked sender pattern identifier"""

    comments: Optional[str] = None

    created_at: Optional[datetime] = None

    is_regex: Optional[bool] = None

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None

    pattern: Optional[str] = None
    """The pattern value to match against. Format depends on `pattern_type`:

    - EMAIL: a valid email address, e.g. `user@example.com`
    - DOMAIN: a valid domain name, e.g. `example.com`
    - IP: a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted; private,
      loopback, link-local, and unspecified addresses are rejected.
    """

    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] = None
    """Type of pattern matching.

    - EMAIL: matches a full email address (e.g. `user@example.com`)
    - DOMAIN: matches a domain name (e.g. `example.com`)
    - IP: matches a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted.
    - UNKNOWN: deprecated, cannot be used when creating or updating policies, but
      may be returned for existing entries.
    """
