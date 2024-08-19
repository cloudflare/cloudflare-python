# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..hostname_param import HostnameParam
from ..redirect_param import RedirectParam

__all__ = ["ItemUpdateParams", "Body"]


class ItemUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    asn: int
    """A non-negative 32 bit integer"""

    comment: str
    """An informative summary of the list item."""

    hostname: HostnameParam
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from
    0 to 9, wildcards (\\**), and the hyphen (-).
    """

    ip: str
    """An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.

    IPv6 CIDRs are limited to a maximum of /64.
    """

    redirect: RedirectParam
    """The definition of the redirect."""
