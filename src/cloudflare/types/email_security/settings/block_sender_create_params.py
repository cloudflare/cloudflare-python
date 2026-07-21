# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BlockSenderCreateParams"]


class BlockSenderCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    is_regex: Required[bool]

    pattern: Required[str]
    """The pattern value to match against. Format depends on `pattern_type`:

    - EMAIL: a valid email address, e.g. `user@example.com`
    - DOMAIN: a valid domain name, e.g. `example.com`
    - IP: a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted; private,
      loopback, link-local, and unspecified addresses are rejected.
    """

    pattern_type: Required[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]]
    """Type of pattern matching.

    - EMAIL: matches a full email address (e.g. `user@example.com`)
    - DOMAIN: matches a domain name (e.g. `example.com`)
    - IP: matches a plain IPv4 address (e.g. `1.2.3.4`) or an IPv4 CIDR block (e.g.
      `1.2.3.0/24`). Only globally reachable addresses are accepted.
    - UNKNOWN: deprecated, cannot be used when creating or updating policies, but
      may be returned for existing entries.
    """

    comments: Optional[str]
