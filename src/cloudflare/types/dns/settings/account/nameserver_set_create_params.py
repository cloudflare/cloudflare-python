# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["NameserverSetCreateParams", "Nameserver"]


class NameserverSetCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    name: Required[str]
    """
    Customer-defined name, unique within the account by exact string equality
    (case-sensitive, with no Unicode normalization). Must be valid UTF-8 and at most
    255 UTF-8 bytes, not 255 characters. Only graphical Unicode characters are
    allowed; leading or trailing whitespace is rejected. The name can be changed
    without changing the set's nameservers or addresses.
    """

    nameservers: Required[Iterable[Nameserver]]
    """Lists each nameserver and the number of addresses to allocate to it.

    Requires a unique name for each entry in the set.
    """

    advanced: bool
    """Whether to allocate the nameservers from distinct Advanced anycast groups."""

    ip_set: int
    """Selects the account-specific IP set that supplies the nameserver addresses.

    Nameserver sets with the same `ip_set` and `advanced` value may reuse addresses;
    otherwise, they use disjoint address groups.
    """


class Nameserver(TypedDict, total=False):
    name: Required[str]
    """A unique lowercase Punycode nameserver name within the set."""

    ip_count: int
    """
    Number of IPv4 addresses and number of IPv6 addresses to allocate to this
    nameserver. All nameservers in an Advanced nameserver set must use the same
    value.
    """
