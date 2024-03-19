# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemUpdateParams", "Body", "BodyHostname", "BodyRedirect"]


class ItemUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class BodyHostname(TypedDict, total=False):
    url_hostname: Required[str]


class BodyRedirect(TypedDict, total=False):
    source_url: Required[str]

    target_url: Required[str]

    include_subdomains: bool

    preserve_path_suffix: bool

    preserve_query_string: bool

    status_code: Literal[301, 302, 307, 308]

    subpath_matching: bool


class Body(TypedDict, total=False):
    asn: int
    """A non-negative 32 bit integer"""

    comment: str
    """An informative summary of the list item."""

    hostname: BodyHostname
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    ip: str
    """An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.

    IPv6 CIDRs are limited to a maximum of /64.
    """

    redirect: BodyRedirect
    """The definition of the redirect."""
