# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BlockSenderBatchParams", "Delete", "Patch", "Post", "Put"]


class BlockSenderBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    deletes: Required[Iterable[Delete]]
    """IDs of the blocked sender patterns to delete."""

    patches: Required[Iterable[Patch]]
    """
    Partial updates to apply — each entry carries the pattern's ID and only the
    fields to change.
    """

    posts: Required[Iterable[Post]]
    """Blocked sender patterns to create."""

    puts: Required[Iterable[Put]]
    """
    Full replacements to apply — each entry carries the pattern's ID and every field
    of its new value.
    """


class Delete(TypedDict, total=False):
    id: Required[str]
    """Blocked sender pattern identifier."""


class Patch(TypedDict, total=False):
    """A blocked sender pattern."""

    comments: Optional[str]

    is_regex: bool
    """Whether `pattern` is a regular expression instead of a literal value."""

    pattern: str
    """The pattern value to match.

    The format depends on `pattern_type`: a valid email address for EMAIL (e.g.
    `user@example.com`), a valid domain name for DOMAIN (e.g. `example.com`), or a
    plain IPv4 or IPv6 address or CIDR block for IP (e.g. `1.2.3.4`, `1.2.3.0/24`,
    `2606:4700:4700::1111`, or `2606:4700:4700::/48`); the API rejects private or
    unique-local, loopback, link-local, unspecified, and IPv4 broadcast addresses,
    including their IPv4-mapped IPv6 equivalents.
    """

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]
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


class Post(TypedDict, total=False):
    """Create a blocked sender pattern."""

    is_regex: Required[bool]
    """Whether `pattern` is a regular expression instead of a literal value."""

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

    comments: Optional[str]


class Put(TypedDict, total=False):
    """A blocked sender pattern."""

    is_regex: Required[bool]
    """Whether `pattern` is a regular expression instead of a literal value."""

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

    comments: Optional[str]
